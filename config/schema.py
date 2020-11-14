import graphene
from rooms.models import Room


class RoomType(graphene.ObjectType):
    name = graphene.String()
    address = graphene.String()
    price = graphene.Int()
    beds = graphene.Int()


class Query(graphene.ObjectType):
    hello = graphene.String()
    rooms = graphene.List(RoomType)

    def resolve_hello(self, info):
        return "hello"

    def resolve_rooms(self, info):
        return Room.objects.all()


class Mutation:
    pass


schema = graphene.Schema(query=Query)
