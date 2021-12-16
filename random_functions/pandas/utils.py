import numpy as np
import pandas as pd


def create_dummy_dataframe(
    time_column: bool,
    columns: list,
    n_rows: int,
    ) -> pd.DataFrame:
    """
    Creates a dummy dataframe with the provided list of
    column names. Includes a datetime column ```time_column``` is set
    to ```True```.

    <u>Usage:</u>
    ```python

    from random_functions.pandas.utils import create_dummy_dataframe

    create_dummy_dataframe(
        time_column=True,
        columns=['col_1', 'col_2', 'col_3'],
        n_rows=100
    )

    ```

    Args:
      time_column (bool): Includes a datetime column if set to True
      columns (list): List of column names to be included in the
                     dummy dataframe returned
      n_rows (int): Number of rows required for the dummy dataframe

    Returns:
      The created dummy dataframe
    """

    data = np.random.random((n_rows, len(columns)))
    df = pd.DataFrame(data, columns=columns)
    if time_column:
        start_date = "2018-10-11"
        df['time'] = pd.date_range(start=start_date, periods=n_rows, freq='D')

    return df