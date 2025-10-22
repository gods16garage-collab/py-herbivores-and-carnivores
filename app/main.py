class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    def __str__(self) -> str:
        return str(Animal.alive)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, other: Animal) -> None:
        # Може кусати тільки травоїдних
        if not isinstance(other, Herbivore):
            return
        # Не може вкусити, якщо жертва ховається
        if other.hidden:
            return

        # Віднімаємо 50 здоров'я
        other.health -= 50

        # Якщо здоров'я закінчилось — видаляємо з alive
        if other.health <= 0 and other in Animal.alive:
            Animal.alive.remove(other)
