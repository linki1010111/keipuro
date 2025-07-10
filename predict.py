import os
import pickle
import src.readdata

project_root_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(project_root_path, "models", "best_model.pkl")
preprocessed_data_path = os.path.join(project_root_path, "data", "data_preprocessed.pkl")
data_path = os.path.join(project_root_path, "data", "data.txt")

with open(model_path, "rb") as f:
    predictor = pickle.load(f)
with open(preprocessed_data_path, "rb") as f:
    preprocessed_data, _ = pickle.load(f)

print(preprocessed_data[1:10])  # 前処理したデータを一部表示
sentence_array = readdata.read(data_path)
predictions = predictor.predict(preprocessed_data)
for i in range(len(predictions)):
    print(sentence_array[i], predictions[i])


