from flask import Flask, json, request
import logging
from datetime import datetime

app = Flask(__name__)

## Format Logs
# create logger with 'spam_application'
logger = logging.getLogger('keg.by')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('app.log', mode='w')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s : %(message)s @[%(asctime)s]', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)


def call_log(s):
    # date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logger.debug(' "%s" endpoint was reached', s)
    return

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}, indent=4),
            status=200,
            mimetype='application/json'
    )
    ## log line
    call_log(str(request.url_rule))

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}, indent=4),
            status=200,
            mimetype='application/json'
    )
    ## log line
    call_log(str(request.url_rule))

    return response

@app.route("/")
def hello():
    ## log line
    call_log(str(request.url_rule))
    
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)