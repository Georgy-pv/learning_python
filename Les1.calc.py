str_command = input("Please type your command a + b or a - b: ")

str_A = ''
str_B = ''
operation = ''

for letter in str_command:
    if letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^' :
        operation = letter
    else:
        if operation == '':
            str_A += letter
        else:
            str_B += letter


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