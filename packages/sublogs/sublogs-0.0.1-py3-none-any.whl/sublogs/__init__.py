import socket
from enum import Enum
import datetime
from threading import Thread
import asyncio


class Sublogconfig():
    """

    userName: 用户名
    projectName：项目名称
    isJsonSerialize：是否进行json序列化，默认是标签模式
    dbtype：存入数据库类型，0es，1mongodb
    targetDB：数据库库链接 []里面放链接字符串
    env：环境
    ip: 操作者ip
    """
    projectName = "undefine"
    dbtype = 0
    targetDB = []
    env = "develop"
    ip = "127.0.0.1"

    @staticmethod
    def addConfig(config):
        if "projectName" in config:
            Sublogconfig.projectName = config["projectName"]
        if "dbtype" in config:
            Sublogconfig.dbtype = config["dbtype"]
        if "targetDB" in config:
            Sublogconfig.targetDB = config["targetDB"]
        if "env" in config:
            Sublogconfig.env = config["env"]
        # 获取本机IP
        ip = "127.0.0.1"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        Sublogconfig.ip = ip


class LogLevel(Enum):
    """
    枚举错误类型
    """
    INFO = 1,
    WARNING = 2,
    ERROR = 3,
    CRITICAL = 4,
    DEBUG = 5

    @staticmethod
    def getEnumName(logLevel):
        if LogLevel.WARNING == logLevel:
            return "WARNING"
        elif LogLevel.ERROR == logLevel:
            return "ERROR"
        elif LogLevel.CRITICAL == logLevel:
            return "CRITICAL"
        elif LogLevel.DEBUG == logLevel:
            return "DEBUG"
        else:
            return "INFO"


class SubLogger():
    """
    初始化log服务
    """

    def __init__(self):
        """
        projectName:项目名称，用于区分文件夹
        dbtype：存入数据库类型，0es，1mongodb
        targetDB：数据库库链接 {host:"",port:""}
        """
        self.datas = []

    """
   记录日志
   module:模块 用于区分日志的模块
   category:大分类 用于区分日志
   sub_category:小分类 用于区分日志
   msg:日志内容
   extra:扩展信息
    """

    async def info(self,
                   username='',
                   module='',
                   category='',
                   sub_category='',
                   msg=None,
                   extra=None):
        await self.log(username=username,
                       module=module,
                       category=category,
                       sub_category=sub_category,
                       msg=msg,
                       extra=extra,
                       logLevel=LogLevel.INFO)

    """
    warning
    """
    async def warning(self,
                      username='',
                      module='',
                      category='',
                      sub_category='',
                      msg=None,
                      extra=None):
        await self.log(username=username,
                       module=module,
                       category=category,
                       sub_category=sub_category,
                       msg=msg,
                       extra=extra,
                       logLevel=LogLevel.WARNING)

    """
    error
    """
    async def error(self,
                    username='',
                    module='',
                    category='',
                    sub_category='',
                    msg=None,
                    extra=None):
        await self.log(username=username,
                       module=module,
                       category=category,
                       sub_category=sub_category,
                       msg=msg,
                       extra=extra,
                       logLevel=LogLevel.ERROR)

    """
    critical
    """
    async def critical(self,
                       username='',
                       module='',
                       category='',
                       sub_category='',
                       msg=None,
                       extra=None, ):

        await self.log(username=username,
                       module=module,
                       category=category,
                       sub_category=sub_category,
                       msg=msg,
                       extra=extra,
                       logLevel=LogLevel.CRITICAL)

    """
    debug
    """
    async def debug(self,
                    username='',
                    module='',
                    category='',
                    sub_category='',
                    msg=None,
                    extra=None):

        await self.log(username=username,
                       module=module,
                       category=category,
                       sub_category=sub_category,
                       msg=msg,
                       extra=extra,
                       logLevel=LogLevel.DEBUG)

    async def log(self,
                  username='',
                  module='',
                  category='',
                  sub_category='',
                  msg=None,
                  extra=None,
                  logLevel=LogLevel.ERROR):
        self.datas.append({
            "username": username,
            "addtime": datetime.datetime.now(),
            "logLevel": LogLevel.getEnumName(logLevel),
            "module": module,
            "category": category,
            "sub_category": sub_category,
            "msg": msg,
            "extra": extra,
            "ip": Sublogconfig.ip,
            "project": Sublogconfig.projectName,
            "env": Sublogconfig.env,
        })
    def __del__(self):
        run_loop_thread = Thread(target=insertTodbByThread,args=(self.datas,))
        run_loop_thread.start()

async def insertToDB(datas):
    if datas:
        import sublogs.mongoHandler as mongoHandler
        await mongoHandler.addlogstoDB(datas)

def insertTodbByThread(datas):
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass
    asyncio.run(insertToDB(datas))
