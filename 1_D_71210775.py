#input data
deret1 = int(input("Masukkan awal deret : "))
deret2 = int(input("Masukkan akhir deret : "))

x = []
if (deret1 + 1) % 2 == 0:
     for i in range (deret1+1,deret2,2):
         if i % 3 == 0 or i % 7 == 0: continue
         print ( i , end = " " )
else:
     for i in range (deret1 , deret2 , 2):
         if i % 3 == 0 or i % 7 == 0 : continue
         print (i , end = " ")
