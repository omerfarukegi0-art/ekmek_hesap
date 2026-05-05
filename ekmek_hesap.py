import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Ekmek Satış Takip", page_icon="🍞")

def main():
    st.title("🍞 Günlük Satış Takip Sistemi")
    st.info("Ekmek sayılarını ve satış adetlerini girerek cironuzu hesaplayın.")

    # --- SABİT VERİLER ---
    KAPASITE = {"Normal": 20, "Kepekli": 25}
    SABIT_URUNLER = {
        "Çavdarlı Ekmek": 43.0,
        "Çok Tahıllı Ekmek": 43.0,
        "Tam Buğday Ekmeği": 32.0,
        "Köy Ekmeği": 43.0,
        "Kurabiye": 55.0
    }

    # --- 1. BÖLÜM: KASA İLE GELEN EKMEKLER ---
    st.header("1. Kasa Hesabı (Ekmekler)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Normal Ekmek")
        n_fiyat = st.number_input("Birim Fiyat (Normal)", value=10.0, step=0.5)
        n_kasa = st.number_input("Gelen Kasa (Normal)", min_value=0, step=1)
        n_kalan = st.number_input("Kalan Adet (Normal)", min_value=0, step=1)
        n_satilan = (n_kasa * KAPASITE["Normal"]) - n_kalan
        n_kazanc = n_satilan * n_fiyat

    with col2:
        st.subheader("Kepekli Ekmek")
        k_fiyat = st.number_input("Birim Fiyat (Kepekli)", value=12.0, step=0.5)
        k_kasa = st.number_input("Gelen Kasa (Kepekli)", min_value=0, step=1)
        k_kalan = st.number_input("Kalan Adet (Kepekli)", min_value=0, step=1)
        k_satilan = (k_kasa * KAPASITE["Kepekli"]) - k_kalan
        k_kazanc = k_satilan * k_fiyat

    # --- 2. BÖLÜM: DİĞER ÜRÜNLER ---
    st.markdown("---")
    st.header("2. Diğer Ürünler (Adet)")
    
    ekstra_toplam = 0.0
    ekstra_detay = []
    
    # Ürünleri yan yana göstermek için kolonlar
    cols = st.columns(2)
    for i, (urun, fiyat) in enumerate(SABIT_URUNLER.items()):
        with cols[i % 2]:
            adet = st.number_input(f"{urun} ({fiyat} TL)", min_value=0, step=1, key=urun)
            if adet > 0:
                kazanc = adet * fiyat
                ekstra_toplam += kazanc
                ekstra_detay.append((urun, adet, kazanc))

    # --- 3. BÖLÜM: SONUÇ RAPORU ---
    st.markdown("---")
    toplam_ciro = n_kazanc + k_kazanc + ekstra_toplam
    
    st.metric(label="📊 GÜNLÜK TOPLAM CİRO", value=f"{toplam_ciro:,.2f} TL")

    if st.button("Özet Raporu Oluştur"):
        st.success("✅ Satış Başarıyla Hesaplandı")
        st.write(f"**Normal Ekmek:** {n_satilan} adet -> {n_kazanc:.2f} TL")
        st.write(f"**Kepekli Ekmek:** {k_satilan} adet -> {k_kazanc:.2f} TL")
        for u, a, k in ekstra_detay:
            st.write(f"**{u}:** {a} adet -> {k:.2f} TL")

if __name__ == "__main__":
    main()
