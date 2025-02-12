import abc
import random
class Do_it(abc.ABC):
    @abc.abstractmethod
    def talk(self):
         pass
    
class Patient(Do_it):
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
    def set_health(self):
        if self.mental_health >10:
            self.mental_health=10
        elif self.mental_health<0:
            self.mental_health=0
        if self.mental_health >10:
            self.mental_health=10
        elif self.mental_health<0:
            self.mental_health=0
    def __str__(self):
        return f"Patient: {self.name}"
    def talk (self):
        state=(self.physical_health+self.physical_health+self.wisdom)/10
        if state>=1:
            print(self.disc[random.randint(0,4)])

        


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
        return f"Monster: {self.name}"


class Item:
    def __init__(self, image, disc, skills, price, name):
        self.image = image
        self.disc = disc
        self.name = name
        self.price = price
        self.skills = skills

    def __str__(self):
        return f"Item: {self.name}"


class Ell:
    def __init__(self, _disc, _ability, _name):
        self._disc = _disc
        self._ability = _ability
        self._name = _name

    def __str__(self):
       return f"Ell: {self._name}"


class Map:
    def __init__(self, _disc, _ability, _name, _massive):
        self._disc = _disc
        self._ability = _ability
        self._name = _name
        self._massive = _massive 
    def pattern_set(self):
        pattern=random.randint(1,3)
        return pattern
    def search(self):
        pattern=self.pattern_set()
        for item in self._massive.values():
            if pattern==1:
                 print("вы встретили ",item)
            elif pattern>=2:
                print("вы встретили ",self._massive["Item"])
                pattern=1
        self.pattern_set()
            

def speed_bum(attack, speed):
    print("Совершён усиленный удар")

Asthma = Ell("Во время сражения персонаж может начать задыхаться", "ыыыыыыыыы", "Астма")
Alina_disc = ["Девушка с серой кожей и тёмными глазами,толстовке и джинсах ,назвалась Алиной... ","Вспыльчива","она работала в грузчиком когда всё началось, у неё бывают мигрени ","у нее осталась младшая сестра в этом городе стоит по искать ","Она очень сильна в ближнем бою"]
Alina = Patient("C:///", Alina_disc, "Алина", 10, 3, 2, 5, 5, Asthma, speed_bum(0, 2), "гуманоид")
Mosman = Monster("C///", "sssss", "Мосман", 100, 50, 10, 5, "Атака", "монстр")
Clock = Item("C////", "Часы, которые увеличивают скорость", "Увеличение скорости", 100, "Часы")
Clock1 = Item("C////", "Часы, которые увеличивают скорость", "Увеличение скорости", 100, "Часы")
messi = {"Item":Clock,"patient":Alina,"Monster":Mosman}
City = Map("Большой город", speed_bum(1, 2), "Город", messi)
def main():
    
    City.search()
    Alina.talk()


if __name__ == "__main__":
    main()