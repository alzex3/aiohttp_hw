from aiohttp import web

from db.database import db_session
from api.controller import get_advert, get_adverts, delete_advert, create_advert, update_advert


class AdvertsView(web.View):
    @staticmethod
    async def get():
        await db_session.init()
        return await get_adverts()

    async def post(self):
        await db_session.init()
        return await create_advert(self.request)


class AdvertView(web.View):
    async def get(self):
        await db_session.init()
        return await get_advert(self.request)

    async def put(self):
        await db_session.init()
        return await update_advert(self.request)

    async def delete(self):
        await db_session.init()
        return await delete_advert(self.request)
