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

def get_keys(val, file_dict):
    for key, value in file_dict.items():
        if val == value:
            return key

def main():
    """Spam Classifier with Streamlit"""
    
    st.title('Spam Classifier App')
    message_text = st.text_area("Enter Message", "Type here ...")
    
    prediction_labels = {"spam": 1, "non-spam":0}
    
    if st.button("Classify"):
        vect_text = spam_vectorizer.transform([message_text]).toarray()
        predictor = load_model("naive_bayes.pickle")
        prediction = predictor.predict(vect_text)
        if prediction == 1:
            st.warning("You message looks fishy ... Spam!")
        else:
            st.success("Your message doesn't look like a spam")
    #     st.write(prediction)
#         final_result = get_keys(prediction, prediction_labels)
#         st.success('You entered a {} message'.format(final_result))
        
if __name__=='__main__': 
    main()

# st.sidebar.slider('hour', 0, 15, 3)

# uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
#     if uploaded_file is not None:
#         image = Image.open(uploaded_file)
#         st.image(image, caption='Uploaded MRI.', use_column_width=True)
#         st.write("")
#         st.write("Classifying...")
#         label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
#         if label == 0:
#             st.write("The MRI scan has a brain tumor")
#         else:
#             st.write("The MRI scan is healthy")

# # this is the main function in which we define our webpage  
# def main():       
#     # front end elements of the web page 
#     html_temp = """ 
#     <div style ="background-color:yellow;padding:13px"> 
#     <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
#     </div> 
#     """
      
#     # display the front end aspect
#     st.markdown(html_temp, unsafe_allow_html = True) 
      
#     # following lines create boxes in which user can enter data required to make prediction 
#     Gender = st.selectbox('Gender',("Male","Female"))
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
#     ApplicantIncome = st.number_input("Applicants monthly income") 
#     LoanAmount = st.number_input("Total loan amount")
#     Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
#     result =""
      
#     # when 'Predict' is clicked, make the prediction and store it 
#     if st.button("Predict"): 
#         result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
#         st.success('Your loan is {}'.format(result))
#         print(LoanAmount)
     
# if __name__=='__main__': 
#     main()

# Alright, let’s now host this app to a public URL using pyngrok library.
# from pyngrok import ngrok
 
# public_url = ngrok.connect('8501')
# public_url



# brightness_4
# # success 
# st.success("Success") 
  
# # success 
# st.info("Information") 
  
# # success 
# st.warning("Warning") 
  
# # success 
# st.error("Error") 

# Diaplay Images 
  
# # import Image from pillow to open images 
# from PIL import Image 
# img = Image.open("streamlit.png") 
  
# # display image using streamlit 
# # width is used to set the width of an image 
# st.image(img, width=200) 

# radio button 
# first argument is the title of the radio button 
# second argument is the options for the ratio button 
# status = st.radio("Select Gender: ", ('Male', 'Female')) 
  
# conditional statement to print  
# Male if male is selected else print female 
# show the result using the success function 
# if (status == 'Male'): 
#     st.success("Male") 
# else: 
#     st.success("Female") 

# # import the streamlit library 
# import streamlit as st 

# # give a title to our app 
# st.title('Welcome to BMI Calculator') 

# # TAKE WEIGHT INPUT in kgs 
# weight = st.number_input("Enter your weight (in kgs)") 

# # TAKE HEIGHT INPUT 
# # radio button to choose height format 
# status = st.radio('Select your height format: ', 
# 				('cms', 'meters', 'feet')) 

# # compare status value 
# if(status == 'cms'): 
# 	# take height input in centimeters 
# 	height = st.number_input('Centimeters') 
	
# 	try: 
# 		bmi = weight / ((height/100)**2) 
# 	except: 
# 		st.text("Enter some value of height") 
		
# elif(status == 'meters'): 
# 	# take height input in meters 
# 	height = st.number_input('Meters') 
	
# 	try: 
# 		bmi = weight / (height ** 2) 
# 	except: 
# 		st.text("Enter some value of height") 
		
# else: 
# 	# take height input in feet 
# 	height = st.number_input('Feet') 
	
# 	# 1 meter = 3.28 
# 	try: 
# 		bmi = weight / (((height/3.28))**2) 
# 	except: 
# 		st.text("Enter some value of height") 

# # check if the button is pressed or not 
# if(st.button('Calculate BMI')): 
	
# 	# print the BMI INDEX 
# 	st.text("Your BMI Index is {}.".format(bmi)) 
	
# 	# give the interpretation of BMI index 
# 	if(bmi < 16): 
# 		st.error("You are Extremely Underweight") 
# 	elif(bmi >= 16 and bmi < 18.5): 
# 		st.warning("You are Underweight") 
# 	elif(bmi >= 18.5 and bmi < 25): 
# 		st.success("Healthy")		 
# 	elif(bmi >= 25 and bmi < 30): 
# 		st.warning("Overweight") 
# 	elif(bmi >= 30): 
# 		st.error("Extremely Overweight") 
