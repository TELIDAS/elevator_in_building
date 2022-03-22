import random

from elevator import Building


def main():
    global customers
    floors = random.randint(5, 20)
    print("Random MAX Floors:", floors)
    for i in range(1, floors + 1):
        customers = i * random.randint(1, 10)

    Building(floors, customers)


if __name__ == "__main__":
    main()
