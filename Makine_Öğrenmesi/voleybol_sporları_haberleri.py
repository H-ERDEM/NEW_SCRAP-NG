from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# WebDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # CSV dosyasını aç ve başlık satırını yaz (Kategori sütunu da eklenmiş)
    with open("voleybol_sporlari_haberleri.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Haber İsmi", "Kategori"])  # Başlık satırı

        # 3 sayfayı dolaş
        for page in range(1, 4):  # 1. sayfadan 3. sayfaya kadar
            url = f"https://www.milliyet.com.tr/skorer/voleybol-haberleri/?page={page}"
            driver.get(url)

            # Sayfanın yüklenmesini bekle
            time.sleep(3)

            # Sayfadaki 'strong' etiketlerine sahip tüm yazıları al
            haberler = driver.find_elements(By.XPATH, "//div[contains(@class, 'cat-list-card__content')]/strong")

            # Haber başlıklarını ve kategoriyi CSV dosyasına kaydet
            for haber in haberler:
                writer.writerow([haber.text, "Voleybol_Sporları"])

            print(f"{page}. sayfa işlendi.")

        print("Voleybol Sporları kategorisindeki başlıklar CSV dosyasına kaydedildi.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    # Tarayıcıyı kapat
    driver.quit()
