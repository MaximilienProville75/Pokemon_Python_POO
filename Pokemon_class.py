### Pokemon Class

class Pokemon:

    def __init__(self, name, type, owner = None):
        self.name = name 
        self.type = type 
        self.owner = owner 
        self.lvl = 1 
        self.xp = 0 
        self.health = 100 
        self.alive = True
        self.max_health = self.lvl * self.health
        self.evolution = 1 
        self.active = False

    def __repr__(self):
        return "{} is a pokemon of type: {}, actual lvl {}".format(self.name , self.type, self.lvl)

    def is_active(self):
        if self.active:
            return "Active"
        else:
            return "Pokeball"

    def get_status(self):
        if self.alive:
            return "{} is alive!".format(self.name)
        return "{} is dead!".format(self.name)

    def is_alive(self):
        return self.alive == True 

    def ko(self):
        if self.is_alive():
            self.alive = False
            self.health = 0 
            print("{}".format(self.get_status()))
            return
        print("{} is already dead!".format(self.name))

    def revive(self):
        if self.is_alive() == False:
            self.alive = True 
            self.health = self.max_health
            return "{} once again ! with {}/{}hp".format(self.get_status(), self.health, self.max_health)
        return "{} is already revive".format(self.name)
    
    def loose_health(self, lost_hp):
        if self.is_alive():
            self.health -= lost_hp
            if self.health > 0:
                return "{} , with {} hp.".format(self.get_status(), self.health)                
            else:
                self.ko()
        else: 
            return "{} is already dead, cannot substract hps".format(self.get_status())
    
    def restore_health(self, gain_hp):
        if self.is_alive():
            self.health += gain_hp
            if self.health >= self.max_health:
                self.health = self.max_health
                print("{} is already full HP, it cannot be healed.".format(self.name))
            else:
                print("{} gained {} hp and is now {} hp.".format(self.name , gain_hp, self.health))
        else:
            print( "{} is dead, cannont be healed!".format(self.name))

    def level_up(self):
        if self.is_alive():
            self.lvl += 1 
            self.max_health *= self.lvl
            self.health = self.max_health
            print("{} gain one lvl of xp and is now lvl {}.".format(self.name, self.lvl))
        else:
            print("{} is dead, cannont lvl up!".format(self.name))

    def add_xp(self, xp_gained):
        if self.is_alive():
            self.xp += xp_gained
            if self.xp >= 100:
                self.level_up()
                self.xp = self.xp - 100
                return "{} gained {} xp and is now lvl {} with {} xp.".format(self.name, xp_gained, self.lvl, self.xp)
        else:
            return "{} is dead, cannont lvl up!".format(self.name) 

    def evolution_up(self):
        if self.is_alive():
            if self.lvl == range(1, 25 ,5):
                self.evolution += 1 
                print(">> {} reached a new evolution lvl  >> {} <<".format(self.name, self.evolution))
            else:
                print(">> Can\'t evolve a dead pokemon...")
        else:
            print(">> Can\'t evolve a dead pokemon...")

    def evolution_attack_boost(self):
        if self.evolution == 2:
            dmg_boost = 1.25
            return dmg_boost
        elif self.evolution == 3:
            dmg_boost = 1.5 
            return dmg_boost
        elif self.evolution == 4:
            dmg_boost = 1.75
            return dmg_boost
        elif self.evolution == 5:
            dmg_boost = 2
            return dmg_boost

    def type_attack_boost(self, target):
        if self.type == "Fire" and target.type == "Water":
            dmg_boost = 0.5
            return dmg_boost
        elif self.type == "Fire" and target.type == "Earth":
            dmg_boost = 2
            return dmg_boost
        elif self.type == "Fire" and target.type == "Electricity":
            dmg_boost = 1.5 
            return dmg_boost
        elif self.type == "Fire" and target.type == "Psy":
            dmg_boost = 0.25
            return dmg_boost

        elif self.type == "Water" and target.type == "Fire":
            dmg_boost = 2 
            return dmg_boost
        elif self.type == "Water" and target.type == "Earth":
            dmg_boost = 0.5
            return dmg_boost
        elif self.type == "Water" and target.type == "Electricity":
            dmg_boost = 2
            return dmg_boost
        elif self.type == "Water" and target.type == "Psy":
            dmg_boost = 0.3
            return dmg_boost
        
        elif self.type == "Earth" and target.type == "Water":
            dmg_boost = 0.5
            return dmg_boost
        elif self.type == "Earth" and target.type == "Fire":
            dmg_boost = 1.5
            return dmg_boost
        elif self.type == "Earth" and target.type == "Electricity":
            dmg_boost = 1
            return dmg_boost
        elif self.type == "Earth" and target.type == "Psy":
            dmg_boost = 0.5
            return dmg_boost
        
        elif self.type == "Electricity" and target.type == "Water":
            dmg_boost = 0.5
            return dmg_boost
        elif self.type == "Electricity" and target.type ==  "Fire":
            dmg_boost = 0.75
            return dmg_boost
        elif self.type == "Electricity" and target.type == "Earth":
            dmg_boost = 1
            return dmg_boost
        elif self.type == "Electricity" and target.type == "Psy":
            dmg_boost = 0.75
            return dmg_boost

        elif self.type == "Psy" and target.type == "Water":
            dmg_boost = 1.3
            return dmg_boost
        elif self.type == "Psy" and target.type == "Fire":
            dmg_boost = 1.25
            return dmg_boost
        elif self.type == "Psy" and target.type == "Earth":
            dmg_boost = 1.5
            return dmg_boost
        elif self.type == "Psy" and target.type == "Electricity":
            dmg_boost = 1.75
            return dmg_boost

    def attack(self, target):
        if self.is_alive():
            if target.is_alive():
                dmg_dealt = self.type_attack_boost(target) * self.lvl * 2 * self.evolution_attack_boost()
                print(">> {} attack {}".format(self.name, target.name))
                target.loose_health(dmg_dealt)
                if target.is_alive():
                    self.add_xp(self.lvl * 1.5)
                else:
                    print(">> Can\'t attack target, {} is dead.".format(target.name))
            else:
                print(">> Can't attack, {} is dead".format(self.name))

 
    