import pickle
import json

import numpy as np

class MedicalInsurance():
    def __init__(self,age,gender,bmi,children,smoker,region):
        self.age=age
        self.gender=gender
        self.bmi=bmi
        self.children=children
        self.smoker=smoker
        self.region=region
        return
    def load_model(self):
        #load model

        with open(r'artifacts\knn.pkl','rb') as f:
            self.model=pickle.load(f)
            print("model==",self.model)

        #load columns_names

        with open(r'artifacts\column_title.json','r') as f:
            self.column_title=json.load(f)
            print("column names==",self.column_title)

        #load scaler

        with open(r'artifacts\scaler.pkl','rb') as f:
            self.scaler=pickle.load(f)
            print("scaler==",self.scaler)

    def predicted_charges(self):
        self.load_model()
        test_array=np.zeros((1,self.model.n_features_in_))
        test_array[0][0]=self.age
        test_array[0][1]=self.column_title['gender'][self.gender]
        test_array[0][2]=self.bmi
        test_array[0][3]=self.children
        test_array[0][3]=self.column_title['smoker'][self.smoker]
        region='region_'+self.region
        index=self.column_title['column names'].index(region)
        test_array[0][index]=1

        print("test array is :",test_array)

        scaled_test_array=self.scaler.transform(test_array)

        predicted_charges=np.around(self.model.predict(scaled_test_array)[0],2)
        print("predicted charges :",predicted_charges)
        return predicted_charges


