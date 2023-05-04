#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='allan@localhost:3306', password='allan1', database='test_db')

cursor = conn.cursor()
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into test_table (firstName, lastName) values (%s, %s)', ('Allan', 'Barrientos'))
print('rowcount =', cursor.rowcount)
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from test_table')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
