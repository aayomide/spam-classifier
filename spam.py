#!/usr/bin/env python
# coding: utf-8

# import libraries
import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# load vectorizer
spam_vectorizer = joblib.load(open("naive_bayes_vectorizer.pickle", "rb"))

# load model
def load_model(model_file):
    classifier = joblib.load(open(os.path.join(model_file), "rb"))
    return classifier


def main():
    """Spam Classifier with Streamlit"""
    
    st.title('Spam Classifier App')
    message_text = st.text_area("Enter Message", "Type here ...")
    
    if st.button("Classify"):
        vect_text = spam_vectorizer.transform([message_text]).toarray()
        predictor = load_model("naive_bayes.pickle")
        prediction = predictor.predict(vect_text)
        if prediction == 1:
            st.warning("You message looks fishy ... Spam!")
        else:
            st.success("Your message doesn't look like a spam")

        
if __name__=='__main__': 
    main()