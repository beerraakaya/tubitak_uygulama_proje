import random
from datetime import datetime

class DetectionService:
    def __init__(self, model_path=None):
        self.is_running=False
        self.hatatype=["Çizik", "Ezik", "Leke", "Çatlak"]
        
    def start(self):
        self.is_running=True
    
    def stop(self):
        self.is_running=False
        
    def predict_image(self, image_path, threshold):
        if not self.is_running:
            return None
        
        confidence= round(random.uniform(0, 1), 2)
        
        if confidence < threshold:
            return None
        
        return {
            "hata_tipi": random.choice(self.hatatype),
            "metre_bilgisi": round(random.uniform(0, 100), 2),
            "guven_skoru": confidence,
            "tarih": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }