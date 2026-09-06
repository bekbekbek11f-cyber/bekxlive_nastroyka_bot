# Bot birinchi marta ishga tushganda shu modellar avtomatik bazaga qo'shiladi.
# Keyinchalik admin panel orqali (➕ Model qo'shish / ➖ Model o'chirish) buni
# o'zgartirish, o'chirish yoki yangi model qo'shish mumkun.
# Xuddi shu nomdagi modelni qayta qo'shsangiz — eski matn yangisi bilan almashadi.

DEFAULT_MODELS = {
"Samsung": (
        "📱 Samsung — Free Fire sensitivity\n\n"
        "🎯 General: 165\n"
        "🔴 Red Dot: 160\n"
        "🔭 2x Scope: 145\n"
        "🔭 4x Scope: 120\n"
        "🎯 Sniper Scope: 95\n"
        "📷 Free Camera: 165\n\n"
        "⚙️ Umumiy: 54%"
    ),
    "Redmi": (
        "📱 Redmi — Free Fire sensitivity\n\n"
        "🎯 General: 150\n"
        "🔴 Red Dot: 145\n"
        "🔭 2x Scope: 130\n"
        "🔭 4x Scope: 108\n"
        "🎯 Sniper Scope: 85\n"
        "📷 Free Camera: 150\n\n"
        "⚙️ Umumiy: 49%"
    ),
    "Xiaomi": (
        "📱 Xiaomi — Free Fire sensitivity\n\n"
        "🎯 General: 155\n"
        "🔴 Red Dot: 150\n"
        "🔭 2x Scope: 135\n"
        "🔭 4x Scope: 112\n"
        "🎯 Sniper Scope: 88\n"
        "📷 Free Camera: 155\n\n"
        "⚙️ Umumiy: 50%"
    ),
    "POCO": (
        "📱 POCO — Free Fire sensitivity\n\n"
        "🎯 General: 170\n"
        "🔴 Red Dot: 165\n"
        "🔭 2x Scope: 150\n"
        "🔭 4x Scope: 125\n"
        "🎯 Sniper Scope: 98\n"
        "📷 Free Camera: 170\n\n"
        "⚙️ Umumiy: 55%"
    ),
    "iPhone": (
        "📱 iPhone — Free Fire sensitivity\n\n"
        "🎯 General: 180\n"
        "🔴 Red Dot: 175\n"
        "🔭 2x Scope: 160\n"
        "🔭 4x Scope: 140\n"
        "🎯 Sniper Scope: 110\n"
        "📷 Free Camera: 180\n\n"
        "⚙️ Umumiy: 58%"
    ),
    "Infinix": (
        "📱 Infinix — Free Fire sensitivity\n\n"
        "🎯 General: 140\n"
        "🔴 Red Dot: 135\n"
        "🔭 2x Scope: 120\n"
        "🔭 4x Scope: 98\n"
        "🎯 Sniper Scope: 78\n"
        "📷 Free Camera: 140\n\n"
        "⚙️ Umumiy: 44%"
    ),
    "Tecno": (
        "📱 Tecno — Free Fire sensitivity\n\n"
        "🎯 General: 135\n"
        "🔴 Red Dot: 130\n"
        "🔭 2x Scope: 115\n"
        "🔭 4x Scope: 94\n"
        "🎯 Sniper Scope: 75\n"
        "📷 Free Camera: 135\n\n"
        "⚙️ Umumiy: 42%"
    ),
    "Realme": (
        "📱 Realme — Free Fire sensitivity\n\n"
        "🎯 General: 155\n"
        "🔴 Red Dot: 150\n"
        "🔭 2x Scope: 135\n"
        "🔭 4x Scope: 112\n"
        "🎯 Sniper Scope: 90\n"
        "📷 Free Camera: 155\n\n"
        "⚙️ Umumiy: 50%"
    ),
    "OPPO": (
        "📱 OPPO — Free Fire sensitivity\n\n"
        "🎯 General: 150\n"
        "🔴 Red Dot: 145\n"
        "🔭 2x Scope: 130\n"
        "🔭 4x Scope: 106\n"
        "🎯 Sniper Scope: 84\n"
        "📷 Free Camera: 150\n\n"
        "⚙️ Umumiy: 48%"
    ),
    "Vivo": (
        "📱 Vivo — Free Fire sensitivity\n\n"
        "🎯 General: 150\n"
        "🔴 Red Dot: 148\n"
        "🔭 2x Scope: 130\n"
        "🔭 4x Scope: 104\n"
        "🎯 Sniper Scope: 82\n"
        "📷 Free Camera: 150\n\n"
        "⚙️ Umumiy: 48%"
    ),
    "Honor": (
        "📱 Honor — Free Fire sensitivity\n\n"
        "🎯 General: 158\n"
        "🔴 Red Dot: 153\n"
        "🔭 2x Scope: 138\n"
        "🔭 4x Scope: 114\n"
        "🎯 Sniper Scope: 90\n"
        "📷 Free Camera: 158\n\n"
        "⚙️ Umumiy: 51%"
    ),
    "Huawei": (
        "📱 Huawei — Free Fire sensitivity\n\n"
        "🎯 General: 160\n"
        "🔴 Red Dot: 155\n"
        "🔭 2x Scope: 140\n"
        "🔭 4x Scope: 116\n"
        "🎯 Sniper Scope: 92\n"
        "📷 Free Camera: 160\n\n"
        "⚙️ Umumiy: 52%"
    ),
    "Nubia": (
        "📱 Nubia — Free Fire sensitivity\n\n"
        "🎯 General: 175\n"
        "🔴 Red Dot: 170\n"
        "🔭 2x Scope: 155\n"
        "🔭 4x Scope: 132\n"
        "🎯 Sniper Scope: 105\n"
        "📷 Free Camera: 175\n\n"
        "⚙️ Umumiy: 56%"
    ),
    "OnePlus": (
        "📱 OnePlus — Free Fire sensitivity\n\n"
        "🎯 General: 170\n"
        "🔴 Red Dot: 165\n"
        "🔭 2x Scope: 150\n"
        "🔭 4x Scope: 128\n"
        "🎯 Sniper Scope: 100\n"
        "📷 Free Camera: 170\n\n"
        "⚙️ Umumiy: 53%"
    ),
    "ASUS ROG": (
        "📱 ASUS ROG — Free Fire sensitivity\n\n"
        "🎯 General: 185\n"
        "🔴 Red Dot: 180\n"
        "🔭 2x Scope: 165\n"
        "🔭 4x Scope: 145\n"
        "🎯 Sniper Scope: 115\n"
        "📷 Free Camera: 185\n\n"
        "⚙️ Umumiy: 59%"
    ),
    "Motorola": (
        "📱 Motorola — Free Fire sensitivity\n\n"
        "🎯 General: 145\n"
        "🔴 Red Dot: 140\n"
        "🔭 2x Scope: 125\n"
        "🔭 4x Scope: 100\n"
        "🎯 Sniper Scope: 80\n"
        "📷 Free Camera: 145\n\n"
        "⚙️ Umumiy: 47%"
    ),
    "Boshqa modellar": (
        "📱 Universal (boshqa modellar uchun)\n\n"
        "🎯 General: 140\n"
        "🔴 Red Dot: 135\n"
        "🔭 2x Scope: 120\n"
        "🔭 4x Scope: 96\n"
        "🎯 Sniper Scope: 76\n"
        "📷 Free Camera: 140\n\n"
        "⚙️ Umumiy: 44%\n\n"
        "ℹ️ Bu universal sozlama, telefoningiz ro'yxatda yo'q bo'lsa shundan foydalaning."
    ),
}
