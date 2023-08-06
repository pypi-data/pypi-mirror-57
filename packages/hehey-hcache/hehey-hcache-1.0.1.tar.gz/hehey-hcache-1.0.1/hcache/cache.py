# -*- coding: utf-8 -*-

from .utils.CacheUtil import CacheUtil;

import json

"""
 * 缓存管理器
 *<B>说明：</B>
 *<pre>
 *  略
 *</pre>
 *<B>示例：</B>
 *<pre>
'cache': {
            'clazz': 'hcache.CacheManager.CacheManager',
            'keyPrefix': "yi",
            'defautlStorage':'redis',
            'customStorages': {
                'redis': {
                    'clazz': 'hcache.storages.RedisStorage.RedisStorage',
                    'red': {'host': '127.0.0.1', 'port': 6379, 'db': 1, 'password': ""}
                }
            },
 },
 
  he.app.cache.mset({"username":"121","pwd":"1212"},expire=20)
  he.app.cache.set("name","hahah",expire = 20)
  he.app.cache.set("name","ok",30)
 
 
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
class CacheManager:


    def __init__(self,**attrs):

        # key 前缀
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.keyPrefix = '';

        # 序列化方式
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.serializer = '';

        # 默认存储器
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.defaultStorage = '';

        # 定义存储器
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.customStorages = {};


        # 存储器对象列表
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.storages = {};
        if attrs:
            CacheUtil.setAttrs(self,attrs)

        return ;


    def makeStorage(self,storageType,options = {}):

        clazz = options.get('clazz', storageType)

        if not clazz:
            raise Exception('the {0} storage conf no find clazz'.format(storageType))

        if clazz.find('.') == -1:
            clazzName = CacheUtil.ucfirst(clazz) + 'Storage'
            clazz = __package__ + '.storages.' + clazzName + '.' + clazzName


        storageMeta = CacheUtil.getClassMeta(clazz)

        return storageMeta(**options);


    def getStorage(self,storageType = '')->'Storage':

        if not storageType:
            storageType = self.defaultStorage;

        storage = self.storages.get(storageType, None)

        if storage:
            return storage

        storageConf = self.customStorages.get(storageType, None)
        if storageConf is None:
            raise Exception('the {0} storage conf no find'.format(storageType))

        storageConf['keyPrefix'] = storageConf.get('keyPrefix',self.keyPrefix)
        storageConf['serializer'] = storageConf.get('serializer', self.serializer)

        storage = self.makeStorage(storageType, storageConf);
        self.storages[storageType] = storage

        return storage;

    # 设置cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def set(self,key,data,**options):

        storage = self.getStorage();
        storage.set(key,data,**options);

        return storage;

    # 返回指定key cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def get(self,key):

        storage = self.getStorage();

        return storage.get(key);

    # 批量返回指定的keys cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def mget(self, keys, *args):

        storage = self.getStorage();

        return storage.mget(keys,*args)

    # 批量设置cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def mset(self, items,**options):

        storage = self.getStorage();
        storage.mset(items, **options);

        return storage;



    # 判断key 是否存在
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def exists(self,key):

        storage = self.getStorage();

        return storage.exists(key)


    def __getattr__(self, storageType):


        return self.getStorage(storageType)


class Storage:

    def __init__(self, **attrs):

        # key 前缀
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.keyPrefix = '';

        # 序列化方式
        # <B> 说明： </B>
        # <pre>
        # 略
        # </pre>
        self.serializer = [];

        # 有效期
        # <B> 说明： </B>
        # <pre>
        # 单位秒,
        # </pre>
        self.expire = 0;

        if attrs:
            CacheUtil.setAttrs(self, attrs)

        return ;

    # 构建完整key
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def buildKey(self,key):

        return self.keyPrefix + key;

    def buildKeys(self,keys):

        keylist = [];
        for key in keys:
            keylist.append(self.buildKey(key))

        return keylist

    def formatItemsKey(self,items = {}):

        values = {};
        for key,data in items.items():
            fullKey = self.buildKey(key)
            values[fullKey] = self.doSerializer(data);

        return values


    # 序列化数据
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def doSerializer(self,data):

        if self.serializer:
            if isinstance(self.serializer[0],str):
                serializerMeta = CacheUtil.getClassMeta(self.serializer[0]);
            else:
                serializerMeta =  self.serializer[0]

            value = serializerMeta(data);
        else:
            value = json.dumps(data)

        return value;

    # 反序列化数据
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def unSerializer(self,data):

        if data is None:
            return data

        if self.serializer:
            if isinstance(self.serializer[1], str):
                serializerMeta = CacheUtil.getClassMeta(self.serializer[1]);
            else:
                serializerMeta = self.serializer[1]

            value = serializerMeta(data);
        else:
            value = json.loads(data)

        return value;

    def batchDoSerializer(self,items = {}):
        values = {};
        for key,value in items.items():
            values[key] = self.doSerializer(value)

        return values

    def batchUnSerializer(self,values = {}):

        items = {};
        for key, value in values.items():
            items[key] = self.unSerializer(value)

        return items



    # 设置cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def set(self,key,data,**options):

        fullKey = self.buildKey(key)

        self.setInternal(fullKey,self.doSerializer(data),**options)

        return ;

    # 批量设置cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def mset(self,items = {},**options):

        for key,data in items.items():
            fullKey = self.buildKey(key)
            self.setInternal(fullKey, self.doSerializer(data), **options)

        return ;

    # 返回指定key cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def get(self,key):

        fullKey = self.buildKey(key)
        value = self.getInternal(fullKey)

        return self.unSerializer(value);

    # 批量返回指定的keys cache
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def mget(self,keys, *args):

        keysList = CacheUtil.list_or_args(keys, args)

        values = {};
        for key in keysList:
            fullKey = self.buildKey(key)
            value =  self.getInternal(fullKey) ;
            values[key] = self.unSerializer(value)

        return values

    # 删除指定key
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def delete(self,key):

        fullKey = self.buildKey(key)

        return self.deleteInternal(fullKey)

    # 判断key 是否存在
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def exists(self,key):

        fullKey = self.buildKey(key)
        value = self.getInternal(fullKey);
        if value is None or value is False:
            return False
        else:
            return True

    # 存储对象set 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def setInternal(self,key,value,**options):

        return ;

    # 存储对象get 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def getInternal(self,key):

        return;

    # 存储对象delete 接口
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    def deleteInternal(self, key):

        return;







