import os.path
import csv

def createFile():
    file = os.path.isfile("results/dados.csv")
    if file:
        csv_file = open("results/dados.csv", "a+", newline='')
    else:
        csv_file = open("results/dados.csv", "a+", newline='')
        csv_row = ["Hora", "Data", "Velocidade_download", "Velocidade_upload"]
        writetoCsv(csv_file, csv_row)
    return csv_file


def writetoCsv(write_obj, list_of_elem):
    csv_writer = csv.writer(write_obj)
    csv_writer.writerow(list_of_elem)