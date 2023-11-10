import enum

class gender(enum.Enum):
	male = 0
	female = 1

print(gender.male)
print(gender.female)

class gender2:
	male = 'm'
	female = 'f'

print(gender2.male)
print(gender2.female)

d = gender2()
d.trans = 't'
print(d.male)
print(d.female)
print(d.trans)

