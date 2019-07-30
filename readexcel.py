import csv

with open('Persons.csv','w') as csvfile:
    filewriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name','Profession'])
    filewriter.writerow(['Venky', 'Python Prgograamer'])
    filewriter.writerow(['Bhuvanesh', 'Student'])
    filewriter.writerow(['Saravana', 'Software Programmer'])
csvfile.close()

with open('Persons.csv','r') as csvfile:
    filereader = csv.reader(csvfile)

    for row in filereader:
        print (row)


