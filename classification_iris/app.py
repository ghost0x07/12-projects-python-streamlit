import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

"""
# Simple Iris Species Prediction

This app predicts the species of Iris flower from its measurements
"""

st.sidebar.header("Input Parameters")


target_names = load_iris().target_names


@st.cache_resource
def iris_classifier() -> RandomForestClassifier:
    print("Training classifier")
    iris = load_iris()
    clf = RandomForestClassifier().fit(iris.data, iris.target)
    return clf


def user_input_features():
    sepal_length = st.sidebar.slider("sepal_length", 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider("sepal_width", 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider("petal_length", 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider("petal_width", 0.1, 2.5, 0.2)
    data = [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width,
    ]

    return data


clf = iris_classifier()
input = user_input_features()
prediction = clf.predict([input])
predict_proba = clf.predict_proba([input])


"## Prediction"
st.write(target_names[prediction])

"## Prediction Probablities"
st.write(predict_proba)
