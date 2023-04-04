import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="stationary",
    auth_plugin='mysql_native_password'
)
n = int(input("1.user 2.customer 3.usercreation"))
if (n == 3):
    empno = int(input("enter employee code"))
    username = input("enter username")
    password = input("enter password")
    mycursor = mydb.cursor()
    sql = "insert into login(empno,username,password)values(%s,%s,%s)"
    val = (empno, username, password)
    mycursor.execute(sql, val)
    mydb.commit()
elif (n == 1):
    empcode = int(input("enter your employee code"))
    username = input("enter username")
    password = input("enter password")
    try:
        mycursor = mydb.cursor()
        sql = "select username from login where empno='{}'".format(empcode)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()

        for x in myresult:
            uname = x
        mycursor = mydb.cursor()
        sql = "select password from login where empno='{}'".format(empcode)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        for y in myresult:
            pword = y

        if (username == uname) and (password == pword):
            print("login succesful")
            ch = 1
            while (ch == 1):
                pid = int(input("enter product id"))
                pname = input("enter product name")
                stock = int(input("enter stocks in inventory"))
                price = int(input("enter price for one unit"))
                mycursor = mydb.cursor()
                sql = "insert into pricelist (pid,pname,stock,price)values(%s,%s,%s,%s)"
                val = (pid, pname, stock, price)
                mycursor.execute(sql, val)
                mydb.commit()
                ch = int(input("1.addotherproduct 2.close"))
        else:
            print("username or password must be wrong")
    except Exception:
        print("username or password must be wrong")

else:
    cname = input("enter your name")
    mycursor = mydb.cursor()
    sql = "select pname from pricelist"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for z in myresult:
        print(z)
    n = input("select your product")
    mycursor = mydb.cursor()
    sql = "select price from pricelist where pname='{}'".format(n)
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for z in myresult:
        price = z
    print("price of one scale is rs", price)
    mycursor = mydb.cursor()
    sql = "select stock from pricelist  where pname='scale'"
    mycursor.execute(sql)
    myresult = mycursor.fetchone()
    for y in myresult:
        stock = y
    quantity = int(input("how many scale do you need"))
    if (quantity <= y):
        total = price * quantity
        print("your total amount is", total)
        newstock = y - quantity
        mycursor = mydb.cursor()
        sql = "update pricelist set stock='{}'where pname='{}'".format(newstock, n)
        mycursor.execute(sql)
        mydb.commit()
        mycursor = mydb.cursor()
        sql = "insert into customer(customername,product,amount)values(%s,%s,%s)"
        val = (cname, n, total)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor = mydb.cursor()
        sql = "select * from customer where customername='{}'".format(cname)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for y in myresult:
            name = y
        print("name\titem\t\tamount")
        print(name[0], "\t", name[1], "\t", name[2])

    else:
        print("low stock in inventory")
