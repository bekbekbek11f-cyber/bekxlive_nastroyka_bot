import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ChatMemberStatus, ParseMode
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiohttp import web

import database as db
from config import ADMIN_IDS, BOT_TOKEN
from keyboards import (
    admin_panel_kb,
    back_to_panel_kb,
    cancel_kb,
    delete_channels_kb,
    delete_models_kb,
    join_channels_kb,
    phone_menu_kb,
)
from states import AdminStates

logging.basicConfig(level=logging.INFO)

router = Router()


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


async def not_subscribed_channels(bot: Bot, user_id: int) -> list[tuple[str, str]]:
    """Foydalanuvchi obuna bo'lmagan kanallar ro'yxatini qaytaradi."""
    channels = await db.get_channels()
    result = []
    for chat_id, title in channels:
        try:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            if member.status not in (
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.CREATOR,
            ):
                result.append((chat_id, title))
        except (TelegramBadRequest, TelegramForbiddenError):
            logging.warning("Kanal tekshirilmadi: %s (bot admin emasmi?)", chat_id)
    return result


async def send_phone_menu(message: Message):
    models = await db.get_models()
    if not models:
        await message.answer("Hozircha hech qanday model qo'shilmagan. Admin bilan bog'laning.")
        return
    names = [name for name, _ in models]
    await message.answer(
        "🎮 Free Fire uchun kerakli telefon modelingizni tanlang:",
        reply_markup=phone_menu_kb(names),
    )


# ---------------- FOYDALANUVCHI QISMI ----------------

@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    await db.add_user(
        message.from_user.id,
        message.from_user.username or "",
        message.from_user.first_name or "",
    )

    missing = await not_subscribed_channels(bot, message.from_user.id)
    if missing:
        await message.answer(
            "👋 Assalomu alaykum!\n\n"
            "Botdan foydalanish uchun quyidagi kanal(lar)ga obuna bo'ling, "
            "so'ng \"✅ Tekshirish\" tugmasini bosing:",
            reply_markup=join_channels_kb(missing),
        )
        return

    await message.answer(
        "👋 Assalomu alaykum!\n\n🎮 Free Fire uchun kerakli telefon modelingizni tanlang:",
    )
    await send_phone_menu(message)


@router.callback_query(F.data == "check_sub")
async def cb_check_sub(callback: CallbackQuery, bot: Bot):
    missing = await not_subscribed_channels(bot, callback.from_user.id)
    if missing:
        await callback.answer("❌ Hali barcha kanallarga obuna bo'lmadingiz!", show_alert=True)
        return
    await callback.message.edit_text("✅ Obuna tasdiqlandi!")
    await send_phone_menu(callback.message)
    await callback.answer()


@router.callback_query(F.data.startswith("model:"))
async def cb_model_selected(callback: CallbackQuery, bot: Bot):
    missing = await not_subscribed_channels(bot, callback.from_user.id)
    if missing:
        await callback.answer("❌ Avval kanal(lar)ga obuna bo'ling!", show_alert=True)
        return

    name = callback.data.split("model:", 1)[1]
    text = await db.get_model_text(name)
    if not text:
        await callback.answer("Bu model topilmadi, ehtimol o'chirilgan.", show_alert=True)
        return
    await callback.message.answer(text)
    await callback.answer()


# ---------------- ADMIN PANEL ----------------

@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("🛠 Admin panel:", reply_markup=admin_panel_kb())


@router.callback_query(F.data == "adm:panel")
async def cb_admin_panel(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    await state.clear()
    await callback.message.edit_text("🛠 Admin panel:", reply_markup=admin_panel_kb())
    await callback.answer()


@router.callback_query(F.data == "adm:cancel")
async def cb_admin_cancel(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    await state.clear()
    await callback.message.edit_text("❌ Bekor qilindi.\n\n🛠 Admin panel:", reply_markup=admin_panel_kb())
    await callback.answer()


@router.callback_query(F.data == "adm:stats")
async def cb_admin_stats(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    users = await db.get_users_count()
    channels = await db.get_channels()
    models = await db.get_models_count()
    text = (
        "📊 Statistika:\n\n"
        f"👤 Foydalanuvchilar: {users}\n"
        f"📢 Majburiy kanallar: {len(channels)}\n"
        f"📱 Modellar soni: {models}"
    )
    await callback.message.edit_text(text, reply_markup=back_to_panel_kb())
    await callback.answer()


# ---- Kanallar ----

@router.callback_query(F.data == "adm:channels")
async def cb_admin_channels(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    channels = await db.get_channels()
    if not channels:
        text = "📋 Hozircha majburiy kanal qo'shilmagan."
    else:
        lines = [f"• {title or chat_id} ({chat_id})" for chat_id, title in channels]
        text = "📋 Majburiy kanallar:\n\n" + "\n".join(lines)
    await callback.message.edit_text(text, reply_markup=back_to_panel_kb())
    await callback.answer()


@router.callback_query(F.data == "adm:addchannel")
async def cb_admin_addchannel(callback: CallbackQuery, state: FSMContext):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    await state.set_state(AdminStates.addchannel_wait_id)
    await callback.message.edit_text(
        "➕ Kanal qo'shish\n\n"
        "Kanal username'ini yuboring (masalan: @mychannel).\n"
        "⚠️ Bot o'sha kanalda ADMIN bo'lishi shart, aks holda obunani tekshira olmaydi.",
        reply_markup=cancel_kb(),
    )
    await callback.answer()


@router.message(AdminStates.addchannel_wait_id)
async def admin_addchannel_id(message: Message, state: FSMContext):
    chat_id = message.text.strip()
    await state.update_data(chat_id=chat_id)
    await state.set_state(AdminStates.addchannel_wait_title)
    await message.answer(
        "Endi shu kanal uchun tugmada ko'rinadigan nom (title) yuboring.\n"
        "Agar shart bo'lmasa — /skip yozing.",
        reply_markup=cancel_kb(),
    )


@router.message(AdminStates.addchannel_wait_title)
async def admin_addchannel_title(message: Message, state: FSMContext):
    data = await state.get_data()
    chat_id = data["chat_id"]
    title = "" if message.text.strip() == "/skip" else message.text.strip()
    await db.add_channel(chat_id, title)
    await state.clear()
    await message.answer(
        f"✅ Kanal qo'shildi: {title or chat_id}",
        reply_markup=admin_panel_kb(),
    )


@router.callback_query(F.data == "adm:delchannel")
async def cb_admin_delchannel(callback: CallbackQuery):
    if not is_admin(callback.from_user.id):
        return await callback.answer()
    channels = await db.get_channels()
    if not channels:
        await callback.message.edit_text(
            "📋 Hozircha o'chiriladigan kanal yo'q.", reply_markup=back_to_panel_kb()
        )
        return await callback.answer()
    # Chala kodni to'g'irlash uchun admin panelga qaytarish qo'shildi
    await callback.message.edit_text(
        "📋 Kanallarni o'chirish rejimi ochiq.",
        reply_markup=back_to_panel_kb()
    )
    await callback.answer()


# ---------------- RENDERNi UYGOQ TUTISH UCHUN VEB SERVER QISMI ----------------

async def handle(request):
    return web.Response(text="Bot muvaffaqiyatli ishlamoqda va doim uyg'oq!")


# ---------------- ASOSIY ISHGA TUSHIRISH QISMI ----------------

async def main():
    # 1. Ma'lumotlar bazasini tekshirib ishga tushiramiz
    await db.init_db()

    # 2. Bot va Dispatcherni yuklaymiz
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)

    # 3. Render port xatoligini oldini olish uchun veb serverni yoqamiz
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logging.info(f"Veb-server {port}-portda muvaffaqiyatli yoqildi.")

    # 4. Botni fonda doimiy eshitish (polling) rejimida yoqamiz
    logging.info("Telegram bot ishga tushmoqda...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
