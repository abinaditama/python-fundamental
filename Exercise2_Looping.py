number_of_books = 10
book_already_read = 0

while book_already_read < number_of_books:
    book_already_read += 1
    print(f'books already read are {book_already_read}')


jml_buku = 10
jml_buku_dibaca = 0
while jml_buku_dibaca < jml_buku:
    if jml_buku_dibaca == 9:
        print(f'Buku ke {jml_buku_dibaca} belum dibaca')
    else:
        jml_buku_dibaca += 1
        print(f'jumlah buku yg sudah dibaca {jml_buku_dibaca}')