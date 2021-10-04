import csv #comma-separated values
header = ['First name', 'Last name', 'Job title', 'Company']
data = [input("Pls state your First name:"), input("Pls your Last name:"), input('What is your Job title:'), input("Which company you work:")]
fxxxx = open("newkv.csv", "a")
writer = csv.writer(fxxxx)
#writer.writerow(header)
writer.writerow(data)
fxxxx.close()
# #writer = csv.DictWriter(f, fieldnames=header)
# #writer.writerows(data)