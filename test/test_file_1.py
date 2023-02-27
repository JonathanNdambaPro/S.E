from package_1 import file_1


def test_file_1_function():
    value = file_1.file_1_function(sentence_1="Goodbye")
    assert "Goodbye World" == value
