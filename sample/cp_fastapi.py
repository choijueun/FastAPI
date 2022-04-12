from cmath import log
import uvicorn
from fastapi import FastAPI, File, UploadFile, Form
from typing import List
from datetime import datetime
from elasticsearch import helpers, Elasticsearch
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime

from multiprocessing import Process, Queue, Manager

######################################################################
# ElasticSearch
######################################################################
ES_HOST = '{}'.format('localhost')
ES_PORT = 9200
ES_USER = 'elastic'
ES_PASS = 'changeme'
es = Elasticsearch(host=ES_HOST, port=ES_PORT, http_auth=(ES_USER, ES_PASS), timeout=30)

app = FastAPI(docs_url=None)

@app.post("/cp_update")
def cp_update(data: dict):
    cp_list = data['data']
    
    if cp_list == None or cp_list == '' or len(cp_list) == 0:
        return
    
    try:
        for data in cp_list:
            code = data.get('code', None)
            name = data.get('name', None)
            team_codes = data.get('team_codes', None)
            type = isinstance(code, int)
            
            if code == None or name == None or team_codes == None or not type:
                return
            
            doc = {'code': code,'name': name,'team_codes': team_codes}
            res = es.index(index="es_test", document=doc)
    except:
        return


if __name__ == "__main__":
    uvicorn.run("cp_fastapi:app", host="0.0.0.0", port=50003, debug=True)
