from country_code_mapping import COUNTRY_CODE_MAPPING

if __name__ == '__main__':
    fout = open('country_codes_gdp_speech_pop.tsv', 'w')
    with open('country_gdp_speech_pop.tsv') as fin:
        for line in fin:
            line_list = line.split('\t')
            country_name, gdp, speech, pop = line_list
            try:
                country_code = COUNTRY_CODE_MAPPING[country_name]
                fout.write('%s\t%s\t%s\t%s' % (country_code, gdp, speech, pop))
            except:
                fout.write('%s\t%s\t%s\t%s' % (country_name, gdp, speech, pop))
    fout.close()
