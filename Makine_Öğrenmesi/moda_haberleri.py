from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os

# WebDriver'i baslatma
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # CSV dosyasini olustur veya ustune ekle
    csv_path = os.path.abspath("moda_haberleri.csv")
    file_exists = os.path.isfile(csv_path)

    # Dosyayi "append" modunda ac, aninda yazma islemi icin
    with open(csv_path, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:  # Eger dosya bos ise baslik ekle
            writer.writerow(["Baslik", "Kategori"])

        # 15 sayfa boyunca islem yap
        for page in range(1, 16):  # 1'den 15'e kadar
            url = f"https://www.milliyet.com.tr/pembenar/moda/?page={page}"
            driver.get(url)

            # Sayfanin tamamen yuklenmesini bekle
            time.sleep(3)

            # Her bir kart icin islemleri yap
            kartlar = driver.find_elements(By.CSS_SELECTOR, "div.col-6.col-md-4")  # Kartlari sec
            for kart in kartlar:
                try:
                    # Baslik
                    baslik = kart.find_element(By.CSS_SELECTOR, "strong.card__title").text

                    # Veriyi CSV'ye aninda yaz
                    writer.writerow([baslik, "Moda"])
                    print(f"Baslik: {baslik}")
                except Exception as e:
                    print(f"Bir kart islenirken hata olustu: {e}")

        print("Moda haberleri detaylari basariyla CSV dosyasina kaydedildi.")
        print(f"CSV dosyasi konumu: {csv_path}")

except Exception as e:
    print(f"Bir hata olustu: {e}")

finally:
    # WebDriver'i kapat
    driver.quit()

import pandas as pd

# CSV dosyasını oku
csv_path = os.path.abspath("moda_haberleri.csv")
df = pd.read_csv(csv_path)

# 'Detay' sütununu sil
if "Detay" in df.columns:  # Eğer Detay sütunu varsa
    df = df.drop("Detay", axis=1)

# Güncellenmiş DataFrame'i tekrar dosyaya kaydet
df.to_csv(csv_path, index=False)
print("'Detay' sütunu başarıyla silindi.")

# Daha önceki verilerle birlikte Detay sütununu sil ve tekrar yaz
try:
    df = pd.read_csv(csv_path)
    if "Detay" in df.columns:
        df = df.drop("Detay", axis=1)
        df.to_csv(csv_path, index=False)
        print("'Detay' sütunu silinmiş olarak dosya güncellendi.")
except Exception as e:
    print(f"Detay sütununu silerken hata oluştu: {e}")
