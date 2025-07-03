import os 
import sys
import src.my_library.trainer as trainer

preprocessed_train_data_path = input("Enter the path for the preprocessed data:")
model_dump_path_base = input("Enter the path for the directory to save the models:")

t = trainer.Trainer()
X, y = t.load_data(preprocessed_train_data_path)
#print(X[0:2])
#print(y[0:2])
hyperparameters = [0.1,1,10,100,1000,10000]
for h in hyperparameters:
    model_dump_path = model_dump_path_base + "SVM_" + str(h) + ".pkl"
    print(model_dump_path)
    t.train_SVM(h, X, y)
    t.dump_model(model_dump_path)


hyperparameters = [1,2,3,4,5]
for h in hyperparameters:
    model_dump_path = model_dump_path_base + "RF_" + str(h) + ".pkl"
    t.train_RF(h, X, y)
    t.dump_model(model_dump_path)
