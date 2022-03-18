from aiohttp import web

from db.models import Advert
from api.schemes import AdvertSchema
from api.validators import is_valid, is_exist


advert_schema = AdvertSchema()
adverts_schema = AdvertSchema(many=True)


async def get_adverts():
    adverts = await Advert.get_all()
    resp = adverts_schema.dump(adverts)

    return web.json_response(resp)


@is_exist
async def get_advert(request):
    advert_id = int(request.match_info.get('advert_id'))

    advert = await Advert.get(advert_id)
    resp = advert_schema.dump(advert)

    return web.json_response(resp)


@is_valid
async def create_advert(request):
    new_advert_attrs = await request.json()
    new_advert = Advert(**new_advert_attrs)

    await Advert.create(new_advert)
    resp = advert_schema.dump(new_advert)

    return web.json_response(resp)


@is_exist
@is_valid
async def update_advert(request):
    advert_id = int(request.match_info.get('advert_id'))
    update_advert_attrs = await request.json()

    await Advert.update(advert_id, **update_advert_attrs)
    updated_advert = await Advert.get(advert_id)
    resp = advert_schema.dump(updated_advert)

    return web.json_response(resp)


@is_exist
async def delete_advert(request):
    advert_id = int(request.match_info.get('advert_id'))

    await Advert.delete(advert_id)

    return web.json_response()
