number_of_books = 10
book_already_read = 0

while book_already_read < number_of_books:
    book_already_read += 1
    print(f'books already read are {book_already_read}')


jml_buku = 10
jml_buku_dibaca = 0
total_baca = 0
while jml_buku_dibaca < jml_buku:
    if jml_buku_dibaca == 10:
        print(f'Buku ke {jml_buku_dibaca +1 } belum dibaca')
        while total_baca < 5:
            print(f'ulangi buku ke {jml_buku_dibaca + 1}')
            total_baca += 1
        jml_buku_dibaca += 1
    else:
        jml_buku_dibaca += 1
        print(f'jumlah buku yg sudah dibaca {jml_buku_dibaca}')
