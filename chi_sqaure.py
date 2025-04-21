import streamlit as st
import pandas as pd
import scipy.stats as stats

def chi_square_test(df,col1,col2):
    contingency_table = pd.crosstab(df[col1],df[col2])
    st.write(contingency_table)
    chi2,pvalue,dof,expected=stats.chi2_contingency(contingency_table)
    st.write(f"Chi_square test between {col1} and {col2}\n")
    st.write(f"Chi square value : {round(chi2),3}\n")
    st.write(f"P value : {pvalue}\n")
    st.write(dof)
    st.write(expected)
    st.write(pd.DataFrame(expected,index = contingency_table.index, columns = contingency_table.columns))
    alpha = 0.05
    if  alpha > pvalue:
      st.write(f"Reject null hypothesis\n{col1} influences {col2}")
    else:
      st.write(f"Accept null hypothesis\n{col1} is independant to {col2}")

st.title('Calculating dependency of variables in product selection')

dictx = {

    "Gender": ['Male', 'Female', 'Male', 'Female', 'Male'] * 5,
    "Age": ['Adult', 'Adult', 'Child', 'Child', 'Adult'] * 5,
    "productpref": ['A', 'B', 'C', 'A', 'C'] * 5

}

df = pd.DataFrame(dictx)
st.subheader('Original Data')
st.write(df)

listx = ['Gender','Age','productpref']

user1 = st.selectbox("Enter the first column name : ",listx)
user2 = st.selectbox("Enter the second column name :",listx)

if st.button("analyse"):
    chi_square_test(df, user1, user2)


