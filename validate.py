import os
import sys
import pickle
import src.my_library.validator as validator

def find_best_model(models_path, data_path):
    v = validator.Validator()
    v.load_data(data_path)

    best_accuracy = 0
    best_model_file_path = None

    for model_file in os.listdir(models_path):
        model_file_path = os.path.join(models_path, model_file)
        v.load_model(model_file_path)
        accuracy, precision, recall = v.evaluate_model()
        print(f"Evaluating {model_file}:")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model_file_path = model_file_path

    if best_model_file_path is not None:
        best_model_file_path_dest = os.path.join(models_path, 'best_model.pkl')
        v.load_model(best_model_file_path)
        with open(best_model_file_path_dest, 'wb') as f:
            pickle.dump(v.model, f)
        print(f"The best model is saved as 'best_model.pkl' with accuracy: {best_accuracy}")


data_path = "data/preprocessed_validation.txt"
models_path = []
models_path.append()
find_best_model(models_path, data_path)
