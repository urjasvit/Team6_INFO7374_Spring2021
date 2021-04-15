**OVERVIEW**

Work with Salesforce to understand the influence of various variables on sales and study various attribution models in marketing industry.

CLAT Document:

https://codelabs-preview.appspot.com/?file_id=1WTl_DgOk29SIe2lGTfnt94EPS64dhGJYyxwDdThJO5M#5

https://codelabs-preview.appspot.com/?file_id=1UP13EM8wQdpV3y8zv7VS4uw26IJR5k9ZFmzB5krfPUE#2

Google Document:

https://docs.google.com/document/d/1WTl_DgOk29SIe2lGTfnt94EPS64dhGJYyxwDdThJO5M/edit?ts=60628e86#

https://docs.google.com/document/d/1UP13EM8wQdpV3y8zv7VS4uw26IJR5k9ZFmzB5krfPUE/edit?ts=605ff4f1#

**Part-A Assignment**

AdStock Analysis on Sales data

Dataset Description:

![image](https://user-images.githubusercontent.com/25616463/114882996-82516f00-9dd2-11eb-9e2d-f319fdee19d6.png)

* Sales Related to Weekly Numbers: 
As per the data given, base sales ranges from estimately $999 to $1197 from week 1 to week 260, respectively. In between, there is a pattern in which sales gradually increases as the week progresses but then it dips again before it increases till the end. The weekly sales are highest at $1222 on week 223 and lowest of $989 on week 38.

* Effects of TV spending to Sales: 
We now will try to understand if there is any correlation between weekly sales and TV spending. There is no conclusive evidence which says that TV spending affects weekly sales.


* Effects of adStock for TV ad Spending: 
Here, barring some anomalies there is a general trend where increase or decrease in Adstock affects TV spending. To understand better the non-zero values of TV spending are taken so that the adstock effects can be analysed.


* Effects of Radio Spending on Sales: 
For this too we have taken non-zero values to analyse the effects of radio spending on weekly sales. The radio spending is more effective on sales which overall uplift the sales price.


* Effects of adStock for Radio Ad Spending: 
For understanding the effects of Adstock on Radio Ad Spending, we have a combination of TV and Radio sales for adstock models(tv_radio_sales_1_adstock and tv_radio_sales_2_adstock). The below plot depicts that the adstock models have similar cycles with different magnitude but they don't have much effect on Spending. This could be because we don’t have separate models for Radio.


**Part-B Assignment**

Attribution Modeling

Attribution modeling is a framework for analyzing which touchpoints, or marketing channels, receive credit for a conversion. Each attribution model distributes the value of a conversion across each touchpoint differently.
A model comparison tool allows you to analyze how each model distributes the value of a conversion.

Types of Attribution models discussed:

* FIRST TOUCH ATTRIBUTION MODEL
* LAST TOUCH ATTRIBUTE MODEL    
* LINEAR ATTRIBUTION    
* TIME DECAY ATTRIBUTION MODEL    
* U-SHAPED ATTRIBUTION MODEL    
* LOGISTIC REGRESSION

**Conclusion**

It is seen in general that Data Driven models perform far better than any traditional heuristic methods. Both in terms of Accuracy to predict conversions as well as Simulating the ROI after optimizing for Budget. From Single and Multi Touch models, Time Decay performs better than others. It can also seen that the right value of pitch also determines the way model performs.
