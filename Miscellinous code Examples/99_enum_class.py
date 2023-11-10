import enum

class gender(enum.Enum):
	male = 0
	female = 1

print(gender.male)
print(gender.female)

class gender2:
	male = 0
	female = 1

print(gender2.male)
print(gender2.female)
