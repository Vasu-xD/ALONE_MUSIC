import os
from pyrogram import Client, idle
from pytgcalls import PyTgCalls
from pytgcalls import idle as pyidle
from config import bot, call_py

bot.start()
print("ALONE Music Bot Started")
call_py.start()
print("ALONE Vc Client Started")
pyidle()
idle()
