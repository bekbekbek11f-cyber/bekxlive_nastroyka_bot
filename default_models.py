# Bot birinchi marta ishga tushganda shu modellar avtomatik bazaga qo'shiladi.
# Keyinchalik admin panel orqali (➕ Model qo'shish / ➖ Model o'chirish) buni
# o'zgartirish, o'chirish yoki yangi model qo'shish mumkun.
# Xuddi shu nomdagi modelni qayta qo'shsangiz — eski matn yangisi bilan almashadi.

DEFAULT_MODELS = {
    "Samsung": (
        "📱 Samsung — Free Fire sensitivity\n\n"
        "🎯 General: 100\n"
        "🔴 Red Dot: 100\n"
        "🔭 2x Scope: 100\n"
        "🔭 4x Scope: 95\n"
        "🎯 Sniper Scope: 80\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 54%"
    ),
    "Redmi": (
        "📱 Redmi — Free Fire sensitivity\n\n"
        "🎯 General: 95\n"
        "🔴 Red Dot: 96\n"
        "🔭 2x Scope: 92\n"
        "🔭 4x Scope: 88\n"
        "🎯 Sniper Scope: 75\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 49%"
    ),
    "Xiaomi": (
        "📱 Xiaomi — Free Fire sensitivity\n\n"
        "🎯 General: 96\n"
        "🔴 Red Dot: 97\n"
        "🔭 2x Scope: 93\n"
        "🔭 4x Scope: 89\n"
        "🎯 Sniper Scope: 76\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 50%"
    ),
    "POCO": (
        "📱 POCO — Free Fire sensitivity\n\n"
        "🎯 General: 98\n"
        "🔴 Red Dot: 98\n"
        "🔭 2x Scope: 95\n"
        "🔭 4x Scope: 90\n"
        "🎯 Sniper Scope: 78\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 51%"
    ),
    "iPhone": (
        "📱 iPhone — Free Fire sensitivity\n\n"
        "🎯 General: 100\n"
        "🔴 Red Dot: 100\n"
        "🔭 2x Scope: 100\n"
        "🔭 4x Scope: 100\n"
        "🎯 Sniper Scope: 85\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 58%"
    ),
    "Infinix": (
        "📱 Infinix — Free Fire sensitivity\n\n"
        "🎯 General: 92\n"
        "🔴 Red Dot: 93\n"
        "🔭 2x Scope: 88\n"
        "🔭 4x Scope: 84\n"
        "🎯 Sniper Scope: 70\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 44%"
    ),
    "Tecno": (
        "📱 Tecno — Free Fire sensitivity\n\n"
        "🎯 General: 90\n"
        "🔴 Red Dot: 92\n"
        "🔭 2x Scope: 87\n"
        "🔭 4x Scope: 82\n"
        "🎯 Sniper Scope: 68\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 42%"
    ),
    "Realme": (
        "📱 Realme — Free Fire sensitivity\n\n"
        "🎯 General: 96\n"
        "🔴 Red Dot: 97\n"
        "🔭 2x Scope: 93\n"
        "🔭 4x Scope: 88\n"
        "🎯 Sniper Scope: 77\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 50%"
    ),
    "OPPO": (
        "📱 OPPO — Free Fire sensitivity\n\n"
        "🎯 General: 95\n"
        "🔴 Red Dot: 95\n"
        "🔭 2x Scope: 91\n"
        "🔭 4x Scope: 87\n"
        "🎯 Sniper Scope: 74\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 48%"
    ),
    "Vivo": (
        "📱 Vivo — Free Fire sensitivity\n\n"
        "🎯 General: 95\n"
        "🔴 Red Dot: 96\n"
        "🔭 2x Scope: 91\n"
        "🔭 4x Scope: 86\n"
        "🎯 Sniper Scope: 73\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 48%"
    ),
    "Honor": (
        "📱 Honor — Free Fire sensitivity\n\n"
        "🎯 General: 97\n"
        "🔴 Red Dot: 97\n"
        "🔭 2x Scope: 94\n"
        "🔭 4x Scope: 89\n"
        "🎯 Sniper Scope: 77\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 51%"
    ),
    "Huawei": (
        "📱 Huawei — Free Fire sensitivity\n\n"
        "🎯 General: 97\n"
        "🔴 Red Dot: 97\n"
        "🔭 2x Scope: 94\n"
        "🔭 4x Scope: 90\n"
        "🎯 Sniper Scope: 78\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 52%"
    ),
    "Nubia": (
        "📱 Nubia — Free Fire sensitivity\n\n"
        "🎯 General: 99\n"
        "🔴 Red Dot: 99\n"
        "🔭 2x Scope: 97\n"
        "🔭 4x Scope: 93\n"
        "🎯 Sniper Scope: 82\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 55%"
    ),
    "OnePlus": (
        "📱 OnePlus — Free Fire sensitivity\n\n"
        "🎯 General: 98\n"
        "🔴 Red Dot: 98\n"
        "🔭 2x Scope: 95\n"
        "🔭 4x Scope: 92\n"
        "🎯 Sniper Scope: 80\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 53%"
    ),
    "ASUS ROG": (
        "📱 ASUS ROG — Free Fire sensitivity\n\n"
        "🎯 General: 100\n"
        "🔴 Red Dot: 100\n"
        "🔭 2x Scope: 98\n"
        "🔭 4x Scope: 96\n"
        "🎯 Sniper Scope: 86\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 59%"
    ),
    "Motorola": (
        "📱 Motorola — Free Fire sensitivity\n\n"
        "🎯 General: 94\n"
        "🔴 Red Dot: 95\n"
        "🔭 2x Scope: 90\n"
        "🔭 4x Scope: 85\n"
        "🎯 Sniper Scope: 72\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 47%"
    ),
    "Boshqa modellar": (
        "📱 Universal (boshqa modellar uchun)\n\n"
        "🎯 General: 90\n"
        "🔴 Red Dot: 90\n"
        "🔭 2x Scope: 85\n"
        "🔭 4x Scope: 80\n"
        "🎯 Sniper Scope: 70\n"
        "📷 Free Camera: 100\n\n"
        "⚙️ Umumiy: 44%\n\n"
        "ℹ️ Bu universal sozlama, telefoningiz ro'yxatda yo'q bo'lsa shundan foydalaning."
    ),
}
