#!/usr/bin/python3

import os
import json
import psycopg2
import hdfs

from sqlalchemy import create_engine

def config(param):
    path = os.getcwd()
    with open(path+'/'+'config.json') as file:
        conf = json.load(file)[param]
    return conf

def psql_conn(conf):
    try:
        conn = psycopg2.connect(host=conf['host'], 
                                database=conf['db'], 
                                user=conf['user'], 
                                password=conf['pwd']
                                )
        print(f"[INFO] Success connect PostgreSQL .....")
        engine = create_engine(f"postgresql+psycopg2://{conf['user']}:{conf['pwd']}@{conf['host']}/{conf['db']}")
        return conn, engine
    except:
        print(f"[INFO] Can't connect PostgreSQL .....")

def hadoop_conn(conf):
    client = conf['client']
    try:
        conn = hdfs.InsecureClient(client)
        print(f"[INFO] Success connect HADOOP .....")
        return conn
    except:
        print(f"[INFO] Can't connect HADOOP .....")
