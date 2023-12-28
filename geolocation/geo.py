import geoip2.database

def get_geolocation(ip):
    with geoip2.database.Reader(r"C:\Users\Andre\Downloads\GeoLite2-City.mmdb") as reader:
        response = reader.city(ip)
        print(response.city.name)
        print(response.country.name)

        return {
            "country": response.country.name,
            "city": response.city.name,
            # Add more fields as needed
        }
    

get_geolocation('138.68.208.11')




