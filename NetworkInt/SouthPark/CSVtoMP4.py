import urllib.request
import csv

# https://archive.org/download/northplayground/

indx = 0
filename = input("file path:")
lower = int(input("What is the lower bounds of the season?: "))
upper = int(input("What is the upper bounds of the season?: "))

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[0] == ".":
            indx += 1
            if (indx>=lower)&(indx<=upper): input("press any key to continue...")
        elif (indx>=lower)&(indx<=upper):
            urllib.request.urlretrieve(row[1], row[0])
    print("Download Complete")
