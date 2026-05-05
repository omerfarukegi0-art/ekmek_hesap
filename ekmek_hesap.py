import streamlit as st

# Mobil uyumlu sayfa ayarı
st.set_page_config(page_title="Ekmek Takip", page_icon="🍞")

# Stil düzenlemeleri
st.markdown("""
    <style>
    .stNumberInput input { font-size: 18px !important; }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 12px; border: 1px solid #e0e0e0; }
    button { height: 3.5em !important; width: 100% !important; font-size: 18px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🍞 Günlük Satış Paneli")
    
    # Sabit Fiyatlar
    EKMEK_FIYAT = 11.0
    SABIT_URUNLER = {
        "Çavdarlı Ekmek": 43.0, "Çok Tahıllı": 43.0, 
        "Tam Buğday": 32.0, "Köy Ekmeği": 43.0, "Kurabiye": 55.0
    }

    # 1. BÖLÜM: ANA EKMEKLER
    st.subheader("🥖 Temel Ekmekler (11 TL)")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Normal (20'li)")
        n_kasa = st.number_input("Gelen Kasa", min_value=0, step=1, key="nk")
        n_kalan = st.number_input("Kalan Adet", min_value=0, step=1, key="ni")
        n_satilan = (n_kasa * 20) - n_kalan
        n_kazanc = n_satilan * EKMEK_FIYAT

    with col2:
        st.info("Kepekli (25'li)")
        k_kasa = st.number_input("Gelen Kasa ", min_value=0, step=1, key="kk")
        k_kalan = st.number_input("Kalan Adet ", min_value=0, step=1, key="ki")
        k_satilan = (k_kasa * 25) - k_kalan
        k_kazanc = k_satilan * EKMEK_FIYAT

    # 2. BÖLÜM: DİĞER ÜRÜNLER
    st.subheader("🍪 Yan Ürünler")
    ekstra_toplam = 0.0
    
    # Ürünleri daha derli toplu göstermek için
    for urun, fiyat in SABIT_URUNLER.items():
        adet = st.number_input(f"{urun} - {fiyat} TL", min_value=0, step=1)
        ekstra_toplam += (adet * fiyat)

    # 3. SONUÇ
    st.markdown("---")
    toplam_ciro = n_kazanc + k_kazanc + ekstra_toplam
    
    st.metric(label="💰 TOPLAM GÜNLÜK CİRO", value=f"{toplam_ciro:,.2f} TL")

    if st.button("HESAPLA VE ÖZETLE"):
        st.balloons()
        st.markdown("### 📋 Gün Özeti")
        st.write(f"✅ **Normal Ekmek:** {n_satilan} adet satıldı.")
        st.write(f"✅ **Kepekli Ekmek:** {k_satilan} adet satıldı.")
        if ekstra_toplam > 0:
            st.write(f"✅ **Yan Ürün Toplamı:** {ekstra_toplam:.2f} TL")

if __name__ == "__main__":
    main()
