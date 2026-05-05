import streamlit as st

# Sayfa ayarlarını mobil için optimize etme
st.set_page_config(
    page_title="Ekmek Takip",
    page_icon="🍞",
    layout="centered" # İçeriği ortaya toplar, mobilde daha iyi görünür
)

# Telefon ekranında butonların ve yazıların daha büyük görünmesi için stil
st.markdown("""
    <style>
    .stNumberInput input { font-size: 20px !important; }
    .stMetric { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
    button { height: 3em !important; width: 100% !important; font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🍞 Satış Takip")
    
    # --- 1. EKMEKLER ---
    st.subheader("🥖 Ekmek Kasaları")
    
    # Normal Ekmek Kartı
    with st.expander("Normal Ekmek (20'li)", expanded=True):
        n_fiyat = st.number_input("Birim Fiyat", value=10.0, step=0.5, key="n_f")
        n_kasa = st.number_input("Gelen Kasa", min_value=0, step=1, key="n_k")
        n_kalan = st.number_input("Kalan Adet (İade)", min_value=0, step=1, key="n_i")
        n_satilan = (n_kasa * 20) - n_kalan
        n_kazanc = n_satilan * n_fiyat

    # Kepekli Ekmek Kartı
    with st.expander("Kepekli Ekmek (25'li)", expanded=True):
        k_fiyat = st.number_input("Birim Fiyat", value=12.0, step=0.5, key="k_f")
        k_kasa = st.number_input("Gelen Kasa", min_value=0, step=1, key="k_k")
        k_kalan = st.number_input("Kalan Adet (İade)", min_value=0, step=1, key="k_i")
        k_satilan = (k_kasa * 25) - k_kalan
        k_kazanc = k_satilan * k_fiyat

    # --- 2. DİĞER ÜRÜNLER ---
    st.subheader("🍪 Diğer Ürünler")
    sabit_urunler = {
        "Çavdarlı": 43.0, "Çok Tahıllı": 43.0, 
        "Tam Buğday": 32.0, "Köy Ekmeği": 43.0, "Kurabiye": 55.0
    }
    
    ekstra_toplam = 0.0
    for urun, fiyat in sabit_urunler.items():
        adet = st.number_input(f"{urun} ({fiyat} TL)", min_value=0, step=1)
        ekstra_toplam += (adet * fiyat)

    # --- 3. GÜN SONU ---
    st.markdown("---")
    toplam_ciro = n_kazanc + k_kazanc + ekstra_toplam
    
    # Büyük Ciro Göstergesi
    st.metric(label="💰 TOPLAM KASA", value=f"{toplam_ciro:,.2f} TL")

    if st.button("HESABI TAMAMLA"):
        st.balloons() # Kutlama efekti
        st.success(f"Bugünkü toplam ciro kaydedilmeye hazır: {toplam_ciro:.2f} TL")

if __name__ == "__main__":
    main()
