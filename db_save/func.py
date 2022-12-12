from .models import *
import sqlite3


def addSoftware (Discipline, OpSys, Name, Practicum_Num):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('INSERT INTO db_save_software ("Discipline","OpSys","Name","Practicum_Num") VALUES (?,?,?,?)'
    , (Discipline, OpSys, Name, Practicum_Num))
    row = cursor.fetchone()
    cursor.close()
    connection.commit()
    return dict({'message':"Призошло добавление:"})


def getSoftware (Discipline, OpSys, Name, Practicum_Num):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute(
        '''SELECT * FROM db_save_software WHERE "Discipline" LIKE ? AND "OpSys" LIKE ? AND "Name" LIKE ? 
        AND "Practicum_Num" LIKE ? ''', (f"%{Discipline}%", f"%{OpSys}%", f"%{Name}%", f"%{Practicum_Num}%"))
    row = curs.fetchall()
    curs.close()
    connection.commit()
    row = [dict(i) for i in row]
    print(row)
    return row
