import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Sarkar123:GAUTAMMISHRA@sarkar.1uiwqkd.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Sarkar123")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "adrinolinks.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "88b906bad8fd83373047b4f777048d286e05d55e")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/DevelopperRadha_Zone/10") # shareus ka tut_vid he 
