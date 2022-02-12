#Latihan 1 : BAB perulangan for
#1. Membuat deret fibonacci

#dengan fungsi input:
#pertama = int(input('masukan angka pertama : ')) #angka pertama bilangan fibonacci dimulai dari angka 0
#kedua = int(input('masukan angka kedua: ')) #angka kedua bilangan fibonacci dimulai dari angka 1
#jumlah_deret = int(input('masukan jumlah suku deret fibonacci: '))

pertama = 0
kedua = 1
panjang_deret = 7
for i in range (panjang_deret):
    print (pertama, end=" ")
    hasil = kedua + pertama # rumus deret fibonacci = angka kedua dijumlah angka pertama
    pertama = kedua
    kedua = hasil
print ('\n')
#>>> rumus fibonacci dengan menggunakan list
#dengan fungsi input:
#jumlah_deret = int(input('masukan jumlah deret: '))
jumlah_deret = 7
fibonacci = [0,1]

for i in range (2,jumlah_deret):
    fibonacci.append(fibonacci[i - 1] + fibonacci [i-2])
print (fibonacci)
print ('\n')

#2. Menentukan Ganjil Genap:
#dengan fungsi input
#x= int(input('masukan angka: '))
x = 10
print ('x adalah bilangan','Ganjil' if (x % 2 == 1) else 'Genap ')
print ('\n')

#>>> Menampilkan List Bilangan Genap/Ganjil dari Range tertentu
print ('Masukan nilai awal dan nilai akhir')
#dengan fungsi input
#nilai_awal = int(input('Masukan nilai awal: '))
#nilai_akhir = int(input('Masukan nilai akhir: '))
nilai_awal = 1
nilai_akhir = 50
print ('''\nTampilkan bilangan :
    1. Ganjil
    2. Genap''') 
#Pilihan = int(input('pilihan 1 atau 2? : '))
Pilihan = 2
if Pilihan not in [1,2]:
    print ('pilihan anda salah!')
else :
 for x in range (nilai_awal,nilai_akhir +1 ) :
    if Pilihan == 1 and x % 2 == 1 :
        print (x, end =' ')
    elif Pilihan == 2 and x % 2 == 0 :
        print (x, end=' ')
 else : 
    print ('\n')

#3 Membuat Program Bilangan Prima
def is_prime (x):
    for i in range(2,x):
        if x % i == 0:
            return False
    
    return True

print (is_prime(2))
print (is_prime(3))
print (is_prime(4))
print (is_prime(5))

#Membuat Fungsi Pencarian Bilangan Prima
#Fungsi input
#awal = int(input('masukan angka awal= '))
#akhir = int (input('masukan angka terakhir= '))
awal = 1
akhir = 100
def cari_bilangan_prima(awal, akhir):
    list_bilangan_prima= []

    for x in range (awal,akhir +1):
        if is_prime(x):
            list_bilangan_prima.append(x)
    return list_bilangan_prima
 
print (cari_bilangan_prima(awal,akhir))

#4 Program Menghitung Huruf Vokal (Pakai 2 Cara)
#Cara 1

kalimat = 'saya'
for huruf in kalimat:
    print (huruf)

#Dengan Fungsi input
#teks = input('Tuliskan teks: ').lower()

tulis_teks = 'i love lombok'.lower()
huruf_vokal = {'a': 0, 'i':0, 'u':0, 'e':0, 'o':0}

total_huruf_vokal = 0
for karakter in tulis_teks:
    if karakter in ['a','i','u','e','o']:       
        huruf_vokal[karakter] += 1 
        total_huruf_vokal += 1

print('Tulis teks: ',tulis_teks)
print (f'Total karakter: {len(tulis_teks)}')
print (f'Total huruf vokal: {total_huruf_vokal}')
print(f"""\
    a -> {huruf_vokal['a']}
    i -> {huruf_vokal['i']}
    u -> {huruf_vokal['u']}
    e -> {huruf_vokal['e']}
    o -> {huruf_vokal['o']}\
        """)

#Cara 2. Menggunakan Fungsi string.count(), dictionary.keys() dan dictionary.values()
#Contoh: Ada berapa huruf a dalam kata "Surabaya"?
print("Surabaya".count('a'))
#ada berapa teks "ta" pada string rata-rata?
print("rata-rata".count("ta"))
#>>> Inti
#dengan fungsi input
#teks= input('Masukan Teks: ').lower()

teks = 'Indonesia'.lower()
dictionary_huruf_vokal = {
    'a': 0,
    'i': 0,
    'u': 0,
    'e': 0,
    'o': 0
}

for huruf_vokal in dictionary_huruf_vokal.keys():
    dictionary_huruf_vokal[huruf_vokal] = teks.count(huruf_vokal)

jumlah_huruf_vokal = sum(dictionary_huruf_vokal.values())
print ('Masukan teks: ',teks)
print (f'Jumlah karakter: {len(teks)}')
print (f'Jumlah huruf vokal: {jumlah_huruf_vokal}')
print(f"""\
    a -> {dictionary_huruf_vokal['a']}
    i -> {dictionary_huruf_vokal['i']}
    u -> {dictionary_huruf_vokal['u']}
    e -> {dictionary_huruf_vokal['e']}
    o -> {dictionary_huruf_vokal['o']}\
    """)