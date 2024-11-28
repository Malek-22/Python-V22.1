# Pet class definition
class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise_sound = noise  # Use a proper attribute name for noise sound (avoid method-name conflict)

    # Make the pet sleep, increasing its energy
    def sleep(self):
        self.energy += 25
        return self

    # Feed the pet, increasing energy energy by 5 and health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # Let the pet play, increasing health by 5 but decreasing energy 
    def play(self):
        self.health += 5
        self.energy -= 15
        return self

    # Make the pet make a noise
    def noise(self):
        print(f"{self.name} makes a noise: {self.noise_sound}")


# Subclass of Pet (Inheritance Bonus) - Dog
class Dog(Pet):
    def __init__(self, name, tricks, noise="Woof!"):
        super().__init__(name, "Dog", tricks, noise)

    # Override the noise method for Dog-specific sound
    def noise(self):
        print(f"{self.name} barks: {self.noise_sound}")


# Subclass of Pet (Inheritance Bonus) - Cat
class Cat(Pet):
    def __init__(self, name, tricks, noise="Meow!"):
        super().__init__(name, "Cat", tricks, noise)

    # Override the noise method for Cat-specific sound
    def noise(self):
        print(f"{self.name} meows: {self.noise_sound}")


# Ninja class definition
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # Method to walk the pet (which makes the pet play)
    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}...")
        self.pet.play()
        return self

    # Method to feed the pet
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no! You need more pet food!")
        return self

    # Method to bathe the pet (which makes it make a noise)
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()  # Correctly calls the noise method
        return self


# Main section: Creating instances and interacting with them
if __name__ == "__main__":
    # Creating a Pet object
    my_treats = ['Snausage', 'Bacon', "Trash Bag"]
    my_pet_food = ['Pizza', 'Burger']

    # Example using a Dog as the pet
    my_dog = Dog("Buddy", ['sit', 'roll over'], "Woof Woof!")

    # Creating a Ninja instance with the dog as a pet
    adrien = Ninja("Adrien", "Dion", my_treats, my_pet_food, my_dog)

    # Ninja feeding the pet
    adrien.feed()
    adrien.feed()
    adrien.feed()

    # Ninja walking the pet
    adrien.walk()

    # Ninja bathing the pet
    adrien.bathe()

    # Example using a Cat as the pet
    my_cat = Cat("Whiskers", ['fetch', 'jump'], "Meow Meow!")
    
    # Creating another Ninja instance with the cat as a pet
    jade = Ninja("Jade", "Stone", my_treats, my_pet_food, my_cat)

    # Ninja feeding the pet
    jade.feed()
    jade.feed()
    jade.feed()

    # Ninja walking the pet
    jade.walk()

    # Ninja bathing the pet
    jade.bathe()
