str_command = input("Please type your command a + b or a - b: ").replace(' ','')
#Числа
str_A = ''
str_B = ''

variables = ()
operations = tuple()

for i, letter in enumerate(str_command):
	if letter in '+-*/^' and (i > 0) and variables[len(operations)] != '':
		operations+=(letter, )
		# variables+=('', )
	else:
		index = len(operations)
		variables[index]+=letter
    print(index)
variables = list(map(float, variables))
result = variables [0]

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



a = (2, 5, 4, 7)
a+=(5, )
print(a)