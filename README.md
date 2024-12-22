# NEW_SCRAPING
# Selenium ile Milliyet Haber Sitesi Scraping Projesi

Bu proje, **Selenium** kütüphanesini kullanarak **Milliyet Haber** sitesindeki çeşitli kategorilerdeki haber başlıklarını toplar ve bu başlıkları bir CSV dosyasına kaydeder. Proje, aşağıdaki kategorilerdeki haberleri içerir:

- **Spor - Basketbol**
- **Dünya**
- **Eğitim**
- **Ekonomi**
- **Spor - Futbol**
- **Spor - Voleybol**
- **Gazete**
- **Gündem**
- **Magazin**
- **Otomobil**
- **Teknoloji**
- **Yerel**
- **Moda**

## Proje Özeti

Bu projede amacımız, Milliyet haber sitesinde yer alan farklı kategorilere ait haber başlıklarını toplamak ve bu başlıkları analiz için kolayca kullanılabilir bir formatta (CSV dosyası) kaydetmektir.

### Kullanılan Teknolojiler

- **Python**: Projeyi geliştirmek için Python programlama dili kullanılmıştır.
- **Selenium**: Web scraping işlemi için Selenium kütüphanesi kullanılmıştır.
- **Pandas**: Verilerin CSV formatında saklanabilmesi için Pandas kütüphanesi kullanılmıştır.

## Kurulum

Projenin çalışabilmesi için öncelikle gerekli kütüphanelerin yüklenmesi gerekmektedir. Aşağıdaki adımları izleyerek kurulumu yapabilirsiniz:

1. **Python 3.x** sürümünü bilgisayarınızda yüklü olduğundan emin olun. Eğer yüklü değilse, [Python resmi web sitesinden](https://www.python.org/downloads/) indirebilirsiniz.
   
2. **Gerekli Kütüphaneleri Yükleyin**:

    ```bash
    pip install selenium pandas
    ```

3. **WebDriver İndirin**:
   - Selenium'un düzgün çalışabilmesi için kullanılan tarayıcıya uygun bir **WebDriver** indirmeniz gerekmektedir.
   - [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) veya [GeckoDriver](https://github.com/mozilla/geckodriver) gibi uygun bir sürüm indirip, sisteminizdeki bir dizine yerleştirin.

## Kullanım

1. **Projenin Çalıştırılması**:
   - Projeyi indirdikten sonra, terminal veya komut istemcisine geçin ve aşağıdaki komut ile çalıştırın:

    ```bash
    python scraper.py
    ```

2. **Çıktı**:
   - Proje çalıştırıldığında, her kategoriden haber başlıklarını içeren bir `haber_basliklari.csv` dosyası oluşturulacaktır.
   - Bu CSV dosyasında her satırda bir haber başlığı ve kategorisi yer alacaktır.

## Proje Akışı

1. **Hedef Web Sayfasına Erişim**:
   - Selenium, Milliyet haber sitesinin ana sayfasına erişir ve sayfanın yüklenmesini bekler.

2. **Kategorilere Göz Atma**:
   - Selenium, sayfadaki tüm haber kategorilerini tespit eder ve her bir kategorinin altındaki haber başlıklarını toplar.

3. **Verilerin Kaydedilmesi**:
   - Toplanan haber başlıkları ve kategorileri bir `CSV` dosyasına kaydedilir. Her haber başlığı, kategorisiyle birlikte dosyada yer alır.

4. **CSV Dosyasının Oluşturulması**:
   - Haber başlıkları ve kategoriler, bir pandas DataFrame kullanılarak CSV formatında kaydedilir.

## Örnek Çıktı

`haber_basliklari.csv` dosyasında aşağıdaki gibi bir çıktı olabilir:

```csv
Başlık,Kategori
"Basketbol Milli Takım'dan tarihi galibiyet","Spor_basketbol"
"Dünya genelinde eğitimdeki yeni trendler","Eğitim"
"Ekonomide son gelişmeler","Ekonomi"
"Futbol dünyasında transfer dönemi başladı","Spor_futbol"
"Spor - Voleybol Milli Takım'dan önemli galibiyet","Spor_voleybol"
"Bugün gazetelerde neler var?","Gazete"
"Gündemdeki son gelişmeler","Gündem"
"Magazin dünyasında bomba gelişme","Magazin"
"Otomobil endüstrisinde yeni yenilikler","Otomobil"
"Teknolojinin geleceği: Yapay zeka ve ötesi","Teknoloji"
"Yerel seçimlerde son gelişmeler","Yerel"
"Moda dünyasında kış trendleri","Moda"
