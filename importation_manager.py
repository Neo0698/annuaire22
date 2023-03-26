import sys
import time
import os
import database_com
import locale
import proposition
import datetime
import command
try:
  import requests
  
except:
  pass
try:
  from bs4 import BeautifulSoup

except:

    pass
try:
    import json
except:
    pass
try:
    import asyncio
except:
    pass
try:
    import websockets
except:
    pass
try:
    import keyboard
except:
    pass

def creat_importation_list():
    """
    """
    module_installed={"requests":False,"bs4":False,"json":False,"asyncio":False,"websockets":False,"keyboard":False,"missing":6}
   
    if "requests" in sys.modules:
        module_installed["requests"]=True
        module_installed["missing"]+=-1
    if "bs4" in sys.modules:
        module_installed["bs4"]=True
        module_installed["missing"]+=-1
    if "json" in sys.modules:
        module_installed["json"]=True
        module_installed["missing"]+=-1
    if "asyncio" in sys.modules:
        module_installed["asyncio"]=True
        module_installed["missing"]+=-1
    if "websockets" in sys.modules:
        module_installed["websockets"]=True
        module_installed["missing"]+=-1
    if "keyboard" in sys.modules:
        module_installed["keyboard"]=True
        module_installed["missing"]+=-1
    return module_installed
def install_packages(module_installed):
    for key in list(module_installed.keys()):
        if(type(key)!=int):
            if(module_installed[key]==False):
                os.system("python -m pip install "+key)
