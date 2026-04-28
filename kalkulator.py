"""
Kalkulator Sederhana v2.0
Author: Anhaproje 
Project: #100DaysOfCode Day 2
"""

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        raise ValueError("Error: Tidak bisa dibagi dengan nol!")
    return a / b

def main():
    print("=" * 30)
    print("  KALKULATOR PROFESIONAL v2.0")
    print("=" * 30)
    
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        print("\nPilih Operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (x)")
        print("4. Pembagian (:)")
        
        pilihan = input("Masukkan pilihan 1/2/3/4: ")
        
        print("\n" + "=" * 30)
        print("HASIL PERHITUNGAN:")
        
        if pilihan == '1':
            print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")
        elif pilihan == '2':
            print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"{angka1} x {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            print(f"{angka1} : {angka2} = {bagi(angka1, angka2)}")
        else:
            print("Error: Pilihan operasi tidak valid!")
            
    except ValueError as e:
        print(f"\nInput Error: {e}")
    
    print("=" * 30)

if __name__ == "__main__":
    main()