class BareMinimumClass:
    pass

b = BareMinimumClass()

class Complex:
    def __init__(self):
        """
        Constructor for Complex numbers.
        Complex numbers are part real, part imaginary.
        Imaginary numbers are roots of negative numbers.
        """
        self.r = realpart
        self.i = imagepart
    
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvote(self):
        self.upvotes += 1
    
    def is_popular(self):
        return self.upvotes > 100

class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'
    
    def eat(self, food):
        return food + ' is delicious, yum!'

class Tiger(Animal):
    pass
    
if __name__ == '__main__':
    # Demo code if you run 'python oop_examples.py'
    # Example 0
    b = BareMinimumClass()
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2) # What should num1 be after?
    print(num1.return, num1.i)
    # Example 2
    user1 = SocialMediaUser('erle', 'Jax')
    user2 = SocialMediaUser('John', 'New York', upvotes=50)
    user3 = SocialMediaUser('John Doe', 'Anytown, USA')
    print(user2.is_popular()) # False
    for _ in range(75):
        user2.receive_upvote()
    print(user2.is_popular()) # True
    