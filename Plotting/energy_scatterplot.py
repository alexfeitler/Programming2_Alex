# https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking/xq83-jr8c

'''
Energy Efficiency of Chicago Schools (35pts)
Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
We will use this data at the link above to look at schools.  
We will visualize the efficiency of schools by scatter plot.  
We hypothesize that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.
Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)

Challenge (for fun if you have time... not required):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type
'''

import matplotlib.pyplot as plt
import csv
import numpy as np

with open("Chicago_Energy_Benchmarking.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)

header = data.pop(0)  # prints headers
print(header)

k_schools = [x[6] for x in data]
print(k_schools)

'''
k_12 = [x for x in data if x[6] == "K-12 School"]
k12_sorted = sorted(k_12, keywords=lambda x: int(x[21]))
'''
school = []
for x in range(len(k_schools)):
    if k_schools[x] == "K-12 School":
        school.append(data[x])

print(school)


names = []
ghg_emissions = []
square_feet = []
for place in school:
    try:
        gas = float(place[20])
        feet = float(place[7])
        ghg_emissions.append(gas)
        square_feet.append(feet)
        names.append(place[2])
    except:
        print("doesn't work")

print(ghg_emissions)
print(square_feet)
print(names)

# Finds Parker
fwp_index = names.index('Francis W Parker School')
print(fwp_index)
print()

# Parker's data
fwp_ghg = int(ghg_emissions[fwp_index])
fwp_feet = int(square_feet[fwp_index])
print(fwp_ghg)
print(fwp_feet)

plt.figure(1)  # Plots the graph

# Graph customization
plt.scatter(square_feet, ghg_emissions, color='lightblue')
plt.scatter(fwp_feet, fwp_ghg, color='blue', label='Francis W. Parker')
plt.title("Gas Emissions -vs- Building Square Footage", color="red")
plt.xlabel("Square Feet", color="red")
plt.ylabel("Gas Emitted", color="red")

# This is for the bottom and top 3 ghg emitters


# Bottom 3


# Top 3


#for i in range(3):


# Best fit line
m, b = np.polyfit(square_feet, ghg_emissions, 1)

fit_x = [0, 700000]
fit_y = [b, 700000 * m + b]

plt.annotate(names[fwp_index], xy=(square_feet[fwp_index], ghg_emissions[fwp_index]))

plt.plot(fit_x, fit_y)
# End of code for best fit line

plt.legend()
plt.show()