**OVERVIEW**

Querying and connecting Snowflake sample database TPCDS_SF10TCL with Einstein Analytics. Using the live connection in Einstein Analytics, we created dashboards to solve the business use cases. 

**Einstein Analytics Dashboard with live integration in Snowflake:**
https://northeasternuniversity32-dev-ed.my.salesforce.com/analytics/wave/dashboard?assetId=0FK4x000000Vj0FGAS&orgId=00D4x000006thN3&loginHost=na150.salesforce.com&urlType=sharing&pageId=d9c58001-0357-4b48-8d02-85790a5dfbed&savedViewId=8wk4x000000GtBVAA0&analyticsContext=analyticsTab

**Google document link** 

https://docs.google.com/document/d/1VPjA4rT1H5A013K2hnvU8xeMVsjPxekXQWmrF_VkodY/edit?usp=sharing

**Clat document**

https://codelabs-preview.appspot.com/?file_id=1VPjA4rT1H5A013K2hnvU8xeMVsjPxekXQWmrF_VkodY#0


**Part A Assignment:**

Evaluate the products, marketing campaigns and strategies used by Japanese company Shiseido.
![image](https://user-images.githubusercontent.com/25616463/114880005-ad868f00-9dcf-11eb-91b3-cba5458813e3.png)

Shiseido is one of the great titans in the skincare industry, and they have been continuously creating unique and beneficial products and treatments for decades.
In 1918, Shiseido launched its perfume and by the end of 1937, it came out with its first skin care line cosmetics. Since then, Shiseido has transformed itself into a full-fledged skincare cosmetics company with a wide range of products encompassing various aspects to cosmetics from skin care to beauty products to general cosmetics.
There are several skincare products from shiseido, both for men and women. Various categories of products include - Prestige, Fragnance, Cosmetics, Personal Care, Professional, Healthcare. 

**Part B Assignment:**

Working with TPC-DS dataset on Snowflake and integrating it with Einstein Analytics to create dashboards.

* Creating a new database MarketDB to query tables from TPCDS_SF10TCL since no writes are allowed on Snowflake’s sample databases.

* Querying around the offline sales present in the Stores_Sales fact table

* Connecting the tables in the newly created MarketDB database from Snowflake to Einstein Analytics using Live SnowFlake Connector.

Use Cases from TPC-DS and dashboards in Einstein Analytics

* Sum of total sales of all the stores in the states of the US.

* Total Sales of stores by their presence in the States.

* The price of sales versus date and quantity of buying the product.

* Product purchase by gender and it’s marital status.

* Details about the products sold during the holiday season.

