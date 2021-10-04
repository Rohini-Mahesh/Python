import csv
header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']

# open the file in the write mode
with open('comp.csv', 'w') as f:

# create the csv writer
    writer = csv.writer(f)

# write a row to the csv file
    writer.writerow(header)
# write the data
    writer.writerow(data)
