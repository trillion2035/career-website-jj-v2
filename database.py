from sqlalchemy import create_engine

db_connection_string= "mysql+pymysql://u670e4hox9livoelznd1:pscale_pw_yLRhS2m9VTgLTqtKwAJbiFzKs8wcFKuBCZAK47vzm6X@aws.connect.psdb.cloud/careerwebsite?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
     "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
  })
