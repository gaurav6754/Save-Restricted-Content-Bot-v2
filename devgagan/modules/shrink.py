# ---------------------------------------------------
# File Name: shrink.py
# Description: Handles token verification, shorteners, and premium redirects.
# ---------------------------------------------------

import os
import string
import random
import aiohttp
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from devgagan import app
from config import OWNER_ID
from datetime import datetime, timedelta
from devgagan.core.mongo import db

async def is_user_verified(user_id):
    if user_id in OWNER_ID:
        return True
    data = await db.get_data(user_id)
    if data and data.get("verify_expires"):
        expires = data.get("verify_expires")
        if datetime.now() < expires:
            return True
    return False

@app.on_message(filters.command("token") & filters.private)
async def token_handler(client, message):
    user_id = message.from_user.id
    if await is_user_verified(user_id):
        await message.reply("You are already verified and have active free access!")
        return
    
    # Generate verification link or token logic here
    verify_url = f"https://t.me/Sudhu123466" # Updated to your username
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Verify Token", url=verify_url)],
        [InlineKeyboardButton("💬 Contact Owner", url="https://t.me/Sudhu123466")]
    ])
    await message.reply_text(
        "Click the button below to verify your token and get 3 hours of free access without time limits!",
        reply_markup=buttons
    )
