import random

class Hider:
    """A code template for a the hider. The responsibility of this 
    class of objects is to hide from the seeker.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Hider (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]

    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """

        
        if self.distance[-1] == 0:
            message = "(;.;) You found me!"
        elif self.distance[-1] < self.distance[-2]:
            message = "(>.<) Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            message = "(^.^) Getting Colder!"
        
        return message


    def watch(self, location):
        """Watches the given location by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """

        
        if self.location > location:
            self.distance.append(self.location - location)

        elif self.location < location:
            self.distance.append(location - self.location)

        elif self.location == location:
            self.distance.append(0)

        return self.distance