#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importanciones
import json
from argparse import ArgumentParser
import requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId

#conexion con mongodb
client = MongoClient("mongodb://localhost:27017")
try:
    client.admin.command("ismaster")
    print("MongoDB connection: Success")
except ConnectionFailure as cf:
    print("MongoDB connection: Failed", cf)

DBcompass = ["JuegosOlimpicosMongo"]

#coneccion con mongodb atlas
client1 = MongoClient("mongodb+srv://usuario1:usuario1@cluster0.snkvt.mongodb.net/test")
try:
    client1.admin.command("ismaster")
    print("MongoDB Atlas connection: Success")
except ConnectionFailure as cf:
    print("MongoDB Atlas connection: Failed", cf)

DBatlas = client1.get_database("juegosOlimpicos_Atlas")
db_one = DBatlas.collection1


#funcion para traspasar los datos de mongodb atlas
for db in DBcompass:
    if db not in ('admin', 'local','config'):  
        cols = client[db].list_collection_names()  
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in client[db][col].find():  
                try:
                    documents=json.loads(json_util.dumps(x))
                    documents["_id"]=str(documents["_id"])
                    print(documents)
                    db_one.insert_one(documents)
                except TypeError as t:

                    print('current document raised error: {}'.format(t))
                    SKIPPED.append(x)  
                    continue    
                except Exception as e:
                    raise e


# In[ ]:





# In[ ]:




