class animal:
    def __init__(Caracteristica, Animal):
     print(f"El {Animal}, es: {Caracteristica}")
     #los atributos
        self.Caracteristica = Caracteristica
        self.Animal = Animal
pollo = animal("Oviparo", "Pollo")
gato = animal("Mamifero", "Gato")
ornitorrinco = animal("Mamifero y oviparo a la vez", "Ornitorrinco")
print (f"El {gato.Animal}, es: {gato.Caracteristica}")
print (f"El {ornitorrinco.Animal}, es: {ornitorrinco.Caracteristica}")
print (f"El {pollo.Animal}, es: {pollo.Caracteristica}")
