import os
import sys
project_root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root_path)
import src.humanread as humanread

file_path = os.path.join(project_root_path, "data", "human_processed_data.txt")
lis = humanread.read(file_path)
print(lis[:10])
