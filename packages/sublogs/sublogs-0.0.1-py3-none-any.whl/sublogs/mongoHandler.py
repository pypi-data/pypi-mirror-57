import motor.motor_asyncio
from sublogs import Sublogconfig

async def addlogstoDB(data=[]):
    if not data:
        return
    dataBaseName = 'sublogs'
    collectName = f'{Sublogconfig.projectName}_{Sublogconfig.env}'

    assert len(Sublogconfig.targetDB) > 0
    config = Sublogconfig.targetDB[0]

    client = motor.motor_asyncio.AsyncIOMotorClient(config)
    db = client[dataBaseName]    #库名
    collection = db[collectName]  #表名

    await collection.insert_many(data)
