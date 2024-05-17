# ============ Question 1 ===============

class Vehicle:
    def __init__(self, reg_number, type, owner):
        self.registration_number = reg_number
        self.type = type
        self.owner = owner
        
    def check_num(registration_number):
        print("12344223")

    def car_type(type):
        print("sedan")
    def update_owner(self, owner):
        print(f"{owner} now owns the car!")

Corolla = Vehicle("123764253", "ford", "Jango")
Corolla.update_owner("Mandy")
Corolla.update_owner("Hannah")
Corolla.update_owner("Coleson")
Corolla.update_owner("Rodknee")
print(Corolla.owner)
