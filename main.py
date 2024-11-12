# Program Auto Gate MRT
# ...

# Assumptions
# - Jarak antar stasiun adalah 2km
# - Tarif perjalanan adalah Rp4000 per 10km, artinya Rp800 per 2km
# - Artinya, saldo minimum (untuk menempuh seluruh stasiun, yaitu 12 stasiun) yang dibutuhkan adalah 12xRp800 = Rp9600

# Algoritma
stations = ["Lebak Bulus Grab", "Fatmawati", "Cipete Raya", "Haji Nawi", "Blok A", "Blok M BCA", "ASEAN", "Senayan", "Isnora Mandiri", "Bendungan Hilir", "Setiabudi Astra", "Dukuh Atas BNI", "Bundaran HI"]
cards = [[16524001, 21000], [19624002, 100000]]

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


def card():
    cards = []

    # ... (random atau pake NIM)

    return cards

def cardReader(idCard):

    cardsCount = len(cards)

    for i in range(0, cardsCount):
        if cards[i][0] == idCard:
            # cek saldo
            if cards[i][1] >= 9600:
                return [True, "Kartu Valid Dan Memenuhi Saldo Minimum"] # kartu valid dan memiliki saldo minimum yang cukup
            return [False, "Saldo Kurang Dari Rp9.600"] 
        else:
            return [False, "Kartu Tidak Valid"]

def gate(idCard):

    startLocation = input("Masukkan Stasiun Awal: ")
        
    idCardExit = int(input("Mohon Masukkan ID Kartu E Money Anda Untuk Keluar: "))

    while idCardExit != idCard:
        print("\nKartu Tidak Terdaftar Pada Sistem")

        idCardExit = int(input("Mohon Masukkan ID Kartu E Money Anda Untuk Keluar: "))

    endLocation = input("\nMasukkan Stasiun Akhir: ")

    startIndex = findIndex(stations, startLocation)
    endIndex = findIndex(stations, endLocation)

    pricePer2KM = 800
    price = abs(startIndex-endIndex)*pricePer2KM

    cardIndex = findCardIndex(cards, idCardExit)

    cards[cardIndex][1] -= price

    print(f"Anda telah menempuh perjalanan sejauh {abs(startIndex-endIndex)*2} KM")
    print(f"Total Tarif Perjalanan Anda: Rp{price}")
    print(f"Saldo Akhir Kartu E Money Anda (ID {idCard}): Rp{cards[cardIndex][1]}")
    print("\nTerima Kasih Telah Menggunakan Layanan MRT")
    print("Sampai Jumpa Di Perjalanan Berikutnya")

def main():
    # note : belum di kurung dalam while

    print("Mohon Masukkan ID Kartu E Money Anda Untuk Masuk: ")

    idCard = int(input("ID Card: "))

    cardStatus = cardReader(idCard)

    if cardStatus[0]:
        # lanjut ke fungsi gate
        gate(idCard)
    else:
        print(cardStatus[1])

main()