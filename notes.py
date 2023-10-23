# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
class dog:
    # Functions that start with __ are not intedned to be called directly
    def __init__(self, furC = "", age = 0, weight = 0.0, name = "") -> None:
        """"Create and instance of the dog class and set attributes. Seting the values are the default if attrubuted are not given"""
        self.fur_color = furC
        self.age = age
        self.weight = weight
        self.name = name
        self.fectch_count = 0
    
    def __str__(self) -> str:
        s = "Dog's name is " + self.name + "\n"
        s += "and their age is " + self.fur_color + "\n"
        s += "ans their fur color is " + self.fur_color + "\n"
        return s
    
    def play_fetch(self, num_times) -> None:
        self.fetch_count += num_times


bergDog = dog("black", 7, 78.2, "logan")
ninaDog = dog("brown", 3, 100, "hobbes")

print(bergDog)
print(ninaDog)

bergDog.play_fetch(20)
ninaDog.play_fetch(15)

print(f"{ninaDog.name} has played fetch {ninaDog.fetch_count} times")