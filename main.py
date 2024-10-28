# Program Auto Gate MRT
# ...

# Kamus
# ...
# ...

# Algoritma
stasiun_MRT = ["Lebak Bulus Grab", "Fatmawati", "Cipete Raya", "Haji Nawi", "Blok A", "Blok M BCA", "ASEAN", "Senayan", "Isnora Mandiri", "Bendungan Hilir", "Setiabudi Astra", "Dukuh Atas BNI", "Bundaran HI"]

posisi_awal = input("masukkan posisi awal anda: ")
a = 0 
for i in stasiun_MRT:
    a+=1
    if posisi_awal.lower() == i.lower():
        index_posisi_awal = a

print(index_posisi_awal)

# test branch merging from dev to main.
