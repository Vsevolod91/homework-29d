class Flight():

    def __init__(self):
        self.__city_from = input("Введите город отправления: ")
        self.__city_to = input("Введите город назначения: ")

    def __str__(self):
        return f"Flight from {self.__city_from} to {self.__city_to}"


print(Flight())
