import pycountry

def get_code(country_name):
    return pycountry.countries.get(name=country_name).alpha2
