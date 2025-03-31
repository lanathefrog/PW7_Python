from app.io.output import output_text, write_file_builtin
from app.io.input import read_file_builtin, read_file_pandas

def main():
    builtin_file_path = 'tests/test_builtin.txt'
    pandas_file_path = 'tests/test_pandas.csv'
    output_file_path = 'output.txt'
    with open(output_file_path, 'w') as file:
        pass
    try:
        builtin_content = read_file_builtin(builtin_file_path)
        output_text(builtin_content)
        write_file_builtin(output_file_path, builtin_content)
    except FileNotFoundError as e:
        output_text(str(e))
        write_file_builtin(output_file_path, str(e))

    try:
        pandas_content = read_file_pandas(pandas_file_path)
        output_text(pandas_content)
        write_file_builtin(output_file_path, pandas_content)
    except FileNotFoundError as e:
        output_text(str(e))
        write_file_builtin(output_file_path, str(e))

if __name__ == '__main__':
    main()