import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform
import warnings
warnings.filterwarnings('ignore')
import pickle

df=pd.read_csv('data/project_coffee.csv', encoding='cp949')

target='target'

base_train= df.copy()

print(base_train)

base_train, base_test = train_test_split(base_train, train_size=0.80, test_size=0.20, 
                              stratify=base_train[target], random_state=2)
print(base_train.shape)
print(base_test.shape)

features = base_train.drop(columns=[target]).columns

X_base_train = base_train[features]
y_base_train = base_train[target]
X_base_test = base_test[features]
y_base_test = base_test[target]

encoder= OrdinalEncoder()

X_base_train= encoder.fit_transform(X_base_train)
X_base_test= encoder.fit_transform(X_base_test)

model=DecisionTreeClassifier()

model.fit(X_base_train,y_base_train)

y_pred = model.predict(X_base_test)

print('베이스 테스트 accuracy score:', accuracy_score(y_pred, y_base_test))




new_data = [['13000', '견과류', '고소', '싱글 오리진', '다크로스팅']]
new_data = pd.DataFrame(new_data, columns=['price', 'tasty1', 'tasty2', 'blend', 'roasting'])
now_data = encoder.transform(new_data)


print(model.predict(now_data))

with open("encoder.pkl", "wb") as encoder_file:
    pickle.dump(encoder, encoder_file)

with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)