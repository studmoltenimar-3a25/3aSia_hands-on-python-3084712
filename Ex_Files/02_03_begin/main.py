NAMES = ["Marco", "Paul", "George", "Ringo"]
AGES = [26, 28, 29, 24]
 

MARCO = NAMES[0]
PAUL = NAMES[1]

MARCO_PAUL = NAMES[::2]
GEORGE_RINGO = NAMES[2::]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(MARCO_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
