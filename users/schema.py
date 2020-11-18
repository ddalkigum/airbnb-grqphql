import graphene
from graphene_django import DjangoObjectType
from .models import User
from .types import UserType


class Query(object):

    user = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user(self, info, id):
        return User.objects.get(id=id)
