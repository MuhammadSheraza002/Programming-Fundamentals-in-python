# arithmetic sequence a(n) = a(0) + (n-1)d
print("example of arithmetic sequence 'a(n) = a(0) + (n-1)d'")
a0 = int(input("enter start 'a(0)'"))
d = int(input("enter common difference 'd'"))
n = int(input("enter count 'n'"))

print("nth item of the sequence	is", a0 + (n-1)*d)
print()

print("The sequence is")

n = 1
while j <= n:
	an = a0 + (j-1)*d
	print(an)
	j = j + 1
