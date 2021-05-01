import streamlit as st
import pandas as pd
import subprocess
import sys
import os
from sklearn import datasets
from sklearn.feature_selection import RFE
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
import base64
from io import BytesIO
#import xlsxwriter
#import matplotlib.pyplot as plt

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('xlsxwriter')
import xlsxwriter

data=pd.read_csv("./data.csv")

cat_vars=['job_type','marital','education','default','housing_loan','personal_loan','communication_type','day_of_month','month','prev_campaign_outcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(data[var], prefix=var)
    data1=data.join(cat_list)
    data=data1

cat_vars=['job_type','marital','education','default','housing_loan','personal_loan','communication_type','day_of_month','month','prev_campaign_outcome']
data_vars=data.columns.values.tolist()
to_keep=[i for i in data_vars if i not in cat_vars]

data_final=data[to_keep]
#data_final.columns.values

#data.shape

data_final_vars=data_final.columns.values.tolist()
y=['term_deposit_subscribed']
X=[i for i in data_final_vars if i not in y]

X.remove('id')

temp = X


logreg = LogisticRegression()

rfe = RFE(logreg, 18)
rfe = rfe.fit(data_final[X], data_final[y] )

rk= rfe.ranking_
cols=list()
for x,y in zip(rk,temp):
  if(x==1):
    cols.append(y)

X=data_final[cols]
y=data_final['term_deposit_subscribed']


logit_model=sm.Logit(y,X)
result=logit_model.fit()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

@st.cache
def reg(test_data):
	cat_vars=['job_type','marital','education','default','housing_loan','personal_loan','communication_type','day_of_month','month','prev_campaign_outcome']
	for var in cat_vars:
	    cat_list='var'+'_'+var
	    cat_list = pd.get_dummies(test_data[var], prefix=var)
	    test_data1=test_data.join(cat_list)
	    test_data=test_data1

	cat_vars=['job_type','marital','education','default','housing_loan','personal_loan','communication_type','day_of_month','month','prev_campaign_outcome']
	test_data_vars=test_data.columns.values.tolist()
	to_keep=[i for i in test_data_vars if i not in cat_vars]

	test_data_final=test_data[to_keep]
	test_data_final_vars=test_data_final.columns.values.tolist()
	X=[i for i in test_data_final_vars]

	Z = test_data[cols]
	return Z


def retent():
	segmentation=pd.read_csv("./segmentation_data.csv")
	previous_campaign = segmentation['prev_campaign_outcome'].value_counts()
	st.table(previous_campaign)

	current_campaign = segmentation['term_deposit_subscribed'].value_counts()
	st.table(current_campaign)

	total_count = segmentation['prev_campaign_outcome'].count()
	st.write("Total count of people participated in both the campaigns:",total_count)

	Retention_prev_camp = previous_campaign['success']*1.0/total_count
	st.write("Success Rate of the previous campaign:",Retention_prev_camp*100)

	Retention_cur_camp = current_campaign[1]*1.0/total_count
	st.write("Success Rate of this campaign:",Retention_cur_camp*100)


#########################################################
st.sidebar.subheader("SELECT FROM BELOW")
add_selectbox = st.sidebar.radio("  ",
    ("Term Deposit Prediction", "Customer Segmentation" , "Customer Retention Metrics")
)

if add_selectbox == 'Term Deposit Prediction' :
        st.title("Term Deposit Prediction")
        st.write("-------------------------------------------------------------------------------------------------")
        st.write("Enter the Below Information")
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
        	df = pd.read_csv(uploaded_file)
        
        if st.button("Predict"):
        	input_data = reg(df)
        	prediction = logreg.predict(input_data)
        	predict_probability = logreg.predict_proba(input_data)
        	df['predicted']=prediction
        	def to_excel(df):
        		output = BytesIO()
        		writer = pd.ExcelWriter(output, engine='xlsxwriter')
        		df.to_excel(writer, sheet_name='Sheet1')
        		writer.save()
        		processed_data = output.getvalue()
        		return processed_data

        	def get_table_download_link(df):
        		val = to_excel(df)
        		b64 = base64.b64encode(val)
        		return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download csv file</a>'
        		#csv = df.to_csv(index=False)
        		#b64 = base64.b64encode(csv.encode()).decode() 
        		#href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
        	st.markdown(get_table_download_link(df), unsafe_allow_html=True)
        	#st.markdown(get_table_download_link(df), unsafe_allow_html=True)

elif add_selectbox == 'Customer Segmentation':
        st.title("Customer Segmentation")
        st.write("-------------------------------------------------------------------------------------------------")
        import warnings
        from sklearn.cluster import KMeans
        warnings.filterwarnings("ignore")
        data= pd.read_csv("./data.csv")
        def order_cluster(cluster_field_name, target_field_name,df,ascending):
        	new_cluster_field_name = 'new_' + cluster_field_name
        	df_new = df.groupby(cluster_field_name)[target_field_name].mean().reset_index()
        	df_new = df_new.sort_values(by=target_field_name,ascending=ascending).reset_index(drop=True)
        	df_new['index'] = df_new.index
        	df_final = pd.merge(df,df_new[[cluster_field_name,'index']], on=cluster_field_name)
        	df_final = df_final.drop([cluster_field_name],axis=1)
        	df_final = df_final.rename(columns={"index":cluster_field_name})
        	return df_final
        sse={}
        df_cluster = data[['balance']]
        for k in range(1, 10):
        	kmeans = KMeans(n_clusters=k, max_iter=1000).fit(df_cluster)
        	df_cluster["clusters"] = kmeans.labels_
        	sse[k] = kmeans.inertia_ 
        kmeans = KMeans(n_clusters=4)
        kmeans.fit(data[['balance']])
        data['BalanceCluster'] = kmeans.predict(data[['balance']])
        data = order_cluster('BalanceCluster', 'balance',data,True)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(data[['customer_age']])
        data['AgeCluster'] = kmeans.predict(data[['customer_age']])
        data = order_cluster('AgeCluster', 'customer_age',data,True)
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(data[['spending_score']])
        data['SpendingCluster'] = kmeans.predict(data[['spending_score']])
        data = order_cluster('SpendingCluster', 'spending_score',data,True)
        data['OverallScore'] = data['AgeCluster'] + data['BalanceCluster'] + data['SpendingCluster']
        st.table(data.groupby('OverallScore')['customer_age','balance','spending_score'].mean())


elif add_selectbox == 'Customer Retention Metrics':
    st.title("Customer Retention Metrics")
    st.write("-------------------------------------------------------------------------------------------------")
    retent()    
