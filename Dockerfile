# استخدم صورة Python رسمية
FROM python:3.11-slim

# حدّث النظام وثبّت ffmpeg و opus
RUN apt-get update && \
    apt-get install -y ffmpeg libopus-dev && \
    rm -rf /var/lib/apt/lists/*

# أنشئ مجلد للعمل
WORKDIR /app

# انسخ ملفات مشروعك
COPY . /app

# ثبّت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# شغّل البوت
CMD ["python", "main.py"]

