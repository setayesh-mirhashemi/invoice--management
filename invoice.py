def getdate():
    year = int(input("year of buying: "))
    month = int(input("month of buying: "))
    day = int(input("day of buying: "))
    return [year, month, day]

def showdate(d):
    print("dd/mm/yyyy:",d[2], '/' , d[1],'/',d[0])
    print("-----------")
#-----------------------------------------------------------------------
def getCustomer():
    custid = int(input('Customer code:'))
    custname=input('Customer name:')

    return [ custid , custname ]

def getCustomers():
    Customers=[]
    ans='y'
    while ans=='y':
        Customer=getCustomer()
        Customers.append(Customer)

        ans = input('\n\t continue for another customer? y|n :').lower()
    return Customers
  
#---------------------------------------------------------------------- 
products = { "book":[1000,100,10],
             "pen":[250,3000,0]
            }
#----------------------------------------------------------------------
def showfactor (date,custid,custname,purchases,final_fee):
    
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("[Final Factor]")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    showdate(date)
    print("Customer : ", custid, ",", custname)
    print("--------------------------------------------")
    print("Product", "Fee", "Count", "Discount", "Final Fee", sep="\t")
    print("--------------------------------------------")

    if not purchases:
        print("No purchases for this factor.")
    else:
        for p in purchases :
            pname, fee, count, discount, final_fee = p
            print(pname,fee,count,discount,final_fee,sep='\t')

        print("--------------------------------------------")
        print("Total Fee:", final_fee)
        print("--------------------------------------------")
#----------------------------------------------------------------------
dpcount={}  #daily product count
dpincome={} #daily product income

def buyingproducts():
    purchases = []
    final_fee = 0
    ans='y'
    while ans == 'y' :
        pname = input ("Prodouct Name:" ).lower()
        if pname  in products :
           a = int(input('tedad kharid:'))
           if a > products[pname][1] :
              print('not enough products!')
           else:

              products[pname][1] -= a
              fee = products[pname][0]
              discount = products[pname][2]
              finalprice = (fee*a)-((fee*a)*(discount/100))
              final_fee += finalprice
              purchases.append([pname, fee, a , discount, finalprice])

              print('new number of book :',products['book'][1] )
              print('new number of pen :' , products['pen'][1] )
              print('fee',pname,':',finalprice)

              if pname in dpcount:
                    dpcount[pname] += a
              else:
                    dpcount[pname] = a

              if pname in dpincome:
                    dpincome[pname] += finalprice
              else:
                    dpincome[pname] = finalprice


        else:
              print('products not found.')
 
        ans=input('do yo want add another product? y|n : ').lower()
    return purchases, final_fee
        


#---------------Main--------------#
date = getdate()
customers = getCustomers()

ans_customer = 'y'
while ans_customer == 'y':
    custid_input = int(input("Enter customer code for factor: "))


    selected_customer = None
    for c in customers:
        if c[0] == custid_input:
            selected_customer = c
            break

    if selected_customer is None:
        print("Customer not found!")
    else:
        custid, custname = selected_customer
        purchases, final_fee = buyingproducts()
        showfactor(date,custid,custname,purchases,final_fee)

    ans_customer = input("Do you want to create facotr for another customer? y|n:").lower()

print("\n-------------------------------------------")
print("daily summary")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if dpcount:
    max_cproduct = list(dpcount.keys())[0] #max_cproduct:max count product
    max_cfee = dpcount[max_cproduct]       #max_cfee:max count fee
    for pname in dpcount:
        if dpcount[pname] > max_cfee:
            max_cfee = dpcount[pname]
            max_cproduct = pname
    print("the most sold:", max_cproduct, "(", max_cfee, ")")


if dpincome:
    max_incomeproduct = list(dpincome.keys())[0]
    max_feeincome = dpincome[max_incomeproduct]
    for pname in dpincome:
        if dpincome[pname] > max_feeincome:
            max_feeincome = dpincome[pname]
            max_incomeproduct = pname
    print("Highest income:", max_incomeproduct, "(", max_feeincome, ")")
    

print("-----------------------------------------------")

#-----------------------------FILE-------------------------------------
g= open("customers.txt", "w")
g.write("code,name\n")
for custid, custname in customers:
     g.write(str(custid) + "," + custname + "\n")
g.close()

h = open("products.txt", "w")
h.write("product,fee,count,discount\n")
for pname in products:
        fee, count, discount = products[pname]
        h.write(pname + "," + str(fee) + "," + str(count) + "," + str(discount))
h.close()

f = open("factors.txt", "w")
f.write("product,fee,count,discont, final fee \n")
for pname, fee, count, discount, finalprice in purchases:
     f.write(pname + "," + str(fee) + "," + str(count) + "," + str(discount) + "," + str(finalprice) + "\n")
f.close()
