

# imports
import streamlit as st
import pandas as pd
import seaborn as sns

# title and subheader
st.title('Data Analysis')
st.subheader('Data Analysis Using Python & Streamlit')

#upload dataset
upload=st.file_uploader('Upload Your Dataset (In CSV Format)')
if upload is not None:
    data=pd.read_csv(upload)

# 3 show dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())
# 4 check the data type of each columns
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)
# 5 find the shape of dataset (number of rows and columns)
if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?",('Rows','Columns'))
    if data_shape=='Rows':
        st.text('Number Of Rows')
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text('Number Of Columns')
        st.write(data.shape[1])
# 6 find the null values in data set
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox('Null Values in the Dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success(" No Missing values found")
        
# 7 handle duplicate values in dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning('This DataSet Contains Duplicate Values')
        dup=st.selectbox("Do you want to remove duplicate values?",\
                         ('Select One',"Yes","No"))
        if dup=="Yes":
           data=data.drop_duplicates()
           st.text('Duplicates are removed')
        if dup=='No':
           st.text("Ok No Problem")
# 8 overall statistics
if upload is not None:
    if st.checkbox('Summary of Dataset'):
        st.write(data.describe(include='all'))
# 9 About section
if st.button('About App'):
    st.text('Built With Streamlit')
    st.text('Thanks To Streamlit')
#.by
if st.checkbox('By'):
    st.success("Basit Hasnain")