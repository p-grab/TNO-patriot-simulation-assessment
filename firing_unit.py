import random


class FiringUnit:
    """Represent a Firing Unit that simulates missile fire with probability of kill"""
    
    def __init__(self, probability_of_kill=0.8):
        if not 0.0 <= probability_of_kill <= 1.0:
            raise ValueError("Probability must be between [0, 1]")
        self.probability_of_kill = probability_of_kill
        
    def fire(self):
        random_number = random.random()
        if random_number <= self.probability_of_kill:
            return True
        return False