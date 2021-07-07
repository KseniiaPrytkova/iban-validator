iban_countries = []
bad_chars = ["[", "]", "'"]
with open('data.txt') as f:
    for ele in f:
        # print(ele)
        # stripped_line = ele.strip("[]")
        for i in bad_chars :
            stripped_line = ele.replace(i, '')
        # print(stripped_line)
        line_list = stripped_line.split(",")
        iban_countries.append(line_list)

f.close()
print(iban_countries[69][0])
print(iban_countries[69][1])
print(iban_countries[69][2])

print(print(iban_countries[69][0]) == 'United Kingdom')

def validate_iban(iban, given_country):
    print(iban)
    # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
    print(len(iban))
    # print(given_country)
    # print(iban_countries)
    # for country in iban_countries:
    #     print(country[0])
    #     if country[0] == given_country:
    #         print (country[0])

if __name__ == '__main__':
    iban = 'GB82 WEST 1234 5698 7654 32	'
    country = 'United Kingdom'

    validate_iban(iban.replace(" ", ""), country)

    # with open('data.txt') as f:
    #     content = f.read().splitlines()
    
    # for names in content:
    #     print(names)
    
    # print (iban)
    # print (thisdict)
    # if chech_validation_chars_iban(my_iban) == int(my_iban[2:4]):
    #     if validate_iban(my_iban) == 1:
    #         print('IBAN ok!\n')
    #     else:
    #         print('IBAN nok!\n')
    # else:
    #     print('IBAN nok!\n')