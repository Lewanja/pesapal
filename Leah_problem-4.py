# pip install markdown

import os

import markdownconversion


def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        raise Exception(f"File {input_file} cannot be found!")

    markdownconversion.markdownFromFile(
        input=input_file,
        output=output_file,
        encoding='utf8',
    )


if __name__ == "__main__":
    input_file = input("Enter input (.md) file name : ")
    output_file = input("Enter output (.html) file name : ")
    try:
        convert_markdown_to_html(input_file, output_file)
        print("Convertion successful!")
    except Exception as e:
        print(f"An error occurred : {e}")