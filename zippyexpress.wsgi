activate_this = '/var/www/zippyexpress/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/var/www/zippyexpress')
from run import app as application
