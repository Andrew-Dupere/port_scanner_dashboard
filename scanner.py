from flask import Flask, jsonify
#import some_log_parser_module  # hypothetical module to parse log files
from log_parser import parse_nginx_log

app = Flask(__name__)

@app.route('/metrics')
def metrics():

    data = parse_nginx_log('/var/log/nginx/access.log')
    # Parse the log file and extract the required data
    
    return jsonify(data)

if __name__ == '__main__':
    app.run()    