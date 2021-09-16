class Trainer:

    def __init__(self, name, nb_potion_health, nb_potion_revive):
        self.name = name 
        self.nb_potion_health = nb_potion_health
        self.nb_potion_revive = nb_potion_revive
        self.badge = 0
        self.title = None
        self.pokelist = [] 
        self.active = None

    def __repr__(self):
        return "{} - Pokemons:\n{}".format(self.name, self.show_pokelist())

    def show_pokelist(self):
        if (len(self.pokelist) > 0):
            for pokemon in self.pokelist:
                print(">> {}, type {}, {} , hp {}/{}, lvl{}, {}/100xp, {}.".format(pokemon.name, pokemon.type, pokemon.get_status(), pokemon.health, pokemon.max_health, pokemon.lvl, pokemon.xp, pokemon.is_active()))
        else:
            print("{} has no pokemon in his pokelist.".format(self.name))
    
    def add_pokelist(self, pokemon):
        if (len(self.pokelist) < 6):
            self.pokelist.append(pokemon)
            pokemon.owner = self
            print(">> Adding {} to {}'s Pokedex".format(pokemon.name, self.name))
            if len(self.pokelist) == 1:
                self.active = self.pokelist[0]
                pokemon.active = True
                print(">> {} defined as a default active pokemon".format(self.pokelist[0].name))
        else:
            user_input = input(">>{}'s Pokedex is full, remove pokemon ? Y/N".format(self.name))
            if user_input.upper() == "Y":
                self.remove_pokelist()
                self.add_pokelist(pokemon)
            else:
                return

    def remove_pokelist(self):
        if (len(self.pokelist) > 0):
            ls_index = [i for i in range(len(self.pokelist))]
            for index in ls_index:
                print(">>Press {} to remove {} - type {} ({}/{}Hps) - Level {} ({}/100XP)".format(index, self.pokelist[index].name, self.pokelist[index].type, self.pokelist[index].health, self.pokelist[index].max_health, self.pokelist[index].lvl, self.pokelist[index].xp))
            user_input = int(input(">> Remove Pokemon choice:"))
            if user_input in ls_index:
                if self.pokelist[user_input].active:
                    user_countinue = input("> Active Pokemon, change active: Y/N ?")
                    if user_countinue.upper() == "Y":
                        self.set_active()
                        self.remove_pokelist()
                    else:
                        return 
                else:
                    self.pokelist.remove(self.pokelist[user_input])
            else:
                user_countinue = input("> Choice not in the list, try again: Y/N ?")
                if user_countinue.upper() == "Y":
                    self.remove_pokelist()
                else:
                    return 

    def user_potion_health(self):
        if self.nb_potion_health > 0:
            self.nb_potion_health -= 1 
            self.active.restore_health(50 * self.active.lvl)
    
    def user_revive_potion(self):
        if self.nb_potion_revive > 0:
            self.nb_potion_revive -= 1
            self.active.revive()
    
    def set_active(self):
        list_index = [i for i in range(len(self.pokelist))]
        print(">> Set Active Pokemon <<")
        for index in list_index:
            print(">>Press {} to remove {} - type {} ({}/{}Hps) - Level {} ({}/100XP)".format(index, self.pokelist[index].name, self.pokelist[index].type, self.pokelist[index].health, self.pokelist[index].max_health, self.pokelist[index].lvl, self.pokelist[index].xp))
        user_input = int(input(">> Define {} active Pokemon.".format(self.name)))
        if user_input in list_index:
            if self.pokelist[user_input].is_alive():
                self.active = self.pokelist[user_input]
                print(">> Definte {} as active pokemon.".format(self.pokelist[user_input].name))
                return
            else:
                print(">>Please choose an alive Pokemon")
                self.set_active()
        else:
            print(">> Choice not in the List.")
            self.set_active()

    def attack_trainer(self, target_trainer):
        print("Trainer {} use {} to attack Trainer {} defends with {}".format(self.name, self.active.name, target_trainer.name, target_trainer.active.name))
        if self.active != None:
            if target_trainer.active != None:
                if self.active.is_alive():
                    if target_trainer.active.is_alive():
                        self.active.attack(target_trainer.active)
                    else:
                        print("Target {} is dead. Pick alive Pokemon to defaut.".format(target_trainer.active.name))
                        target_trainer.set_active()
                        self.attack_trainer(target_trainer)
                        return
                else:
                    print("You {} is dead. Please pick alive pokemon to Attack".format(self.active.name))
                    self.set_active()
                    self.attack_trainer(target_trainer)
                    return
            else:
                print("Trainer target {} should select active Pokemon".format(target_trainer.name))
                target_trainer.set_active()
                self.attack_trainer(target_trainer)
                return
        else:
            print("Trainer {} should select an active Pokemon.".format(self.name))
            self.set_active
            self.attack_trainer(target_trainer)
            return

    def badge_counter(self, target_trainer):
        if target_trainer.pokelist == 0:
            

    def get_trainer_title(self):
        if self.badge >=2 and self.badge < 4:
            self.title = "Amateur Trainer"
            print(">> {} has the Title : >> {} <<".format(self.name, self.title))
        elif self.badge == 4:
            self.title = "Professional Trainer"
            print(">> {} has the Title : >> {} <<".format(self.name, self.title))
        elif self.badge >= 5:
            self.title = "Expert Trainer"
            print(">> {} has the Title : >> {} <<".format(self.name, self.title))
            return

            