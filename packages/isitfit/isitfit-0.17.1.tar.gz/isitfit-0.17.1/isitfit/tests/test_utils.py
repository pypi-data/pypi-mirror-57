# mocker fixture becomes available after installing pytest-mock
# https://github.com/pytest-dev/pytest-mock
def test_pingMatomo_unit(mocker):
  from ..utils import ping_matomo
  def mockreturn(url, json, timeout): return "foo"
  mocked_post = mocker.patch('isitfit.utils.requests.post', side_effect=mockreturn)
  ping_matomo("/test")

  # check that mocked object is called
  # https://github.com/pytest-dev/pytest-mock/commit/68868872195135bdb90d45a5cb0d609400943eae
  mocked_post.assert_called()



def test_pingMatomo_functional(mocker):
  from ..utils import ping_matomo
  ping_matomo("/test")





def test_isitfitCliError():
    import pytest
    from ..utils import IsitfitCliError

    class MockContext:
        obj = {'bar': 1}
        command = None

    ctx = MockContext()
    with pytest.raises(IsitfitCliError) as e:
        raise IsitfitCliError("foo", ctx)



def test_mergeSeriesOnTimestampRange():
  import pandas as pd
  df_cpu = pd.DataFrame({'Timestamp': [1,2,3,4], 'field_1': [5,6,7,8]})
  df_type = pd.DataFrame({'Timestamp': [1,3], 'field_2': ['a','b']})

  # update 2019-11-20 had initially written example as field_2: a, a, b, b
  # but maybe that was an outdated example
  expected = pd.DataFrame({'Timestamp': [1,2,3,4], 'field_1': [5,6,7,8], 'field_2': ['a','b','b','b']})

  # reverse sort
  df_cpu  = df_cpu.sort_values(['Timestamp'], ascending=False)
  df_type = df_type.sort_values(['Timestamp'], ascending=False)

  # set index
  df_type = df_type.set_index('Timestamp')

  # test
  from ..utils import mergeSeriesOnTimestampRange
  actual = mergeSeriesOnTimestampRange(df_cpu, df_type, ['field_2'])

  # straight sort
  actual = actual.sort_values(['Timestamp'], ascending=True)

  #print(expected)
  #print(actual)
  pd.testing.assert_frame_equal(expected, actual)


def test_b2l():
  from isitfit.utils import b2l
  a = b2l(True)
  assert a=='T'
  a = b2l(False)
  assert a=='F'



def test_l2s():
  from isitfit.utils import l2s
  a = l2s(list(range(10)))
  assert a=='0,1,...,8,9'



def test_taglist2str():
  from isitfit.utils import taglist2str

  a = taglist2str([{'Key':'app', 'Value':'isitfit'}, {'Key':'app', 'Value':'another'}], None)
  assert a == 'app = isitfit\napp = another'

  a = taglist2str([{'Key':'app', 'Value':'isitfit'}, {'Key':'app', 'Value':'another'}], 'is')
  assert a == 'app = isitfit'

  a = taglist2str([{'Key':'app', 'Value':'isitfit'}, {'Key':'app', 'Value':'another'}], 'foo')
  assert a == ''
