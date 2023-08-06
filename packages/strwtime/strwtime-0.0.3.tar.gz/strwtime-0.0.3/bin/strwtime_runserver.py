#!/usr/bin/env python

import strwtime.core as swtime
from wsgiref.simple_server import make_server
import os

if "PORT" in os.environ:
    port = int(os.environ["PORT"])
else:
    port = 8000
httpd = make_server('', port, swtime.app)
httpd.serve_forever()
