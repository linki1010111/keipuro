import os

def load_lines_from_text_file(file_path: str):
 
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line.strip()) # 行末の改行文字と前後の空白を除去
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'. Please check the path and ensure the file exists.")
        return []
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}")
        return []
    return lines