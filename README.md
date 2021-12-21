# Surfs Up!
Practice project regarding SQLite, SQLalchemy, and Flask.

## Overview
Analysis of Hawaiian weather patterns to  determine viability of a surf + ice cream shop.
</br>

## Results
####  Temperature Comparison
![Temperature Comparison](https://user-images.githubusercontent.com/91762315/146860510-d79e8983-09de-411e-93b1-32d3ffe2a31f.png)

* There is little difference in the average temperatures in the region during these months, less than 4°F.
* The difference between max temperatures is only 2°F.
* The difference between minimum temperatures is 8°F.

## Summary

Due to the consistent temperatures throughout the year, we recommend opening an ice cream shop addition to the surf shop.  
Even during the coldest months, the weather is consistently above 70°F.

****  
### _**Additional query suggestions**_  

We encourage analysis on a year by year basis.  
This will help to identify any shifts in temperature caused by climate change.

<br/>

We encourage additional review precipitation data, based on the station closest to the proposed location.  
This may assist in identifying if this particular location is suitable for ice cream, as sales of this product may be reduced during the rainy season.


<!-- #Sample Query
`dec_precp_results = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12)`  
`dec_precp_df = pd.DataFrame(dec_precp_results, columns=['date','precipitation'])`  
`dec_precp_df.describe()`
-->

