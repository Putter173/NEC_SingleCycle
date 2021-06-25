import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            no = row[0]
            energy = row[14]
            mass = row[13]
            energy = float(energy)
            mass = float(mass)
            eme = round(energy / mass, 2)
            x.append(no)
            y.append(eme)
            line_count += 1     

plt.scatter(x, y, color= "red", marker= ".", s=30)
plt.xlabel('Cell No.')
plt.ylabel('EME')
plt.title('EME & Cell - @ Cycle 1')
plt.show()