if __name__ == '__main__':
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

    fout = open('country_codes_gdp_pop_lat_long.tsv', 'w')
    fout.write('country\tgdp\tpop\tlatitude\tlongitude\n')
    with open('country_codes_gdp_speech_pop.tsv') as fin:
        fin.readline()
        for line in fin:
            country_code, gdp, pop, speech = line.split('\t')
            gdp, pop, speech = float(gdp), int(pop), float(speech.strip())
            location = country_coords_dict[country_code]
            latitude, longitude = location
            fout.write('%s\t%s\t%s\t%s\t%s\n' % \
                           (country_code, gdp, pop, latitude, longitude))
        fout.close()
