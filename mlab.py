import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds259119.mlab.com:59119/chung

host = "ds259119.mlab.com"
port = 59119
db_name = "chung"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
