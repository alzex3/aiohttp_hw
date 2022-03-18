from aiohttp import web
from marshmallow import ValidationError

from db.models import Advert
from api.schemes import AdvertSchema


def is_valid(func):
    async def wrapper(request):

        try:
            AdvertSchema().load(await request.json())

        except ValidationError as err:
            return web.json_response(
                {'error': err.messages},
                status=400
            )

        return await func(request)

    wrapper.__name__ = func.__name__
    return wrapper


def is_exist(func):
    async def wrapper(request):

        try:
            advert_id = request.match_info.get('advert_id')
            if not await Advert.get(int(advert_id)):
                raise AssertionError

        except AssertionError:
            return web.json_response(
                {'error': 'Advert not found!'},
                status=404
            )

        return await func(request)

    wrapper.__name__ = func.__name__
    return wrapper
