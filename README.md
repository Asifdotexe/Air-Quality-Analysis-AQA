# AQA: Air Quality Analysis

AQA is a project focused on analyzing air quality data sourced from [data.gov.in](https://data.gov.in/resource/real-time-air-quality-index-various-locations). This project involves data preprocessing and analysis to gain insights into air pollution levels across various locations.

## About Pollutants

### NH3 (Ammonia)
**Environmental Impact:** Ammonia can contribute to eutrophication of water bodies, leading to algal blooms and oxygen depletion. It can also contribute to soil acidification and harm aquatic life.  
**Main Causes:** Agricultural activities such as fertilizer application and livestock waste are the primary sources of ammonia emissions. Industrial processes and combustion of biomass also release ammonia into the atmosphere.

### SO2 (Sulfur Dioxide)
**Environmental Impact:** Sulfur dioxide contributes to acid rain, which can harm aquatic ecosystems, forests, and buildings. It also contributes to the formation of fine particulate matter (PM2.5), which has adverse health effects.  
**Main Causes:** Combustion of fossil fuels, particularly in power plants and industrial facilities, is the main source of sulfur dioxide emissions. Smelting of metal ores and volcanic eruptions also release sulfur dioxide into the atmosphere.

### PM2.5 (Particulate Matter with diameter less than 2.5 micrometers)
**Environmental Impact:** PM2.5 can penetrate deep into the respiratory system, causing respiratory and cardiovascular diseases. It also reduces visibility and contributes to haze.  
**Main Causes:** PM2.5 is generated from various sources, including vehicle emissions, industrial processes, construction activities, and biomass burning. It can also be formed through chemical reactions in the atmosphere.

### PM10 (Particulate Matter with diameter less than 10 micrometers)
**Environmental Impact:** PM10 has similar health and environmental impacts as PM2.5, though typically to a lesser extent due to larger particle size.  
**Main Causes:** PM10 sources overlap with PM2.5 sources and include vehicle emissions, industrial processes, construction activities, and natural sources such as dust storms and wildfires.

### OZONE (O3)
**Environmental Impact:** Ground-level ozone can cause respiratory problems, reduce lung function, and aggravate asthma. It also damages vegetation, reduces crop yields, and harms ecosystems.  
**Main Causes:** Ozone is not directly emitted into the atmosphere but forms through chemical reactions between nitrogen oxides (NOx) and volatile organic compounds (VOCs) in the presence of sunlight. Major sources of NOx and VOCs include vehicle emissions, industrial processes, and combustion of fossil fuels.

### CO (Carbon Monoxide)
**Environmental Impact:** Carbon monoxide is a toxic gas that can cause headaches, dizziness, and even death at high concentrations. It also contributes to the formation of ground-level ozone and smog.  
**Main Causes:** Incomplete combustion of fossil fuels in vehicles, industrial processes, and residential heating systems are the primary sources of carbon monoxide emissions.

### NO2 (Nitrogen Dioxide)
**Environmental Impact:** Nitrogen dioxide can cause respiratory problems, exacerbate asthma, and contribute to the formation of ground-level ozone and particulate matter. It also leads to acid rain and eutrophication.  
**Main Causes:** Combustion processes in vehicles, power plants, industrial facilities, and residential heating are the main sources of nitrogen dioxide emissions. Agricultural activities and natural sources like wildfires also release nitrogen oxides into the atmosphere.

## Data Source

The air quality data used in this project is sourced from [data.gov.in](https://data.gov.in/resource/real-time-air-quality-index-various-locations).

## Data Preprocessing

The data preprocessing steps involved reading the dataset using pandas, handling missing values, converting data types, and imputing missing values. Here's a summary of the preprocessing steps:

- Reading the dataset
- Handling missing values
- Converting 'last_update' to datetime format
- Imputing missing values using mean values for each pollutant category

## Data Analysis

The data analysis phase included calculating summary statistics and creating visualizations to gain insights into air quality levels. Key aspects of the analysis include:

- Summary statistics for pollutant levels
- Histograms showing the distribution of pollutant levels
- Boxplots illustrating the spread of pollutant levels by type
- Bar charts displaying the distribution of pollutants by state

## Conclusion and Insights

The analysis revealed significant variations in air quality levels across different states and pollutants. Some key insights include:

- Identification of states with high and low pollutant levels
- Factors contributing to air pollution in specific regions (e.g., industrial activities, vehicular emissions)
- Trends in pollutant levels over time and location

## Usage

To use this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies (`pandas`, `matplotlib`, `seaborn`, `folium`).
3. Run the Jupyter Notebook or Python script to perform data preprocessing and analysis.

## Acknowledgements

- This project utilizes data from [data.gov.in](https://data.gov.in/).
- We acknowledge the contributions of the open-source community and various libraries used in this project.

## Contact Information

For inquiries or collaborations, please contact [asifdotexe@gmail.com](mailto:asifdotexe@gmail.com).
