
from ..CacheManager import Storage

from ..utils.CacheUtil import CacheUtil;
import os,time;

"""
 * 文件缓存存储器
 *<B>说明：</B>
 *<pre>
 *  每个cache key 自动生成一个缓存文件
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
class FileStorage(Storage):

    def __init__(self, **attrs):

        # 缓存的文件路径
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.cachePath = '';

        # 目录的层级
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.dirLevel = 5;

        # 缓存文件后缀
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.cacheFileSuffix = 'bin'

        super().__init__(**attrs)

        self._init();

    # 初始化
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def _init(self):


        return ;

    # 获取缓存文件
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getCacheFile(self,key):

        filepath = self.buildCacheFile(key);

        return filepath;

    # 检测缓存文件是否有效
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def checkCacheFile(self,key):

        filepath = self.buildCacheFile(key);
        # 判断有效期
        if not os.path.exists(filepath):
            return filepath

        st_mtime = os.stat(filepath).st_mtime
        nowTime = int(time.time())
        if st_mtime > nowTime:
            return True
        else:
            return False

    # 构建缓存文件路径
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def buildCacheFile(self,key,automkdir = False):

        filepath = '';
        if self.dirLevel > 0:
            filedir = self.cachePath;
            for index in range(self.dirLevel):
                try :
                    i = (index + index)
                    prefix = key[i::2]
                    filedir = '{0}/{1}'.format(filedir,prefix)
                except Exception as e:
                    break
            filepath = '{0}{1}.{2}'.format(filedir, key, self.cacheFileSuffix)
        else:
            filepath = '{0}/{1}.{2}'.format(self.cachePath,key,self.cacheFileSuffix)

        dir = os.path.dirname(filepath)
        if automkdir and not os.path.exists(dir):
            os.makedirs(dir);

        return filepath;



    # 存储对象set 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def setInternal(self, key, value, **options):

        cacheFilepath = self.buildCacheFile(key,True);
        with open(cacheFilepath, 'w') as f:
            f.write(value)

        # 设置文件最后更新时间,用于验证其有效期
        expire = options.get('expire', self.expire)
        if expire <= 0:
            expire = 31536000 # 如果未设置有效期,默认是1年
        nowTime = int(time.time());
        st_mtime = nowTime + expire

        os.utime(cacheFilepath,(nowTime,st_mtime))

        return ;

    # 存储对象get 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getInternal(self, key):

        if not self.checkCacheFile(key):
            return None;

        cacheFilepath = self.buildCacheFile(key);
        data = '';
        with open(cacheFilepath, 'r') as f:
            data = f.read()

        return data;

    # 存储对象delete 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, key):

        cacheFilepath = self.buildCacheFile(key);
        if os.path.exists(cacheFilepath):
            os.remove(cacheFilepath)

        return True;

    def exists(self,key):

        fullKey = self.buildKey(key)

        if self.checkCacheFile(fullKey):
            return True
        else:
            return False;


    def mget(self,keys, *args):

        keysList = CacheUtil.list_or_args(keys,args)
        fullKeys = self.buildKeys(keysList);
        fileValues = [];
        for key in fullKeys:
            value = self.getInternal(key)
            fileValues.append(value)

        if not fileValues:
            return {};
        items = {};
        for i in range(len(fullKeys)):
            value = fileValues[i];
            key = keysList[i];
            items[key] = value

        return self.batchUnSerializer(items);


    def mset(self,items = {},**options):

        values = self.formatItemsKey(items);
        for key,value in values.items():
            self.setInternal(key,value,**options)







