import streamlit as st
import pandas as pd 


# dataframe 
df = pd.read_csv("A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\Startup_funding_mini_project\startup_funding.csv")
st.sidebar.title("Startup Funding Analysis")

# filling NA  value in Investors Name

df['Investors Name']=df['Investors Name'].fillna('Undisclosed')


# creating list of Drop down 

option=st.sidebar.selectbox("Select One", ["Overall Analysis", "Start-up", "Investor"])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "Start-up":
    st.sidebar.selectbox("Select Star-UP", sorted(df['Startup Name'].unique().tolist())) # passed all the unique value from startup column
    btn1 = st.sidebar.button("find Start-up Details")
    st.title("Start-up Analysis")
else:
    st.sidebar.selectbox("Select Star-UP", sorted(df['Investors Name'].unique().tolist()))
    btn2 = st.sidebar.button("find Investor  Details")
    st.title("Investor Analysis")


