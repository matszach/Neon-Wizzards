"""
This is to be used for all of the game's random number needs.
This allows for level's to be generated from a seed with the same results
"""

# used for traversing through pseudo random number list
seed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# holds index of the next seed number
seed_pointer = [0]

SEED_LENGTH = 10

# list of pseudo random numbers, range 0 - 255
numbers = [35, 171, 10, 38, 113, 226, 242, 67, 29, 234, 159, 11, 225, 220, 253, 148, 68, 135, 243, 64, 27, 199, 86, 170,
           85, 12, 254, 57, 149, 184, 98, 222, 80, 230, 232, 251, 40, 201, 34, 56, 33, 66, 152, 79, 63, 19, 206, 108,
           60, 39, 139, 240, 125, 126, 250, 128, 21, 255, 173, 214, 72, 131, 227, 50, 25, 2, 134, 54, 118, 144, 151, 73,
           176, 44, 229, 123, 70, 61, 127, 169, 238, 99, 8, 249, 165, 252, 28, 17, 77, 100, 158, 81, 49, 194, 142, 191,
           112, 47, 75, 210, 53, 7, 101, 198, 185, 5, 18, 223, 84, 16, 30, 119, 87, 65, 245, 3, 143, 46, 213, 203, 52,
           94, 172, 76, 205, 196, 136, 117, 161, 138, 211, 93, 105, 137, 83, 167, 97, 90, 14, 192, 204, 116, 228, 91,
           96, 62, 168, 193, 71, 120, 31, 147, 202, 233, 150, 102, 48, 231, 153, 114, 224, 175, 107, 9, 1, 189, 174,
           219, 180, 246, 247, 78, 178, 182, 160, 110, 55, 95, 221, 157, 186, 163, 133, 145, 188, 140, 218, 51, 22, 209,
           89, 239, 58, 195, 200, 24, 216, 82, 6, 129, 181, 132, 237, 0, 156, 41, 217, 23, 187, 208, 177, 26, 88, 207,
           103, 236, 241, 20, 92, 106, 104, 130, 121, 15, 215, 155, 124, 183, 122, 197, 74, 37, 36, 13, 109, 164, 42,
           235, 115, 69, 212, 162, 59, 179, 154, 43, 4, 190, 248, 45, 146, 244, 111, 166, 141, 32]

# holds index of the next pseudo random number
number_pointer = [0]

NUMBERS_LENGTH = 256


# performs a jump to the next number pointer
def jump():

    number_pointer[0] += seed[seed_pointer[0]]
    if number_pointer[0] >= NUMBERS_LENGTH:
        number_pointer[0] = 0

    seed_pointer[0] += 1
    if seed_pointer[0] == SEED_LENGTH:
        seed_pointer[0] = 0


# resets the generator
def reset():
    seed_pointer[0] = 0
    number_pointer[0] = 0


# sets new seed
def set_seed(new_seed):
    if not validate_seed(new_seed):
        return False
    else:
        for i in range(SEED_LENGTH):
            seed[i] = int(new_seed[i]) + 1  # +1 prevents seeds overloaded with zeros
        reset()
        return True


# returns true false if the passed seed
# - contains non-number symbols
# - seed is of incorrect length (not 10)
def validate_seed(new_seed):
    pass  # TODO


# returns random from 0 to 0.996 ~
def random():
    jump()
    return numbers[number_pointer[0]]/NUMBERS_LENGTH


# returns random integer from a to b (both included)
def randint(a, b):
    jump()
    return a + int(random() * (b - a + 1))



