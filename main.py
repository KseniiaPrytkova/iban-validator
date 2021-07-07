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

    for i in range(len(iban_rearranged)):
        if iban_rearranged[i].isalpha():
            # print(iban_rearranged[i])
            # print(ord(iban_rearranged[i]))
            iban_rearranged[i] = ord(iban_rearranged[i]) - 55

    # print("".join(iban_rearranged))
    print(iban_rearranged)
    
if __name__ == '__main__':
    iban = '   GB82 WEST 1234 5698 7654 32    '
    country = 'United Kingdom'

    # if validate_iban(iban.replace(" ", ""), country) == 0:
    #     print('IBAN is not valid')
    iban = iban.replace(" ", "")
    # print(iban)
    if validate_iban(iban, country) == 0:
        print('IBAN is not valid')