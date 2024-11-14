# TO DO 
# - cek fungsi gate
# - pake fungsi aqeelappend (untuk ganti fungsi append)

# Program Auto Gate MRT
# ...

# Assumptions
# - Jarak antar stasiun adalah 2km
# - Tarif perjalanan adalah Rp4000 per 10km, artinya Rp800 per 2km
# - Artinya, saldo minimum (untuk menempuh seluruh stasiun, yaitu 12 stasiun) yang dibutuhkan adalah 12xRp800 = Rp9600

# Algoritma
stations = ["Lebak Bulus Grab", "Fatmawati", "Cipete Raya", "Haji Nawi", "Blok A", "Blok M BCA", "ASEAN", "Senayan", "Isnora Mandiri", "Bendungan Hilir", "Setiabudi Astra", "Dukuh Atas BNI", "Bundaran HI"]
cards = []

# fungsi pembantu
def findIndex(array, find):
    index = 0
    for i in array:
        if find != i:
            index += 1
        else:
            return index
def findCardIndex(cards, cardID):
    index = 0
    for i in cards:
        if cardID != i[0]:
            index += 1
        else:
            return index
def aqeelappend(prevArray , obj):
    y = [0] * (len(prevArray)+1)
    for i in range(0, len(y)):
        if i < len(prevArray):
            y[i] = prevArray[i]
        else:
            y[i] = obj
    return y

# untuk memasukkan data id kartu dan saldo awal (check isValid)
def card(cardID, initialBalance):
    # ... (random atau pake NIM)

    indeks=[161,198,162,165,190,199,196]
    ada=False
    nomor_unik=cardID//100000
    if len(str(cardID))!= 8:
        print("Nomor Tidak Valid (Jumlah Digit Tidak Sesuai)")
    else:
        for i in range (len(indeks)):
            if nomor_unik==indeks[i] and ada==False:
                ada=True
            if ada==True and nomor_unik!=indeks[i]:
                ada=True
        if ada==False:
            return [False, 'Nomor Tidak Valid (3 Digit Awal Wajib Merupakan NIM Jurusan Dengan Awalan "Sekolah")']
        if ada==True and initialBalance<14000:
            return [False, f"Saldo Anda Tidak Cukup (Dibutuhkan Saldo Minimum Rp14000)"]
        elif ada==True and initialBalance>=14000:
            cards.append([cardID, initialBalance]) # ganti pake aqeel append.
            return [True, f"Silahkan Melanjutkan Perjalanan"]        

def cardReader(idCard):

    cardsCount = len(cards)


    for i in range(0, cardsCount):
        if cards[i][0] == idCard:
            # cek saldo
            if cards[i][1] >= 14000:
                return [True, "Kartu Valid Dan Memenuhi Saldo Minimum"] # kartu valid dan memiliki saldo minimum yang cukup
            return [False, "Saldo Kurang Dari Rp14000"]
    # Mendaftarkan kartu baru
    print("\nKartu Anda Baru Akan Didaftarkan.")
    initialBalance = int(input("Masukkan Saldo Awal Anda: "))
    cardStatus = card(idCard, initialBalance)
    return cardStatus    



def gate(idCard):

    # Buat list stasiun dari no 1-13.

    # Nanti inputnya berdasarkan no 1-13.

    # Buat pengecualian kondisi jika user input selain 1-13. (Jika input selain 1-13, maka beri tahu bahwa input stasiun tidak sesuai dan jalankan kembali loop)

    startLocation = input("\nMasukkan Stasiun Awal: ")
        
    idCardExit = int(input("Mohon Masukkan ID Kartu E Money Anda Untuk Keluar: "))

    while idCardExit != idCard:
        print("\nKartu Tidak Terdaftar Pada Sistem")

        idCardExit = int(input("Mohon Masukkan ID Kartu E Money Anda Untuk Keluar: "))

    endLocation = input("\nMasukkan Stasiun Akhir: ")

    startIndex = findIndex(stations, startLocation)
    endIndex = findIndex(stations, endLocation)

    pricePer2KM = 800
    price = (abs(startIndex-endIndex)*pricePer2KM) + 3200 # Rp4000 adalah tarif minimum

    cardIndex = findCardIndex(cards, idCardExit)

    cards[cardIndex][1] -= price

    print(f"\nAnda telah menempuh perjalanan sejauh {abs(startIndex-endIndex)*2} KM")
    print(f"Total Tarif Perjalanan Anda: Rp{price}")
    print(f"Saldo Akhir Kartu E Money Anda (ID {idCard}): Rp{cards[cardIndex][1]}")
    print("\nTerima Kasih Telah Menggunakan Layanan MRT")
    print("Sampai Jumpa Di Perjalanan Berikutnya")

def main():

    while True:
        print("\n==========================================")
        inp = input("Selamat Datang\n\nMohon Pilih Untuk Melanjutkan:\n1. Masuk MRT\n(tekan selain 1 untuk keluar program)\n\n: ")
        if inp == "1":
            # masuk
            print("\nMohon Masukkan ID Kartu E Money Anda Untuk Masuk: ")
            idCard = int(input("ID Card: "))

            cardStatus = cardReader(idCard)

            if cardStatus[0]:
                # lanjut ke fungsi gate
                gate(idCard)
            else:
                print(cardStatus[1])
        else:
            print("\nTerima Kasih Telah Menggunakan Layanan MRT")
            break

main()