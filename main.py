iban_countries = []

with open('data.txt') as f:
    for ele in f:
        line_list = ele.split(",")
        iban_countries.append(line_list)
f.close()

def validate_iban(iban, given_country):
    # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
    for country in iban_countries:
        if country[0] == given_country:
            if (len(iban)) != int(country[2]):
                print(len(iban) - 1)
                print(int(country[2]))
                return 0

    # Move the four initial characters to the end of the string
    iban_rearranged = list(iban[4:] + iban[:4])

    # Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11, ..., Z = 35
    for i in range(len(iban_rearranged)):
        if iban_rearranged[i].isalpha():
            iban_rearranged[i] = str(ord(iban_rearranged[i]) - 55)

    # Interpret the string as a decimal integer and compute the remainder of that number on division by 97
    if int("".join(iban_rearranged)) % 97 != 1:
        return 0	
    
if __name__ == '__main__':
    iban = '   GB82 WEST 1234 5698 7654 32    '
    country = 'United Kingdom'

    iban = iban.replace(" ", "")

    if validate_iban(iban, country) == 0:
        print('IBAN is NOT valid')
    else:
        print('IBAN is valid')
    