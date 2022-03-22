import random

waiting_list = []


class Building:
    list_of_customers = []
    num_floors = 0
    elevator = 0

    def __init__(self, floors, customers):
        self.num_floors = floors
        global waiting_list

        for ID in range(1, customers + 1):
            new_customer_instance = Elevator_Guest(ID, self.num_floors)
            self.list_of_customers.append(new_customer_instance)

        waiting_list = self.list_of_customers
        self.elevator = Elevator(floors)
        self.run()

    def run(self):
        number_of_customers = len(self.list_of_customers)
        while self.elevator.customer_reached != number_of_customers:
            self.elevator.move()


class Elevator:
    doorOpened = True
    total_floor_number = 0
    direction = 1
    stop_floor = 1
    customer_reached = 0
    max_floor = 0

    def __init__(self, total_floor_number):
        self.total_floor_number = total_floor_number
        self.register_list = []

    def move(self):
        global waiting_list

        if self.stop_floor == self.total_floor_number:
            self.direction = -1
        if self.stop_floor == 1:
            self.direction = 1

        print("\t\tFloor: ", self.stop_floor)

        for customer in self.register_list:
            if customer.end_floor == self.stop_floor:
                self.cancel_customer(customer)
        for customer in waiting_list:
            if customer.start_floor == self.stop_floor:
                self.register_customer(customer)

        self.get_max_floor()
        if self.max_floor < self.stop_floor:
            self.direction = -1
        else:
            self.direction = 1

        if self.direction == 1:
            self.stop_floor = self.stop_floor + 1
        else:
            self.stop_floor = self.stop_floor - 1
        self.output()

    def output(self):
        if self.doorOpened:
            print("\t\tCLOSE_DOOR")
            self.doorOpened = False
        if self.direction == 1:
            print("\t\tMoving direction: UP_1")
        else:
            print("\t\tMoving direction: DOWN_1")
        print(
            "\n\t\t_________________________________________________"
        )

    def register_customer(self, customer):
        global waiting_list
        self.register_list.append(customer)
        waiting_list.remove(customer)

        if not self.doorOpened:
            print("\t\tOPEN_DOOR")
            self.doorOpened = True
        print("\t\tElevator_Guest with ID = ",
              customer.id,
              " enters into the elevator")

    def cancel_customer(self, customer):
        global waiting_list
        customer.finished = True
        self.register_list.remove(customer)
        self.customer_reached = self.customer_reached + 1

        if not self.doorOpened:
            print("\t\tOPEN_DOOR")
            self.doorOpened = True
        print("\t\tElevator_Guest with ID = ",
              customer.id,
              " left the elevator")

    def get_max_floor(self):
        self.max_floor = 0
        global waiting_list
        for customer in self.register_list:
            if customer.end_floor > self.max_floor:
                self.max_floor = customer.end_floor
        for customer in waiting_list:
            if customer.start_floor > self.max_floor:
                self.max_floor = customer.start_floor


class Elevator_Guest:
    id = 0
    start_floor = 1
    end_floor = 1
    finished = False

    def __init__(self, id, number_of_floor):
        self.id = id
        for i in range(len(str(number_of_floor))):
            self.start_floor = random.randint(i, number_of_floor)
        self.end_floor = random.randint(1, number_of_floor)
        while self.end_floor == self.start_floor:
            self.end_floor = random.randint(1, number_of_floor)
        print(
            "Elevator_Guest ID = ",
            self.id,
            "\tStart Floor: ",
            self.start_floor,
            "\t End Floor: ",
            self.end_floor,
        )
