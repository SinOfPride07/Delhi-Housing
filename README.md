# Delhi-Housing

URL : http://ec2-3-19-240-231.us-east-2.compute.amazonaws.com/

![Preview](https://i.ibb.co/WckcvMV/Screenshot-302.png)

This project uses 9 different features to estimate the price of a property in different localities of Delhi. RandomForestRegressor was
found to be the most accurate algorithm for this data (GridSearchCV was used to find the apt algorithm).

The model is currently deployed in AWS EC2 instance and can be used by visting the link above.

The code can be found in the Data folder of the repository.

Features Used:
Area 
BHK
Locality
No. of Bathrooms
No. of Parking spaces
Current status of the property
Transaction status of the property
Type of the property
Furnishing status of the apartment

Target:
Price of the property
