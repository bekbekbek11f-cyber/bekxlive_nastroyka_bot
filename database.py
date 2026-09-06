"""
Ma'lumotlar bazasi:
 - channels : majburiy obuna kanallari
 - users    : botdan foydalangan barcha userlar (xabar yuborish uchun, referal statistikasi)
 - models   : telefon modellari va ularning sensitivity matni (admin panel orqali boshqariladi)
 - unlocks  : har bir user qaysi modellarni allaqachon ochganini saqlaydi (referal tizimi uchun)
"""

import aiosqlite
from config import DB_PATH


# ---------- INIT ----------

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS channels (
                chat_id TEXT PRIMARY KEY,
                title TEXT
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                joined_at TEXT DEFAULT CURRENT_TIMESTAMP,
                referred_by INTEGER,
                referral_count INTEGER DEFAULT 0
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS models (
                name TEXT PRIMARY KEY,
                sensitivity_text TEXT,
                sort_order INTEGER DEFAULT 0
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS unlocks (
                user_id INTEGER,
                model_name TEXT,
                PRIMARY KEY (user_id, model_name)
            )
            """
        )
        await db.commit()

        # eski (referal ustunlari yaratilmasdan oldin ishga tushirilgan) bazalar uchun
        # migratsiya — ustunlar allaqachon bo'lsa xato e'tiborsiz qoldiriladi
        for ddl in (
            "ALTER TABLE users ADD COLUMN referred_by INTEGER",
            "ALTER TABLE users ADD COLUMN referral_count INTEGER DEFAULT 0",
        ):
            try:
                await db.execute(ddl)
                await db.commit()
            except Exception:
                pass

    # birinchi marta ishga tushganda tayyor modellarni qo'shib qo'yamiz
    existing = await get_models()
    if not existing:
        from default_models import DEFAULT_MODELS
        for i, (name, text) in enumerate(DEFAULT_MODELS.items()):
            await add_model(name, text, i)


# ---------- CHANNELS ----------

async def add_channel(chat_id: str, title: str = ""):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO channels (chat_id, title) VALUES (?, ?)",
            (chat_id, title),
        )
        await db.commit()


async def remove_channel(chat_id: str) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("DELETE FROM channels WHERE chat_id = ?", (chat_id,))
        await db.commit()
        return cur.rowcount > 0


async def get_channels() -> list[tuple[str, str]]:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT chat_id, title FROM channels")
        return await cur.fetchall()


# ---------- USERS ----------

async def add_user(user_id: int, username: str, first_name: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id, username, first_name) VALUES (?, ?, ?)",
            (user_id, username, first_name),
        )
        await db.execute(
            "UPDATE users SET username = ?, first_name = ? WHERE user_id = ?",
            (username, first_name, user_id),
        )
        await db.commit()


async def remove_user(user_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        await db.commit()


async def get_all_user_ids() -> list[int]:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT user_id FROM users")
        rows = await cur.fetchall()
        return [r[0] for r in rows]


async def get_users_count() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT COUNT(*) FROM users")
        row = await cur.fetchone()
        return row[0] if row else 0


async def user_exists(user_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return (await cur.fetchone()) is not None


async def set_referred_by(user_id: int, referred_by: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET referred_by = ? WHERE user_id = ? AND referred_by IS NULL",
            (referred_by, user_id),
        )
        await db.commit()


async def increment_referral_count(user_id: int) -> int:
    """Referal sonini 1 taga oshiradi va yangi qiymatni qaytaradi."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET referral_count = referral_count + 1 WHERE user_id = ?",
            (user_id,),
        )
        await db.commit()
        cur = await db.execute(
            "SELECT referral_count FROM users WHERE user_id = ?", (user_id,)
        )
        row = await cur.fetchone()
        return row[0] if row else 0


async def get_referral_count(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT referral_count FROM users WHERE user_id = ?", (user_id,)
        )
        row = await cur.fetchone()
        return row[0] if row else 0


# ---------- UNLOCKS (referal orqali ochilgan modellar) ----------

async def is_model_unlocked(user_id: int, model_name: str) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT 1 FROM unlocks WHERE user_id = ? AND model_name = ?",
            (user_id, model_name),
        )
        return (await cur.fetchone()) is not None


async def unlock_model(user_id: int, model_name: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR IGNORE INTO unlocks (user_id, model_name) VALUES (?, ?)",
            (user_id, model_name),
        )
        await db.commit()


async def count_unlocked_models(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT COUNT(*) FROM unlocks WHERE user_id = ?", (user_id,)
        )
        row = await cur.fetchone()
        return row[0] if row else 0


# ---------- MODELS (nastroykalar) ----------

async def add_model(name: str, sensitivity_text: str, sort_order: int = 100):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO models (name, sensitivity_text, sort_order) VALUES (?, ?, ?)",
            (name, sensitivity_text, sort_order),
        )
        await db.commit()


async def remove_model(name: str) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("DELETE FROM models WHERE name = ?", (name,))
        await db.commit()
        return cur.rowcount > 0


async def get_models() -> list[tuple[str, str]]:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT name, sensitivity_text FROM models ORDER BY sort_order, name"
        )
        return await cur.fetchall()


async def get_model_text(name: str) -> str | None:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute(
            "SELECT sensitivity_text FROM models WHERE name = ?", (name,)
        )
        row = await cur.fetchone()
        return row[0] if row else None


async def reset_default_models() -> int:
    """default_models.py dagi barcha modellarni bazaga qayta yozadi (overwrite).

    Admin panel qo'shgan/o'zgartirgan boshqa (default bo'lmagan) modellarga tegmaydi.
    Qaytadan deploy qilingandan keyin yangi sensitivity qiymatlarini bazaga
    tushirish uchun ishlatiladi. Nechta model yangilanganini qaytaradi.
    """
    from default_models import DEFAULT_MODELS

    for i, (name, text) in enumerate(DEFAULT_MODELS.items()):
        await add_model(name, text, i)
    return len(DEFAULT_MODELS)


async def get_models_count() -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cur = await db.execute("SELECT COUNT(*) FROM models")
        row = await cur.fetchone()
        return row[0] if row else 0
