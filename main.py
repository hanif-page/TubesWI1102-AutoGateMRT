# Program Auto Gate MRT
# Program sederhana berbasis command line yang menyerupai sistem auto gate MRT. 

# Assumptions
# - Jarak antar stasiun adalah 2km
# - Tarif perjalanan adalah Rp4000 per 10km, artinya Rp800 per 2km
# - Artinya, saldo minimum (untuk menempuh seluruh stasiun, yaitu 12 stasiun) yang dibutuhkan adalah 12xRp800 = Rp9600

# Algoritma
stations = ["Lebak Bulus Grab", "Fatmawati", "Cipete Raya", "Haji Nawi", "Blok A", "Blok M BCA", "ASEAN", "Senayan",
                "Istora Mandiri", "Bendungan Hilir", "Setiabudi Astra", "Dukuh Atas BNI", "Bundaran HI"] #array stasiun mrt
indeks = [161,198,162,165,190,199,196] #array nim TPB
cards = []

# fungsi pembantu
def findIndex(array, find): #input array dan item, output index item tsb dalam array 
    index = 0
    for i in array:
        if find != i:
            index += 1
        else:
            return index
def findCardIndex(cards, cardID): #input array cards dan id card, output index id card tersebut dalam array cards.
    index = 0
    for i in cards:
        if cardID != i[0]:
            index += 1
        else:
            return index

# untuk memasukkan data id kartu dan saldo awal (check isValid)
def kartuvalid(nomor_unik): #menentukan apakah 3 digit pertama id kartu merupakan nim tpb
    ada = False
    for i in range(0, len(indeks)):
        if nomor_unik == indeks[i]:
            ada = True
    return ada

def cekidcard(cards, idcard):
    ada = False
    y = 0
    for i in range(0, len(cards)):
        if cards[i][0] == idcard:
            ada = True
            y = i
    return [ada, y]

def cekntopup(cards):
    if len(cards) != 0:
        print("\nID Card : Nominal")
        for i in range(0, len(cards)):
            print(f"{cards[i][0]} : {cards[i][1]}")
    else:
        print("\nBelum ada kartu yang terdaftar.")
    ingintopup = input("\nApakah anda ingin topup/meregistrasi kartu? (y/n): ")
    if ingintopup == "n":
        pass
    else:
        while True:
            idcard = int(input("\nMohon masukan nomor ID Card: "))
            if len(str(idcard)) != 8:
                print("\nNomor Tidak Valid (Jumlah Digit Tidak Sesuai)")
            else:
                if not kartuvalid(idcard // 100000):
                    print('\nNomor Tidak Valid (3 Digit Awal Wajib Merupakan NIM Jurusan Dengan Awalan "Sekolah")')
                else:
                    TopUp = int(input("\nMasukan nominal Top Up: "))
                    y = cekidcard(cards, idcard)
                    if y[0]:
                        cards[y[1]][1] += TopUp
                        print(f"\nSaldo terbaru anda (ID {cards[y[1]][0]}) adalah {cards[y[1]][1]}")
                    else:
                        cards += [[idcard, TopUp]]
                        print(f"\nSaldo terbaru anda (ID {cards[len(cards)-1][0]}) adalah {cards[len(cards)-1][1]}")
                    break

def cardReader(idCard, cards):
    status = cekidcard(cards, idCard)
    if status[0]:
    # cek saldo
        if cards[status[1]][1] >= 14000:
            return [True, "\nKartu Valid Dan Memenuhi Saldo Minimum"], cards # kartu valid dan memiliki saldo minimum yang cukup
        else:
            return [False, "\nSaldo Kurang Dari Rp14000"], cards
    else:
        return [False, "\nKartu belum terdaftar"], cards

def gate(idCard, cards):
    startLocation = int(input("\nMasukkan nomor stasiun awal: "))
    while startLocation < 1 or startLocation > 13:
        print("\nInput tidak valid!")
        startLocation = int(input("\nMasukkan Nomor Stasiun Awal"))
    
    print("\nSelamat menikmati layanan MRT :)\n")

    idCardExit = int(input("Mohon masukkan ID kartu E-Money anda untuk keluar: "))
    while idCardExit != idCard:
        print("\nKartu tidak terdaftar pada sistem")
        idCardExit = int(input("Mohon masukkan ID kartu E-Money anda untuk keluar: "))

    endLocation = int(input("\nMasukkan nomor stasiun akhir: "))
    
    while endLocation < 1 or endLocation > 13 or endLocation == startLocation:
        print("\nInput tidak valid!")
        endLocation = int(input("\nMasukkan nomor stasiun akhir: "))
    
    price_per_km = 400
    jarak_ditempuh = abs(endLocation-startLocation)*2 #asumsikan jarak antar stasiun 2 km
    tarif_awal = 3200

    price= jarak_ditempuh*price_per_km + tarif_awal #menentukan tarif
    cardIndex = findCardIndex(cards, idCardExit)#mencari index kartu di database
    cards[cardIndex][1] -= price #mengurangi saldo kartu
    
    #penyajian data
    print(f"\nAnda telah menempuh perjalan sejauh {jarak_ditempuh} km")
    print(f"Total tarif perjalan anda: Rp.{price},00")
    print(f"Saldo akhir kartu E-Money anda (ID {idCard}): Rp.{cards[cardIndex][1]},00")
    print("\nTerima Kasih telah menggunakan layanan MRT")
    print("Sampai jumpa di perjalanan berikutnya")

def main(cards):
    while True:
        print("\n==========================================")
        inp = input("\nSelamat Datang\n"
                    "\nMohon Pilih Untuk Melanjutkan:"
                    "\n1. Masuk MRT"
                    "\n2. Cek Saldo dan Top Up Kartu"
                    "\n(Ketik angka selain 1 atau 2 untuk keluar)\n\n: ")
        if inp == "1":
            # masuk
            print("\nList Stasiun MRT:\n"
                  "1. Lebak Bulus Grab\n"
                  "2. Fatmawati\n"
                  "3. Cipete Raya\n"
                  "4. Haji Nawi\n"
                  "5. Blok A\n"
                  "6. Blok M BCA\n"
                  "7. ASEAN\n"
                  "8. Senayan\n"
                  "9. Istora Mandiri\n"
                  "10. Bendungan Hilir\n"
                  "11. Setiabudi Astra\n"
                  "12. Dukuh Atas BNI\n"
                  "13. Bundaran HI")
            print("\nMohon Masukkan ID Kartu E Money Anda Untuk Masuk: ")
            idCard = int(input("ID Card: "))

            cardStatus, cards = cardReader(idCard, cards)
            if cardStatus[0]:
                # lanjut ke fungsi gate
                gate(idCard, cards)
            else:
                print(cardStatus[1])
        elif inp == "2":
            cekntopup(cards)
        else:
            print("\nTerima Kasih Telah Menggunakan Layanan MRT")
            break

main(cards)