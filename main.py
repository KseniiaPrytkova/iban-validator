import argparse

iban_countries = []

with open('iban-data.txt') as f:
    for ele in f:
        line_list = ele.split(",")
        iban_countries.append(line_list)
f.close()

def modify_iban_for_analysis(iban):
    res = 0
    # Move the four initial characters to the end of the string.
    iban_rearranged = list(iban[4:] + iban[:4])
    # Replace the letters in the string with digits, expanding the string as necessary,
    #  such that A or a = 10, B or b = 11, and Z or z = 35.
    #  Each alphabetic character is therefore replaced by 2 digits
    for i in range(len(iban_rearranged)):
        if iban_rearranged[i].isalpha():
            iban_rearranged[i] = str(ord(iban_rearranged[i]) - 55)
    # Convert the string to an integer (i.e. ignore leading zeroes).
    return int("".join(iban_rearranged))

def validate_iban(iban, given_country):
    print (given_country)
    # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
    for country in iban_countries:
        if country[0] == given_country:
            if (len(iban)) != int(country[2]):
                return 0
        else:
            print('Given country is not supported')
            return 0

    # Generate IBAN check digits
    iban_check_digits = list(iban[:2] + ['0', '0'] + iban[4:])
    res = 98 - (modify_iban_for_analysis(iban_check_digits) % 97)
    if res < 10:
        res = '{:02}'.format(int(res))
    iban = ''.join(iban)

    # analyzing the results of two algorithms: validating the IBAN and generate IBAN check digits
    if modify_iban_for_analysis(iban) % 97 != 1 and res != int(iban[2:4]):
        return 0
    
if __name__ == '__main__':
    # iban = '   GB82 WEST 1234 5698 7654 32    '
    # country = 'United Kingdom'

    parser = argparse.ArgumentParser()
    parser.add_argument("iban", help="IBAN number itself (ex: 'GB82 WEST 1234 5698 7654 32')", type=str)
    parser.add_argument("country", help="Service country (ex: 'United Kingdom')", type=str)
    args = parser.parse_args()

    iban = args.iban
    country = args.country
    iban = iban.replace(" ", "")

    if validate_iban(list(iban), country) == 0:
        print('IBAN is NOT valid')
    else:
        print('IBAN is valid')
