#!/usr/bin/env python

# Use connector directly
import connector
import os

os.environ.setdefault('CLICKHOUSE_USE_TIMEZONE','Asia/Chongqing')

# cursor = connector.connect('default', db_url='http://default:borui2020@localhost:8123/default').cursor()

cursor.execute('SELECT NOW()')
print(cursor.fetchone())
print('-------------------------------')

cursor = connector.connect('default').cursor()
cursor.execute('SELECT * FROM test LIMIT 10')
print(cursor.fetchone())

# Register SQLAlchemy dialect
from sqlalchemy.dialects import registry
registry.register("clickhouse", "base", "dialect")

# Test engine and table 
from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *

engine = create_engine('clickhouse://default:@localhost:8123/default')
logs = Table('test', MetaData(bind=engine), autoload=True)
print(select([func.count('*')], from_obj=logs).scalar())
