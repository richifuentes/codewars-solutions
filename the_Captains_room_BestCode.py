nom = int(input())
members = list(map(int, input().split()))
rooms = set()   # Contains all the rooms.
room_more_mem = set()   # Contains only the rooms with families.

for m in members:
        if m not in rooms:
                rooms.add(m)
        else:
                room_more_mem.add(m)
print(rooms.difference(room_more_mem).pop())
