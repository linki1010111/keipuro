from src import accuracy_result
from src import humanread
from src import jisho
from src import make_textfile
from src import readdata
from src import to_compare_read
from src import yosoku

d1 = src.jisho.process_dictionaries_combined_from_paths("data/dictionary1.txt")
d2 = src.jisho.process_dictionaries_combined_from_paths("data/dictionary1.txt")
ds = src.readdata.load_lines_from_text_file("data/dataset.txt")
result = yosoku(d1,d2,ds)
