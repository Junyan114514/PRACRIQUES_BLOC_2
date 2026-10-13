for n1 in range(3):
 for n2 in range(5):
  print("n1 = " + str(n1) + ", n2 = " + str(n2))

n1 = 0
while n1<3:
 n2 = 0
 while n2<5:
  print("n1 = " + str(n1) + ", n2 = " + str(n2))
  n2 = n2 + 1
 n1 = n1 + 1

n1 = 0
while n1<3:
 for n2 in range(5):
  print("n1 = " + str(n1) + ", n2 = " + str(n2))
 n1 = n1 + 1
