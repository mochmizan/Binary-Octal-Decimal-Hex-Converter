def decimal_biner (angka, kode):
  if kode == 2:
    if (angka <= 1):
      return angka
    else:
      return str(decimal_biner(angka // 2, kode)) + str(angka % 2)
  elif kode == 10:
    if (angka <= 1):
      return angka
    else:
      jumlah = 0
      for i in range(len(str(angka))):
        jumlah += int(str(angka)[i]) * (2 ** (int(len(str(angka))) - (i + 1)))
      return jumlah
  else:
    print("Kode tidak ditemukan, pilih 2 untuk biner dan 10 untuk decimal")

def decimal_oktal(angka, kode):
  if kode == 8:
    if (angka <= 7):
      return angka
    else:
      return str(decimal_oktal(angka // 8, kode)) + str(angka % 8)
  elif kode == 10:
    if (angka <= 7):
      return angka
    else:
      jumlah = 0
      for i in range(len(str(angka))):
        jumlah += int(str(angka)[i]) * (8 ** (int(len(str(angka))) - (i + 1)))
      return jumlah
  else:
    print("Kode tidak ditemukan, pilih 8 untuk oktal dan 10 untuk decimal")

hexmap =  {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
           9: "9", 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
rhexmap = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8",
           9: "9", 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def decimal_hexa(angka, kode):
  if kode == 16:
    if (angka <= 15):
      return hexmap[int(angka)]
    else:
      return str(decimal_hexa(angka // 16, kode)) + hexmap[angka % 16]
  elif kode == 10:
    if (isinstance(angka, int) and int(angka) <= 9):
      return angka
    else:
      jumlah = 0
      for i in range(len(str(angka))):
        jumlah += int(rhexmap[str(angka)[i]]) * (16 ** (int(len(str(angka))) - (i + 1)))
      return jumlah
  else:
    print("Kode tidak ditemukan, pilih 16 untuk hexadecimal dan 10 untuk decimal")

def biner_oktal(angka, kode):
  if kode == 2:
    if (angka <= 1):
      return angka
    else:
      return decimal_biner(decimal_oktal(angka, 10), 2)
  elif kode == 8:
    if (angka <= 1):
      return angka
    else:
      return decimal_oktal(decimal_biner(angka, 10), 8)
  else:
    print("Kode tidak ditemukan, pilih 2 untuk biner dan 8 untuk oktal")

def biner_hexa(angka, kode):
  if kode == 2:
    if (isinstance(angka, int) and angka <= 1):
      return angka
    else:
      return decimal_biner(decimal_hexa(angka, 10), 2)
  elif kode == 16:
    angka = int(angka)
    if (angka <= 1):
      return angka
    else:
      return decimal_hexa(decimal_biner(angka, 10), 16)
  else:
    print("Kode tidak ditemukan, pilih 2 untuk biner dan 16 untuk hexadecimal")

def oktal_hexa(angka, kode):
  if kode == 8:
    if (isinstance(angka, int) and angka <= 7):
      return angka
    else:
      return decimal_oktal(decimal_hexa(angka, 10), 8)
  elif kode == 16:
    angka = int(angka)
    if (angka <= 7):
      return angka
    else:
      return decimal_hexa(decimal_oktal(angka, 10), 16)
  else:
    print("Kode tidak ditemukan, pilih 8 untuk oktal dan 16 untuk hexadecimal")

def menu():
  while (True):
    print("-----------Konversi Sistem Bilangan-----------")
    print("1. Decimal-Biner")
    print("2. Decimal-Oktal")
    print("3. Decimal-Hexa")
    print("4. Biner-Oktal")
    print("5. Biner-Hexa")
    print("6. Oktal-Hexa")
    print("0. Keluar")
    print()
    masukkan = input("Masukkan jenis konversi: ")
    if masukkan == "0":
      break
    manggil = angka, kode = input("Masukkan angka dan sistem bilangan yang diinginkan: ").split()
    if masukkan == "1":
      print("Hasil:", decimal_biner(int(angka), int(kode)))
    elif masukkan == "2":
      print("Hasil:", decimal_oktal(int(angka), int(kode)))
    elif masukkan == "3":
      print("Hasil:", decimal_hexa(int(angka), int(kode)))
    elif masukkan == "4":
      print("Hasil:", biner_oktal(int(angka), int(kode)))
    elif masukkan == "5":
      print("Hasil:", biner_hexa(angka, int(kode)))
    elif masukkan == "6":
      print("Hasil:", oktal_hexa(angka, int(kode)))
    else:
      print("Kode tidak ditemukan, pilih 1-6")
    print()

menu()