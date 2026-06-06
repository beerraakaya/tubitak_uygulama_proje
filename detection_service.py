import random
from datetime import datetime
from ultralytics import YOLO

class DetectionService:
    def __init__(self, model_path=None):
        self.is_running=False
        self.hatatype=["Çizik", "Ezik", "Leke", "Çatlak"]
        try:
            print("Model yükleniyor...")
            self.model=YOLO("best.pt")
            print("Model başarıyla yüklendi.")
        except Exception as e:
            print(f"Model yüklenirken hata oluştu: {e}, Mock modu çalışacak.")
            self.model=None
       
        
    def baslat(self):
        self.is_running=True
    
    def durdur(self):
        self.is_running=False
        
    def model_tahmini_yap(self, goruntu_yolu, esik_degeri):
        if not self.is_running:
            return None
        
        if self.model is not None:
           sonuclar=self.model.predict(goruntu_yolu, conf=esik_degeri, verbose=False)
           
           sonuc= sonuclar[0]
           if len(sonuc.boxes) > 0:
               kutu=sonuc.boxes[0]
               sinif_id=int(kutu.cls[0])
               guven_skoru=float(kutu.conf[0])
               
               gercek_hata_tipi=self.hatatype[sinif_id] 
               return {
                    "hata_tipi": gercek_hata_tipi,
                    "metre_bilgisi": round(random.uniform(0, 100), 2),
                    "guven_skoru": guven_skoru,
                    "zaman_bilgisi": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
       
        guven_skoru=round(random.uniform(0, 1), 2)
        if guven_skoru < esik_degeri:
            return None
        return {
            "hata_tipi": random.choice(self.hatatype),
            "metre_bilgisi": round(random.uniform(0, 100), 2),
            "guven_skoru": guven_skoru,
            "zaman_bilgisi": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        