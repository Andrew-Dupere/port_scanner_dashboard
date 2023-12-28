import re
import geoip2.database
import os

def get_geolocation(ip, db_path):
    with geoip2.database.Reader(db_path) as reader:
        response = reader.city(ip)
        return {
            "country": response.country.name,
            "city": response.city.name
        }

def parse_nginx_log(log_file_path, db_path):
    data = []
    with open(log_file_path, 'r') as file:
        for line in file:
            regex_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] ".*?" (\d+) \d+ ".*?" "(.*?)"'
            match = re.search(regex_pattern, line)
            if match:
                ip, time_local, status, user_agent = match.groups()
                geo_data = get_geolocation(ip, db_path)

                data.append({
                    "ip": ip,
                    "time": time_local,
                    "status": status,
                    "user_agent": user_agent,
                    "city": geo_data["city"],
                    "country": geo_data["country"]
                })

    return data[:50]

# Example usage
log_file_path = '/var/log/nginx/access.log'  # Update this path
db_path = os.path.expanduser('~/apps/scanner/GeoLite2-City.mmdb')  # Update this path
parsed_logs = parse_nginx_log(log_file_path, db_path)
