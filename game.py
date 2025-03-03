import pygame
import abc
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

try:
    path_image = 'image/base.jpg'
    base_img = pygame.image.load(path_image)
except pygame.error as e:
    print(f"Ошибка загрузки изображения: {e}")
    base_img = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    base_img.fill((237, 229, 221))  

class GameCharacter(abc.ABC):
    @abc.abstractmethod
    def take_damage(self, amount):
        try:
            if amount < 0:
                raise ValueError("Урон не может быть отрицательным")
            self.health -= amount
            print(f"{self.name} нанесено {amount} урона!")
        except ValueError as e:
            print(f"Ошибка в методе take_damage: {e}")
            raise
        finally:
            print(f"Здоровье {self.name}: {self.health}")
    
    @abc.abstractmethod
    def heal(self, amount):
        try:
            if amount < 0:
                raise ValueError("Лечение не может быть отрицательным")
                self.health += amount
            elif amount >20:
                self.health =20 
            print(f"{self.name} вылечено {amount}!")
            

        except ValueError as e:
            print(f"Ошибка в методе heal: {e}")
            raise
        finally:
            print(f"Здоровье {self.name}: {self.health}")

class Player(GameCharacter):
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.inventory = []
        self.party = []
        self.equip = {"right": 0, "left": 1, }
        self.speed = 2
        self.map_in = "base"
    
    def take_damage(self, amount):
       super().take_damage(amount)

    def heal(self, amount):
        super().heal(amount)
    def command(self, comm):
            if comm == 1:
                try:
                    path_image = 'image/bg_city.jpg'
                    screen.blit(base_img, (0, 0))
                except pygame.error as e:
                    print(f"Ошибка загрузки изображения: {e}")
            elif comm == 2:
                for item in self.inventory:
                    print(item)
            elif comm == 3:
                try:
                    with open("output.txt", "a") as file:
                        file.write("Запись в файл\n")
                    print("Данные записаны в файл 'output.txt'.",print(map._name))
                except IOError as e:
                    print(f"Ошибка записи в файл: {e}")
      



class Button:
    def __init__(self, text, x, y, width, height, comm):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.comm = comm

    def draw(self, screen):
        pygame.draw.rect(screen, (99, 186, 186), self.rect)
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, (29, 56, 48))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def __repr__(self):
        return f"Button(text='{self.text}', x={self.rect.x}, y={self.rect.y}, width={self.rect.width}, height={self.rect.height}, comm={self.comm})"

class Patient(GameCharacter):
    def __init__(self, image, disc, name, mental_health, physical_health, strong, speed, wisdom, complaints, ability, type):
        self.image = image
        self.disc = disc
        self.name = name
        self.mental_health = mental_health
        self.physical_health = physical_health
        self.strong = strong
        self.speed = speed
        self.wisdom = wisdom
        self.complaints = complaints
        self.ability = ability
        self.type = type
        self.live = True

    def take_damage(self, amount):
        super().take_damage(amount)

    def heal(self, amount):
         super().take_damage(amount)


    def talk(self):
            state = (self.physical_health + self.mental_health + self.wisdom) / 10
            if state >= 1:
                print(self.disc[random.randint(0, 4)])
            else:
                print("Пациент не в состоянии говорить")
   


class Monster(GameCharacter):
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

    def take_damage(self, amount):
        super().take_damage(amount)

    def heal(self, amount):
        super().heal(amount)

 
class Item:
    def __init__(self, image, disc, skills, price, name):
        self.image = image
        self.disc = disc
        self.name = name
        self.price = price
        self.skills = skills



class Ell:
    def __init__(self, _disc, _ability, _name):
        self._disc = _disc
        self._ability = _ability
        self._name = _name



class Map:
    def __init__(self, _disc, _ability, _name, massive):
        self._disc = _disc
        self._ability = _ability
        self._name = _name
        self.massive = massive

    def pattern_set(self):
            pattern = random.randint(1, 3)
            return pattern
     
    def search(self):
            pattern = self.pattern_set()
            for item in self._massive[0]:
                nomer_mass = random.randint(0, 2)
                if pattern == 1:
                    print("Вы встретили ", item[nomer_mass][random.randint(0, self._massive[nomer_mass])])
                elif pattern == 2:
                    print("Вы встретили ", self._massive[0][random.randint(0, len(self._massive[0]) - 1)])
                    pattern = nomer_mass
                else:
                    print("Вы встретили ", self._massive[1][random.randint(0, len(self._massive[0]) - 1)])
            self.pattern_set()
       

def speed_bum(attack, speed):
    print("Совершён усиленный удар")

Asthma = Ell("Во время сражения персонаж может начать задыхаться", "ыыыыыыыыы", "Астма")
Alina_disc = [
    "Девушка с серой кожей и тёмными глазами, толстой в толстовке и джинсах, назвалась Алиной...",
    "Вспыльчива",
    "Она работала грузчиком, когда всё началось, у неё бывают мигрени.",
    "У неё осталась младшая сестра в этом городе, стоит поискать.",
    "Она очень сильна в ближнем бою."
]
Alina = Patient("C:///", Alina_disc, "Алина", 0, 10, 2, 5, 5, Asthma, speed_bum(0, 2), "гуманоид")
Mosman = Monster("C///", "sssss", "Мосман", 100, 50, 10, 5, "Атака", "монстр")
Clock = Item("C////", "Часы, которые увеличивают скорость", "Увеличение скорости", 100, "Часы")
messi_City = [
    [Mosman],
    [Clock],
    [Alina]
]
player = Player("Player1")
buttons = [
    Button("X", 10, 20, 30, 30, 1),
    Button("Переместиться", 210, 500, 150, 30, 2),
    Button("Проверить карманы", 370, 500, 150, 30, 3),
    Button("Оглянуться на команду", 540, 500, 170, 30, 4),
    Button("Сохранить", 730, 500, 150, 30, 5),
    Button("Посмотреть погоду", 50, 500, 150, 30, 6),
]

City = Map("Большой город", speed_bum(1, 2), "Город", messi_City)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("игра")
    clock = pygame.time.Clock()
    #player.heal(-500)
    com = None
  
    print(max(player.equip))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttons:
                        print (buttons.__repr__())

                        if button.is_clicked(event.pos):
                            com = player.command(button.comm)
                            screen.blit(base_img, (0, 0))

        screen.fill((237, 229, 221))
        screen.blit(base_img, (0, 0))
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()