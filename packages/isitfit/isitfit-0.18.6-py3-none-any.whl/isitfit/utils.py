SECONDS_IN_ONE_DAY = 60*60*24 # 86400  # used for granularity (daily)


import logging
logger = logging.getLogger('isitfit')


class NoCloudwatchException(Exception):
    pass


def raise_noCwExc(rc_id):
  raise NoCloudwatchException("No cloudwatch data for %s"%rc_id)


class NoCloudtrailException(Exception):
    pass


def mergeSeriesOnTimestampRange(df_cpu, df_type, fields):
  """
  Upsamples df_type to df_cpu.
  Check unit test for an example
  """
  # check that df_type dataframe are sorted descending
  # This does not apply to df_cpu
  #if df_cpu.Timestamp.iloc[0] < df_cpu.Timestamp.iloc[-1]:
  #  raise Exception("CPU Dataframe should be sorted descending for utils.mergeSeriesOnTimestampRange")

  if df_type.iloc[0].name < df_type.iloc[-1].name:
    raise Exception("Types Dataframe should be sorted descending for utils.mergeSeriesOnTimestampRange")

  import numpy as np

  for f in fields:
    df_cpu[f] = None

  # assume df_type is sorted in decreasing EventTime order (very important)
  # NB: since some instances are not present in the cloudtrail (for which we append artificially the "now" type)
  #     Need to traverse the df_type matrix backwards
  for index, row_type in df_type.iterrows():
    row_i = np.where(df_cpu.Timestamp <= row_type.name)[0]
    for f in fields:
      # use row_type.name instead of row_type['EventTime']
      # check note above about needing to traverse backwards
      # df_cpu.iloc[np.where(df_cpu.Timestamp >= row_type.name)[0], df_cpu.columns.get_loc('instanceType')] = row_type['instanceType']
      col_i = df_cpu.columns.get_loc(f)
      df_cpu.iloc[row_i, col_i] = row_type[f]

  # fill na at beginning with back-fill
  # (artifact of cloudwatch having data at days before the creation of the instance)
  for f in fields:
    df_cpu[f] = df_cpu[f].fillna(method='backfill')

  return df_cpu







# copied from git-remote-aws
def mysetlocale():
  li = 'en_US.utf8'
  import os
  os.environ["LC_ALL"] = li
  os.environ["LANG"]   = li




MAX_ROWS = 10
MAX_COLS = 5
MAX_STRING = 20
def display_df(title, df, csv_fn, shape, logger):
    # https://pypi.org/project/termcolor/
    from termcolor import colored
    import click

    click.echo("")

    if shape[0]==0:
      click.echo(title)
      click.echo(colored("None", "red"))
      return

    if csv_fn is not None:
      click.echo(colored("The table '%s' was saved to the CSV file '%s'."%(title, csv_fn), "cyan"))
      click.echo(colored("It could be opened in the terminal with visidata (http://visidata.org/)","cyan"))
      click.echo(colored("and you can close visidata by pressing 'q'","cyan"))
      open_vd = input(colored('Would you like to do so? yes/[no] ', 'cyan'))
      if open_vd.lower() == 'yes' or open_vd.lower() == 'y':
        click.echo("Opening CSV file `%s` with visidata."%csv_fn)
        from subprocess import call
        call(["vd", csv_fn])
        click.echo("Exited visidata.")
        click.echo(colored("The table '%s' was saved to the CSV file '%s'."%(title, csv_fn), "cyan"))
        return
      else:
        click.echo("Not opening visidata.")
        click.echo("To open the results with visidata, use `vd %s`."%csv_fn)


    # if not requested to open with visidata
    from tabulate import tabulate
    df_show = df.head(n=MAX_ROWS)
    df_show = df_show.applymap(lambda c: (c[:MAX_STRING]+'...' if len(c)>=MAX_STRING else c) if type(c)==str else c)

    click.echo(tabulate(df_show, headers='keys', tablefmt='psql', showindex=False))

    if (shape[0] > MAX_ROWS) or (shape[1] > MAX_COLS):
      click.echo("...")
      click.echo("(results truncated)")
      # done
      return

    # done
    return


def prompt_upgrade(pkg_name, current_version):
  """
  check if current version is out-of-date
  https://github.com/alexmojaki/outdated

  copied from https://github.com/WhatsApp/WADebug/blob/958ac37be804cc732ae514d4872b93d19d197a5c/wadebug/cli.py#L40
  """
  import outdated

  is_outdated = False
  try:
    is_outdated, latest_version = outdated.check_outdated(pkg_name, current_version)
  except requests.exceptions.ConnectionError as error:
    # e.g.
    # requests.exceptions.ConnectionError:
    # HTTPSConnectionPool(host='pypi.python.org', port=443):
    # Max retries exceeded with url: /pypi/isitfit/json
    # (Caused by NewConnectionError(... Name or service not known)
    # Thrown upon internet disconnection
    pass
  except ValueError as error:
    # catch case of "ValueError: Version 0.10.0 is greater than the latest version on PyPI: 0.9.1"
    # This would happen on my dev machine
    if not "is greater than" in str(error):
      raise

    # In this case, outdated does not cache the result to disk
    # so cache it myself (copied from https://github.com/alexmojaki/outdated/blob/565bb3fe1adc30da5e50249912cd2ac494662659/outdated/__init__.py#L61)
    latest_version = str(error).split(":")[1].strip()
    import datetime as dt
    import json
    with outdated.utils.cache_file(pkg_name, 'w') as f:
      try:
        data = [latest_version, outdated.utils.format_date(dt.datetime.now())]
        json.dump(data, f)
      except Exception as e:
        print('Error: ' + str(e))
        raise


  # is_outdated = True # FIXME for debugging
  if not is_outdated:
      return is_outdated

  import click
  msg_outdated = """The current version of {pkg_name} ({current_version}) is out of date.
Run `pip3 install {pkg_name} --upgrade` to upgrade to version {latest_version},
or use `isitfit --skip-check-upgrade ...` to skip checking for version upgrades of isitfit.
"""
  msg_outdated = msg_outdated.format(
      pkg_name=pkg_name, current_version=current_version, latest_version=latest_version
    )
  click.secho(msg_outdated, fg="red")

  # Give the user some time to read the message and possibly update
  import time
  from tqdm import tqdm
  wait_outdated = 10
  click.secho("Will continue in %i seconds"%wait_outdated, fg='yellow')
  for i in tqdm(range(wait_outdated)):
    time.sleep(1)

  return is_outdated


# This import needs to stay here for the sake of the mock in test_utils
import requests
SKIP_PING=False
def ping_matomo(action_name):
  """
  Gather anonymous usage statistics
  """
  logger.debug("ping_matomo('%s')"%action_name)

  # get uuid
  from .dotMan import DotMan
  uuid_val = DotMan().get_myuid()

  # get version
  from . import isitfit_version as isitfit_cli_version

  # build action name field. note that "action_name" already starts with "/"
  full_actionName = "%s%s"%(isitfit_cli_version, action_name)

  # use base function
  from matomo_sdk_py.matomo_sdk_py import ping_matomo as ping_matomo_base
  ping_matomo_base(
    action_name=full_actionName,
    action_base="https://cli.isitfit.io",
    idsite=2, # 2 is for cli.isitfit.io
    uuid_val=uuid_val,
    matomo_url="https://isitfit.matomo.cloud/piwik.php"
  )


def display_footer():
    import click

    from . import isitfit_version

    click.echo("")
    click.echo("⛅ Generated by isitfit version %s"%isitfit_version)
    click.echo("")
    click.echo("Useful links:")
    click.echo("ℹ️  isitfit homepage         https://isitfit.autofitcloud.com")
    click.echo("😞 isitfit issues           https://github.com/autofitcloud/isitfit/issues")
    click.echo("🌎 Global Climate Strike    https://twitter.com/hashtag/ClimateStrike")
    click.echo("❤️  Built by AutofitCloud    https://www.autofitcloud.com")





def myreturn(df_xxx):
    if df_xxx.shape[0] > 0:
      return df_xxx
    else:
      return None # this means that the data was found in cache, but it was empty (meaning aws returned no data)



def b2l(b_in):
  """
  return "T" on true and "F" on false
  Instead of "True" and "False"
  """
  return str(b_in)[0]


def l2s(x):
  """
  [1,2,3,4,5,6,7,8] -> '1,2,...,7,8'
  """
  if len(x)>5: x = x[:2] + ['...'] + x[-2:]
  y = [str(z) for z in x] # convert to list of strings, eg if list of int
  y = ",".join(y)
  return y



def taglist2str(taglist, filter_tags):
  """
  eg
  taglist2str([{'Key':'app', 'Value':'isitfit'}], 'boo')
  returns ""

  taglist2str([{'Key':'app', 'Value':'isitfit'}], 'is')
  returns "app = isitfit"
  """
  if filter_tags is not None:
    # filter the tag list for only those containing the filter-tags string
    f_tn = filter_tags.lower()

    # similar to the isitfit.mainManager.tagsContain function, but filtering the tags themselves
    taglist = [x for x in taglist if (f_tn in x['Key'].lower()) or (f_tn in x['Value'].lower())]

  # list to string
  taglist = ["%s = %s"%(x['Key'], x['Value']) for x in taglist]
  taglist = "\n".join(taglist)

  return taglist


def pd_series_frozenset_union(s1, s2):
  """
  Pandas doesn't have a built-in set union.
  Worse, it doesn't support set as column type
  Need to use frozenset
  Check test for example
  Ref https://python-forum.io/Thread-Error-Message-TypeError-unhashable-type-set
  """
  import pandas as pd
  df1=pd.DataFrame({'a1': s1})
  df2=pd.DataFrame({'a2': s2})
  df3=df1.merge(df2, left_index=True, right_index=True, how='left')
  df3['a3'] = df3.apply(lambda row: row.a1 if pd.isnull(row.a2) else row.a1.union(row.a2), axis=1)
  return df3['a3']



class AwsProfileMan:
  def __init__(self):
    import boto3
    self.p_l = boto3.session.Session().available_profiles

  def validate_profile(self, ctx, param, value):
    if value is None: return value
    if value not in self.p_l:
      import click
      err_m = 'Profile %s is not from ~/.aws/credentials file.'%value
      raise click.BadParameter(err_m)

    # set the profile in an env var so that boto3 picks it up automatically
    if value is not None:
      import os
      os.environ['AWS_PROFILE'] = value

    # save profile in click context for other usage in displayed/emailed report
    ctx.obj['aws_profile'] = value

    # done
    return value


  def prompt(self):
    x = []
    x.append("Profiles in AWS credential file:")
    x += ["- %s"%z for z in self.p_l]
    x.append("")
    x.append("(use `AWS_PROFILE=myprofile isitfit ...` or `isitfit --profile=myprofile ...` to skip this prompt)")
    x.append("Profile to use")
    y = "\n".join(x)
    return y

