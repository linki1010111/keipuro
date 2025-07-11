from sklearn.linear_model import LinearRegression
import lightgbm as lgb
import sklearn.svm as SVM
import sklearn.ensemble as Ensemble
import pickle
import numpy

class Trainer:
    def __init__(self):
        """
        Trainerクラスのコンストラクタ。
        """
        self.model = None  # モデルを格納するインスタンス変数を初期化
    def load_data(self, file_path):
        """
        データセットのファイルパスからデータを読み込み、特徴量とラベルを分けて返す。
        Args:
            file_path (str): データセットのファイルパス

        Returns:
            X (numpy.ndarray): 前処理済みの訓練データ
            y (numpy.ndarray): ラベルデータ
        """        
        with open(file_path, 'rb') as f:
            X, y = pickle.load(f)        
        return X, y
        
    def dump_model(self, file_path):
        """
        学習したモデルを指定されたファイルパスに保存する。
        Args:
            file_path (str): モデルを保存するファイルパス
        """ 
        with open(file_path, 'wb') as f:
            pickle.dump(self.model, f)

    def train_SVM(self, hyperparameter, X, y):
        self.model = SVM.SVC(C=hyperparameter)
        self.model.fit(X,y)

    def train_RF(self, hyperparameter, X, y):
        self.model = Ensemble.RandomForestClassifier(max_depth=hyperparameter)
        self.model.fit(X,y)
    def train_LR(self ,X ,y):
        self.model = LinearRegression()
        self.model.fit(X,y)
        
        
