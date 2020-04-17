class Item:
    def __new__(cls, name, amount):
        if not name:
            print('Cannot create item without name')
            return None
        elif not amount:
            print('Cannot create item without amount')
            return None
        else:
            try:
                int(amount)
            except Exception:
                print('Amount Should be a numeric value')
            return super(Item, cls).__new__(cls)

    def __init__(self, name, cost):
        self.name = name
        self.cost = int(cost)
        self.currency = 'USD'

    def __str__(self):
        return self.name


class Room:
    def __new__(cls, name, items):
        if len(items) < 5:
            print('Room should contain atleast 5 items')

        return super(Room, cls).__new__(cls)

    def __init__(self, name, items):
        self.name = name
        self.items = []
        self.add_items(items)

    def add_items(self, items):
        for item in items:
            item_obj = Item(item[0], item[1])
            self.items.append(item_obj)

    @property
    def cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.cost
        return total_cost

    def print_items(self):
        print('Item name |', 'Cost')
        print('-------------------------------')
        for item in self.items:
            print(item.name, '|',item.cost, item.currency)

    def __str__(self):
        return self.name


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_name, items):
        room = Room(room_name, items)
        self.rooms.append(room)

    def get_all_rooms(self):
        for room in self.rooms:
            print('-------------------------------')
            print(room)
            print('-------------------------------')
            room.print_items()
            print('-------------------------------')

    def get_budget_rooms(self, budget):
        print('Room name | ', 'Cost (USD)')
        for room in self.rooms:
            if room.cost <= budget:
                print(room.name, ' | ', room.cost)


from cmd import Cmd


class MyPrompt(Cmd):
    intro = """1. Add a hotel
2. Add a room to the hotel with any of the 5 items.
3. Print out each room along with the individual items and values. This needs to be properly formatted, eg: no printing an object as is
4. Accept a budget from the user(in $) and list only those rooms which will cost less than or equal to his budget.
5. Exit"""

    hotel_obj = None
    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True

    def default(self, inp):
        if inp == "1":
            hotel_name = input('Enter the hotel name to create: ')
            self.hotel_obj = Hotel(hotel_name)
            print('Hotel created successfully')
        elif inp == "2":
            room_count = input('Enter number of rooms to create: ')
            for index in range(int(room_count)):
                room_name = input('Enter room name: ')
                item_count = input('Enter number of items included in that room: ')
                print('Enter item name with their cost in USD (space separated)')
                items = []
                for i in range(int(item_count)):
                    items.append(input('').split(' '))
                self.hotel_obj.add_room(room_name, items)
        elif inp == "3":
            self.hotel_obj.get_all_rooms()
        elif inp == "4":
            budget = int(input('Enter the budget in USD: '))
            self.hotel_obj.get_budget_rooms(budget)
        elif inp == '5':
            return self.do_exit(inp)

if __name__ == '__main__':
    MyPrompt().cmdloop()


