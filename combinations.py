import random
import string

def generate_codes (num, length = 6):
    chars = string.ascii_uppercase + string.digits # define the char pool: uppercase + digits

    codes_set = set() # set to avoid duplicate codes

    while len(codes_set) < num:
        code = ''.join(random.choice(chars) for _ in range(length)) # generate a random code
        codes_set.add(code)
    


    codes_list = list(codes_set)

    return codes_list


    # generate 50 000 unique codes
comb_needed = 50000
codes = generate_codes(comb_needed)


print(codes, end =' ')
