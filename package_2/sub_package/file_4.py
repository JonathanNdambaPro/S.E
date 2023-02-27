import typing as t
from pathlib import Path

import pandas as pd

from package_2.file_3 import file_3_function


def file_4_function():
    file_3_function()
    print("package_2.file_4_function")


def read_header_csv(path: Path) -> t.List:
    if path.is_file() and path.suffix == "csv":
        df_data = pd.read_csv(path)
        columns = [column for column in df_data.columns]
        return columns

    columns = []
    return columns
