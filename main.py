from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detection_service import DetectionService

app= FastAPI()
servis= DetectionService()

bilgiler={
    "urun_adi":"",
    "urun_etiketi":"",
    "esik_degeri":0.0
    
}
bulunan_hatalar=[]

class OperatorGirdisi(BaseModel):
    urun_adi: str
    urun_etiketi: str
    esik_degeri: float

@app.post("/baslat")
def sistemi_baslat(girdi: OperatorGirdisi):
    global bilgiler, bulunan_hatalar
    bilgiler=girdi.dict()
    bulunan_hatalar=[]
    servis.baslat()
    return {"message":"Sistem başlatıldı, tespit yapılıyor", "bilgiler":bilgiler}
    
@app.post("/durdur")
def sistemi_durdur():
    servis.durdur()
    return {"message":"Sistem durduruldu", "bilgiler":bilgiler, "bulunan_hatalar":bulunan_hatalar}

@app.post("/resetle")
def sistemi_resetle():
    global bilgiler, bulunan_hatalar
    servis.durdur()
    bilgiler={
        "urun_adi":"",
        "urun_etiketi":"",
        "esik_degeri":0.0
    }
    bulunan_hatalar=[]
    return {"message":"Sistem resetlendi", "bilgiler":bilgiler, "bulunan_hatalar":bulunan_hatalar}


