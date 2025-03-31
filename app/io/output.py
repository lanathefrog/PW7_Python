def output_text(text):
    """
    Outputs text to the console.

    Examples:
        >>> output_text('Hello, World!')
        Hello, World!

    Args:
        text (str): The text to output.
    """
    print(text)

def write_file_builtin(file_path, text):
    """
    Writes text to a file using built-in Python capabilities.

    Examples:
        >>> write_file_builtin('data/output.txt', 'Hello, World!')

    Args:
        file_path (str): The path to the file to write.
        text (str): The text to write to the file.

    Raises:
        IOError: If the file cannot be written.
    """
    with open(file_path, 'a') as file:
        file.write(text + '\n')