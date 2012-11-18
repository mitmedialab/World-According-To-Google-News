from country_lang_mapping import COUNTRY_TO_LANGS
from pprint import pprint

fout = open('lang_country_mapping.py', 'w')

if __name__ == '__main__':
    langs_dict = {}
    for country, langs_counts in COUNTRY_TO_LANGS.iteritems():
        country = country[0]
        for lang, count in langs_counts.iteritems():
            if lang not in langs_dict:
                langs_dict[lang] = {country: count}
            else:
                langs_dict[lang][country] = count
    pprint(langs_dict)
