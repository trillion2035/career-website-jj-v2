from sqlalchemy import create_engine

db_connection_string= "mysql+pymysql://2ft66lzpv5vuuuivua11:pscale_pw_HfHAwueJQsSOVsEtc463bm4SrbzJuevfnw3LjYUcDwu@aws.connect.psdb.cloud/careerwebsite?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
     "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
  })

