# UdemyBot - A Simple Udemy Free Courses Scrapper


import asyncio

from telethon import TelegramClient
from udemy import api_hash, api_id, token


class UdemyBOT(TelegramClient):
    def __init__(self):
        super().__init__("udemybot", api_id=api_id, api_hash=api_hash)

    async def __start(self):
        await super().start(bot_token=token)
        me = await self.get_me()
        print(f"<<<  UdemyBot: Started at @{me.username}  >>>\n")
        await super().run_until_disconnected()

    def start_(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__start())
