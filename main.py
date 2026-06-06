from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from detection_service import DetectionService
import json
from fastapi.responses import FileResponse

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)
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
    
@app.get("/")
def ana_sayfayi_goster():
    return FileResponse("index.html")
                        
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

@app.get("/kamera_simulasyonu")
def kamera_simulasyonu():
    sahte_goruntu_yolu="test-fotografi.jpg"
    hata=servis.model_tahmini_yap(sahte_goruntu_yolu, bilgiler["esik_degeri"])
    if hata:
        bulunan_hatalar.append(hata)
        
    return {"hata":hata}
    
@app.get("/rapor_olustur")
def rapor_olustur():
    hata_detaylari=[
        {
            "hata_tipi":hata["hata_tipi"],
            "metre_bilgisi":hata["metre_bilgisi"],
            "guven_skoru":hata["guven_skoru"],
            "zaman_bilgisi":hata["zaman_bilgisi"]
        }
        for hata in bulunan_hatalar
    ]
    rapor={
        "urun_adi": bilgiler.get("urun_adi", ""),
        "urun_etiketi": bilgiler.get("urun_etiketi", ""),
        "esik_degeri": bilgiler.get("esik_degeri", 0.0),
        "toplam_hata_sayisi": len(bulunan_hatalar),
        "hata_detaylari": hata_detaylari
    }
    with open("rapor.json", "w", encoding="utf-8") as dosya:
        json.dump(rapor, dosya, ensure_ascii=False, indent=4)
    return {
        "message": "Rapor oluşturuldu",
        "rapor": rapor
    }