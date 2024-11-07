from database.db import DataBase

database = DataBase()
for chid in database.get_channels_id():
    print(chid[0])
