import os
from src import accuracy_result
from src import humanread
from src import jisho
from src import make_textfile
from src import readdata
from src import to_compare_read
from src import yosoku

file_paths = []
file_paths.append("data/dictionary1.txt")
file_paths.append("data/dictionary2.txt")
d = jisho.process_dictionaries_combined_from_paths(file_paths)
ds = readdata.load_lines_from_text_file("data/dataset.txt")
result = yosoku.yosoku(d,ds)
print(result[:10])
