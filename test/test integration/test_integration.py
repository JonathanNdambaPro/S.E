from pathlib import Path

from package_2.sub_package import file_4


def test_file_4_read_file():
    header_csv = "column_1,column_2,column_3"
    current_folder = Path(".").resolve()
    path_csv_path = current_folder / "test.csv"

    with path_csv_path.open("w") as path:
        path.write(header_csv)

    value = file_4.read_header_csv(path_csv_path)

    assert value == ["column_1", "column_2", "column_3"]

    path_csv_path.unlink()
