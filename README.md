# Analysis of US Rental Market
Project Overview:
Explore the US apartment rental landscape to identify distinct rental segments and their defining characteristics.

Data Overview & Preparation Steps
Source: University of Irvine, Machine Learning repository. https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified![image](https://github.com/EllaC12345/US_Rental_Market/assets/103433242/ee8d05ff-a76b-4e3a-93b4-315651a7ffbe)

The dataset comprises a compilation of apartment listings available for rent across the United States as of December 25, 2019, predating the onset of the pandemic.

Methodology Overview :
1. Performed data exploratory and cleansing techniques using pandas, numpy libraries
2. Performed further analysis around apartment amenities and apartment size (i.e. 1bed/1ba , 2 beds/2bas etc..)
3. Leveraged Scikit Learn's Hot encoding and StandardScaler techniques to normalize and standardize the dataset
4. Leveraged unsupervised learning techniques ( KMeans Clustering and PCA) to determine the market segments
   - KMeans Outcome :2 segments identified
   - Principal Components Analysis Outcome: 2 segments identified with an Explained Variance Ratio  of 62%.
5. Leveraged PYcaret and XGboost algorithm to boost clustering techniques and determine feature importance
   - Accuracy rate = 99%
   
Results & Outcomes:
classification driven by rental price, square feet, sports,Outdoor, Luxury, Convenience amenities and geographical location
2 segments identified:
A- Segment 0 Specifications:
- Average/Median rent: $1,375
- Median SQ feet: 905
- median number of sports amenities: 0
- Median number of outdoor amenities: 0
- Median number of convenience amenities: 1
- Median number of luxury amenities: 0
B- Segment 1 Characterictics:
Average rent: $ 1414
Median Rent: 1250
M


Growth and Next Steps 
