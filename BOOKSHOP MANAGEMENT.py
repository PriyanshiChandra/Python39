import mysql.connector as a
con=a.connect (host="localhost",user="root",passwd="priyanshi",database="library")

def addbook():
    bn=input("Enter BOOK Name:")
    bc=input("Enter BOOK Code:")
    tb=input("Total Books:")
    s=input("Enter Subject:")
    data=(bn,bc,tb,s)
    sql='insert into books values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n=input("Enter Name:")
    rno=input("Enter Reg No:")
    bco=input("Enter Book Code:")
    d=input("Enter Date:")
    a='insert into issue values(%s,%s,%s,%s)'
    data=(n,rno,bco,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Books issued to:",n)
    bookup(bco,-1)

def submitb():
    n=input("Enter Name:")
    rno=input("Enter Reg No:")
    bco=input("Enter Book Code:")
    d=input("Enter Date:")
    a='insert into submit values(%s,%s,%s,%s)'
    data=(n,rno,bco,d)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-------------------------------------------------------------<")
    print("Books submitted from:",n)
    bookup(bco,1)

def bookup(bco,u):
    a="select TOTAL from books where BCODE=%s"
    data=(bco,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0]+u
    sql="update books set TOTAL=%s where BCODE=%s"
    d=(t,bco)
    c.execute(sql,d)
    con.commit()
    main()

def dbook():
    ac=input("Enter Book Code:")
    a="delete from books where BCODE=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    con.commit()
    main()

def dispbook():
    a="select *from books"
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("Book Name",i[0])
        print("Book Code",i[1])
        print("Total",i[2])
        print(">---------------------<")
    main()

def main():
        print("""
                                         BOOKSHOP MANAGEMENT
        1. ADD BOOK
        2. ISSUE BOOK
        3. SUBMIT BOOK
        4. DELETE BOOK
        5. DISPLAY BOOKS
        """)
        choice=input("Enter Task No:")
        print(">----------------------------------------------------------------------------------------------<")
        if(choice=='1'):
            addbook()
        elif(choice=='2'):
            issueb()
        elif(choice=='3'):
            submitb()
        elif(choice=='4'):
            dbook()
        elif(choice=='5'):
            dispbook()
        else:
            print("Wrong choice.......")
            main()

def pswd():
    ps=input("Enter Password:")
    if ps=="py123":
        main()
    else:
        print("Wrong Password")
        pswd()
pswd()



