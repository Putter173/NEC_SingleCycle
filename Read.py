import csv
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        elif line_count == 1:
            line_count += 1
        else:
            no = row[0]
            energy = row[14]
            mass = row[13]
            energy0 = float(energy)
            mass0 = float(mass)
            eme = round(energy0 / mass0, 2)
            print(no + ' ' + energy + ' ' + mass + ' | ' + str(eme))
            line_count += 1     