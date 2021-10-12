# Title

# List import
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

# Menjalankan program
# streamlit run 'Equation Solver 3 - 3.py'

# Streamlit
st.title('Equation Solver 3')
st.write('Selamat datang di program ini')
st.write('')

st.write('### **Persamaan**')

st.sidebar.write('### **Persamaan**')
persamaan_list = ["Persamaan Linear", "Persamaan 2 Variabel", "Persamaan Kuadrat"]
persamaan = st.sidebar.selectbox("Pilih persamaan:", persamaan_list)

# Konversi float ke int, contoh: 3.0 menjadi 3, 3.2 menjadi 3.2
def fungsi(angka):
    if round(angka, 5) == round(angka, 0):
        angka = int(angka)
    else:
        angka = round(angka, 5)
    
    return angka

# Plus minus
def fungsi2(angka):
    if angka < 0:
        angka = f"- {-angka}"
    else:
        angka = f"+ {angka}"

    return angka

# Kurung
def fungsi3(angka):
    if angka < 0:
        angka = f"({angka})"

    return angka

# Angka 1 dengan variabel
def fungsi4(angka):
    if angka == "+ 1" or angka == 1:
        if angka == 1: angka = ""
        else: angka = "+ "
    elif angka == "- 1" or angka == -1:
        if angka == -1: angka = "-"
        else: angka = "- "

    return angka

if persamaan == persamaan_list[0]:
    st.markdown("a*x + b = c")
    st.sidebar.write('### **Masukkan angka**')
    a = float(st.sidebar.text_input("a (Default: 2)", value=2))
    b = float(st.sidebar.text_input("b (Default: 1)", value=1))
    c = float(st.sidebar.text_input("c (Default: 5)", value=5))

    st.write('### **Hasil Persamaan**')

    ruas_kiri = f"{fungsi(a)}x + {fungsi(b)}"
    ruas_kanan = fungsi(c)

    hasil_persamaan = f"{ruas_kiri} = {ruas_kanan}"

    st.markdown(hasil_persamaan)

    st.write('### **Hasil Penyelesaian**')

    hasil = (c - b) / a
    st.markdown(f"x = {fungsi(hasil)}")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)

    if muncul_1:
        st.write('### **Langkah Penyelesaian**')

        st.write("### 1. Siapkan inputnya")
        st.write(f"   {hasil_persamaan}")
        st.write("### 2. Buatlah pengurangan ruas kiri dan kanan")
        st.write(f"   {ruas_kiri} - {fungsi(b)} = {ruas_kanan} - {fungsi(b)}")
        st.write("### 3. Kurangkan kedua ruas")
        st.write(f"   {fungsi(a)}x = {fungsi(c - b)}")
        st.write("### 4. Buatlah pembagian ruas kiri dan kanan")
        st.write(f"   ({fungsi(a)} / {fungsi(a)})x = {fungsi(c - b)} / {fungsi(a)}")
        st.write("### 5. Bagikan kedua ruas")
        st.write(f"   x = {fungsi(hasil)}")

    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)

    if muncul_2:
        st.write('## **Grafik**')

        jarak = -5
        batas = 5
        ukuran = 0.01

        plt.style.use('seaborn')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = a*x + b
        plt.plot(x,y1)

        y2 = 0*x + c
        plt.plot(x,y2)

        plt.xlabel("x", size=12)
        plt.ylabel("y")
        plt.legend([ruas_kiri, ruas_kanan])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)

if persamaan == persamaan_list[1]:
    st.latex(r"ax + by = c")
    st.latex(r"dx + ey = f")
    st.sidebar.write('### Masukkan angka')
    a = float(st.sidebar.text_input("a (Default: 1)", value=2))
    b = float(st.sidebar.text_input("b (Default: 1)", value=1))
    c = float(st.sidebar.text_input("c (Default: 5)", value=5))
    d = float(st.sidebar.text_input("d (Default: 3)", value=3))
    e = float(st.sidebar.text_input("e (Default: -2)", value=-2))
    f = float(st.sidebar.text_input("f (Default: 4)", value=4))

    st.write('### **Hasil Persamaan**')

    ruas_kiri_1 = fr"{fungsi4(fungsi(a))}x {fungsi4(fungsi2(fungsi(b)))}y"
    ruas_kanan_1 = fungsi(c)
    ruas_kiri_2 = fr"{fungsi4(fungsi(d))}x {fungsi4(fungsi2(fungsi(e)))}y"
    ruas_kanan_2 = fungsi(f)
    persamaan_1 = fr"{ruas_kiri_1} = {ruas_kanan_1}"
    persamaan_2 = fr"{ruas_kiri_2} = {ruas_kanan_2}"
    st.latex(persamaan_1)
    st.latex(persamaan_2)

    st.write('### **Hasil Penyelesaian**')

    hasil_y = (d * c - a * f) / (d * b - a * e)
    hasil_x = (c - b * hasil_y) / a
    st.latex(fr"x = {fungsi(hasil_x)}")
    st.latex(fr"y = {fungsi(hasil_y)}")

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)

    if muncul_1:
        st.write('### **Langkah Penyelesaian**')

        jenis_list = ["Eliminasi", "Subsitusi", "Determinan"]
        jenis = st.selectbox("Pilih cara langkah penyelesaian:", jenis_list)

        jumlah = st.number_input("Detail", value=3, min_value=1, max_value=3)

        if jenis == jenis_list[0]:
            nomor = 1
            st.write(f"### {nomor}")
            # st.markdown("<h1 style='text-align: left; color: red;'><math>Some title</math></h1>", unsafe_allow_html=True)
            # st.markdown(r"<h1 style='text-align: left; color: red;'><MATH>2x \times 2</MATH></h1>", unsafe_allow_html=True)
            st.latex(fr"{persamaan_1}")
            st.latex(fr"{persamaan_2}")
            if jumlah >= 3:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(f"{persamaan_1}")
                st.latex(f"{persamaan_2}")
            st.write(f"Di Persamaan 1, kalikan kedua ruas dengan {fungsi(d)}")
            st.write(f"Di Persamaan 2, kalikan kedua ruas dengan {fungsi(a)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"{fungsi4(fungsi(d * a))}x {fungsi4(fungsi2(fungsi(d * b)))}y = {fungsi(d * c)}")
            st.latex(fr"{fungsi4(fungsi(a * d))}x {fungsi4(fungsi2(fungsi(a * e)))}y = {fungsi(a * f)}")
            st.write("Kurangkan persamaan atas dengan bawah")
            if jumlah >= 3:
                nomor += 1
                st.write(f"### {nomor}")
                st.latex(fr"{fungsi4(fungsi(d * b))}y - {fungsi4(fungsi3(fungsi(a * e)))}y = {fungsi(d * c)} - {fungsi3(fungsi(a * f))}")
            st.latex(fr"{fungsi4(fungsi(d * b - a * e))}y = {fungsi(d * c - a * f)}")
            if fungsi(d * b - a * e) != 1:
                if jumlah >= 3:
                    st.latex(fr"""\frac{{{fungsi(d * b - a * e)}}}{{{fungsi(d * b - a * e)}}} y = \frac{{{fungsi(d * c - a * f)}}}{{{fungsi(d * b - a * e)}}}""")
                st.latex(fr"y = {fungsi(hasil_y)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.write(f"(Subsitusikan y = {fungsi(hasil_y)} ke Persamaan 1)")
            st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b))} \times {fungsi3(fungsi(hasil_y))} = {fungsi(c)}")
            if jumlah >= 2:
                st.latex(fr"{fungsi4(fungsi(a))}x {fungsi2(fungsi(b * hasil_y))} = {fungsi(c)}")
            if jumlah >= 3:
                st.latex(fr"{fungsi4(fungsi(a))}x + {fungsi3(fungsi(b * hasil_y))} - {fungsi3(fungsi(b * hasil_y))} = {fungsi(c)} - {fungsi3(fungsi(b * hasil_y))}")
            if jumlah >= 2:
                st.latex(fr"{fungsi4(fungsi(a))}x = {fungsi(c - b * hasil_y)}")
            if jumlah >= 3:
                st.latex(fr"\frac{{{fungsi(a)}}}{{{fungsi(a)}}} x = \frac{{{fungsi(c - b * hasil_y)}}}{{{fungsi(a)}}}")
            st.latex(fr"x = {fungsi(hasil_x)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

        if jenis == jenis_list[1]:
            st.write("Terlalu kompleks!")

        if jenis == jenis_list[2]:
            nomor = 1
            st.write(f"### {nomor}")
            st.write(f"{persamaan_1} (Persamaan 1)")
            st.write(f"{persamaan_2} (Persamaan 2)")
            if jumlah >= 2:
                nomor += 1
                st.write(f"### {nomor}")
                st.write(f"D = [[{fungsi(a)}, {fungsi(b)}], [{fungsi(d)}, {fungsi(e)}]]")
                st.latex(fr"\begin{bmatrix}{{a}} & {{b}}\\{{d}} & {{e}}\end{bmatrix}")
                st.write(f"D1 = [[{fungsi(c)}, {fungsi(b)}], [{fungsi(f)}, {fungsi(e)}]]")
                st.write(f"D2 = [[{fungsi(a)}, {fungsi(c)}], [{fungsi(d)}, {fungsi(f)}]]")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(rf"D = a \times d - b \times c")
            st.latex(rf"D = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(d))}")
            st.latex(rf"D_1 = {fungsi3(fungsi(c))} \times {fungsi3(fungsi(e))} - {fungsi3(fungsi(b))} \times {fungsi3(fungsi(f))}")
            st.latex(rf"D_2 = {fungsi3(fungsi(a))} \times {fungsi3(fungsi(f))} - {fungsi3(fungsi(c))} \times {fungsi3(fungsi(d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(rf"D = {fungsi(a * e)} {fungsi2(fungsi(-b * d))}")
            st.latex(rf"D_1 = {fungsi(c * e)} {fungsi2(fungsi(-b * f))}")
            st.latex(rf"D_2 = {fungsi(a * f)} {fungsi2(fungsi(-c * d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(rf"D = {fungsi(a*e-b*d)}")
            st.latex(rf"D_1 = {fungsi(c*e-b*f)}")
            st.latex(rf"D_2 = {fungsi(a*f-c*d)}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(rf"x = \frac{{D_1}}{{D}} = \frac{{{fungsi(c*e-b*f)}}}{{{fungsi(a*e-b*d)}}} = {fungsi((c*e-b*f)/(a*e-b*d))}")
            st.latex(rf"y = \frac{{D_2}}{{D}} = \frac{{{fungsi(a*f-c*d)}}}{{{fungsi(a*e-b*d)}}} = {fungsi((a*f-c*d)/(a*e-b*d))}")
            nomor += 1
            st.write(f"### {nomor}")
            st.latex(fr"(x, y) = ({fungsi(hasil_x)}, {fungsi(hasil_y)})")

            # st.latex(r"a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)")
            # st.latex(rf"a + ar + a r^2 + a r^3 + \cdots + a r^{12-1} = \sum_{13}^{12-1} ar^k = a \left(\frac{31}{13}\right)")

    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)

    if muncul_2:
        st.write('## **Grafik**')

        jarak = hasil_x - 5
        batas = hasil_x + 5
        ukuran = 0.01

        plt.style.use('seaborn')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = -a/b*x + c/b
        plt.plot(x,y1)

        y2 = -d/e*x + f/e
        plt.plot(x,y2)

        plt.xlabel("x", size=12)
        plt.ylabel("y")
        plt.legend([persamaan_1, persamaan_2])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)

if persamaan == persamaan_list[2]:
    st.markdown("Rumus persamaan:")
    st.markdown("ax^2 + bx + c = 0")
    st.sidebar.write('### **Masukkan angka**')
    a = float(st.sidebar.text_input("a (Default: 1)", value=1))
    b = float(st.sidebar.text_input("b (Default: 3)", value=3))
    c = float(st.sidebar.text_input("c (Default: 2)", value=2))

    st.write('## **Hasil Persamaan**')

    ruas_kiri = fr"{fungsi4(fungsi(a))}x^2 {fungsi4(fungsi2(fungsi(b)))}x {fungsi2(fungsi(c))}"
    ruas_kanan = "0"

    hasil_persamaan = fr"{ruas_kiri} = {ruas_kanan}"

    st.latex(hasil_persamaan)

    st.write('## **Hasil Penyelesaian**')

    # Hasil Penyelesaian
    d = b ** 2 - 4 * a * c

    # Hasil 2 Solusi
    hasil_x1 = (-b + d ** 0.5) / (2 * a)
    hasil_x2 = (-b - d ** 0.5) / (2 * a)

    # Mencari Jumlah Solusi
    if d > 0: e = 2
    elif d == 0: e = 1
    elif d < 0: e = 0

    # Titik Puncak
    f1 = -b / (2*a)
    f2 = -b**2 / (4*a) + c

    # Solusi
    if d < 0:
        st.write("x = Tidak ada")
    else:
        st.write(f"x1 = {fungsi(hasil_x1)}")
        st.write(f"x2 = {fungsi(hasil_x2)}")
    
    st.write(f"Diskriminan = {fungsi(d)}")
    st.write(f"Jumlah Solusi = {fungsi(e)}")
    st.write(f"Titik Puncak = ({fungsi(f1)}, {fungsi(f2)})")
    st.write("")

    #a = fungsi(a)
    #b = fungsi(b)

    muncul_1 = st.checkbox(label="Tampilkan langkah penyelesaian", value=False)

    if muncul_1:
        st.write('## **Langkah Penyelesaian**')

        # jenis_list = ["Selesaikan persamaan kuadrat", ""]
        # jenis = st.selectbox("Pilih cara langkah penyelesaian:", jenis_list)

        jumlah = st.number_input("Detail", value=3, min_value=1, max_value=3)

        g1 = fr"\sqrt{{{fungsi(b)} ^ 2 - 4 \times {fungsi(a)} \times {fungsi(c)}}}"
        g2 = fr"\sqrt{{{fungsi(b ** 2)} - {4 * fungsi(a) * fungsi(c)}}}"
        g3 = fr"\sqrt{{{fungsi(d)}}}"

        nomor = 1
        st.write(f"### {nomor}. Siapkan inputnya")
        st.latex(fr"   {hasil_persamaan}")
        nomor += 1
        st.write(f"### {nomor}. Gunakan rumus persamaan kuadrat")
        st.latex(fr"   x_1 = \frac{{{fungsi(-b)} + {g1}}}{{2 \times {fungsi(a)}}}")
        st.latex(fr"   x_2 = \frac{{{fungsi(-b)} - {g1}}}{{2 \times {fungsi(a)}}}")
        if jumlah >= 3:
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan")
            st.latex(fr"   x_1 = \frac{{{fungsi(-b)} + {g2}}}{{{fungsi(2 * a)}}}")
            st.latex(fr"   x_2 = \frac{{{fungsi(-b)} - {g2}}}{{{fungsi(2 * a)}}}")
        nomor += 1
        st.write(f"### {nomor}. Kurangkan")
        st.latex(fr"   x_1 = \frac{{{fungsi(-b)} + {g3}}}{{{fungsi(2 * a)}}}")
        st.latex(fr"   x_2 = \frac{{{fungsi(-b)} - {g3}}}{{{fungsi(2 * a)}}}")
        if d >= 0:
            nomor += 1
            st.write(f"### {nomor}. Hitung akarnya")
            st.latex(fr"   x_1 = \frac{{{fungsi(-b)} + {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
            st.latex(fr"   x_2 = \frac{{{fungsi(-b)} - {fungsi(d ** 0.5)}}}{{{fungsi(2 * a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Sederhanakan kedua hasil")
            st.latex(fr"x_1 = \frac{{{fungsi(-b + d ** 0.5)}}}{{{fungsi(2 * a)}}}")
            st.latex(fr"x_2 = \frac{{{fungsi(-b - d ** 0.5)}}}{{{fungsi(2 * a)}}}")
            nomor += 1
            st.write(f"### {nomor}. Bagikan dan dapat semua hasil")
            st.latex(fr"x_1 = {fungsi(hasil_x1)}")
            st.latex(fr"x_2 = {fungsi(hasil_x2)}")
        else:
            nomor += 1
            st.write(f"### {nomor}. Hasil")
            st.latex(r"   x \notin \R")
            st.write("   x = Tidak ada")

    muncul_2 = st.checkbox(label="Tampilkan grafik", value=False)

    if muncul_2:
        st.write('## **Grafik**')

        jarak = -5
        batas = 5
        ukuran = 0.01

        plt.style.use('seaborn')

        x = np.arange(jarak, batas + 1e-14, ukuran)
        plt.figure(figsize=(10,10))

        y1 = a*x**2 + b*x + c
        plt.plot(x,y1)

        y2 = 0*x + 0
        plt.plot(x,y2)

        plt.xlabel("x", size=12)
        plt.ylabel("y")
        plt.legend([ruas_kiri, ruas_kanan])

        plt.savefig('Preview.png')
        img = Image.open('Preview.png')
        st.image(img, width=500)
