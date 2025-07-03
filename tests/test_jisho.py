import os
import sys
project_root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.jisho as jisho

file_paths = []
file_paths.append(os.path.join(project_root_path, "data", "dictionary1.txt"))
file_paths.append(os.path.join(project_root_path, "data", "dictionary2.txt"))
lis = jisho.process_dictionaries_combined_from_paths(file_paths)
print(lis[:20])
