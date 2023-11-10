class point:
	class pp:
		x = 0
		y = 0
	t = pp()
	z = 0

p = point()

p.t.x = 10
p.t.y = 20
p.z = 30

print(p.t.x, end=',')
print(p.t.y, end=',')
print(p.z)
