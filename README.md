# Analysis of US Rental Market
**Project Overview and Objectives:**

Explore the US apartment rental landscape to identify distinct rental segments and their defining characteristics.

**Data Overview & Preparation Steps:**

Source: University of Irvine, Machine Learning repository. https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified!



The dataset comprises a compilation of apartment listings available for rent across the United States as of December 25, 2019, predating the onset of the pandemic.

**Methodology Overview** :

1. Performed data exploration and cleaning techniques using pandas and numpy libraries
2. Analyzed apartment amenities and sizes (i.e. 1bed/1ba , 2 beds/2bas etc..)
   - Sports amenities: Pool, Gym, Tennis, Basketball, Golf
   - Outdoor amenities: Patio/Deck, Clubhouse, Playground'
   - Convenience amenities: Parking, Garbage Disposal, Washer Dryer, AC, Elevator, Dishwasher, Storage, Gated, Refrigerator,Cable or Satellite,Internet Access
   - Luxury amenities: Fireplace, Wood Floors, View, Doorman, Luxury, Hot Tub  
3. Utilized Scikit Learn's One-Hot Encoding and StandardScaler techniques to normalize and standardize the dataset.
4. Applied unsupervised learning techniques (i.e. KMeans Clustering and PCA) to determine the market segments
   - KMeans Outcome :2 segments identified
   - Principal Components Analysis Outcome: 2 segments identified with an Explained Variance Ratio  of 69%.
5. Employed PyCaret and the XGboost algorithm to enhance clustering techniques and determine feature importance
   - Achieved an accuracy rate = 99%
   
**Results & Outcomes:**

Classification based by rental price, square feet, sports,outdoor, luxury, convenience amenities and geographical location.
2 segments identified:

A- Segment 0 Characteristics:
- Average/Median rent: $1,375
- Median SQ feet: 905
- Predominant count of sports amenities: 0
- Predominant count of outdoor amenities: 0
- Predominant Count of convenience amenities: 1
- Predominant Count of luxury amenities: 0
  
B- Segment 1 Characterictics:
- Average rent: $1,414
- Median Rent: $1,250
- Median Sq feet: 879
- Predominant count of sports amenities: 2
- Predominant count of outdoor amenities: 1
- Predominant Count of convenience amenities: 4
- Predominant Count of luxury amenities: 0

**Conclusion:**

The American rental market is predominantly a Segment 0 market, though both segments are present in all cities, varying by neighborhood. Segment 0 rentals are characterized by spacious apartments with fewer amenities. In contrast, Segment 1 rentals are characterized by smaller apartments with more amenities and are primarily located in the Northeast region of the country.

