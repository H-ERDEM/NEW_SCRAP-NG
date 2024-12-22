from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# WebDriver başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # CSV dosyasını aç ve başlık satırını yaz
    with open("gazete_haberleri.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Haber İsmi", "Kategori"])  # Sütun başlıkları

        # 7 sayfa boyunca gez
        for page in range(1, 8):  # 1'den 7'ye kadar
            url = f"https://www.milliyet.com.tr/gazete-haberleri/?page={page}"
            driver.get(url)

            # Sayfanın yüklenmesini bekle
            time.sleep(3)

            # Haber başlıklarını al (strong etiketine sahip içerikler)
            haberler = driver.find_elements(By.XPATH, "//div[contains(@class, 'cat-list-card__content')]/strong")

            # Her haberi CSV dosyasına kaydet
            for haber in haberler:
                writer.writerow([haber.text, "Gazete"])

            print(f"{page}. sayfa işlendi.")

        print("Gazete haberleri başarıyla CSV dosyasına kaydedildi.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    # WebDriver kapat
    driver.quit()
