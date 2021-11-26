import json

# 存取配置文件

def load_config():
    fd=open('../Config/config.json','r',encoding='utf-8-sig')
    jsonobj=json.load(fd)
    return jsonobj

def save_config(jsonobj):
    fd=open('../Config/config.json','w',encoding='utf-8-sig')
    fd.truncate(0)
    fd.seek(0)
    json.dump(jsonobj,fd)

# 存取属性

def load_attr(attribute):
    jsonobj=load_config()
    return jsonobj[0][attribute]

def save_attr(attribute,value):
    jsonobj=load_config()
    jsonobj[0][attribute]=value
    save_config(jsonobj)