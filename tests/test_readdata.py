import os
import sys
project_root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.readdata as readdata

file_path = os.path.join(project_root_path, "data", "dataset.txt")
lis = readdata.load_lines_from_text_file(file_path)
print(lis)
