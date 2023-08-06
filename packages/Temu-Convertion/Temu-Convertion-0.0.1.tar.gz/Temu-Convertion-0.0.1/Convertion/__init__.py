class Convertion:
    def __init__(self,unit):
        self.weight = unit


    def kg_to_lb(self):
        unit = input("select either of conversions(L)bs or (K)g: ")
        weight = int(input("Please enter weight: "))

        if unit.upper() == "L":
            converted = weight * 0.45
            print(f"Your weight is {converted}kg")
        else:
            converted = weight / 0.45
            print(f"You are {converted}pounds")


call = Convertion(7)
p = call.kg_to_lb()
print(p)