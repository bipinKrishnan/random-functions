import pytest
from random_functions.pandas import utils


@pytest.mark.parametrize("time", ["True", "False"])
def test_create_dummy_dataframe(time):
    rows = 100
    columns = ["test 1", "test 2", "test 3"]
    df = utils.create_dummy_dataframe(
            time_column=time,
            columns=columns,
            n_rows=rows,
        )

    if not time:
        assert df.columns.tolist()==columns
        assert df.shape==(rows, len(columns))
    else:
        columns.append("time")
        assert df.columns.tolist()==columns
        assert df.shape==(rows, len(columns))