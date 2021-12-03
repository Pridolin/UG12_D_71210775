#input data
a = int(input("Masukan Angka : "))

for i in range(a):
    for j in range(a,i,-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()

for i in range(a-2,-1,-1):
    for j in range(a,i,-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
