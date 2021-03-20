instr = '2 + 2 * 2'.replace(' ','')

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

for letter in instr: 
    if letter in all_ops and actions[-1]:
        actions.append({'opr': letter, 'val': ''})
    elif letter in digit_chars:
        actions[-1]['val'] += letter
print(actions)

