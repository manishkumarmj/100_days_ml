import streamlit as st
import pandas as pd  
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide",page_title="Startup Analysis")  


# dataframe 
df = pd.read_csv(r'A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\Startup_funding_mini_project\startup_clean.csv')
df2 = pd.read_csv(r'A:\AIML_DEV_FOLDER\Data visualization_Web_dev\Z_P_Streamlit\Startup_funding_mini_project\startup_clean.csv')
def load_overall_analysis ():
    st.title("overall analysis")
    # total_invested_amount
    total = round(df2['amount'].sum())
    st.metric("Toal", str(total) + "Cr")


     # maxed amount

    max_funding = df2.groupby('starup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    st.metric("Max", str(max_funding) + "Cr") 
    #average
    mean_funding = df.groupby('starup')['amount'].sum().mean()
    st.metric("Mean", str(mean_funding) + "Cr") 

    # total funded startup 
    nums = df['starup'].nunique()
    st.metric("total number of funded ", str(nums)  ) 


    st.header("Mom graph")
    temp_df['df']




















df.loc[df['amount'] == 0, 'amount'] = np.random.randint(10, 101, size=(df['amount'] == 0).sum())















def load_investor_details(investor):
    st.title(investor)
    # last 5 
    last_5 =  df[df['investors'].str.contains(investor)].head()[["date","starup","Vertical","Round","amount"]]
    st.subheader("most recent investment ")
    st.dataframe(last_5)



    #  bigest investment 
    biggest=df[df['investors'].str.contains(investor)].groupby("starup")['amount'].sum().sort_values(ascending=False).head()
    st.subheader("Big boie")
    fig,ax = plt.subplots()
    ax.bar(biggest.index,biggest.values)
    st.pyplot(fig)



    # vertical round
    vertical_series = df[df['investors'].str.contains(investor)].groupby('Vertical')["amount"].sum()
    st.subheader('Sectors invested in vertical round')
    fig1, ax1 = plt.subplots()
    ax1.pie(vertical_series.values, labels=vertical_series.index, autopct='%1.1f%%')
    st.pyplot(fig1)
    
    
    # city  


    city_series = df[df['investors'].str.contains(investor, case=False, na=False)].groupby('city')["amount"].sum().sort_values(ascending=False).head(5)
    st.subheader('city inviested in ')
    fig2, ax2 = plt.subplots()
    ax2.pie(city_series.values, labels=city_series.index, autopct='%1.1f%%')
    ax2.axis('equal')
    st.pyplot(fig2)


    # stage_series
    stage_series = df[df['investors'].str.contains(investor, case=False, na=False)].groupby('Round')["amount"].sum().sort_values(ascending=False).head(3)

    st.subheader('Stage ')
    fig3, ax3 = plt.subplots()
    ax3.pie(stage_series.values, labels=stage_series.index, autopct='%1.1f%%')
    ax3.axis('equal')
    st.pyplot(fig3)


    # year on year
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year']=df["date"].dt.year 
    year_on_year=df[df['investors'].str.contains(investor)].groupby('year')["amount"].sum()
    st.subheader("Year on year growth")
    fig4,ax4 = plt.subplots()
    ax4.plot(year_on_year.index,year_on_year.values)
    st.pyplot(fig4)





# creating list of Drop down 

option=st.sidebar.selectbox("Select One", ["Overall Analysis", "Start-up", "Investor"])

if option == "Overall Analysis":
    btn0= st.sidebar.button("show over all analysis")
    if btn0:
        load_overall_analysis()

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
        



