class animal:
    def __init__(especie, Animal):
     print(f"El {Animal}, es: {especie}")
     #los atributos
        self.especie = especie
        self.Animal = Animal
    super().__init__(especie, Animal)
pollo = animal("Oviparo", "Pollo")
gato = animal("Mamifero", "Gato")
ornitorrinco = animal("Mamifero y oviparo a la vez", "Ornitorrinco")
print (f"El {gato.Animal}, es: {gato.especie}")
print (f"El {ornitorrinco.Animal}, es: {ornitorrinco.especie}")
print (f"El {pollo.Animal}, es: {pollo.especie}")
