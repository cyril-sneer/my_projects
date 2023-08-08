# dict

Capitals = {
    'Russia': 'Moscow',
    'Ukraine': 'Kiev',
    'USA': 'Washington'
    }

print(Capitals)

Capitals2 = dict(France='Paris', Italy='Rome', Germany='Berlin')

print(Capitals2)

Capitals3 = dict([('Spain', 'Madrid'), ('Norway', 'Oslo'), ('Poland', 'Warsaw')])

print(Capitals3)

for key, val in Capitals.items():
    print(key, val)

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)
# True