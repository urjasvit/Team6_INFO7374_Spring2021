**DATA DRIVEN MARKETING CAMPAIGN**

Google Document link:  https://docs.google.com/document/d/11BTPVjhLBjqAOkuNMwqoC7e5SJr7otwuiVliR092pA8/edit#heading=h.fmgdyd5iuj2h

Clat Documentation: https://codelabs-preview.appspot.com/?file_id=11BTPVjhLBjqAOkuNMwqoC7e5SJr7otwuiVliR092pA8#3


**Overview**

Marketing campaigns are generally characterized by focusing on customer needs and their overall satisfaction.

There are many different reasons to determine whether a marketing campaign will be successful or not. Some of the important features of a marketing campaign can be the segmentation of the population, finding appropriate distribution channels to reach the customer’s place, analyzing previous campaigns and designing the promotional strategies.

![image](https://user-images.githubusercontent.com/25616463/115968946-4c199b00-a508-11eb-9d30-c8ef01035264.png)


**Business Case**

Here is a banking institution seeing customer and revenue declines. After some root cause analysis it is found that there is a revenue decline in the area of fixed term deposits. These term deposits allow banks to hold onto a deposit for a specific amount of time, so banks can lend more and thus make more profits. In addition, banks also hold a better chance to persuade term deposit clients into buying other products such as funds or insurance to further increase their revenues.

The institution wants to run a marketing campaign to increase and retain their customers. So as an algorithmic market strategist we have to perform analysis with the data provided by the bank (customer details and their previous campaign), help them run a successful campaign and prevent customers from churning.


**Dataset Description**

The dataset contains details of marketing campaigns done via phone with other details for customers such as demographics, last campaign details etc. There are around 45,000 unique values and 18 columns which are already divided into train and test. The link to the dataset is provided in the “References” section.

![image](https://user-images.githubusercontent.com/25616463/115968967-79664900-a508-11eb-861d-ee4af2c8acb6.png)


**Strategies for the Marketing Campaign**

Firstly, we need to understand the customer demographics and perform customer segmentation so as to get the prospective customers. Then we need to find the most effective strategy in order to get the most out of this marketing campaign. Some of the questions can be what segment of the population should we address? which instrument should we use to get our message out? (Ex: Telephones, Radio, TV, Social Media Etc.). Lastly, we need to perform in-depth analysis of previous campaigns (If possible) in order to learn from previous mistakes and to determine how to make the marketing campaign much more effective. Along with that we need to determine the churn rates of the customers so as to prevent them from leaving.

**Flow Diagram**

The Flow diagram for the project would be like below. The raw csv file will be uploaded to the Google drive so that it can be easily accessed by the Google Colaboratory where we will perform Customer Segmentation on the dataset as well as build other marketing and machine learning models. As for reporting, we will store the data onto the cloud and access the tables using relational databases and use connectors to connect with the data reporting tools like Data Studio or Einstein Analytics. All of these will be put on the Streamlit web framework to host the findings and this whole architecture will be deployed on Heroku platform.

 


**Customer Segmentation**

In the context of customer segmentation, we will implement cluster analysis. It is a mathematical model used to discover groups of similar customers based on finding the smallest variations among customers within each group.
The goal of customer segmentation in marketing is to accurately segment customers in order to derive more effective marketing strategies via personalization. For this project, we will be using a clustering method to perform segmentation on our customer database. This will help the bank to classify and understand their customers and effectively design their marketing strategy. 

![image](https://user-images.githubusercontent.com/25616463/115968999-af0b3200-a508-11eb-89b5-7940537beb8c.png)


**Customer Retention Metrics**

We can know our best customers by segmentation and lifetime value prediction, we should also work hard on retaining them. That is why retention rate is one of the most critical metrics.
Customer retention measurement refers to the steps taken to uncover and document how well a business is retaining customers.Organizations track success in this area to see how well they are meeting customer needs and if they are continuing to earn their business over time. 

Here in this section we will look at some of the customer retention metrics applicable to retaining their customers from previous campaigns and we will compare between them.

![image](https://user-images.githubusercontent.com/25616463/115969018-d235e180-a508-11eb-9bcc-6cc04c17f8ec.png)


**Testing Design & Execution**

To see how the model behaves when it is put to test, we will execute our test programmatically and report the statistics behind it. For that we will create our own dataset and evaluate different possibilities and evaluate results.

**Streamlit Application Deployment**

Deployment Link: https://share.streamlit.io/urjasvit/proj/main/streamlit.py


![image](https://user-images.githubusercontent.com/25616463/116770105-30822900-aa0f-11eb-9de3-f23566354070.png)

![image](https://user-images.githubusercontent.com/25616463/116770107-37a93700-aa0f-11eb-99e3-f24211286018.png)

![image](https://user-images.githubusercontent.com/25616463/116770113-41329f00-aa0f-11eb-9edc-faed68b75f2c.png)


**BI REPORTING AND DASHBOARDS**
The Tableau Dashboards are generated as below:


