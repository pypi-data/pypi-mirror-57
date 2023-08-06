# hehey-hcache 组件

#### 介绍
hehey-hcache 是一个python 数据缓存工具组件

#### 依赖以及版本要求
- python >= 3.5


#### 安装
- 直接下载:
```

```
- 命令安装：
```
pip install hehey-hcache
```
#### 基础文件以目录


#### 参数配置
```python
conf = {
        'keyPrefix': "yi",
        'defaultStorage':'memcached',
        'customStorages': {
            # redis 远程存储 配置
            'redis': {
                'clazz': 'hcache.storages.RedisStorage.RedisStorage',
                'red': {'host': '127.0.0.1', 'port': 6379, 'db': 1, 'password': ""}
            },
            # file 文件配置
            'file': {
                'clazz': 'hcache.storages.FileStorage.FileStorage',
                'cachePath': '/home/hehe/www/cache',
                'dirLevel':2,
            },
            # 本地内存配置
            'local': {
                'clazz': 'hcache.storages.LocalStorage.LocalStorage',
                'options':{
                    'mode': 'lru',
                }

            },
            # memcached远程存储配置
            'memcached': {
                'clazz': 'hcache.storages.MemcachedStorage.MemcachedStorage',
                'mc': {
                    'servers': ['127.0.0.1:11211'],
                }

            }
        },
}

# 支持四种存储,redis,file,memcached,local(进程内存)
# keyPrefix: key 前缀
# defaultStorage: 默认存在类型,比如redis

```
#### 基本示例
- 快速使用
```python
from hcache.cache import CacheManager;
conf = {
        'keyPrefix': "yi",
        'defaultStorage':'memcached',
        'customStorages': {
            # redis 远程存储 配置
            'redis': {
                'clazz': 'hcache.storages.RedisStorage.RedisStorage',
                'red': {'host': '127.0.0.1', 'port': 6379, 'db': 1, 'password': ""}
            },
            # file 文件配置
            'file': {
                'clazz': 'hcache.storages.FileStorage.FileStorage',
                'cachePath': '/home/hehe/www/cache',
                'dirLevel':2,
            },
        },
}
hcache = CacheManager(conf)

# 设置缓存
hcache.set("accountInfo",{"realName":"hehe","stauts":1})
hcache.set("name","hahahxxxx",expire = 20)
# 获取缓存
hcache.get("name")
hcache.get("accountInfo")

```

- 批量设置/批量获取
```python
from hcache.cache import CacheManager;
conf = {
        'keyPrefix': "yi",
        'defaultStorage':'memcached',
        'customStorages': {
            # redis 远程存储 配置
            'redis': {
                'clazz': 'hcache.storages.RedisStorage.RedisStorage',
                'red': {'host': '127.0.0.1', 'port': 6379, 'db': 1, 'password': ""}
            },
            # file 文件配置
            'file': {
                'clazz': 'hcache.storages.FileStorage.FileStorage',
                'cachePath': '/home/hehe/www/cache',
                'dirLevel':2,
            },
        },
}

hcache = CacheManager(conf)
# 批量设置
datas = {"account":{"realName":"hehe"},"address":{"cityId":1,"userId":20}};
hcache.mset(datas,expire = 20)

# 批量获取

hcache.mget("account","address")

# 或 

hcache.mget(["account","address"])


```

- 检验key 是否存在
```python
from hcache.cache import CacheManager;
conf = {};
hcache = CacheManager(conf)
if hcache.exists("account"):
    print("yes")
else:
    print("no")

```


- 直接使用存储set/get
```python
from hcache.cache import CacheManager;
conf = {
        'keyPrefix': "yi",
        'defaultStorage':'memcached',
        'customStorages': {
            # redis 远程存储 配置
            'redis': {
                'clazz': 'hcache.storages.RedisStorage.RedisStorage',
                'red': {'host': '127.0.0.1', 'port': 6379, 'db': 1, 'password': ""}
            },
            # file 文件配置
            'file': {
                'clazz': 'hcache.storages.FileStorage.FileStorage',
                'cachePath': '/home/hehe/www/cache',
                'dirLevel':2,
            },
        },
}

hcache = CacheManager(conf)

hcache.file.set("accountInfo",{"realName":"hehe","stauts":1})
hcache.file.set("name","hahahxxxx",expire = 20)
# 获取缓存
hcache.file.get("name")
hcache.file.get("accountInfo")

```


- 装饰器注解缓存数据
```python
from hclient.client import Client;


```

