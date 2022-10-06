import mysql.connector as mysql
db=mysql.connect(host="localhost",user="root",password="123456",database="shop")
cur=db.cursor()
cellno=0
password="0"
def register():
              
               try:
                  cellno=int(input("ENTER YOUR MOBILE NUMBER\n"))
                  password=(input("CREATE A PASSWORD TO YOUR ACCOUNT"))
                  data=(cellno,password)
                  sql='insert into buyers(cellno,password) values(%s, %s)' 
                  cur.execute(sql,data)
                  db.commit()
                  print("REGISTERED SUCCESSFULLY\n"
                        "again enter your credentials to log in\n")
                  login()
               except:
                  print(" already an account exists with the number you entered\n")
                  print("1.again register with another number\n2.log in")
                  p=int(input("enter your choice"))
                  if(p==1):
                        register()
                  else:
                        login()
def registers():
              
               try:
                  cellno=int(input("ENTER YOUR MOBILE NUMBER\n"))
                  password=(input("CREATE A PASSWORD TO YOUR ACCOUNT"))
                  data=(cellno,password)
                  sql='insert into sellers(cellno,password) values(%s, %s)' 
                  cur.execute(sql,data)
                  db.commit()
                  print("REGISTERED SUCCESSFULLY\n"
                        "again enter your credentials to log in\n")
                  logins()
               except:
                  print(" already an account exists with the number you entered\n")
                  print("1.again register with another number\n2.log in")
                  p=int(input("enter your choice"))
                  if(p==1):
                        registers()
                  else:
                        logins()

def login():
     cellno=int(input("ENTER YOUR MOBILE NUMBER"))
     password=(input("ENTER YOUR PASSWORD"))
     sql='select cellno from buyers where cellno= %s'
     cur.execute(sql, (cellno, ))
     y=0
     for x in cur:
          y=int(x[0])
          print(y)
          break
     if(cellno==y):
          sql='select password from buyers where cellno= %s'
          cur.execute(sql, (cellno, ))
          for z in cur:
               g=z[0]
               break
          if(password==g):
               print("logged in successfull")
               home(cellno)
          else:
               print("wrong password\n1.try agian\n2.forgot password\n")
               c=int(input("Enter your Choice"))
               if(c==1):
                    login()
               else:
                    forgot()
               
          
     else:
          print("#######################\n",
                "##  user doesnt exist##\n",
                "##   1.register      ##\n",
                "##   2.log in        ##\n"
                "#######################\n")
          z=int(input("enter your choice"))
          if(z==1):
              register()
          elif z==2:
              login()
          else :
              print("wrong choice\n")
def logins():
     cellno=int(input("ENTER YOUR MOBILE NUMBER"))
     password=(input("ENTER YOUR PASSWORD"))
     sql='select cellno from sellers where cellno= %s'
     cur.execute(sql, (cellno, ))
     y=0
     for x in cur:
          y=int(x[0])
          print(y)
          break
     if(cellno==y):
          sql='select password from sellers where cellno= %s'
          cur.execute(sql, (cellno, ))
          for z in cur:
               g=z[0]
               break
          if(password==g):
               print("logged in successfull")
               homes(cellno)
          else:
               print("wrong password\n1.try agian\n2.forgot password\n")
               c=int(input("Enter your Choice"))
               if(c==1):
                    logins()
               else:
                    forgots()
               
          
     else:
          print("#######################\n",
                "##  user doesnt exist##\n",
                "##   1.register      ##\n",
                "##   2.log in        ##\n"
                "#######################\n")
          z=int(input("enter your choice"))
          if(z==1):
              registers()
          elif z==2:
              logins()
          else :
              print("wrong choice\n")

def forgot():
    print("enter your mobile number")
    m1=(input("enter mobile number"))
    print("enter new password")
    ch=str(input("enter here"))
    sql3='update buyers set password= %s where cellno= %s'
    data2=(ch,m1)
    cur.execute(sql3,data2)
    print("successfully password has be changed")
    login()
def forgots():
    m1=(input("enter mobile number"))
    print("enter new password")
    ch=str(input("enter here"))
    sql3='update sellers set password= %s where cellno= %s'
    data2=(ch,m1)
    cur.execute(sql3,data2)
    print("successfully password has be changed")
    logins()
def home(cellno):
    print("###main menu###\n"
          "1.account settings\n"
          "2.show all products shop wise\n"
          "3.search a shop by pin code\n"
          "4.exit\n")
    bz=int(input("enter your choice"))
    if bz==1:
        account(cellno)
    elif bz==2:
        showallproducts(cellno)
    elif bz==3:
        searchbypincode(cellno)
    elif bz==4:
        exit()
    else:
        print("invalid choice")
def account(cellno):
    sql='select buyerid from buyersdetails where buyerid= %s'
    cur.execute(sql, (cellno, ))
    y=0
    for x in cur:
        y=int(x[0])
        print(y)
        break 
    if(cellno==y):
            print("details are updated")
            home(cellno)
    else:
        buyername=input("enter your name")
        shipping_address=input("ente complete adress ( product will be delivered here)")
        pincode1=int(input("enter pincode"))
        sql='insert into buyersdetails(buyerid,buyername,shipping_address,pincode1) values(%s, %s, %s, %s)'
        data=(cellno,buyername,shipping_address,pincode1)
        cur.execute(sql,data)
        print("details updated")
        home(cellno)
def showallproducts(cellno):
    sql='select * from  productdetails '
    cur.execute(sql)
    result=cur.fetchall()
    print("shop id,product id,product name,cost")
    for x in result:
        print(x)
    print("Enter 1 to by any produc\n"
          "2 . go back\n")
    cz=int(input())
    if cz==1:
        cart(cellno)
    else:
        home(cellno)
def searchbypincode(cellno):
    pincode=int(input("enter pin code details\n"))
    sql='select * from  shopdetails where pincode= %s'
    cur.execute(sql,(pincode, ))
    result=cur.fetchall()
    print("##shop name##")
    for x in result:
        print(x)
    home(cellno)
def cart(cellno):
    sum=0
    print("Enter product details to buy")
    l=list(int(x) for x in input().split(" "))
    print(l)
    for x in l:
        sql='select productcost from productdetails where productid = %s'
        cur.execute(sql,(x,))
        for y in cur:
            sum=sum+int(y[0])
            break
    print("total cost is",sum)
    
def homes(cellno):
    print("AccountNo:\n",cellno)
    print("1.account\n"
    "2.add a item\n"
    "3.show added items\n"
    "4.exit\n")
    az=int(input("enter your choice"))
    if az==1:
        accounts(cellno)
    elif az==2:
        additems(cellno)
    elif az==3:
        showitems(cellno)
    elif az==4:
        exit()
    else:
        print("invalid choice")
def accounts(cellno):
    sql='select shopid from shopdetails where shopid= %s'
    cur.execute(sql, (cellno, ))
    y=0
    for x in cur:
        y=int(x[0])
        print(y)
        break 
    if(cellno==y):
            print("details are updated")
            homes(cellno)
    else:
        shopname=input("enter shop name")
        pincode=int(input("enter pincode"))
        shoptype=input("enter shoptype")
        shopkeepername=input("enter shopkeepername")
        sql='insert into shopdetails(shopid,shopname,pincode,shoptype,shopkeepername) values(%s, %s, %s, %s, %s)'
        data=(cellno,shopname,pincode,shoptype,shopkeepername)
        cur.execute(sql,data)
        print("details updated")
    
def additems(cellno):
      print(cellno)
      productid= int(input("enter product id"))
      sql='select productid from productdetails where productid= %s'
      cur.execute(sql, (productid, ))
      y=0
      for x in cur:
              y=int(x[0])
              print(y)
              break 
      if(productid==y):
            print("product with",productid," already added")
            homes(cellno)
      else:
              productname=input("enter product name")
              productcost=float(input("enter product cost"))
              sql='insert into productdetails(shopid,productid,productname,productcost) values(%s, %s, %s, %s)'
              data=(cellno,productid,productname,productcost)
              cur.execute(sql,data)
              print("item successfully added")
              homes(cellno)
def showitems(cellno):
    sql='select productid,productname,productcost from productdetails where shopid= %s'
    cur.execute(sql,(cellno, ))
    result=cur.fetchall()
    print("product id  productname  cost")
    for row in result:
        print(row)
    homes(cellno)
    
def exit():
    print("thanks for using deal to deal app")
def tittle():
    print("###############################\n",
    "## welcome to Deal to Deal   ##\n",
    "###############################\n"
    "##                           ##\n"
    "##  enter 1 to continue      ##\n"
    "##  enter 0 to exit          ##\n"
    "###############################\n")
    a=int(input("input"))
    if(a==1):
        category()
    else:
        exit()


def category():
    print("###############################\n",
    "##     select your category  ##\n",
    "##        1.buyer            ##\n",
    "##        2.seller           ##\n",
    "##        3.back             ##\n",
    "###############################\n")
    b=int(input("enter input"))
    if(b==1):
        reglogin()
    elif b==2:
        reglogins()
    elif b==3:
        tittle()
    else:
        print("invalid choice")
        category()
def reglogin():
    print("##############################\n",
    "##   1.regestration          ##\n",
    "##   2.login                 ##\n",
    "##   3.back                  ##\n",
    "###############################\n",)
    d=int(input("enter here"))
    if(d==1):
        register()
    elif d==2:
         login()
    elif d==3:
        category()
    else:
        print("invalid choice")
        reglogin()
def reglogins():
    print("##############################\n",
    "##   1.regestration          ##\n",
    "##   2.login                 ##\n",
    "##   3.back                  ##\n",
    "###############################\n",)
    d=int(input("enter here"))
    if(d==1):
        registers()
    elif d==2:
         logins()
    elif d==3:
        category()
    else:
        print("invalid choice")
        reglogins()

tittle()
#print(cellno,password)
db.commit()
db.close()
      
