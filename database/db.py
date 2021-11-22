# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from configurations import app_config, app_active

config = app_config[app_active]

def connect_database():
    try:
        engine = create_engine('postgresql://'+config.USER+':'+config.PASS+'@'+config.IP+':'+config.PORT+'/'+config.DATABASE)
        dbConnection = engine.connect()
        return dbConnection
    except:
        print("Não foi possível conectar ao banco de dados.")
        return None