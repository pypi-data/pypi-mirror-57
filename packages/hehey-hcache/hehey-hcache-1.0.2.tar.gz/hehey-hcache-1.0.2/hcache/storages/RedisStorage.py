
from ..CacheManager import Storage

from redis import Redis
import redis.exceptions
from ..utils.CacheUtil import CacheUtil;

"""
 * redis 缓存存储器
 *<B>说明：</B>
 *<pre>
 *  略
 *</pre>
 *<B>示例：</B>
 *<pre>
 * 略
 *</pre>
 *<B>日志：</B>
 *<pre>
 *  略
 *</pre>
 *<B>注意事项：</B>
 *<pre>
 *  略
 *</pre>
"""
class RedisStorage(Storage):

    def __init__(self, **attrs):

        self.red = None;

        super().__init__(**attrs)

    # 连接redis 服务
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def connect(self):

        if isinstance(self.red, dict):
            self.red = Redis(**self.red)

        return self.red

    # 获取连接
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getConnection(self) -> 'Redis':

        return self.connect()

    # 存储对象set 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def setInternal(self, key, value, **options):

        redisconnect = self.getConnection()
        expire = options.get('expire',self.expire)

        if expire:
            redisconnect.setex(key, expire,value)
        else:
            redisconnect.set(key, value)

        return ;

    # 存储对象get 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getInternal(self, key):

        value = self.getConnection().get(key);

        if value:
            value = value.decode();

        return value;

    # 存储对象delete 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, key):

        result = self.getConnection().delete(key)

        return result;

    def exists(self,key):

        fullKey = self.buildKey(key)
        result = self.getConnection().exists(fullKey)

        if result == 1:
            return True
        else:
            return False


    def mget(self,keys, *args):

        keysList = CacheUtil.list_or_args(keys,args)
        fullKeys = self.buildKeys(keysList);
        redisValues = self.getConnection().mget(fullKeys);

        if not redisValues:
            return {};
        items = {};
        for i in range(len(fullKeys)):
            value = redisValues[i];
            if value:
                value = value.decode();
            key = keysList[i];
            items[key] = value

        return self.batchUnSerializer(items);


    def mset(self,items = {},**options):

        values = self.formatItemsKey(items);
        expire = options.get('expire', self.expire)
        redisconnect = self.getConnection()

        if expire:
            try:
                redisconnect.mset(values)
                pipe = redisconnect.pipeline()
                pipe.multi()
                for key in values.keys():
                     pipe.expire(key, expire)
                result = pipe.execute()
            except redis.exceptions.WatchError as e:
                raise e

        else:
            redisconnect.mset(values)

        return ;



