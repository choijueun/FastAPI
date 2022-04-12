import os.path
import configparser
import subprocess, json
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import models

def main():
    NMS_HOME = '/Users/Shared/SynologyDrive/Practice'
    # NMS_HOME = os.getenv("INSGEN_NMS_HOME")
    if NMS_HOME is None:
        return

    config_file = os.path.join(NMS_HOME, "conf", "nms.ini")
    if os.path.exists(config_file) is False:
        return

    conf = configparser.ConfigParser()
    conf.read(config_file)

    if not conf.has_option("NMS", "NMS_HOME"):
        return

    DATABASE_URI = conf.get("NMS", "DATABASE_URI")
    
    engine = create_engine(DATABASE_URI)
    session = None
    try:
        session = Session(bind=engine)
        session.connection()
    except:
        return

    result = session.query(models.CmSkGroupTb).all()
    send_data = list()
    for r in result:
        send_data.append({
            'code': r.code,
            'name': r.name,
            'team_codes': r.team_codes,
        })
    params = {'data': send_data}
    create_cmd = 'curl -i -X "POST" -H "Content-Type: application/json; charset=utf-8;" -d \'{0}\' http://121.254.27.171:50003/cp_update'.format(json.dumps(params, ensure_ascii=False))
    proc = subprocess.Popen(create_cmd, stdout=subprocess.PIPE, shell=True)
    out, err = proc.communicate()
    session.close()

# if __name__ == "__main__":
main()