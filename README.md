# Free Fire Nastroyka Bot

Free Fire uchun telefon modeliga qarab sensitivity (nastroyka) ko'rsatadigan,
majburiy obunali Telegram bot. Kanallar, telefon modellari va foydalanuvchilarga
xabar yuborish — barchasi **admin panel** orqali boshqariladi (kodga tegmasdan).

## 1. O'rnatish

```bash
pip install -r requirements.txt
```

## 2. Sozlash

`config.py` faylini oching va quyidagilarni to'ldiring:

```python
BOT_TOKEN = "..."      # @BotFather dan olingan token
ADMIN_IDS = [123456789]  # o'zingizning Telegram ID'ingiz (@userinfobot orqali bilib oling)
```

Bir nechta admin qo'shish uchun: `ADMIN_IDS = [111111, 222222]`

## 3. Ishga tushirish

```bash
python3 bot.py
```

Birinchi ishga tushganda `bot.db` fayli va 17 ta tayyor telefon modeli
(Samsung, Redmi, Xiaomi, POCO, iPhone va h.k.) avtomatik yaratiladi.

## 4. Admin panel — `/admin`

Botga adminlar `/admin` buyrug'ini yozganda tugmali panel ochiladi:

| Tugma | Vazifasi |
|---|---|
| 📢 Xabar yuborish | Keyingi yuborgan xabaringiz (matn/rasm/video) barcha foydalanuvchilarga yuboriladi |
| ➕ Kanal qo'shish | Majburiy obuna kanali qo'shadi |
| ➖ Kanal o'chirish | Ro'yxatdan kanal tanlab o'chiradi |
| 📋 Kanallar | Joriy majburiy kanallar ro'yxati |
| ➕ Model qo'shish | Yangi telefon modeli va uning sensitivity matnini qo'shadi (bir xil nom bo'lsa — yangilaydi) |
| ➖ Model o'chirish | Ro'yxatdan model tanlab o'chiradi |
| 📋 Modellar | Joriy modellar ro'yxati |
| 📊 Statistika | Foydalanuvchilar, kanallar, modellar soni |

**Muhim:** kanal qo'shganingizda **bot o'sha kanalda admin bo'lishi shart**,
aks holda obunani tekshira olmaydi.

## 5. Oddiy foydalanuvchi oqimi

1. `/start` → bot majburiy kanal(lar)ga obunani tekshiradi
2. Obuna bo'lmasa — "➕ Kanal" va "✅ Tekshirish" tugmalari chiqadi
3. Obuna tasdiqlansa — telefon modellari menyusi chiqadi
4. Model tanlansa — o'sha model uchun sensitivity matni yuboriladi

## Fayllar tuzilishi

```
bot.py              - asosiy fayl, barcha handlerlar
config.py            - token va admin ID lar
database.py           - SQLite bilan ishlash (channels, users, models)
default_models.py     - birinchi ishga tushganda qo'shiladigan tayyor modellar
keyboards.py          - inline klaviaturalar
states.py             - admin ko'p bosqichli amallar uchun FSM holatlar
bot.db (avtomatik)    - ma'lumotlar bazasi fayli
```

## Eslatmalar

- Bot 24/7 ishlashi uchun serverga (VPS) joylashtiring va `screen`/`systemd`/`pm2`
  yordamida fon rejimida ishga tushiring.
- Broadcast paytida bot bloklagan foydalanuvchilar bazadan avtomatik o'chiriladi.
- Ko'p bosqichli amal (masalan kanal qo'shish) davomida bot qayta ishga tushirilsa,
  shu amal bekor bo'ladi — qaytadan boshlash kifoya, saqlangan ma'lumotlarga ta'sir qilmaydi.
