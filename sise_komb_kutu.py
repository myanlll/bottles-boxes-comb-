
def kombinasyon(kapasite, siseler):
    if siseler < 1:
        return set()
    kombinasyonlar = [[i] for i in range(kapasite + 1)]

    for i in range(1, siseler):
        yeni_kombinasyonlar = []
        for kombine in kombinasyonlar:
            tum_kapasite = kapasite - sum(kombine)
            for i in range(tum_kapasite + 1):
                yeni_kombinasyonlar.append(kombine + [i])
        kombinasyonlar = yeni_kombinasyonlar


    kombinasyonlar = [kombine for kombine in kombinasyonlar if sum(kombine) > 0]
    
    gecerli_kombinasyonlar = [tuple(kombine) for kombine in kombinasyonlar if sum(kombine) <= kapasite]

    return set(gecerli_kombinasyonlar)

siseler = int(input("Şişe çeşit sayısını giriniz: "))
kapasite = int(input("Kutu kapasitesini giriniz: "))


gecerli_kombinasyonlar = kombinasyon(kapasite, siseler)
print(f"Toplam {len(gecerli_kombinasyonlar)} farklı kombinasyon bulunmuştur.")
for kombine in gecerli_kombinasyonlar:
    print(kombine)
print(f"Toplam {len(gecerli_kombinasyonlar)} farklı kombinasyon bulunmuştur.")

