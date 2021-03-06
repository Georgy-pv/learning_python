str_input=input("Введите первое число: ")

varA=float(str_input)
print(type(varA))

operation=input("Введите оператор: ")

str_input2=input("Введите второе число: ")

varB=float(str_input2)
print(type(varB))

result=None

if operation=='/' :
    if varB == 0:
        result = "Inf"
    else:
        result = varA/varB
elif operation=='*' : 
    result=varA*varB
elif operation=='-' : 
    result=varA-varB 
elif operation=='+' : 
    result=varA+varB
elif operation=='^' : 
    result=varA**varB
else : 
    result='Введите корректный оператор'


print("Result: " + str(result))