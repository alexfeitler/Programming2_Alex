# Plotting (with mathplotlib)

import matplotlib.pyplot as plt

plt.figure(1)   # creates a new window

plt.plot([1, 2, 3, 4])  # if there is no x axis it just uses the index

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # new plot --- (x, y)

plt.figure(2, facecolor='lightblue')  #new window
x = [x for x in range(100)]
y = [y ** 2 for y in range(100)]

plt.plot(x, y, color="green", marker="^", linestyle='--')

plt.xlabel('x label (units')
plt.ylabel('y label (units')
plt.title('Example Plot', color='blue', fontsize=20)
plt.axis([10, 20, 100, 500])  # xmin, xmax, ymin, ymax

#plt.show()

import matplotlib.pyplot as plt
import csv

with open('data/Libraries_-_2018_Visitors_by_Location.csv') as f:
    reader = csv.reader(f)  # create a reader object from csv
    data = list(reader)  # cast it as a a list

#print(data)

month_numbers = [x for x in range(12)]  # month numbers on x

library_names = [x[0] for x in data[1:]]  # month names on x
print(library_names)

header = data.pop(0)
#print(header)


month_data = [x[1:-1] for x in data]  # Jan to Dec data for all libraries
#print(month_data[0])

plt.figure(3, tight_layout=True, figsize=(12, 8))  # tight layout allows data to fit axes

library_data = [int(x) for x in month_data[library_names.index('Lincoln Park')]]
plt.plot(month_numbers, library_data)
plt.xlabel('Month')
plt.ylabel('Visitors')
plt.title('Lincoln Park Library- Vistitors by Month 2018 ', color='blue', fontsize=20)

month_names = header[1:-1]
print(month_names)
plt.xticks(month_numbers, month_names, rotation=90)  # replace our number with labels


# make a graph of all library attendance in Chicago
plt.figure(4, tight_layout=True, figsize=(6, 4), facecolor='lightblue')

print(month_data)

all_lib_months = [0 for x in range(12)]
print(all_lib_months)

for library in month_data:
    for i in range(12):
        all_lib_months[i] += int(library[i])

print(all_lib_months)

plt.bar(month_numbers, all_lib_months, color='red')
plt.xticks(month_numbers, month_names, rotation = 60)
plt.xlabel("Months")
plt.ylabel("Visitors")
plt.title("Chicago Library Visitors by Month(2018)")

plt.legend()
plt.show()