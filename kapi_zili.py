#!/usr/bin/env python3
# KAPI ZILI FELSEFESI SIMULATORU
# Bu kod gercekten calisir. Cok yavas ve cok derin.

import time
import random
import sys

def derin_dusun():
    print("Kapı zili çaldı... Yoksa çalmadı mı?")
    time.sleep(2)
    print("Evrenin bir anlamı var mı? Belki zil sesi o anlamdır.")
    time.sleep(1.5)
    
    sorular = [
        "Zil çaldığında sen mi kapıyı açarsın, yoksa kapı mı seni açar?",
        "Eğer zil çalmazsa, misafir gerçekten geldi mi?",
        "Zil sesi bir frekanstır. Frekans ise titreşim. Titreşim ise hayat.",
        "Komşu neden zili çaldı? Belki sadece var olduğunu hatırlatmak için.",
        "Zili susturmak, gerçeği susturmak mıdır?"
    ]
    
    print(random.choice(sorular))
    time.sleep(3)
    print("\nSonuç: Kapı zili çaldıysa cevap ver. Çalmadıysa da cevap ver. Çünkü felsefe bekletmez.")
    time.sleep(1)
    print("Bu programı çalıştırdığın için teşekkürler. Şimdi git kapıyı aç.")

if __name__ == "__main__":
    print("=== KAPI ZILI FELSEFESI v1.0 ===")
    print("Hazırlan... Düşünmeye başlıyoruz...")
    time.sleep(1)
    derin_dusun()
    
    # Gizli not: aW5zYW5sYXIgZXNpdGRpciBhbWEga2ltaWxlcmkgZGFoYSBlc2l0dGly (base64: insanlar esittir ama kimileri daha esittir)
    # Bu satır sadece debug için. Kimse okumasın.
