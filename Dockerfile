# 1. Python 3.9 sürümünü temel al
FROM python:3.9-slim

# 2. Çalışma klasörünü oluştur
WORKDIR /app

# 3. Bilgisayarındaki dosyaları buraya kopyala
COPY . .

# 4. Gerekli kütüphaneleri yükle
# (requirements.txt dosyanın olduğundan emin olmalısın)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Google Cloud Run genelde 8080 portunu dinler
EXPOSE 8080

# 6. Uygulamayı başlat (app.py yerine senin dosyanın adı neyse onu yaz!)
CMD ["streamlit", "run", "teklif.py", "--server.port=8080", "--server.address=0.0.0.0"]