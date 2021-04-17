import streamlit as st
import pandas as pd



#########################################################
st.sidebar.subheader("SELECT SEARCH METHOD")
add_selectbox = st.sidebar.radio("  ",
    ("Cosine Image Similarilty", "FAISS")
)

if add_selectbox == 'Cosine Image Similarilty' :
        st.title("Cosine Similarity Search")
        st.write("-------------------------------------------------------------------------------------------------")
        df=pd.read_csv('method1.csv')
            
elif add_selectbox == 'Spotify annoy':
        st.title("Similar Products using Faiss - Facebook AI Similarity Search")
        st.write("-------------------------------------------------------------------------------------------------")
        
        
elif add_selectbox == 'FAISS':
    st.title("Similar Products using Faiss - Facebook AI Similarity Search")
    st.write("-------------------------------------------------------------------------------------------------")
    df=pd.read_csv('df.csv')

n=1
images = df['0'].unique()
temp= st.selectbox('Select', ['Select from dropdown','Upload a file'])
if temp== 'Select from dropdown':
    #images1 = df['second']
    st.subheader("Select a Product :")
    pic = st.selectbox('Choices:', images)
    st.write("**You selected:**")
    st.image(pic,width=None)
    z = st.slider('Select Number of Similar Products:', 1, 9, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    st.write('**Similar Products:**')
    for index, row in df.iterrows():
        if row['0']==pic:
            while n < z+1:
                st.image(row[n], use_column_width=None, caption=row[n])
                n+=1
elif temp == 'Upload a file':
    try:
        pic=[]
        mfile= st.file_uploader("eadsx", accept_multiple_files=True)

        for file in mfile:
            p=file.name
            pic.append(p)
        for i in pic:
            st.image(i,width=None)
    except:
        st.write("errer")

count = 1
try:
    z = st.slider('Select Number of Similar Products:', 1, 9, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Output:")
    for index, row in df.iterrows():
        for i in pic:
            n=1
            if row['0']==i:
                st.write('**Similar Products for ** ', i)
                count=count+1
                while n < z+1:
                    st.image(row[n], use_column_width=None, caption=row[n])
                    n+=1
                st.write("-------------------------------------------------------------------------------------------------")
except:
    pass