# (c) @Royalkrrishna

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Yᴏᴜ Aʀᴇ Bᴀɴ Tᴏ Usᴇ Mᴇ. Cᴏɴᴛᴀᴄᴛ Mʏ [Oᴡɴᴇʀ](https://t.me/MOVIES_VILLA_UPDATE).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except Exception as err:
            print(f"Uɴᴀʙʟᴇ Tᴏ Dᴏ Fᴏʀᴄᴇ Sᴜʙsᴄʀɪʙᴇ Tᴏ {Config.UPDATES_CHANNEL}\n\nEʀʀᴏʀ: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Jᴏɪɴ Oᴜʀ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ❗**\n\n"
                 "Dᴜᴇ Tᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ❗",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🍿 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🍿", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Rᴇғʀᴇsʜ 🔄", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Sᴏᴍᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ Mʏ [Oᴡɴᴇʀ](https://t.me/MOVIES_VILLA_UPDATE).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
