class Fighter:
    """Клас бійця."""

    total_fighters = 0

    def __init__(self, name="Невіомий", health=100, damage_per_attack=10):
        """Конструктор класу."""
        self.__name = name
        self.__health = health
        self.__damage_per_attack = damage_per_attack
        Fighter.total_fighters += 1

    def __del__(self):
        """Деструктор класу."""
        print(f"Боєць {self.__name} видалений з пам'яті.")

    @classmethod
    def get_total_fighters(cls):
        """Метод класу: повертає змінну класу (кількість бійців)."""
        return cls.total_fighters

    @staticmethod
    def is_valid_damage(damage):
        """Cтатичний метод: перевіряє, що шкодф більша за нуль."""
        return damage > 0

    # Функції доступу
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def get_damage_per_attack(self):
        return self.__damage_per_attack

    def set_damage_per_attack(self, damage_per_attack):
        if Fighter.is_valid_damage(damage_per_attack):
            self.__damage_per_attack = damage_per_attack
        else:
            print("Шкода має бути більше 0.")

    def is_alive(self):
        """Повертає Тrue, якщо боєць живий (здоров'я > 0)."""
        return self.__health > 0

    def attack(self, other):
        """Атакує іншого бійця."""
        other.set_health(other.get_health() - self.__damage_per_attack)

    def show_info(self):
        """Виведення інформації на екран."""
        print(f"Боєць: {self.__name}, здоров'я: {self.__health}, "
              f"шкода за атаку: {self.__damage_per_attack}")


class Fight:
    """Клас поєдинку, який містить пару бійців."""

    def __init__(self, fighter1, fighter2):
        """Конструктор класу."""
        self.__fighter1 = fighter1
        self.__fighter2 = fighter2

    def __del__(self):
        """Деструктор класу."""
        print("Поєдинок завершено.")

    def get_fighter1(self):
        return self.__fighter1

    def get_fighter2(self):
        return self.__fighter2

    def get_winner(self):
        """Повертає ім'я переможця в поєдинку двох бійців."""
        first = self.__fighter1
        second = self.__fighter2

        if first.get_damage_per_attack() <= 0 \
                and second.get_damage_per_attack() <= 0:
            return "Ніхто (обидва бійці не завдають шкоди)"

        while True:
            first.attack(second)
            if not second.is_alive():
                return first.get_name()

            second.attack(first)
            if not first.is_alive():
                return second.get_name()

    def show_info(self):
        """Виведення інформації на екан."""
        print("Поєдинок між бійцями:")
        self.__fighter1.show_info()
        self.__fighter2.show_info()


def main():
    fighter1 = Fighter("Іван", 100, 15)
    fighter2 = Fighter("Петро", 120, 10)

    print(f"Створено бійців: {Fighter.get_total_fighters()}")
    print(f"Шкода 15 коректна: {Fighter.is_valid_damage(15)}")
    print(f"Шкода -5 коректна: {Fighter.is_valid_damage(5)}")

    fight = Fight(fighter1, fighter2)
    fight.show_info()

    winner = fight.get_winner()
    print(f"Переможець: {winner}")

    print("Стан бійців після поєдинку:")
    fighter1.show_info()
    fighter2.show_info()
    Fighter.total_fighters

if __name__ == "__main__":
    main()