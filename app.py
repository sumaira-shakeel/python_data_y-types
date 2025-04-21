# python data types
# my_num:int = 20
# print(type(my_num),my_num)
# # float example
# num1:float=13.5
# print(type(num1), num1)
# if you want to change your data type then apply this
# my_num = int(my_num)
# print(type(complex(my_num)), complex(my_num))


# complex data types
# num2:complex=3 + 4j
# print(type(num2),"The value of complex number is=", num2)
# # Accessing Real and Imaginary Parts
# print("Real part:", num2.real, "Imaginary part:", num2.imag)
# sequence data type
# x:list=[1,2,3,"Ali","Sana","Farah",3.4 ,3+4j,True]
# Accessing elements of the list\nprint("First element:", x[0], "Last element:", x[-1])
# print(type(x),x)
# x[2]= 10
# x[3]="Ayesha"
# x.append("Zunaira")
# print("Updated list:", x)
# tuples data types
# x:tuple=(1,2,3.4,False,"Sana",["faisal"],3+5j)
# print("Tuple length:", len(x))
# print("First element:", x[0], "Last element:", x[-1])
# print(type(x), x)  # Displaying the type and value of the tuple
# range data types
# x:range=range(1,10,2)
# for i in x: print(i)
# print(x.start)//1
# print(x.stop)//10
# print(x.step)//2
x:range = range(2,20,2)
for i in x: print(i)
print("Current range values:", list(x))
