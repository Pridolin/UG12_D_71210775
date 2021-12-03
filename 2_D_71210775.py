#input data
hari = input("Hi Kiko, Silahkan Masukkan hari yang ingin Anda telusuri: ")
hari1 = ("kelas ke-1 Algorima Graf","kelas ke-3 Sistem Operasi","kelas ke-4 PAK")
hari2 = ("kelas ke-2 Matematika Teknik","kelas ke-4 Bhs Indonesia","kelas ke-6 PKN")
hari3 = ("kelas ke-2 Sistem Basis Data","kelas ke-4 Praktikum Sistem Basis Data")
hari4 = ("kelas ke-1 IMK","kelas ke-3 LogMat","kelas ke-4 Praktekkom")

if hari == "senin" :
    for i in range(len(hari1)):
        print(hari1[i])
elif hari == "selasa" :
    for i in range(len(hari2)):
        print(hari2[i])
elif hari == "rabu" :
    for i in range(len(hari3)):
        print(hari3[i])
elif hari == "kamis" :
    for i in range(len(hari4)):
        print(hari4[i])
elif hari == "jumat" :
    print("Hari Jumat Anda tidak ada kelas")
    