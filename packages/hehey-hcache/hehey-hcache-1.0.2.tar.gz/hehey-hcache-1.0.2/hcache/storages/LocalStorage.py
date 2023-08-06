
from ..CacheManager import Storage
from ..utils.CacheUtil import CacheUtil;
from cacheout import memoization,Cache
from cacheout.cache import Cache
from cacheout.fifo import FIFOCache
from cacheout.lfu import LFUCache
from cacheout.lifo import LIFOCache
from cacheout.lru import LRUCache
from cacheout.mru import MRUCache
from cacheout.rr import RRCache

"""
 * 本地缓存存储器
 *<B>说明：</B>
 *<pre>
 *  缓存器使用cacheout 模块
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
class LocalStorage(Storage):

    def __init__(self, **attrs):

        # cacheout 缓存对象
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self._cache = None;

        # cacheout cache 配置
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.options = {};

        super().__init__(**attrs)

        return ;


    # 获取缓存文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getCache(self)->'Cache':

        if self._cache:
            return self._cache

        opts = self.options.copy();
        mode = opts.get("mode")
        opts.pop("mode")
        if mode == 'fifo':
            cache = FIFOCache(**opts)
        elif mode == 'lifo':
            cache = LIFOCache(**opts)
        elif mode == 'lfu':
            cache = LFUCache(**opts)
        elif mode == 'lru':
            cache = LRUCache(**opts)
        elif mode == 'mru':
            cache = MRUCache(**opts)
        elif mode == 'rr':
            cache = RRCache(**opts)

        self._cache = cache

        return self._cache;


    # 存储对象set 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def setInternal(self, key, value, **options):

        cache = self.getCache();
        expire = options.get('expire', self.expire)
        cache.set(key,value,expire)

        return ;

    # 存储对象get 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getInternal(self, key):

        cache = self.getCache();

        return cache.get(key);

    # 存储对象delete 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, key):

        cache = self.getCache();
        result = cache.delete(key)

        return result;

    def exists(self,key):

        cache = self.getCache();
        result = cache.has(key)

        if result:
            return True
        else:
            return False


    def mget(self,keys, *args):

        keysList = CacheUtil.list_or_args(keys,args)
        fullKeys = self.buildKeys(keysList);
        cache = self.getCache();
        redisValues = cache.get_many(fullKeys);

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
        cache = self.getCache();
        cache.set_many(values,expire)

        return ;



