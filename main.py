"""Python script to load exoplanet XML data into a dataframe for manipulation"""

import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

URL = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
xml_file = ET.parse("systems.xml")

# Initiate empty data list for colelcting a list of lists for creating a pandas DataFrame
data = []

# For each planet in the xml file, retireve the planet's attributes
for planet in xml_file.findall(".//planet"):
    data.append(
        [
            planet.findtext("name"),
            pd.to_numeric(planet.findtext("mass")),
            pd.to_numeric(planet.findtext("semimajoraxis")),
            pd.to_numeric(planet.findtext("eccentricity")),
            pd.to_numeric(planet.findtext("temperature")),
            pd.to_numeric(planet.findtext("period")),
        ]
    )

# Create the DataFrame from the planet data. Clean the data.
PLANET_DF = pd.DataFrame(data)
PLANET_DF = PLANET_DF.rename(
    columns={
        0: "name",
        1: "mass",
        2: "semimajoraxis",
        3: "eccentricity",
        4: "temperature",
        5: "period",
    },
)
PLANET_DF.convert_dtypes()
PLANET_DF = PLANET_DF.replace("", np.nan)
PLANET_DF = PLANET_DF.dropna()  # Drops any rows that have missing values

# Plot the data on graphs using matplotlib
x = PLANET_DF["period"].values
y = PLANET_DF["temperature"].values
fig, ax = plt.subplots()
ax.scatter(
    x,
    y,
    s=2,
)

# Create a trendline for the graph using Least Squares regression (i.e Polynomial.fit())
p_fitted = np.polynomial.Polynomial.fit(np.log(x), np.log(y), 1)
# The line above creates a polynomial object which when given an x-value will return a y-value
# according to the Least Squares regression (y = mx + b)
trend_x = np.linspace(min(x), max(x), 1000)
trend_y = list(map(lambda x: np.exp(p_fitted(np.log(x))), (trend_x)))
print(max(trend_y))
print(max(x))

ax.plot(trend_x, trend_y, color="red", linestyle="--")

plt.xscale("log")
plt.yscale("log")
plt.show()
