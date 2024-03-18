from tkinter import *

def roma_to_arabic(roma):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_num = 0
    prev_value = 0
    for char in roma:
        if char not in roman_numerals:
            return None
        current_value = roman_numerals[char]
        if current_value > prev_value:
            arabic_num += current_value - 2 * prev_value
        else:
            arabic_num += current_value
        prev_value = current_value
    return arabic_num

def arabic_to_roma(arabic_num):
    roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while arabic_num >= value:
            result += numeral
            arabic_num -= value
    return result

def cevir_butonu_tiklandi():
    giris = giris_kutusu.get().strip()
    if giris.isdigit():  # Girilen değer normal bir sayı ise
        arabic_num = int(giris)
        if 1 <= arabic_num <= 4999:
            roma_rakami = arabic_to_roma(arabic_num)
            ekran_alani.delete(0.0, END)
            ekran_alani.insert(0.0, roma_rakami)
        else:
            ekran_alani.delete(0.0, END)
            ekran_alani.insert(0.0, "Hatalı Giriş! 1 ile 4999 arasında bir sayı girin.")
    else:  # Girilen değer Roma rakamı ise
        roma_input = giris.upper()
        arabic_num = roma_to_arabic(roma_input)
        if arabic_num is not None:
            if 1 <= arabic_num <= 4999:
                ekran_alani.delete(0.0, END)
                ekran_alani.insert(0.0, str(arabic_num))
            else:
                ekran_alani.delete(0.0, END)
                ekran_alani.insert(0.0, "Hatalı Giriş! 1 ile 4999 arasında bir Roma rakamı girin.")
        else:
            ekran_alani.delete(0.0, END)
            ekran_alani.insert(0.0, "Hatalı Giriş! Geçersiz Roma rakamı veya sayı.")

pencere = Tk()
pencere.geometry("300x200")
pencere.title("Roma Rakamı / Sayı Çevirici")

giris_etiketi = Label(text="Giriş:", font=("Arial", 12))
giris_etiketi.pack()

giris_kutusu = Entry(width=30, font=("Arial", 12))
giris_kutusu.pack()

cevir_butonu = Button(text="Çevir", command=cevir_butonu_tiklandi, font=("Arial", 12))
cevir_butonu.pack()

ekran_alani = Text(width=30, height=5, font=("Arial", 12))
ekran_alani.pack()

pencere.mainloop()
