def main():
    class patient:
        def __init__(self,image,disc,name,mental_health,physical_health,strong,speed,wisdom,complaits,ability,type):
            self.image=image
            self.disc=disc
            self.name=name
            self.menthal_health=mental_health
            self.physical_health=physical_health
            self.wisdom=wisdom
            self.ability=ability
            self.speed=speed
            self.complaits=complaits
            self.type=type
            self.strong=strong
    class monster:
        def __init__(self,image,disc,name,physical_health,strong,speed,wisdom,ability,type):
            self.image=image
            self.disc=disc
            self.name=name
            self.physical_health=physical_health
            self.wisdom=wisdom
            self.ability=ability
            self.speed=speed
            self.type=type
            self.strong=strong
    class item:
        def __init__ (self,image,disc,skils,price,name):
            self.image=image
            self.disc=disc
            self.name=name
            self.price=price
            self.skils=skils
    class ell:
        def __init__ (self,disc,ability,name):
            self.disc=disc
            self.ability=ability
            self.name=name
    class map:
        def __init__ (self,disc,ability,name,massive):
            self.disc=disc
            self.ability=ability
            self.name=name
            self.massive=massive
    if __name__ == "__main__":
        main()
print("Выполнен вход на закрытую территорию , будьте готовы к столкновениям")