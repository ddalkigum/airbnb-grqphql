import graphene
from graphene_django import DjangoObjectType
from .models import Room
from . import types
from .quries import resolve_rooms, resolve_room


class Query(object):

    rooms = graphene.Field(
        types.RoomListResponse, page=graphene.Int(), resolver=resolve_rooms
    )
    room = graphene.Field(
        types.RoomType, id=graphene.Int(required=True), resolver=resolve_room
    )
