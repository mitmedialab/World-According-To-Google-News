from country_to_code import get_code
from country_lang_mapping import COUNTRY_TO_LANGS
from pprint import pprint

if __name__ == '__main__':
    country_code_dict = {}
    for country_name_tuple in COUNTRY_TO_LANGS:
        country_name = country_name_tuple[0]
        try:
            country_code = get_code(country_name)
            country_code_dict[country_name] = country_code
        except:
            print "FAIL: ", country_name
    pprint(country_code_dict)
