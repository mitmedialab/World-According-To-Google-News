from country_code_mapping import COUNTRY_CODE_MAPPING
from coordinate_distance import distance_on_unit_sphere
import sys


if __name__ == '__main__':

    langs_info_dict = {}
    with open('language_codes_gdp_pop_lat_long.tsv') as fin_lang:
        fin_lang.readline()
        for line in fin_lang:
            lang, gdp, pop, latitude, longitude = line.split('\t')
            gdp, pop, latitude, longitude = float(gdp), float(pop), float(latitude), float(longitude.strip())
            langs_info_dict[lang] = (gdp, pop, latitude, longitude)

    countries_info_dict = {}
    with open('country_codes_gdp_pop_lat_long.tsv') as fin_country:
        fin_country.readline()
        for line in fin_country:
            country, gdp, pop, latitude, longitude = line.split('\t')
            gdp, pop, latitude, longitude = float(gdp), float(pop), float(latitude), float(longitude.strip())
            countries_info_dict[country] = (gdp, pop, latitude, longitude)

    dataset_name = 'gnews_time_annual_all_fixed.csv'
    year_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
    infiles_list = [open(dataset_name.split('.')[0] + '_' + str(year) + '.tsv') for year in year_list]

    for fin in infiles_list:
        min_distance = sys.maxint
        fout = open(fin.name.split('.')[0] + '_regression_dataset.tsv', 'w')
        fout.write('language\tcountry\tnum_results\tlang_gdp\tlang_pop\tcountry_gdp\tcountry_pop\tdistance\n')
        for line in fin:
            try:
                year, s_country, s_lang, t_country, num_results = line.split(',')
                t_country = COUNTRY_CODE_MAPPING[t_country]
                num_results = int(num_results.strip())
                lang_gdp, lang_pop, lang_lat, lang_long = langs_info_dict[s_lang]
                country_gdp, country_pop, country_lat, country_long = countries_info_dict[t_country]
                distance = distance_on_unit_sphere(lang_lat, lang_long, country_lat, country_long)
                if distance < min_distance and distance:
                    min_distance = distance
            except:
                pass

        print "MIN DISTANCE:", min_distance

        with open(fin.name) as fin:
            for line in fin:
                try:
                    year, s_country, s_lang, t_country, num_results = line.split(',')
                    t_country = COUNTRY_CODE_MAPPING[t_country]
                    num_results = int(num_results.strip())
                    num_results += 1
                    lang_gdp, lang_pop, lang_lat, lang_long = langs_info_dict[s_lang]
                    country_gdp, country_pop, country_lat, country_long = countries_info_dict[t_country]
                    distance = distance_on_unit_sphere(lang_lat, lang_long, country_lat, country_long)
                    if not distance:
                        distance = min_distance * 0.1
                    distance += 1
                    fout.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (s_lang, t_country, num_results, lang_gdp, lang_pop, country_gdp, country_pop, distance * 6373))
                except:
                    print line
                    continue
        fout.close()
