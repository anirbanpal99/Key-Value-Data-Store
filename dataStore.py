#Python version: 3.6.8
import sys
import time
import threading
from threading import *
import json

data = {}
def create(key, value, ttl=3600):
    if key in data:
        print("Keyerror: Duplicate key error!\n")
    else:
       if(key.isalnum()):
           if sys.getsizeof(data) <= 1073741824: #1GB = 1073741824 Bytes
               if len(key) < 32:
                   try:
                       Val = json.loads(value)
                       if sys.getsizeof(Val) <= (16*1024):
                           data[key] = [Val, int(time.time())+ttl]
                           print("Data created successfully\n")
                       else:
                           print("Memoryerror: Memory limit error! Maximum value size is 16 KB\n")
                   except:
                       print("Typeerror: Value should be in JSON format\n")
               else:
                   print("Memoryerror: Memory limit exceeded! Max key length should be 32\n")
           else:
               print("Memoryerror: Memory limit exceeded! Data limit is 1GB\n")
       else:
           print("Typeerror: Key type error! Only string is allowed\n")

def read(key):
    if key not in data:
        print("Keyerror: Given key "+key+" is not present in database\n")
    else:
        if int(time.time()) < data[key][1]:
            return data[key][0]
        else:
            print("TTLError: Time-to-live time has expired\n")

def delete(key):
    if key not in data:
        print("Keyerror: Given key "+key+" is not present in database\n")
    else:
        if int(time.time()) < data[key][1]:
            del data[key]
            print(key+" successfully deleted\n")
        else:
            print("TTLError: Time-to-live time has expired\n")
            
if __name__ == "__main__":
    t1 = threading.Thread(target=create, args=("Player1", '{"name":"Sachin Tendulkar", "age":42}'))
    t2 = threading.Thread(target=create, args=("Player2", '{"name":"Sourav Ganguly", "age":41}',0))
    t3 = threading.Thread(target=create, args=("Player3", '{"name":"Yuvraj Singh", "age":39}'))
    t4 = threading.Thread(target=create, args=("Player2", '{"name":"Virat Kholi", "age":33}'))
    t5 = threading.Thread(target=create, args=("wuaihviuasdhviuashiuvhasiufdvusaiduvbiuasdbviuasbviubsauvbsiuabviusabvubsavsaveabsea", '{"name":"M. S. Dhoni", "age":38}'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print("Successfully entered all the details\n")
    print("Your Final Database:\n")
    print(data)
