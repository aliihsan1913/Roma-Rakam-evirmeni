from tkinter import Tk, Text, Button, messagebox, font
from tkinter.filedialog import asksaveasfilename

def hizli_okuma():
    metin = metin_alani.get("1.0", "end-1c")
    kelimeler = metin.split()
    yeni_metin = ""
    for i in range(len(kelimeler)):
        yeni_metin += kelimeler[i]
        if (i + 1) % 3 == 0:
            yeni_metin += "\n"
        else:
            yeni_metin += " "
    kaydet(metin_basligi.get("1.0", "end-1c"), yeni_metin)

def kaydet(baslik, metin):
    dosya_adi = baslik + "_hizli_okuma.txt"
    dosya_yolu = asksaveasfilename(initialfile=dosya_adi)
    if dosya_yolu:
        with open(dosya_yolu, "w") as dosya:
            dosya.write(metin)
        messagebox.showinfo("Başarılı", "Dosya başarıyla kaydedildi.")
        temizle()

def temizle():
    metin_basligi.delete("1.0", "end")
    metin_basligi.insert("1.0", "Başlık Giriniz")
    metin_alani.delete("1.0", "end")

# Arayüzüm
root = Tk()
root.title("Hızlı Okuma Metin Dönüştürücü")

metin_basligi = Text(root, height=1, width=40)
metin_basligi.insert("1.0", "Başlık Giriniz")  # Başlık için placeholder
metin_basligi.pack()

metin_alani = Text(root, height=10, width=50)
metin_alani.pack()

bold_font = font.Font(metin_alani, metin_alani.cget("font"))
bold_font.configure(weight="bold")

def bold_middle_words(event):
    start_index = "1.0"
    while True:
        start_index = metin_alani.search(" ", start_index, stopindex="end", regexp=True)
        if not start_index:
            break
        end_index = metin_alani.search(" ", f"{start_index}+1c", stopindex="end", regexp=True)
        if not end_index:
            break
        metin_alani.tag_add("bold", f"{start_index}+1c", f"{end_index}-1c")
        metin_alani.tag_config("bold", font=bold_font)
        start_index = end_index

metin_alani.bind("<KeyRelease>", bold_middle_words)

dönüştür_button = Button(root, text="Metni Dönüştür", command=hizli_okuma)
dönüştür_button.pack()

root.mainloop()
