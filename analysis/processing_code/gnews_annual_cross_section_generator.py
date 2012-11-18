from country_code_mapping import COUNTRY_CODE_MAPPING

if __name__ == '__main__':
    fin_name = 'gnews_time_annual_all_fixed.csv'
    year_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]
    years_dict = dict([(year, open(fin_name.split('.')[0] + '_' + str(year) + '.tsv', 'w')) for year in year_list])
    for out_file in years_dict.values():
        out_file.write('date_period,orig_country,orig_lang,dest_country,num_results\n')

    with open(fin_name) as fin:
        fin.readline()
        for line in fin:
            try:
                year, _, _, _, _  = line.split(',')
                year = int(year)
                years_dict[year].write(line)
            except:
                print line
    for out_file in years_dict.values():
        out_file.close()
