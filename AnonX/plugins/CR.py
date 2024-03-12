import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين كاتيا","المطورين","مطورين","مطورين Katya"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5fe893bc2fafc971178c9.mp4",
        caption=f"""**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين Katya ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗠𝗮𝗭𝗲𝗡 ", url=f"https://t.me/Ve_G4"), 
                 ],[
                    InlineKeyboardButton(
                        "𝗡𝗶𝗡𝗝𝗔", url=f"https://t.me/Mikl5"),
                ],[
                    InlineKeyboardButton(
                        "ᥲ️𝗁ꪔᥱժ", url=f"https://t.me/A7_M3"),
                    InlineKeyboardButton(
                        "kᥲ️ƚYᥲ️", url=f"https://t.me/D1F66"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝⚡", url=f"https://t.me/Source_Katya"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مازن انجم","ميزو","مازن","مبرمج","Mazen","mazen"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Ve_G4")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["ماظن انجم","ماظن","ماظن","ماظين","mazen","mazen"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Ve_G4")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["كاتيا انجم","كاتيا","كاتيا","كاتيا","Katya","كاتيا"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("D1F66")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["نينجا انجم","نينجا","المطور","mano","Mano"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Ve_G4")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d611842a0cee1884f725d.jpg",
        caption=f"""**⩹⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس Katya\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗠𝗮𝗭𝗲𝗡", url=f"https://t.me/Ve_G4"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝⚡", url=f"https://t.me/Source_Katya"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d611842a0cee1884f725d.jpg",
        caption=f"""**⩹⊷━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس Katya\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗠𝗮𝗭𝗲𝗡", url=f"https://t.me/Ve_G4"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ 𝗦𝗼𝗨𝗿𝗖𝗲 ⏣ 𝗞𝗮𝗧𝘆𝗔 ⌝⚡", url=f"https://t.me/Source_Katya"),
                ],

            ]

        ),

    )



    
