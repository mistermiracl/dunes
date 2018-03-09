from configparser import ConfigParser
from django.conf import settings
import MySQLdb

__DATABASE_CONFIG = ConfigParser()
__DATABASE_CONFIG.read('%s\\config\\config.ini' % settings.PROJECT_ROOT) #I GUESS THIS IS THE EQUIVALENT TO STATIC BLOCK / CONSTRUCTOR

def get_connection():
    return MySQLdb.connect(
        user=__DATABASE_CONFIG['DATABASE']['USER'], 
        passwd=__DATABASE_CONFIG['DATABASE']['PASSWORD'], 
        db=__DATABASE_CONFIG['DATABASE']['NAME']
    )
