import graphene
from graphene_django import DjangoObjectType
from .models import Room
from . import types


class Query(object):

    rooms = graphene.Field(types.RoomListResponse, page=graphene.Int())
    room = graphene.Field(types.RoomType, id=graphene.Int(required=True))

    def resolve_rooms(self, info, page=1):
        if page < 0:
            page = 1
        page_size = 10
        skipping = page_size * (page - 1)
        taking = page_size * page
        rooms = Room.objects.all()[skipping:taking]
        total = Room.objects.count()
        return types.RoomListResponse(arr=rooms, total=total)

    def resolve_room(self, info, id):

        return Room.objects.get(id=id)
