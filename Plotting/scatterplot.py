# Scatter plot
import matplotlib.pyplot as plt
import csv
import numpy as np

with open("World firearms murders and ownership.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)

header = data.pop(0)
print(header)

# make a scatter of firearms_per_100 vs homicides_100k

homicide_100k = []
firearms_100 = []
countries = ["United States", "New Zealand", "Canada", "South Korea", "Japan", "England and Wales", "Netherlands", "France", "Nigeria", "Belgium", "Taiwan", "Singapore", "Hungary", "Denmark", "Finland", "Spain", "Iceland", "Switzerland"]

countries_label = []

for country in data:
    if country[0] in countries:
        try:
            homicides = float(country[5])
            firearms = float(country[-2])
            name = country[0]
            homicide_100k.append(homicides)
            firearms_100.append(firearms)
            countries_label.append(name)
        except:
            print(country[0], "data is inadequate")

print(homicide_100k)
print(firearms_100)
print(countries)

plt.figure(1, figsize=(12, 6), facecolor='lightblue')
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("Homicides per 100k population")
plt.xlabel("Firearms per 100 people")
plt.title("Homicides vs. Gun Ownership by Country")

# make a best fit line
m, b = np.polyfit(firearms_100, homicide_100k, 1)

fit_x = [0, 100]
fit_y = [b, 100 * m]

plt.annotate("my Text", xy=(40, 2))

print(len(firearms_100), len(homicide_100k), len(countries))

for i in range(len(countries_label)):
    plt.annotate(countries_label[i], xy=(firearms_100[i], homicide_100k[i]))

plt.plot(fit_x, fit_y)

plt.show()