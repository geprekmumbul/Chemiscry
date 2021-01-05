import os
from nama import input_nama, Salah
from struk import struktur_standar
from jpeg import print_text


def main():
    while True:
        try:
            nama = input_nama()
            struktur = struktur_standar(nama)
            print_text(struktur)
            os.startfile("C:/Users/Admin/Desktop/Alkana/image.jpeg")
        except Salah as error:
            print('Kesalahan :', error.value)


main()

'''
metuna
3-butena
1-butena
1-metilpentana
7-etil-3,4-dimetil-1-oktena
4-etil-2,3-dimetil-1-oktena

'''