# Smoky Mountains Data Challenge
data processing and web application code for the 2018 Smoky Mountains Computational Sciences and Engineering Conference (SMC2018) annual Data Challenge 

## Impact of Urban Weather on Energy Use
Recent advances in multi-scale coupling of models have started to provide unique insights into how interdependent processes affect one another. The effect of these processes is uniquely observable in urban environments.

This data set comprises of three elements:

a.	High resolution, 90-meter simulated weather data for one month at 15-minute intervals (with known gaps towards the end of each month). These files are in netcdf file format and about 45 GB in size.

b.	A mapping of individual buildings with individual IDs, their lat/lon location, their 2D footprint, and height. (Excel file)

c.	Energy simulation output of these individual buildings, at 15-minute intervals for a whole year.

The questions that are of interest for this challenge are:

1.	Are there interesting variations in the weather and building energy use data for the geographic area?

2.	Which buildings in the study have their energy use impacted the most by external factors including, including the weather?

3.	Are there any interesting visualizations that illustrate the changing dynamics of the simulated urban environment?

Participants are welcome to bring in additional datasets and fuse with the provided data to create meaningful insights.  

---------------------------------------------------------------------------------------------------------------------------------
### Solution:  
# An interactive web-based mapping tool for weather and energy consumption analysis

## Stage 1: Data Preprocessing  
1. Create a spatial dataset of buildings for the study area.  
    a. use the csv provided  
    b. incorporate information from the city of Chicago buildings dataset (https://data.cityofchicago.org/Buildings/Building-Footprints-current-/hz9b-7nh8)  
    c. incorporate building information from the energy data (wall area, window area, roof area, skylight area, m^2 per person, etc.)  
    d. write out to a shapefile 
## Stage 2: Data Analysis  
1. Energy data  
2. Weather data  
## Stage 2: Web App Development
1. Develop the web mapping application.  
    a. OpenLayers, javascript, html, css  
    b. host the web app on personal web page  
2. Key components:
    a. buildings layer with energy data for each building
    b. high resolution simulated weather data along with informative summary statistics (anomalies, heating/cooling degree days, etc.)
    c. time slider for spatiotemporal data visualization
    d. popups for detailed information about buildings and local weather
