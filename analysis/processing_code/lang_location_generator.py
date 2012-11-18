'''
Generate a set of coordinates for the location of a language

v1 (11/17/12): Location of the most populous country
'''

from lang_country_mapping import LANG_TO_COUNTRIES
from country_code_mapping import COUNTRY_CODE_MAPPING
from pprint import pprint
import sys

def main():
    # Create dictionary mapping country codes to coordinates
    country_coords_dict = {}
    with open('country_centroids_all.csv') as fin:
        fin.readline()
        for line in fin:
            try:
                line_list = line.split('\t')
                latitude, longitude, _, _, _, _, _, _, _, short_name, full_name, _, country_code = line_list
                country_code = country_code.strip()
                country_coords_dict[country_code] = (float(latitude), float(longitude))
            except:
                # Misses some small countries without ISO codes
                continue

    # Add population to the previous mapping dictionary
    country_pop_dict = {}
    with open('country_codes_gdp_speech_pop.tsv') as fin:
        for line in fin:
            line_list = line.split('\t')
            country_code, gdp, pop, speech = line_list
            pop = float(pop.strip())
            country_pop_dict[country_code] = pop

    # Create dictionary mapping language codes to coordinate pairs
    langs_locations = {}
    missed_mappings = []
    for lang, countries in LANG_TO_COUNTRIES.iteritems():
        max_pop_country = ''
        max_pop = -sys.maxint - 1
        for country_name, proportion in countries.iteritems():
            try:
                country_code = COUNTRY_CODE_MAPPING[country_name]
                country_pop = country_pop_dict[country_code] * (proportion / 100.)
                if country_pop > max_pop:
                    max_pop = country_pop
                    max_pop_country = country_code
            except:
                if country_name not in missed_mappings:
                    missed_mappings.append(country_name)
                continue
        try:
            langs_locations[lang] = country_coords_dict[max_pop_country]
        except:
            print max_pop_country
    print "MISSED MAPPING FOR: ", ', '.join(missed_mappings)

    lang_gdp_dict = {}
    with open('lang_avg_gdp.tsv') as fin:
        fin.readline()
        for line in fin:
            language, gdp = line.split('\t')
            gdp = float(gdp.strip())
            lang_gdp_dict[language] = gdp

    lang_pop_dict = {}
    with open('lang_pop.tsv') as fin:
        fin.readline()
        for line in fin:
            language, pop = line.split('\t')
            pop = float(pop.strip())
            lang_pop_dict[language] = pop

    # Write file with language, gdp, pop, and coordinates
    fout_final = open('language_codes_gdp_pop_lat_long.tsv', 'w')
    fout_final.write('language\tgdp\tpopulation\tlatitude\tlongitude\n')
    for lang, location in langs_locations.iteritems():
        fout_final.write('%s\t%s\t%s\t%s\t%s\n' \
                             % (lang, lang_gdp_dict[lang], lang_pop_dict[lang], location[0], location[1]))
    fout_final.close()

if __name__ == '__main__':
    main()
