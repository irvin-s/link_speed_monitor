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
        csv_row = ["Hora", "Data", "Velocidade_download", "Velocidade_upload"]
        writetoCsv(csv_file, csv_row)
    return csv_file


def writetoCsv(write_obj, list_of_elem):
    csv_writer = csv.writer(write_obj)
    csv_writer.writerow(list_of_elem)

def getDate():
    today = datetime.now().strftime('%d/%m/%y')
    current_time = datetime.now().strftime('%H:%M:%S')
    now_date = [today, current_time]
    return now_date

def downloadCheck():
    s = speedtest.Speedtest()
    speed_down = s.download(threads=None)*(10**-6)
    speed_down = round(speed_down)
    #Timer(180, testInternet).start()
    return speed_down


def uploadCheck():
    s = speedtest.Speedtest()
    speed_up = s.upload(threads=None)*(10**-6)
    speed_up = round(speed_up)
    return speed_up


def main():
    print("Verificando a velocidade da conexão!")
    csv_file = createFile()
    down = downloadCheck()
    up = uploadCheck()
    csv_row = getDate()
    csv_row.append(down)
    csv_row.append(up)
    writetoCsv(csv_file, csv_row)

if __name__ == "__main__":
    main()
