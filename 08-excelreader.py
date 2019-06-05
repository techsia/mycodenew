#!usr/bin/python3

import pyexcel

def main():
    excelrecords = pyexcel.iget_records(file_name="portsservice.xls")

    for row in excelrecords:
        print(row['service'], "-", row['ip'] + ":" + str(row['port'])) # don't want white btwn ip & port, join them


if __name__ == "__main_": #only true if you run it from command line
    main()
