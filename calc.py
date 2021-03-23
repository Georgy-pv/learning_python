str_command = input("Please type your command a + b or a - b: ").replace(' ','')
#Числа

operations_tuple = ('^', '*', '/', '+', '-')
str_A = ''
str_B = ''

variables = ['']
operations = []

# prioritet = {
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2,
#     '^': 3
# }
digit_chars = tuple(map(str, range(10))) + tuple('.-')


for i, letter in enumerate(str_command):
	if letter in operations_tuple and (i > 0) and variables[len(operations)] != '':
		operations.append(letter)
		variables.append('')
	elif letter in digit_chars:
		index = len(operations)
		variables[index] += letter
        
variables = list(map(float, variables))
result = variables[0]

for i, operation in enumerate(operations): 
    if type (result) == str:
        break
    varA=result
    varB=variables[i+1]
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