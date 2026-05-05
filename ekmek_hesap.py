import streamlit as st

# 1. SAYFA VE MOBİL TASARIM AYARLARI
st.set_page_config(page_title="Ekmek Satış Takip", page_icon="🍞", layout="centered")

# Rakamların her türlü ekranda (karanlık/aydınlık) okunması için özel stil
st.markdown("""
    <style>
    /* Metrik değerini ve yazılarını siyah/koyu gri yaparak okunur kılar */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
    }
    /* Metrik kutusunun arka planını açık sarı/beyaz yapar */
    [data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 20px !important;
        border-radius: 15px !important;
        border: 2px solid #f0ad4e !important;
    }
    /* Giriş kutularını büyütür */
    .stNumberInput input { font-size: 20px !important; }
    /* Butonu dikkat çekici yapar */
    button { 
        height: 4em !important; 
        width: 100% !important; 
        font-size: 20px !important; 
        font-weight: bold !important;
        background-color: #f0ad4e !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🍞 Günlük Satış Paneli")
    
    # --- SABİT FİYATLAR VE VERİLER ---
    EKMEK_FIYAT = 11.0
    SABIT_URUNLER = {
        "Çavdarlı Ekmek": 43.0, 
        "Çok Tahıllı": 43.0, 
        "Tam Buğday": 32.0, 
        "Köy Ekmeği": 43.0, 
        "Kurabiye": 55.0
    }

    # --- 1. BÖLÜM: ANA EKMEKLER ---
    st.subheader("🥖 Kasa Hesabı (11 TL)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("Normal (20'li)")
        n_kasa = st.number_input("Gelen Kasa", min_value=0, step=1, key="n_kasa")
        n_kalan = st.number_input("Kalan Adet", min_value=0, step=1, key="n_kalan")
        n_satilan = (n_kasa * 20) - n_kalan
        n_kazanc = n_satilan * EKMEK_FIYAT

    with col2:
        st.warning("Kepekli (25'li)")
        k_kasa = st.number_input("Gelen Kasa ", min_value=0, step=1, key="k_kasa")
        k_kalan = st.number_input("Kalan Adet ", min_value=0, step=1, key="k_kalan")
        k_satilan = (k_kasa * 25) - k_kalan
        k_kazanc = k_satilan * EKMEK_FIYAT

    # --- 2. BÖLÜM: SABİT ÜRÜNLER ---
    st.markdown("---")
    st.subheader("🍪 Yan Ürünler")
    ekstra_toplam = 0.0
    
    # Ürünleri daha şık bir liste halinde sunar
    for urun, fiyat in SABIT_URUNLER.items():
        adet = st.number_input(f"{urun} ({fiyat} TL)", min_value=0, step=1, key=urun)
        ekstra_toplam += (adet * fiyat)

    # --- 3. SONUÇ RAPORU ---
    st.markdown("---")
    toplam_ciro = n_kazanc + k_kazanc + ekstra_toplam
    
    # Rakamın görünmediği yer burasıydı, şimdi siyah yaptık
    st.metric(label="💰 GÜNLÜK TOPLAM CİRO", value=f"{toplam_ciro:,.2f} TL")

    if st.button("HESAPLA VE ÖZETİ GÖSTER"):
        st.balloons()
        st.success("✅ Hesaplama Başarıyla Tamamlandı!")
        
        # Detaylı Özet Tablosu
        with st.expander("Detaylı Satış Özeti", expanded=True):
            st.write(f"🔹 **Normal Ekmek:** {n_satilan} Adet | {n_kazanc:.2f} TL")
            st.write(f"🔹 **Kepekli Ekmek:** {k_satilan} Adet | {k_kazanc:.2f} TL")
            if ekstra_toplam > 0:
                st.write(f"🔹 **Diğer Ürünler:** {ekstra_toplam:.2f} TL")
            st.write("---")
            st.write(f"🏆 **Genel Toplam: {toplam_ciro:.2f} TL**")

if __name__ == "__main__":
    main()
