a = 33
b = 33
if b > a:
    print("b is grater than a")

    # elif- if previous condition werenot true then try this conditions
elif a == b:
    print("a and b are equal")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for m in range(10):
   print(m)
else:
   print("finally finish")

for n in range(2, 30, 3):
   if n == 8: continue
   print(n)
else:
   print("finally finished")

   adj = ["red", "big", "tasty"]
   for j in adj:
      for k in fruits:
         print(j, k)
