from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def phone_menu_kb(model_names: list[str]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for name in model_names:
        builder.button(text=f"📱 {name}", callback_data=f"model:{name}")
    builder.adjust(2)
    return builder.as_markup()


def join_channels_kb(channels: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for chat_id, title in channels:
        if chat_id.startswith("http://") or chat_id.startswith("https://"):
            url = chat_id
        elif chat_id.startswith("@"):
            url = f"https://t.me/{chat_id[1:]}"
        else:
            url = f"https://t.me/{chat_id}"
        label = title if title else chat_id
        builder.button(text=f"➕ {label}", url=url)
    builder.button(text="✅ Tekshirish", callback_data="check_sub")
    builder.adjust(1)
    return builder.as_markup()


def admin_panel_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="📢 Xabar yuborish", callback_data="adm:broadcast")
    builder.button(text="➕ Kanal qo'shish", callback_data="adm:addchannel")
    builder.button(text="➖ Kanal o'chirish", callback_data="adm:delchannel")
    builder.button(text="📋 Kanallar", callback_data="adm:channels")
    builder.button(text="➕ Model qo'shish", callback_data="adm:addmodel")
    builder.button(text="➖ Model o'chirish", callback_data="adm:delmodel")
    builder.button(text="📋 Modellar", callback_data="adm:models")
    builder.button(text="📊 Statistika", callback_data="adm:stats")
    builder.adjust(2)
    return builder.as_markup()


def cancel_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Bekor qilish", callback_data="adm:cancel")
    return builder.as_markup()


def back_to_panel_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Admin panel", callback_data="adm:panel")
    return builder.as_markup()


def delete_channels_kb(channels: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i, (chat_id, title) in enumerate(channels):
        label = title if title else chat_id
        builder.button(text=f"🗑 {label}", callback_data=f"delch:{i}")
    builder.button(text="⬅️ Orqaga", callback_data="adm:panel")
    builder.adjust(1)
    return builder.as_markup()


def delete_models_kb(models: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i, (name, _text) in enumerate(models):
        builder.button(text=f"🗑 {name}", callback_data=f"delmd:{i}")
    builder.button(text="⬅️ Orqaga", callback_data="adm:panel")
    builder.adjust(1)
    return builder.as_markup()
