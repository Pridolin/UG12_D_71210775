#input data
def nilai_maksimal(deret_bilangan):
  nilai_terbesar = deret_bilangan[0]

  for nilai in deret_bilangan:
    if nilai > nilai_terbesar:
      nilai_terbesar = nilai
  return nilai_terbesar

def nilai_minimal(deret_bilangan):
  nilai_terkecil = deret_bilangan[0]
  for nilai in deret_bilangan:
    if nilai < nilai_terkecil:
      nilai_terkecil = nilai
  return nilai_terkecil

n = [3, 20, 100, -35, 50]
print(n)
print('Nilai terbesar:', nilai_maksimal(n))
print('Nilai terkecil:', nilai_minimal(n))
