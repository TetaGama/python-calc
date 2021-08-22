x = float(input("giv 1: "))
y = float(input("giv 2: "))
choice= input('wyw 1 2 3 4 for add sub mul div: ')

if choice == "1":
    a= (x+y)
    print("addition"+ str(a))


elif choice == "2":
    a= (x-y)
    print("subtraction"+ str(a))


elif choice == "3":
    a= (x*y)
    print("multiplication"+ str(a))
    

elif choice == "4":
    a= (x/y)
    print("division"+ str(a))


else :
    print("wrong dummy mf")
