import os
def read(file_path: str):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                lines.append(line.split()) # 行末の改行文字と前後の空白を除去
    return lines
