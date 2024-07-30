import random

with open('Nouns Unfinished.txt', 'r') as infile:
    nouns = infile.read().strip(' \n').split('\n')
with open('Adjectives Unfinished.txt', 'r') as infile:
    adjectives = infile.read().strip(' \n').split('\n')

def generate_username():
    word1 = random.choice(adjectives).title()
    word2 = random.choice(nouns).title()
    username = '{}{}{}'.format(word1, word2, random.randint(1, 99))
    return username

#print(generate_username())
    