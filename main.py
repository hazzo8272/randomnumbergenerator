import random

lower_bound = input("Enter lower number: ")
upper_bound = input("Enter upper number: ")

random_number = random.randrange(int(lower_bound), int(upper_bound))

print(random_number)