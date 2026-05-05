import streamlit as st

# 1. SAYFA VE MOBİL TASARIM AYARLARI
st.set_page_config(page_title="Ekmek Satış Takip", page_icon="🍞", layout="centered")

# Rakamların okunması için özel stil
st.markdown("""
    <style>
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] { color: #000000 !important; }
    [data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 20px !important;
        border-radius: 15px !important;
        border: 2px solid #f0ad4e !important;
    }
    .stNumberInput input { font-size: 20px !important; }
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
    
    # --- SABİT FİYATLAR ---
    EKMEK_FIYAT = 11.0
    SABIT_URUNLER = {
        "Çavdarlı Ekmek": 43.0, 
        "Çok Tahıllı": 43.0, 
        "Tam Buğday": 32.0, 
        "Köy Ekmeği": 43.0, 
        "Kurabiye": 55.0
    }

    # --- 1. BÖLÜM: BİRLEŞTİRİLMİŞ EKMEKLER (11 TL) ---
    st.subheader("🥖 Ekmek Satışı (Normal + Kepekli)")
    st.info("Normal ve kepekli ekmeklerin toplam sayısını giriniz.")
    
    col1, col2 = st.columns(2)
    with col1:
        toplam_gelen = st.number_input("Toplam Gelen Ekmek", min_value=0, step=1)
    with col2:
        toplam_kalan = st.number_input("Toplam Kalan Ekmek", min_value=0, step=1)
    
    ekmek_satilan = toplam_gelen - toplam_kalan
    ekmek_kazanc = ekmek_satilan * EKMEK_FIYAT

    # --- 2. BÖLÜM: YAN ÜRÜNLER ---
    st.markdown("---")
    st.subheader("🍪 Diğer Ürünler")
    ekstra_toplam = 0.0
    
    for urun, fiyat in SABIT_URUNLER.items():
        adet = st.number_input(f"{urun} ({fiyat} TL)", min_value=0, step=1, key=urun)
        ekstra_toplam += (adet * fiyat)

    # --- 3. SONUÇ RAPORU ---
    st.markdown("---")
    toplam_ciro = ekmek_kazanc + ekstra_toplam
    
    st.metric(label="💰 GÜNLÜK TOPLAM CİRO", value=f"{toplam_ciro:,.2f} TL")

    if st.button("HESAPLA VE ÖZETİ GÖSTER"):
        st.balloons()
        st.success("✅ Hesaplama Başarıyla Tamamlandı!")
        
        with st.expander("Detaylı Satış Özeti", expanded=True):
            st.write(f"🔹 **Satılan Ekmek (Toplam):** {max(0, ekmek_satilan)} Adet")
            st.write(f"🔹 **Ekmek Cirosu:** {max(0, ekmek_kazanc):.2f} TL")
            if ekstra_toplam > 0:
                st.write(f"🔹 **Diğer Ürünler:** {ekstra_toplam:.2f} TL")
            st.write("---")
            st.write(f"🏆 **Genel Toplam: {max(0, toplam_ciro):.2f} TL**")

if __name__ == "__main__":
    main()
