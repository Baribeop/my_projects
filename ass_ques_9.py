# question 9
h = []
k =[]
for i in range(1,1001):
 p = i**2
 h.append(p)
for n in h:
 if n < 1000:
  print(n)
  k.append(n)
print(k)
perfect_square_count = (len(k))
print(perfect_square_count)
q = []
r =[]
for i in range(2,1001):
 p = i**3
#  print (q)
 q.append(p)
# print(r)
for m in q:
 if m < 1000:
  print(m)
  r.append(m)
print(r)
perfect_cube_count =(len(r))
print(perfect_cube_count)

s = []
t =[]
for i in range(2,1001):
 p = i**5
#  print (s)
 s.append(p)
# print(s)
for l in s:
 if l < 1000:
  print(l)
  t.append(l)
print(t)
perfect_fifth_count = (len(t))
print(perfect_fifth_count)
tot_count = perfect_square_count + perfect_cube_count + perfect_fifth_count
print(tot_count)
non_count = i-tot_count
print(non_count)
