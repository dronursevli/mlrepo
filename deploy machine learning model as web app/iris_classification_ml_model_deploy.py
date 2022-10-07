# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:30:48 2022

@author: ONUR
"""

import gradio as gr
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#%%

iris_dataset = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

#%% modeli kaydet
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(knn, f) 

#%% daha önce kaydedilmiş modeli geri yükle

def make_prediction(sepal_length, sepal_width, petal_length, petal_width):
    with open("model.pkl", "rb") as f:
        clf  = pickle.load(f)
    
    preds = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return "Tahmin sonucu:"+str(preds[0])


#Veri girişi için gradio arayüzünde 4 adet alan oluştur

sepal_length_input = gr.Number(label = "Sepal length")
sepal_width_input = gr.Number(label= "Sepal width")
petal_length_input = gr.Number(label = "Petal length")
petal_width_input = gr.Number(label= "Petal width")
# We create the output
output = gr.Textbox(label="Sonuç")

# alttaki kod bölmesinde özelleştirilmiş arayüz tasarımı var.
app = gr.Interface(fn = make_prediction, inputs=[sepal_length_input, sepal_width_input, petal_length_input, petal_width_input], outputs=output)
app.launch()
#%% özelleştirilmiş arayüz

def predict(sepal_length, sepal_width, petal_length, petal_width):
    with open("model.pkl", "rb") as f:
        clf  = pickle.load(f)
   
    preds = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return "Tahmin sonucu:"+str(preds[0])
  
    
with gr.Blocks() as demo:
    gr.Label(value="Iris Species Prediction", label="")
    sl = gr.Number(label = "Sepal length")
    sw = gr.Number(label= "Sepal width")
    pl = gr.Number(label = "Petal length")
    pw = gr.Number(label= "Petal width")
    submit_btn = gr.Button("predict")
    outputbox = gr.Label(label="Sonuç")

    
    submit_btn.click(fn=predict, inputs=[sl, sw, pl, pw], outputs=outputbox)



demo.launch()