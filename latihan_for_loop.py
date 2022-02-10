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
#rumus fibonacci dengan menggunakan list
#dengan fungsi input:
#jumlah_deret = int(input('masukan jumlah deret: '))
jumlah_deret = 7
fibonacci = [0,1]

for i in range (2,jumlah_deret):
    fibonacci.append(fibonacci[i - 1] + fibonacci [i-2])
print (fibonacci)