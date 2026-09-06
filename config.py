"""
Bot sozlamalari.

Bu fayl endi maxfiy ma'lumot (token) saqlamaydi — u "environment variables"
(muhit o'zgaruvchilari) dan o'qiladi. Shuning uchun bu faylni GitHub'ga
yuklash xavfsiz.

MAHALLIY KOMPYUTERDA ishga tushirish uchun:
  1. Shu papkada ".env" nomli fayl yarating (aynan ".env.example" nusxasi kabi)
  2. Ichiga haqiqiy BOT_TOKEN va ADMIN_IDS'ingizni yozing
  3. ".env" fayli hech qachon GitHub'ga yuklanmaydi (.gitignore ichida)

RENDER.COM'DA ishga tushirish uchun:
  Render dashboard -> Environment -> "Add Environment Variable" orqali
  BOT_TOKEN va ADMIN_IDS'ni u yerda kiritasiz.
"""

import os

from dotenv import load_dotenv

load_dotenv()  # agar mahalliy kompyuterda ".env" fayli bo'lsa, o'shandan o'qiydi

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

_admin_ids_raw = os.environ.get("ADMIN_IDS", "")
ADMIN_IDS = [int(x.strip()) for x in _admin_ids_raw.split(",") if x.strip()]

DB_PATH = os.environ.get("DB_PATH", "bot.db")

# Har bir oddiy foydalanuvchi referalsiz nechta TURLI model uchun nastroyka
# ola oladi. 1-chisidan keyingi har bir yangi model uchun 1 tadan referal
# (do'stini botga qo'shishi) talab qilinadi. Adminlarga bu cheklov tegmaydi.
FREE_MODELS_COUNT = 1

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN topilmadi! .env faylga yoki Render Environment Variables'ga "
        "BOT_TOKEN qo'shganingizni tekshiring."
    )

if not ADMIN_IDS:
    raise RuntimeError(
        "ADMIN_IDS topilmadi! .env faylga yoki Render Environment Variables'ga "
        "ADMIN_IDS qo'shganingizni tekshiring (masalan: 123456789,987654321)."
    )
