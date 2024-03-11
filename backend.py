from config import Config
from db import database
import random,threading,asyncio
from pyrogram import Client

DB = database()
api_id = Config.APP_ID
api_hash = Config.API_HASH
class app :
    async def ADDuser(slef,GrobUser,inGRob,id,bot):
        list = DB.accounts()
        random.shuffle(list)
        numberMin = 40
        inGRob = inGRob.split("/")[3]
        for name in list :
            num = 0          
            for user in GrobUser:      
                try:
                    num +=1
                    GrobUser.remove(user)
                    async with Client("::memory::", api_id, api_hash,no_updates=True,in_memory=True,lang_code="ar",session_string=name) as app:
                        await asyncio.sleep(10)
                        try:
                            print(user)            
                            await app.add_chat_members(inGRob, user)                    
                        except Exception as e:
                            print(e)
                            if "FLOOD_WAIT_X" in str(e):
                                break
                            pass
                    if num== numberMin :
                        break
                except:
                    pass          
    async def GETuser(slef,GrobUser,Ingrob):
        if 0 == 0:  
            list = DB.accounts()
            random.shuffle(list)
            GrobUser = GrobUser.split("/")[3]
            print(3)   
            Ingrob = Ingrob.split("/")[3]       
            name = str("".join(random.choice(list)for i in range(1)))
            administrators = []
            async with Client("::memory::", api_id, api_hash,no_updates=True,in_memory=True,lang_code="ar",session_string=name) as app:      
                await app.join_chat(Ingrob)
                async for m in app.get_chat_members(GrobUser):
                    try:
                        if m.user.username != None :
                           administrators.append(m.user.username)
                    except:
                        print("rrrrrr")
                        pass
            threading.current_thread().return_value = administrators	
            print(administrators)
            return administrators
        # except Exception as e:
        #     print(e)

       

# list = T.return_value

