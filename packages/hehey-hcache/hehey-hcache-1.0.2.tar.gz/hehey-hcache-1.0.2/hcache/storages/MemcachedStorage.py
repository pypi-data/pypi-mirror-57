
from ..CacheManager import Storage

import memcache

from ..utils.CacheUtil import CacheUtil;

"""
 * memcached 缓存存储器
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
class MemcachedStorage(Storage):

    def __init__(self, **attrs):

        self.mc = None;

        super().__init__(**attrs)

    # 连接redis 服务
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def connect(self):

        if isinstance(self.mc, dict):
            self.mc = memcache.Client(**self.mc,debug=True)

        return self.mc

    # 获取连接
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getConnection(self) -> 'memcache.Client':

        return self.connect()

    # 存储对象set 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def setInternal(self, key, value, **options):

        mcconnect = self.getConnection()
        expire = options.get('expire',self.expire)
        result = mcconnect.set(key, value,expire)

        return ;

    # 存储对象get 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getInternal(self, key):

        mcconnect = self.getConnection()
        value = mcconnect.get(key)

        return value;

    # 存储对象delete 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, key):

        result = self.getConnection().delete(key)

        return result;


    def mget(self,keys, *args):

        keysList = CacheUtil.list_or_args(keys,args)
        mcValues = self.getConnection().get_multi(keysList,self.keyPrefix);

        if not mcValues:
            return {};
        else:
            return self.batchUnSerializer(mcValues);


    def mset(self,items = {},**options):

        items = self.batchDoSerializer(items);
        expire = options.get('expire', self.expire)
        mcconnect = self.getConnection()
        mcconnect.set_multi(items,expire,self.keyPrefix)

        return ;



