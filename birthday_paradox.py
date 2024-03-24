from random import randint

NUM_OF_PEOPLE = 23
NUM_OF_DAYS = 365
NUM_OF_TRIALS = 10000

# Generate a random birthday. 
def random_birthday():
    birthday = randint(1, NUM_OF_DAYS)
    return birthday

# Generate a set of birthdays, pass a parameter equal to number of people in the room.
def generate_k_birthdays(k):
    birthdays  = [random_birthday() for _ in range(k)]
    return birthdays 

# Check for duplications, pass a set of birthdays.
def duplication_check(birthdays):
    unique_birthdays = set(birthdays) # Recall that the set() function returns the unique elements in a list. 
    len_unique_birthdays = len(unique_birthdays)
    len_birthdays = len(birthdays)

    duplicate = (len_unique_birthdays != len_birthdays)
    return duplicate

# Loop through number of trials to find total number of duplications. 
def probability_of_duplication():
    num_duplication = 0
    for _ in range(NUM_OF_TRIALS):
        birthdays = generate_k_birthdays(NUM_OF_PEOPLE)
        duplicate = duplication_check(birthdays)
        if duplicate:   
            num_duplication += 1
    # Divide by number of trials to find the proportion with at least one duplication.    
    probability_duplication = num_duplication / NUM_OF_TRIALS
    return probability_duplication

# Output the fraction of trials with at least one duplication to the user. 
probability_duplication = probability_of_duplication()
print(f'Estimated fraction of trials with at least one duplication is {probability_duplication}')
