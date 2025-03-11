import os, sys

# edit your path below
sys.path.append("/home/amogus22877769.heliohost.us/httpdocs/flasktest");

sys.path.insert(0, os.path.dirname(__file__))
from myapp import app as application

# set this to something harder to guess
application.secret_key = 'secret'