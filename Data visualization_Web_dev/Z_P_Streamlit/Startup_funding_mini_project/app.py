import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 


# dataframe 
df = pd.read_csv(r'A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\Startup_funding_mini_project\startup_clean.csv')




def load_investor_details(investor):
    st.title(investor)
    # last 5 
    last_5 = df[df["investors"].str.contains('investor')].head()[["date","starup","Vertical","Round","amount"]]
    st.subheader("most recent investment ")
    st.dataframe(last_5)
    # bigest investment 
    biggest=df[df['investors'].str.contains('investor')].groupby("starup")['amount'].sum().sort_values(ascending=False).head(5)
    st.subheader("Big boie")
    st.dataframe(biggest)
    fig,ax = plt.subplots()
    ax.bar(biggest.index,biggest.values)
    st.pyplot(fig)


    fig, ax = plt.subplots()
    ax.pie(biggest.values, labels=biggest.index, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures pie is circular
    st.pyplot(fig)

# filling NA  value in Investors Name




# creating list of Drop down 

option=st.sidebar.selectbox("Select One", ["Overall Analysis", "Start-up", "Investor"])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "Start-up":
    st.sidebar.selectbox("Select Star-UP", sorted(df['starup'].unique().tolist())) # passed all the unique value from startup column
    btn1 = st.sidebar.button("find Start-up Details")
    st.title("Start-up Analysis")
else:

    st.title("Investor Analysis")

    selected_investor=st.sidebar.selectbox("Select Star-UP", sorted(set(df['investors'].str.split(',').sum())))

    btn2 = st.sidebar.button("find Investor  Details")
    if btn2: 
        load_investor_details(selected_investor)
        



