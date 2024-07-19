import tkinter as tk

# Fungsi yang akan dipanggil saat tombol ditekan
def on_button_click():
    label.config(text="Tombol ditekan!")

# Membuat instance dari Tkinter
root = tk.Tk()

# Mengatur judul jendela
root.title("Contoh GUI Sederhana")

# Membuat label
label = tk.Label(root, text="Halo, ini GUI sederhana menggunakan Tkinter!")
label.pack(pady=10)

# Membuat tombol
button = tk.Button(root, text="Tekan saya!", command=on_button_click)
button.pack()

# Menjalankan main loop
root.mainloop()
