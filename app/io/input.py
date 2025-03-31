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
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")

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
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except pd.errors.EmptyDataError:
        return 'Empty DataFrame\nColumns: []\nIndex: []'