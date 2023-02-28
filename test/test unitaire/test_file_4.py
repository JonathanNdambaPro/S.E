import typing as t

from package_2.sub_package import file_4


def test_file_4_read_file(mocker, path_faker, dataframe_faker):
    mocker.patch("package_2.sub_package.file_4.pd.read_csv", return_value=dataframe_faker)
    value = file_4.read_header_csv(path_faker)

    assert value == ["column_1", "column_2", "column_3"]


def test_file_4_read_file_false(mocker, path_faker_false, dataframe_faker):
    mocker.patch("package_2.sub_package.file_4.pd.read_csv", return_value=dataframe_faker)
    value = file_4.read_header_csv(path_faker_false)

    assert value == []
