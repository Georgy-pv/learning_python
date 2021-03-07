str_command = input("Please type your command a + b or a - b: ")

str_A = ''
str_B = ''
operation = ''
i = 0


while i < len(str_command) :
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^' :
        operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B += str_command[i]
    print(str_command[i])
    i += 1
    


str_A = str_A.strip()
str_B = str_B.strip()
varA=float(str_A)
varB=float(str_B)


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