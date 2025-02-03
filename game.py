class Patient:
    def __init__(self, image, disc, name, mental_health, physical_health, strong, speed, wisdom, complaits, _ability, type):
        self.image = image
        self.disc = disc
        self.name = name
        self.mental_health = mental_health
        self.physical_health = physical_health
        self.strong = strong
        self.speed = speed
        self.wisdom = wisdom
        self.complaits = complaits
        self._ability = _ability
        self.type = type

    def __str__(self):
        return f"Patient: {self.name}, Description: {self.disc}, Type: {self.type}"
    def talk (wish):
        if (wish==angry):
            pass


class Monster:
    def __init__(self, image, disc, name, physical_health, strong, speed, wisdom, ability, type):
        self.image = image
        self.disc = disc
        self.name = name
        self.physical_health = physical_health
        self.strong = strong
        self.speed = speed
        self.wisdom = wisdom
        self.ability = ability
        self.type = type

    def __str__(self):
        return f"Monster: {self.name}, Description: {self.disc}, Type: {self.type}"


class Item:
    def __init__(self, image, disc, skills, price, name):
        self.image = image
        self.disc = disc
        self.name = name
        self.price = price
        self.skills = skills

    def __str__(self):
        return f"Item: {self.name}, Description: {self.disc}, Price: {self.price}"


class Ell:
    def __init__(self, _disc, _ability, _name):
        self._disc = _disc
        self._ability = _ability
        self._name = _name

    def __str__(self):
       return f"Ell: {self._name}, Description: {self._disc}, Ability: {self._ability}"


class Map:
    def __init__(self, _disc, _ability, _name, _massive):
        self._disc = _disc
        self._ability = _ability
        self._name = _name
        self._massive = _massive

    def search(self):
        for item in self._massive:
            print("вы встретили ",item)


def speed_bum(attack, speed):
    print("Совершён усиленный удар")


def main():
    
    Asthma = Ell("Во время сражения персонаж может начать задыхаться", "ыыыыыыыыы", "Астма")
    Alina_disc = ["Девушка с серой кожей и тёмными глазами,толстовке и джинсах ,назвалась Алиной... ","Вспыльчива","она работала в грузчиком когда всё началось, у неё бывают мигрени ","у нее осталась младшая сестра в этом городе стоит по искать "]
    Alina = Patient("C:///", Alina_disc, "Алина", 10, 3, 2, 5, 5, Asthma, speed_bum(0, 2), "гуманоид")
    Mosman = Monster("C///", "sssss", "Мосман", 100, 50, 10, 5, "Атака", "монстр")
    Clock = Item("C////", "Часы, которые увеличивают скорость", "Увеличение скорости", 100, "Часы")
    messi = [Clock, Asthma, Alina, Mosman]
    City = Map("Большой город", speed_bum(1, 2), "Город", messi)
    City.search()


if __name__ == "__main__":
    main()