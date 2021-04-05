import os.path
import speedtest
from datetime import datetime
import csv
from threading import Timer


def createFile():
    file = os.path.isfile("dados.csv")
    if file:
        csv_file = open("dados.csv", "a+", newline='')
    else:
        csv_file = open("dados.csv", "a+", newline='')
        csv_row = ["Hora", "Data", "Velocidade"]
        writetoCsv(csv_file, csv_row)
    return csv_file


def writetoCsv(write_obj, list_of_elem):
    csv_writer = csv.writer(write_obj)
    csv_writer.writerow(list_of_elem)


def testInternet():
    print("Verificando a velocidade da conexão!")
    csv_file = createFile()
    s = speedtest.Speedtest()
    data_atual = datetime.now().strftime('%d/%m/%y')
    hora_atual = datetime.now().strftime('%H:%M:%S')
    velocidade = s.download(threads=None)*(10**-6)
    csv_row = [data_atual, hora_atual, round(velocidade)]
    writetoCsv(csv_file, csv_row)
    #Timer(180, testInternet).start()


if __name__ == "__main__":
    testInternet()
