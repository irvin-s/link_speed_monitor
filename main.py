from logger.csvWriter import createFile, writetoCsv
from speedCheck.getSpeed import downloadCheck, uploadCheck
from logger.getDate import getDate
from threading import Timer

def main():
    print("Verificando a velocidade da conexão!")
    #Timer(180, main).start()
    csv_file = createFile()
    down = downloadCheck()
    up = uploadCheck()
    csv_row = getDate()
    csv_row.append(down)
    csv_row.append(up)
    writetoCsv(csv_file, csv_row)
    csv_file.flush()

if __name__ == "__main__":
    main()
