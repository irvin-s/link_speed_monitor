import os.path
import csv

def createFile():
    file = os.path.isfile("results/data.csv")
    if file:
        csv_file = open("results/data.csv", "a+", newline='')
    else:
        csv_file = open("results/data.csv", "a+", newline='')
        csv_row = ["Hour", "Date", "Download_speed(Mbit/s)", "Upload_speed(Mbit/s)"]
        writetoCsv(csv_file, csv_row)
    return csv_file


def writetoCsv(write_obj, list_of_elem):
    csv_writer = csv.writer(write_obj)
    csv_writer.writerow(list_of_elem)