import pycountry
import pycountry_convert 

for country in pycountry.countries:
    try:
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country.alpha_2)
        continent_name = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
        
    except KeyError:
        #Gérer les cas où le pays n'a pas de code de continent ou de nom de continent
        continent_name = 'unknown'
    print(f"{country.name}({continent_name})".rstrip())