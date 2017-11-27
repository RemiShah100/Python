import pymongo
import json
import pyodbc

c = pyodbc.connect(r'DSN=mysqlconn;UID=python;PWD=oklahoma1')
cur = c.cursor()

query = r"select \
	 soh.SalesOrderNumber \
	,sod.LineTotal \
	,sod.OrderQty \
	,p.firstname + ' ' + p.lastname customer \
	,replace(pr.Name, ',', '') productname \
	,ps.name productsubcategory \
	,pc.name productcategory \
from sales.salesorderheader soh \
inner join sales.customer c \
	 on soh.CustomerID = c.CustomerID \
inner join person.person p \
	 on c.PersonID = p.BusinessEntityID \
inner join sales.SalesOrderDetail sod \
	 on soh.SalesOrderID = sod.SalesOrderID \
inner join Production.Product pr \
	 on sod.ProductID = pr.ProductID \
inner join production.ProductSubcategory ps \
	 on pr.ProductSubcategoryID = ps.ProductSubcategoryID \
inner join production.productcategory pc \
	 on ps.ProductCategoryID = pc.ProductCategoryID"

sales_order_num = []

sql_data = cur.execute(query)
for row in sql_data:
    if row[0] in sales_order_num:
        next
    else:
        sales_order_num.append(row[0])

sql_data_dict = {}

for i in sales_order_num:
    sql_data_dict[i] = []

sql_data = cur.execute(query)

for row in sql_data:
    if row[0] in sql_data_dict:
        sql_data_dict[row[0]].append({'Line Total': row[1], 'Order Quantity':row[2],
                                         'Customer':row[3],'Product Name':row[4],'Prod SubCat':row[5],'ProCat':row[6]})
    else:
        next

c = pymongo.MongoClient("mongodb://localhost")

db = c.test.sqljson

for k, v in sql_data_dict.items():
    for i in v:
        i['Line Total'] = float(i['Line Total'])
print(sql_data_dict)

for k, v in sql_data_dict.items():
    db.insert_one({k:v})