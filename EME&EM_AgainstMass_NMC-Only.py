import matplotlib.pyplot as plt
import csv

x = []
y0 = []
y1 = []

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[2] == "NMC":
                no = row[0]
                energy = row[18]
                if energy == "":
                    energy = 0
                else:
                    energy = row[18]
                mass = row[13]
                energy = float(energy)
                mass = float(mass)
                eme = round(energy / mass, 2)
                anode = row[6]
                if anode == "Al":
                    anode = 0.0106
                elif anode == "Cu":
                    anode = 0.0175
                else:
                    raise ValueError('Unindentified Value for Anode Foil Material on row: ' + line_count)
                active = round(mass - 0.0106 - anode, 4)
                em = round(energy / active, 4)
                x.append(mass)
                y0.append(eme)
                y1.append(em)
                line_count += 1
            else:
                line_count += 1

plt.scatter(x, y0, color= "red", marker= ".", label = "EME", s=30)
plt.scatter(x, y1, color= "blue", marker= ".", label = "EM", s=30)
plt.xlabel('Mass')
plt.ylabel('EME & EM')
plt.title('EME, EM & Mass - @ Cycle 5 (NMC ONLY)')
plt.legend()
plt.show() 