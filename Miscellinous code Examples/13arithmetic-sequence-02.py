# arithmetic sequence a(n) = a(0) + (n-1)d

def main():
	print("printing arithmetic sequence a(n) = a(0) + (n-1)d")
	a0 = int(input("enter start "))
	d = int(input("enter common difference "))
	count = int(input("enter count "))

	i=1
	while i <= count:
		an = a(a0, d, i)
		print(an)
		i = i + 1

def a(a0, d, n):
	return a0 + (n-1)*d

main()