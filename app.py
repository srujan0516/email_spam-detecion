import streamlit as st
import pickle


model = pickle.load(open('model.pkl','rb'))
cv=pickle.load(open('vectorizer.pkl','rb'))

st.title("Email spam classification application ")
st.write("This is a Machine Learing application to classify emails as spam or not spam")
user_input=st.text_area("Enter your email to check spam or ham",height=150)

if st.button("classify"):
    if user_input:
        data=[user_input]
        vectorized_data =cv.transform(data).toarray()
        result = model.predict(vectorized_data)
        if result[0]==0:
            st.write("The email is not spam")
        else:
            st.write("The email is spam")
    else:
        st.write("Please enter some text to Classify")