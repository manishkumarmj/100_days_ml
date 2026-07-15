import streamlit as st
import pandas as pd 
import time  

st.title("Startup Dashboard")
st.header("I am learnign Streamlit ")
st.subheader("gand fat gaya hai bhai koie job dedo ")

st.write("this is the normal text")


st.markdown("""
### My fav movies
    - Race 3 
    - Wish Dragon
    - HouseFull             
            """)


st.code(""" 
de foo(input):
        return fooo ==2 

X = foo(2)
""")
st.latex('x^2+y^2= 10')



st.metric("Revenuse", 'Rs  3L', '-3%')
st.json({
    "name":['Nitish', 'Ankit', 'Anupam'],
    "marks":['70', '80', '90'],
    "name":['50L', '40L', '30L'],
})




st.sidebar.title("Sidebar ka title ")
col1, col2 = st.columns(2)
with col2:
    st.image(r'A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\startup-dashboard\image.png')
with col1:
    st.video(r'A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\startup-dashboard\Snap.mp4')
st.error("log in error")
st.success("log in done")
st.info("done ")
st.warning("warining")


# bar  = st.progress(0)
# for i  in range(1,101):
#     time.sleep(0.1) # delay 
#     bar.progress(i)


# # text input 
# email = st.text_input("etner the email ")
# number = st.number_input("Enter the age ")
# date = st.date_input("Dat e ")




# button 
email = st.text_input("etner the email ")
passwrod = st.text_input("Enter the passwrod")

btn = st.button("log in ")

if btn: 
    if email == "manishtheprogrammer@gmail.com"and passwrod == '1234':
        st.success('login Sucessfull')
        st.balloons()
    else:
        st.error("Invaid login details " )

# upload a file 

file = st.file_uploader("Upload a csv ")
if file is not None:
    df= pd.read_csv(file)
    st.dataframe(df.describe())
    