#!/usr/bin/env python

import strwtime.core as swtime
from wsgiref.simple_server import make_server

httpd = make_server('', 8000, swtime.app)
httpd.serve_forever()
