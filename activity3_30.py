class India():
    def Capital(self):
        print("New Dheli is the capital of India :")
    def language(self):
        print("Hind is a widely spread lanuage over India")
    def type(self):
        print("India is a developing country")
class USA():
    def Capital(self):
        print("Washington.dc is the capital of Usa ")
    def language(self):
        print("English is primarily spoken in the Usa ")
    def type(self):
            print("Usa is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.Capital()
    country.language()
    country.type()