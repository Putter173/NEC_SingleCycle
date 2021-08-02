import matplotlib.pyplot as plt
import csv

x0 = []
x1 = []
x2 = []
x3 = []
y0 = []
y01 = []
y1 = []
y11 = []
y2 = []
y21 = []
y3 = []
y31 = []


with open('Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if row[2] == "NMC": #Filter for NMC Cells Only
                no = row[0]
                energy = row[18]
                if energy == "": #NaN Energy Data Fallback
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
                if eme <= 10 and em <= 10 : #Energy Threshold
                    line_count += 1
                else:
                    if float(row[5]) == 50: #Filter for 50μm
                        if row[7] == 'CuBFO':
                            y2.append(eme)
                            y21.append(em)
                            x2.append(active)
                            line_count += 1
                        else:
                            y0.append(eme)
                            y01.append(em)
                            x0.append(active)
                            line_count += 1
                    elif float(row[5]) == 25: #Filter for 25μm
                        if row[7] == 'CuBFO':
                            y3.append(eme)
                            y31.append(em)
                            x3.append(active)
                            line_count += 1
                        else:
                            y1.append(eme)
                            y11.append(em)
                            x1.append(active)
                            line_count += 1
                    else:
                        line_count += 1
            else:
                line_count += 1

plt.scatter(x0, y0, color= "red", marker= ".", label = "50μm EME")
plt.scatter(x0, y01, color= "red", marker= "x", label = "50μm EM")
plt.scatter(x1, y1, color= "blue", marker= ".", label = "25μm EME")
plt.scatter(x1, y11, color= "blue", marker= "x", label = "25μm EM")
plt.scatter(x2, y2, color= "orange", marker= ".", label = "50μm CuBFO EME")
plt.scatter(x2, y21, color= "orange", marker= "x", label = "50μm CuBFO EM")
plt.scatter(x3, y3, color= "green", marker= ".", label = "25μm CuBFO EME")
plt.scatter(x3, y31, color= "green", marker= "x", label = "25μm CuBFO EM")
plt.xlabel('Active Material Mass')
plt.ylabel('EM & EME')
plt.title('EM, EME & Mass - @ Cycle 5 (NMC ONLY)')
plt.legend()
plt.show() 