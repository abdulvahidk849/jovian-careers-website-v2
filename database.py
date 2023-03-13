import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/certs/ca-certificates.crt"
    }
  })
def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    
    result_dicts = []
    
    for row in result.all():
      result_dicts.append(dict(zip(column_names, row)))
    return result_dicts

def load_job_from_db(id):
  value = []
  value.append(id)
  with engine.connect() as conn:
    query = "SELECT * FROM jobs WHERE id = %s"
    result = conn.execute(query,value)
    column_names = result.keys()
    result_dicts = []
    
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return result_dicts.append(dict(zip(column_names,rows[0])))
