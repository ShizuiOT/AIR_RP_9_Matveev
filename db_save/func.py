from .models import *
import sqlite3


def addSoftware (Discipline, OpSys, Name, Practicum_Num):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute('INSERT INTO db_save_software ("Discipline","OpSys","Name","Practicum_Num") VALUES (?,?,?,?)'
                 ' RETURNING *', (Discipline, OpSys, Name, Practicum_Num))
    row = curs.fetchone()
    curs.close()
    connection.commit()
    return dict(row)


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
