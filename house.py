import json

STATE_OPENED = "Opened"
STATE_CLOSED = "Closed"


class Room(object):

    def __init__(self, length, width, height, furniture, windows_quantity,
                 door_quantity, window_state, door_state, air_conditioner,
                 radiator):
        self.length = length
        self.width = width
        self.height = height
        self.furniture = furniture
        self.windows_quantity = windows_quantity
        self.door_quantity = door_quantity
        self.window_state = window_state
        self.door_state = door_state
        self.air_conditioner = air_conditioner
        self.radiator = radiator

    def add_furniture(self):
        new_furniture = raw_input("Enter name of furniture: ")
        new_x = raw_input("Enter x: ")
        new_y = raw_input("Enter y: ")
        crossing_x = False
        crossing_y = False
        for furn in self.furniture:
            if new_x == furn.x or new_x >= furn.x + furn.length / 2 or \
               new_x <= furn.x - furn.length / 2 or new_x > furn.length:
                crossing_x = True
            if new_y == furn.y or new_y >= furn.y + furn.width / 2 or \
                    new_y <= furn.y - furn.width / 2 or new_y > furn.width:
                crossing_y = True
            if not crossing_x or not crossing_y:
                self.furniture.append(new_furniture())

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_area(self):
        return self.length * self.width


class BedRoom(Room):
    furniture = []

    def __init__(self, **kwargs):
        super(BedRoom, self).__init__(**kwargs)


class Kitchen(Room):
    furniture = []

    def __init__(self, **kwargs):
        super(Kitchen, self).__init__(**kwargs)


class DrawingRoom(Room):
    furniture = []

    def __init__(self, **kwargs):
        super(DrawingRoom, self).__init__(**kwargs)


class Furniture(object):
    def __init__(self, x, y, length, width, height, weight, color, material):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.material = material
        self.color = color


class Table(Furniture):
    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)


class Chair(Furniture):
    def __init__(self, **kwargs):
        super(Chair, self).__init__(**kwargs)


class KitchenRange(Furniture):
    def __init__(self, max_temp, brand, **kwargs):
        super(KitchenRange, self).__init__(**kwargs)
        self.max_temp = max_temp
        self.brand = brand


class Refrigerator(Furniture):
    def __init__(self, min_temp, brand, current_temp, power, **kwargs):
        super(Refrigerator, self).__init__(**kwargs)
        self.min_temp = min_temp
        self.brand = brand
        self.current_temp = current_temp
        self.power = power


class Wardrobe(Furniture):
    def __init__(self, door_quantity, mirror=False, **kwargs):
        super(Wardrobe, self).__init__(**kwargs)
        self.door_quantity = door_quantity
        self.mirror = mirror


class Bed(Furniture):
    def __init__(self, brand, places_quantity, **kwargs):
        super(Bed, self).__init__(**kwargs)
        self.brand = brand
        self.places_quantity = places_quantity


class Tv(Furniture):
    def __init__(self, diagonal, brand, power, matrix_type, **kwargs):
        super(Tv, self).__init__(**kwargs)
        self.diagonal = diagonal
        self.brand = brand
        self.power = power
        self.matrix_type = matrix_type


class House(object):
    def __init__(self, rooms):
        self.rooms = rooms

    def calculate_volume(self):
        return sum(room.calculate_volume() for room in self.rooms)

    def calculate_area(self):
        return sum(room.calculate_area() for room in self.rooms)

    def calculate_weight(self):
        total_weight = 0
        for room in self.rooms:
            for furn in room.furniture:
                total_weight += furn.weight
        return total_weight

    def calculate_power(self):
        total_power = 0
        for room in self.rooms:
            for furn in room.furniture:
                try:
                    total_power += furn.power
                except AttributeError:
                    continue
        return total_power

    def add_furniture(self):
        room_name = raw_input("Enter room name: ")
        for room in self.rooms:
            if room.__class__.__name__ == room_name:
                room.add_furniture()

    def calculate_coast_of_heating(self):
        area = sum(room.calculate_area() for room in self.rooms)
        cost = area / 10 * 0.86 / 1000 / 8000 / 0.9 * 1000000 * 8 * 30 * 6.879
        print cost


house = House([BedRoom(length=10, width=6, height=3,
                       furniture=[Table(x=2.5, y=1.5, length=1, width=1,
                                        height=0.5, weight=10, color="brown",
                                        material="wood"),
                                  Chair(x=2.5, y=1.3, length=0.5, width=0.5,
                                        height=4, weight=3, color="brown",
                                        material="wood"),
                                  Wardrobe(x=4, y=4, length=2, width=2.5,
                                           height=80, weight=60, color="brown",
                                           material="wood", door_quantity=3,
                                           mirror=True),
                                  Bed(x=6, y=4, length=2, width=1.5, height=70,
                                      weight=80, color="white", material="wood",
                                      brand="Sweet_Sleep", places_quantity=2)],
                       windows_quantity=2, door_quantity=1,
                       window_state=STATE_OPENED, door_state=STATE_OPENED,
                       air_conditioner=True, radiator=25),
              Kitchen(length=6, width=6, height=3,
                      furniture=[Table(x=1.5, y=1.5, length=1.5, width=1.5,
                                       height=0.5, weight=10, color="White",
                                       material="Glass"),
                                 Refrigerator(x=4, y=5, length=1.5, width=2,
                                              height=2, weight=60,
                                              color="Silver", material="Metal",
                                              min_temp=-20, brand="Bosch",
                                              current_temp=-15, power=1000),
                                 KitchenRange(x=5, y=6, length=1, width=1,
                                              height=0.5, weight=50,
                                              color="Silver", material="Metal",
                                              max_temp="400", brand="Bosch")],
                      windows_quantity=2, door_quantity=2,
                      window_state=STATE_OPENED, door_state=STATE_CLOSED,
                      air_conditioner=False, radiator=45),
              DrawingRoom(length=7, width=5, height=3,
                          furniture=[Tv(x=1, y=1, length=1.5, width=1,
                                        height=1.2, weight=35, color="Black",
                                        material="Metal", diagonal="50''",
                                        brand="Philips", power=100,
                                        matrix_type="IPS"),
                                     Bed(x=3, y=1, length=2, width=0.5,
                                         height=0.5, weight=60, color="White",
                                         material="Wood", brand="It's Cool",
                                         places_quantity=1.5)],
                          windows_quantity=2, door_quantity=2,
                          window_state=STATE_CLOSED, door_state=STATE_CLOSED,
                          air_conditioner=False, radiator=55)])


instance_list = list()
final_list = list()


def serialize(obj):
    def serialize_list(list_obj):
        serialized_list = list()
        for item in list_obj:
            if isinstance(item, (int, basestring)):
                serialized_list.append(item)
            elif hasattr(item, "__dict__"):
                serialized_list.append(serialize(item))
            elif isinstance(item, list):
                serialized_list.append(serialize_list(item))
            else:
                pass
        return serialized_list

    obj_name = obj.__class__.__name__
    serialized_data = {
        obj_name: {}
    }
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, float, basestring)):
            serialized_data[obj_name][key] = value
        elif isinstance(value, list):
            serialized_data[obj_name][key] = serialize_list(value)
        elif hasattr(value, "__dict__"):
            serialized_data[obj_name][key] = serialize(value)
        else:
            pass
    return serialized_data


def export(data):
    f = open(raw_input('Enter name: ') + ".txt", 'w')
    json.dump(serialize(data), f, indent=4, sort_keys=True)
    f.close()


def import_data():
    buff = json.load(file(raw_input("Enter filename: ") + ".txt"), encoding="utf-8")
    data = unpack(buff)
    return data


def unpack(obj):
    def list_unpack(list_obj):
        for list_item in list_obj:
            if isinstance(list_item, dict):
                unpack(list_item)
    if isinstance(obj, unicode):
        obj = dict(obj)
    for key in obj:
        instance_list.append(str(key))
        if isinstance(key, (dict, unicode)):
            for value in obj[key]:
                if isinstance(value, unicode):
                    new_obj = obj[key][value]
                    if isinstance(new_obj, list):
                        list_unpack(new_obj)
                    else:
                        instance_list.append((str(value), str(new_obj)))
    return instance_list


if __name__ == "__main__":
    export(house)
    import_data()

