from sqlalchemy import create_engine, text
import os

db_connection_string = "mysql+pymysql://j9cthms5usjp7m6qv04l:pscale_pw_QdBK9whUeczEJWwMJk4wLPQNzdIsJN0DcRQsviBVwjy@ap-south.connect.psdb.cloud/joviancareers?charset=utf8mb4"

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
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs