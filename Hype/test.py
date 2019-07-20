# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/login_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QPSQL')
db.setHostName("localhost")
db.setPort(5433)
db.setDatabaseName("bama_prj")
db.setUserName("postgres")
db.setPassword("51136616")
if db.open():
    for item in db.tables():
        print(item)
    print(db.databaseName())
    print(db.driverName())
else:
    print("NOOOOOOOOOOOOOO")

myquery = QtSql.QSqlQuery()
myquery.exec_("select * from amain_car_info")
rows = myquery.fetchall()
print(rows)