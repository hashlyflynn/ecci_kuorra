import web

db_host = 'bfjrxdpxrza9qllq.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'h1kc7hdqez5ycwe8'
db_user = 'gbtqgw92wg5jlsgr'
db_pw = '	z1urnujodv62xscl'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )