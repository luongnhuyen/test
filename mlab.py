import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds119820.mlab.com:19820/muadongkhonglanh
# mongodb://<dbuser>:<dbpassword>@ds147420.mlab.com:47420/goldenwallet

host = "ds147420.mlab.com"
port = 47420
db_name = "goldenwallet"
user_name = "admin"
password = "vnds@123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
