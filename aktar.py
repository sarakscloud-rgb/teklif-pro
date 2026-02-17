import sqlite3
import pandas as pd

dbs = ["musteri_veritabanı.db", "teklif_veritabanı.db", "teklif_yonetim_sistemi.db"]

for db in dbs:
    try:
        conn = sqlite3.connect(db)
        # Veritabanındaki tablo isimlerini bul
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablolar = cursor.fetchall()
        
        for tablo_adi in tablolar:
            df = pd.read_sql_query(f"SELECT * FROM {tablo_adi[0]}", conn)
            # Her tabloyu kendi adıyla excel olarak kaydet
            df.to_excel(f"{db.replace('.db', '')}_{tablo_adi[0]}.xlsx", index=False)
            print(f"Aktarıldı: {db} -> {tablo_adi[0]}")
        conn.close()
    except Exception as e:
        print(f"Hata oluştu ({db}): {e}")