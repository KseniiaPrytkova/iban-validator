import sys, argparse
import unittest

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    iban = list(iban)
    country_found = False
    # Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid
    for country in iban_countries:
        if country[0] == given_country:
            country_found = True
            if (len(iban)) != int(country[2]):
                sys.stderr.write('Length of given IBAN number is incorrect\n')
                return 0
    if not country_found:
        sys.stderr.write('Given country is not supported\n')
        return 0

    # Generate IBAN check digits
    iban_check_digits = list(iban[:2] + ['0', '0'] + iban[4:])
    res = 98 - (modify_iban_for_analysis(iban_check_digits) % 97)
    if res < 10:
        res = '{:02}'.format(int(res))
    iban = ''.join(iban)

    # Analyze the results of two algorithms: validate the IBAN and generate IBAN check digits
    if modify_iban_for_analysis(iban) % 97 != 1 and res != int(iban[2:4]):
        return 0
    else:
        return 1
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iban",
        help="2 arguments: IBAN number itself as a string (ex: 'GB82 WEST 1234 5698 7654 32') and Service country as a string (ex: 'United Kingdom')", 
        nargs=2, type=str, action="append")
    parser.add_argument("-f", "--file", type=str)
    args = parser.parse_args()

    if not args.iban and not args.file:
        sys.stderr.write('No data\n')
        sys.exit(1)
    
    ibans = []
    if args.iban:
        ibans = args.iban
    if args.file:
        with open(args.file) as f:
            for ele in f:
                line_list = [x.strip() for x in ele.split(',')]
                if (len(line_list) != 2):
                    sys.stderr.write('Length of read line is not 2\n')
                    sys.exit(1)
                ibans.append(line_list)
        f.close()

    for element in ibans:
        print('\n' + str(element))
        iban = element[0].replace(" ", "")
        if validate_iban(iban, element[1]) == 0:
            print(f'{bcolors.FAIL}IBAN is NOT valid{bcolors.ENDC}')
        else:
            print(f'{bcolors.OKGREEN}IBAN is valid{bcolors.ENDC}')

# UNIT TESTS
class TestIban(unittest.TestCase):
    def setUp(self):
        iban_countries  = [['United Kingdom','GB','22'], ['Ukraine','UA','29']]
    def tearDown(self):
        iban_countries = []
    def test_return_valid(self):
        actual = validate_iban('UA903052992990004149123456789', 'Ukraine')
        expected = 1
        self.assertEqual(actual, expected)
    def test_return_invalid(self):
        actual = validate_iban('UA90305299299044004149123456789', 'Ukraine')
        expected = 0
        self.assertEqual(actual, expected)
    def test_empty_params(self):
        actual = validate_iban('', '')
        expected = 0
        self.assertEqual(actual, expected)
