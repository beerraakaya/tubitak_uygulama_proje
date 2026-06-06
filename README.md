# Mini Yüzey Hatası Tespit Prototipi

## 📌 Temel Özellikler

* **Tam Yığın (Full-Stack) Mimari:** Kullanıcı arayüzü (`index.html`), harici bir sunucuya ihtiyaç duymadan doğrudan FastAPI arka planı üzerinden kök dizinde (`/`) servis edilmektedir.
* **Gerçek Zamanlı Kamera Simülasyonu:** Sistem, statik bir veri tablosu yerine, banttan akan görüntüleri asenkron olarak simüle eden dinamik bir "kamera dinleme" yapısına sahiptir.
* **Dinamik Hata Yönetimi ve Eşik (Threshold):** Tespit edilen hatalar anlık olarak listelenir. Yanlış alarmları (False Positive) önlemek adına, operatör panelden dinamik bir eşik değeri belirleyerek sadece bu güven skorunun (confidence) üzerindeki hataların raporlanmasını sağlayabilir.
* **Otomatik Raporlama:** Sistemdeki veriler derlenerek, diğer sistemlerin veya veri tabanlarının kolayca okuyabileceği standart `JSON` formatında (`hata_raporu.json`) detaylı bir rapor oluşturulur.
* **Bağımsız Çalışabilirlik:** Uygulama, kütüphane veya işletim sistemi bağımlılıklarını ortadan kaldırmak için tamamen Dockerize edilmiştir.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Yapay Zeka:** PyTorch, Ultralytics (YOLO)
* **DevOps:** Docker

* ## 🚀 Kurulum ve Çalıştırma (Docker)

Uygulamayı herhangi bir bağımlılık kurmadan çalıştırmak için bilgisayarınızda Docker'ın yüklü ve çalışır durumda olması yeterlidir.

1. Terminali açın ve projenin ana dizinine (Dockerfile'ın bulunduğu klasöre) gidin.
2. Gerekli kütüphaneleri (FastAPI, Ultralytics vb.) indirecek olan Docker imajını oluşturun:
   ```bash
   docker build -t yuzey-hata-tespiti .
İmaj başarıyla oluşturulduktan sonra konteyneri ayağa kaldırın:

```bash
docker run -p 8000:8000 yuzey-hata-tespiti
