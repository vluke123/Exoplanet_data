import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import urllib.request
import gzip
import io

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
xml_file = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))
root = xml_file.getroot()

planet_df = pd.DataFrame(
    np.array([[planet.findtext("mass"), planet.findtext("radius")] for planet in xml_file.findall('.//planet')]))

print(planet_df)


'''
# Step 2: Create an empty pandas DataFrame
df = pd.DataFrame(columns=['column_name_1', 'column_name_2'])

# Step 3: Loop through the XML elements and extract the data you want to include in the DataFrame. 
# Append each row of data to the DataFrame
for planet in xml_file.findall(".//planet"):
    for child in planet:
        # Extract the data from each element using the .find() method
        column_1_value = child.find('planet').text
        column_2_value = child.find('name').text

        # Create a list of values for the row
        row = [column_1_value, column_2_value]

        # Append the row to the DataFrame using .loc[]
        df.loc[len(df)] = row

    # Step 4: Print the DataFrame to confirm that it contains the tabulated form of the XML data
print(df)
'''



'''
# Output mass and radius of all planets 
for planet in oec.findall(".//planet"):
    print("mass: " + str(planet.findtext("mass")), 
          "radius: " + str(planet.findtext("radius")))
 
# Find all circumbinary planets 
for planet in oec.findall(".//binary/planet"):
    print("name: " + planet.findtext("name"))
 
# Output distance to planetary system (in pc, if known) and number of planets in system
for system in oec.findall(".//system"):
    print("distance: " + str(system.findtext("distance")),
          len(system.findall(".//planet")))

for country in root.findall('country'):
    rank = country.find('rank').text #.find() finds the first child with a particular tag
    name = country.get('name') #.get() finds the element's attributes, this case it's 'country' names
    print(name, rank)

# https://docs.python.org/3/library/xml.etree.elementtree.html#elementtree-xpath

[tag='text'] # This can be used to search for a child named 'tag'
# whose complete text content equals 'text'

#iterfind(match, namespaces=None)
#Finds all matching subelements, by tag name or path. Returns an iterable yielding all matching elements in document order. namespaces is an optional mapping from namespace prefix to full name.

for planet in root.iterfind('.//planet'):
    print(planet.findtext('name'))

or

for planet in xml.xml_object.iter('.//planet'):
    print(planet.findtext('name'))
'''
