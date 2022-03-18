from aiohttp import web

from api.view import AdvertsView, AdvertView


app = web.Application()

app.add_routes([
    web.view('/api/adverts', AdvertsView),
    web.view('/api/advert/{advert_id}', AdvertView),
    ])
