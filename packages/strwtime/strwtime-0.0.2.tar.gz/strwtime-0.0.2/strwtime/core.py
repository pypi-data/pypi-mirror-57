from datetime import datetime
from time import time
import json

def app(env, start_response):
    start_response('200 OK', [('Content-Type','application/json')])
    format = "%s"
    timestring = datetime.fromtimestamp(time()).strftime(format)
    return(json.dumps({"result": "OK", "data":{"format": format, "timestring": timestring}}))
