from app.io.output import output_text, write_file_builtin

def main():
    text = "Hello, World!"
    output_text(text)
    write_file_builtin('output.txt', text)

if __name__ == '__main__':
    main()