# CTA Ridership (28pts)

#  Get the csv from the following data set.
#  https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
#  This shows CTA ridership by year going back to the 80s

import matplotlib.pyplot as plt
import csv

with open('CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

# 1  Make a plot of rail usage for the most current 10 year period.  (year on x axis, and ridership on y) (5pts)
plt.figure(1, tight_layout=True, figsize=(11, 7), facecolor='lightblue' )

header = data.pop(0)
year = [x[0] for x in data]
ten_year = year[-10:]
ten_year = [int(x) for x in ten_year]

rail = [x[3] for x in data]
ten_rail = rail[-10:]
ten_rail = [int(x) for x in ten_rail]

plt.plot(ten_year, ten_rail, color='black', label="Rail", linestyle='--', marker="^")
plt.xticks(ten_year, rotation=45, fontsize=8)


# 2  Plot bus usage for the same years as a second line on your graph. (5pts)
bus_usage = [x[1] for x in data]
bus = [x[1] for x in data]
bus_ten = bus[-10:]
ten_bus = [int(x) for x in bus_ten]

plt.plot(ten_year, ten_bus, color='blue', label="Bus", linestyle='--', marker="^")


# 3  Plot bus and rail usage together on a third line on your graph. (5pts)
total = [x[4] for x in data]
total_ten = total[-10:]
ten_total = [int(x) for x in total_ten]

plt.plot(ten_year, ten_total, color='red', label="Bus + Rail", linestyle='--', marker="^")

# Title and label of Axis
plt.title("CTA Ridership By Year Over the Last 10 Years")
plt.xlabel("Years")
plt.ylabel("Number of Riders in millions")

# Legend
plt.legend()

plt.show()


# 4  Add a title and label your axes. (5pts)

# done above

# 5  Add a legend to show data represented by each of the three lines. (5pts)

# done above

# 6  What trend or trends do you see in the data?  Offer at least two hypotheses which might explain the trend(s). (3pts)
'''
I would hypothezise that the reason for the decline in usage of CTA can be attributed to two things. First, the elimination of
paratransit. While it was replaced by Pace this was not accounted for. Therefore, many individuals who take advantage of this are
no longer accounted for. Second, over the past ten years apps like Uber and Lyft have been able to lower their prices inorder ot become 
competitive with the low prices of public transit. People are able to justify paying a bit more for Uber becuase often it can be 
more efficient the public transportation. Also, when CTA buses are behind schedule people who are able chose to resort to more reliable and efficient
modes of transportation like ride sharing. 
'''