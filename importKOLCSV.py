import csv

from defineInfluencer import Influencer

with open('/Users/bolglo/Documents/VSC/python/KOL_Selection_Pack/KOL_Initialisation.csv', 'r') as file: #consider newline='' and dialect='excel' for later editions
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[0] in (None, ""):
            break
        else:
            newInfluencer = Influencer(row[0], row[1], row[2], int(row[3]), int(row[4]), float(row[5]), float(row[6]), int(row[7]), int(row[8]), int(row[9]))