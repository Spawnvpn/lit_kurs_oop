import json


class Room(object):
    def __init__(self, length, width, height, furniture, windows_quantity,
                 door_quantity):
        self.length = length
        self.width = width
        self.height = height
        self.furniture = furniture
        self.windows_quantity = windows_quantity
        self.door_quantity = door_quantity

    def add_furniture(self, furniture, new_furniture, new_x, new_y):
        crossing_x = False
        crossing_y = False
        for furn in furniture:
            if new_x == furn.x or new_x >= furn.x + furn.length / 2 or \
               new_x <= furn.x - furn.length / 2 or new_x > furn.length:
                crossing_x = True
            elif new_y == furn.y or new_y >= furn.y + furn.width / 2 or \
                    new_y <= furn.y - furn.width / 2 or new_y > furn.width:
                crossing_y = True
            elif not crossing_x and not crossing_y:
                furniture.append(new_furniture)

    def calculate_volume(self):
        return self.length * self.width * self.height


class BadRoom(Room):
    furniture = []

    def __init__(self, length, width, height, furniture, windows_quantity,
                 door_quantity, window_status="Close", door_status="Close",
                 air_conditioner=False):
        super(Room, self).__init__()
        self.length = length
        self.width = width
        self.height = height
        self.furniture = furniture
        self.windows_quantity = windows_quantity
        self.door_quantity = door_quantity
        self.window_status = window_status
        self.door_status = door_status
        self.air_conditioner = air_conditioner


class Kitchen(Room):
    furniture = []

    def __init__(self, length, width, height, furniture, windows_quantity,
                 door_quantity, window_status="Close", door_status="Close"):
        super(Room, self).__init__()
        self.length = length
        self.width = width
        self.height = height
        self.furniture = furniture
        self.windows_quantity = windows_quantity
        self.door_quantity = door_quantity
        self.window_status = window_status
        self.door_status = door_status


class DrawingRoom(Room):
    furniture = []

    def __init__(self, length, width, height, furniture, windows_quantity,
                 door_quantity, window_status="Close", door_status="Close"):
        super(Room, self).__init__()
        self.length = length
        self.width = width
        self.height = height
        self.furniture = furniture
        self.windows_quantity = windows_quantity
        self.door_quantity = door_quantity
        self.window_status = window_status
        self.door_status = door_status


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
    def __init__(self, x, y, length, height, weight, color, material):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material


class Chair(Furniture):
    def __init__(self, x, y, length, height, weight, color, material):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material


class KitchenRange(Furniture):
    def __init__(self, x, y, length, height, weight, color, material, max_temp, brand):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material
        self.max_temp = max_temp
        self.brand = brand


class Refrigerator(Furniture):
    def __init__(self, x, y, length, height, weight, color, material, min_temp,
                 brand, current_temp, power):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material
        self.max_temp = min_temp
        self.brand = brand
        self.current_temp = current_temp
        self.power = power


class Wardrobe(Furniture):
    def __init__(self, x, y, length, height, weight, color, material,
                 door_quantity, mirror=False):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material
        self.door_quantity = door_quantity
        self.mirror = mirror


class Bed(Furniture):
    def __init__(self, x, y, length, height, weight, color, material,
                 brand, places_quantity):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material
        self.brand = brand
        self.places_quantity = places_quantity


class Tv(Furniture):
    def __init__(self, x, y, length, height, weight, color, material,
                 diagonal, brand, power, matrix_type):
        super(Furniture, self).__init__()
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.weight = weight
        self.color = color
        self.material = material
        self.diagonal = diagonal
        self.brand = brand
        self.power = power
        self.matrix_type = matrix_type


class House(object):
    def __init__(self, rooms):
        self.rooms = rooms

    def calculate_volume(self):
        return sum(room.calculate_volume() for room in self.rooms)


house = House([BadRoom(10, 6, 3,
                       [Table(2.5, 1.5, 1, 1, 0.5, "brown", "wood"),
                        Chair(2.5, 1.3, 0.5, 0.5, 4, "brown", "wood"),
                        Wardrobe(4, 4, 2, 2.5, 80, "brown", "wood", 3, True),
                        Bed(6, 4, 2, 1.5, 70, "white", "wood", "Sweet_Sleep",
                            2)], 2, 1, "Open", "Open", True),
              [Kitchen(6, 6, 3,
                       [Table(1.5, 1.5, 1.5, 1.5, 10, "White", "Glass"),
                        Refrigerator(4, 5, 1.5, 2, 60, "Silver", "Metal", -20,
                                     "Bosch", -15, "1000w"),
                        KitchenRange(5, 6, 1, 1, 55, "Silver", "Metal", "400",
                                     "Bosch")], 2, 2, "Open")],
              [DrawingRoom(7, 5, 3,
                           [Tv(1, 1, 1.5, 1, 35, "Black", "Metal", "50''",
                               "Philips", "100w", "IPS")],
                           Bed(3, 1, 2, 0.5, 70, "White", "Wood", "It's Cool",
                               1.5), 2, "Open", "Open, Close")]])

print house.calculate_volume()


def export(data):
    f = open(raw_input('Enter name: ') + ".txt", 'w')
    json.dump(data, f)
    f.close()


def import_data():
    buff = json.load(file(raw_input("Enter filename: ") + ".txt"))
    print buff
