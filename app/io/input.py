def input_text():
    """
    Inputs text from the console.

    Examples:
        >>> input_text()
        'Hello, World!'

    Returns:
        text (str): The text input from the console.
    """
    return input("Enter text: ")

def read_file_builtin(file_path):
    """
    Reads text from a file using built-in Python capabilities.

    Examples:
        >>> read_file_builtin('data/input_builtin.txt')
        'File content'

    Args:
        file_path (str): The path to the file to read.

    Returns:
        content (str): The content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(file_path, 'r') as file:
        return file.read()

def read_file_pandas(file_path):
    """
    Reads text from a file using the pandas library.

    Examples:
        >>> read_file_pandas('data/input_pandas.csv')
        'DataFrame content as string'

    Args:
        file_path (str): The path to the file to read.

    Returns:
        content (str): The content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        pandas.errors.EmptyDataError: If the file is empty.
    """
    import pandas as pd
    try:
        df = pd.read_csv(file_path)
        return df.to_string()
    except pd.errors.EmptyDataError:
        return 'Empty DataFrame\nColumns: []\nIndex: []'