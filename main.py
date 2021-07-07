iban_countries = []

with open('data.txt') as f:
    for ele in f:
        line_list = ele.split(",")
        iban_countries.append(line_list)
f.close()

def get_integer(iban):
    res = 0
    # Move the four initial characters to the end of the string.
    iban_rearranged = list(iban[4:] + iban[:4])
    # Replace the letters in the string with digits, expanding the string as necessary, such that A or a = 10, B or b = 11, and Z or z = 35. Each alphabetic character is therefore replaced by 2 digits
    for i in range(len(iban_rearranged)):
        if iban_rearranged[i].isalpha():
            iban_rearranged[i] = str(ord(iban_rearranged[i]) - 55)
    # Convert the string to an integer (i.e. ignore leading zeroes).
    return int("".join(iban_rearranged))

def validate_iban(iban, given_country):
    # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
    for country in iban_countries:
        if country[0] == given_country:
            if (len(iban)) != int(country[2]):
                return 0

    # Move the four initial characters to the end of the string
    # iban_rearranged = list(iban[4:] + iban[:4])

    # Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11, ..., Z = 35
    # for i in range(len(iban_rearranged)):
    #     if iban_rearranged[i].isalpha():
    #         iban_rearranged[i] = str(ord(iban_rearranged[i]) - 55)

    # Interpret the string as a decimal integer and compute the remainder of that number on division by 97
    # if int("".join(iban_rearranged)) % 97 != 1:
        # return 0
    
    # print(iban)

    # 1. Validating the IBAN
    print (get_integer(iban) % 97)

    # 2. Generating IBAN check digits
    iban_check_digits = list(iban[:2] + ['0', '0'] + iban[4:])
    print (get_integer(iban_check_digits))
    
if __name__ == '__main__':
    iban = '   GB82 WEST 1234 5698 7654 32    '
    country = 'United Kingdom'

    iban = iban.replace(" ", "")

    if validate_iban(list(iban), country) == 0:
        print('IBAN is NOT valid')
    else:
        print('IBAN is valid')
    