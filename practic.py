
instr = '2 * 3 + 5 + 2^3'.replace(' ','')

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = tuple('+-')
all_ops = hp_ops + mp_ops + lp_ops

# digit_chars = tuple(map(str, range(10))) + tuple('.-')
digit_chars = tuple('0123456789.-')

actions = []
d = dict()
d['opr'] = ''
d['val'] = ''

actions.append(d)

for i, letter in enumerate(instr) : 
    if letter in all_ops and (i>0) and actions[-1].get('val') != '':
        actions.append({'opr': letter, 'val': ''})
    elif letter in digit_chars:
        actions[-1]['val'] += letter
# print(actions)

result = '0'
error = False

i = 0 
actions.reverse()
while i < len(actions):
    action = actions[i]
    operation = action.get('opr')
    if operation in hp_ops:
        if operation == '^':
            pre_res = float(actions[i+1].get('val'))**float(action.get('val'))
            actions[i+1]['val'] = str(pre_res)
            del actions[i]
    else:
        i+=1
print(actions)
actions.reverse()

print(actions)
i = 0 
while i < len(actions):
    action = actions[i]
    operation = action.get('opr')
    if operation in mp_ops:
        if float(action.get('val')) == 0 and operation == '/':
            result = 'Inf'
            error = True
        else:
            pre_res = eval('{0}{1}{2}'.format(float(actions[i-1].get('val')), operation, float(action.get('val')))) 
            actions[i-1]['val'] = str(pre_res)
        del actions[i]
    else:
        i+=1
print(actions)

if not error:
    for action in actions:
        if error:
            break
        var_A = result
        var_B = action.get('val')
        operation = action.get('opr')
        if operation in lp_ops:
            result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
        else:
            result = var_B
print(actions)

print('Результат: {}'.format(result))