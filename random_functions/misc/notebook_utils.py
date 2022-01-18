import nbformat as nbf
from pathlib import Path


def find_notebooks(
    path: str, 
    string: str, 
    cell_type: str
    ) -> None:
    """
    If you have a directory containing a whole lot of jupyter notebooks and you
    need to find the notebook containing a specific string/code, this function is
    for you.

    <u>Usage:</u>
    ```python

    from random_functions.misc.notebook_utils import find_notebooks

    string_to_search = "import numpy as np"
    dir_to_search = "/home/myuser/notebooks"

    find_notebooks(
        path=directory_to_search,
        string=string_to_search,
        cell_type="code,
    )

    ```

    Args:
      path (str): The path where the notebooks(ipynb) are present
      string (str): The word to search for in the notebooks
      cell_type (str): Can be either ```markdown``` or ```code```.
                       If the word you wish to search for is in the 
                       markdown cell, use "markdown" else use "code".
    """

    path = Path(path)
    for ipynb in path.glob("*.ipynb"):
        with open(ipynb, 'r', encoding='utf-8') as f:
            nodes = nbf.read(f, as_version=4)
            for cell in nodes['cells']:
                if cell['cell_type']==cell_type and string in cell['source']:
                    print(f"Name: {ipynb}\nSource:\n{cell['source']}")



