class CoffeMachine():
    WATER_LEVEL = 100 # attribut de class

    def _start_machine(self): #_ pour qu'elle soit proteger 
        # Start the machine
        if self.WATER_LEVEL > 20:
            return True
        else :
            print("Please add water")
            return False

    def __boil_water(self): # __ pour que sa soit private
    # Faire bouille l'eau
        return "boilling..."

    def make_coffee(self):
    # Make a new coffee!
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffe is ready my dear!")
        
machine = CoffeMachine()
for i in range(0,5):
    machine.make_coffee()