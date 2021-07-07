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
            if (len(iban) - 1) != int(country[2]):
                return 0

if __name__ == '__main__':
    iban = 'GB82 WEST 1234 5698 7654 32	'
    country = 'United Kingdom'

    if validate_iban(iban.replace(" ", ""), country) == 0:
        print('IBAN is not valid')