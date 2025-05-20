import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Aplikasi Maklumat Peribadi", layout="wide")

# Tajuk aplikasi
st.title("📝 Aplikasi Maklumat Peribadi (Web Version)")

with st.form("borang_maklumat"):
    # Input fields
    nama = st.text_input("Nama Penuh*")
    ic = st.text_input("No. Kad Pengenalan*")
    tarikh_lahir = st.date_input("Tarikh Lahir*", datetime.now())
    alamat = st.text_area("Alamat*")
    telefon = st.text_input("No. Telefon*")
    email = st.text_input("Email*")
    jantina = st.radio("Jantina*", ["Lelaki", "Perempuan"])
    
    # Button submit
    submitted = st.form_submit_button("💾 Simpan Maklumat")
    
    if submitted:
        if not all([nama, ic, alamat, telefon, email]):
            st.error("Sila isi semua medan wajib (*)")
        else:
            # Kira umur
            umur = (datetime.now().year - tarikh_lahir.year)
            
            # Simpan ke dictionary
            data = {
                "Nama": nama,
                "No. KP": ic,
                "Umur": umur,
                "Alamat": alamat,
                "Telefon": telefon,
                "Email": email,
                "Jantina": jantina
            }
            
            # Tunjukkan preview
            st.success("Maklumat berjaya disimpan!")
            st.json(data)  # Boleh ganti dengan st.table() untuk tampilan lebih cantik
            
            # Simpan ke file (optional)
            with open("maklumat.txt", "a") as f:
                f.write(f"\n{datetime.now()}:\n")
                for k, v in data.items():
                    f.write(f"{k}: {v}\n")