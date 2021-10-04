import csv
list1=['a','b','c']
with open('names.csv') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(row)
   # writer=csv.writer(csvfile)
   # writer.writerow(list1)
        
   