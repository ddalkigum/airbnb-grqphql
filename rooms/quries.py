from .models import Room
from .types import RoomListResponse


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