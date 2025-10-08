import json
from difflib import get_close_matches as yakin_sonuclari_getir
import time

def veritabanini_yukle():
    with open('C:/Users/MONSTER/Desktop/python yapay zeka/akilli-chatbot/veritabani.json', 'r') as dosya:
        return json.load(dosya)
    
def veritabanina_yukle(veriler):
    with open('C:/Users/MONSTER/Desktop/python yapay zeka/akilli-chatbot/veritabani.json', 'w') as dosya:
        json.dump(veriler, dosya, indent=2)
        
def yakin_sonuc_bul(soru, sorular):
    eslesen=yakin_sonuclari_getir(soru, sorular,n=1,cutoff=0.6)
    return eslesen[0] if eslesen else None

def cevabini_bul(soru,veritabani):
    for soru_cevaplar in veritabani["sorular"]:
        if soru_cevaplar["soru"] == soru:
            return soru_cevaplar["cevap"]
    return None
    
        
def chatbot():
    veritabani=veritabanini_yukle()
    
    while True:
        soru=input("Siz: ")
        if soru == "çık":
            break
        
        
        gelen_sonuc=yakin_sonuc_bul(soru,[soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
        
        if gelen_sonuc:
            print("Bot düşünüyor...")
            time.sleep(2)  # Botun düşündüğünü simüle etmek için bekleme süresi
            verilecek_cevap=cevabini_bul(gelen_sonuc,veritabani) 
            print(f"Bot: {verilecek_cevap}") 
        else:
            print("Bot:Bunu nasıl cevaplayacağımı bilmiyorum. Bana öğretmek ister misin?")
            yeni_cevap=input("Öğretmek için yazabilir veya 'geç' yazabilirsin: ")
            
            if yeni_cevap != "geç":
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veritabanina_yukle(veritabani)
                print("Bot: Teşekkürler! Öğrendim.")
        
    
if __name__ == "__main__":
    chatbot()