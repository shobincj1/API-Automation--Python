import csv

with open('Utilities/loanapp.csv') as csvFile:
    csvReader=csv.reader(csvFile,delimiter=',')
    print(csvReader)
    listCSV=list(csvReader)
    print(listCSV)
    name=[]
    stats=[]
    for row in listCSV:
        print(row)
        name.append(row[0])
        stats.append(row[1])
print(name)
print(stats)
csvFile.close()
with open('Utilities/loanapp.csv','a') as csvWriteFile:
    csvWriter=csv.writer(csvWriteFile)
    csvWriterEachRow = csvWriter.writerow(["Shob","Rejected"])
csvWriteFile.close()


