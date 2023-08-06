# -*- coding: utf-8 -*-

import importlib


"""
 * 路由器帮助类
 *<B>说明：</B>
 *<pre>
 *  提供基本类操作,获取属性值,设置属性等等
 *</pre>
 *<B>示例：</B>
 *<pre>
 *  略
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
class CacheUtil:


    # 获取类或对象的自定义属性
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def setAttrs(cls,object,attrDict = {}):
        for attr in attrDict:
            setattr(object, attr, attrDict[attr])


    # 获取类或对象的自定义属性
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def getClassMeta(cls,clazz):
        if type(clazz) == str:
            packageClass = clazz.rsplit('.', 1)
            packageMeta = importlib.import_module(packageClass[0])
            return  getattr(packageMeta, packageClass[1])
        else:
            return clazz


    # 首字母大写
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def ucfirst(cls,str):

        return str[0].upper() + str[1:]

    @classmethod
    def list_or_args(cls,keys, args):
        # returns a single new list combining keys and args
        try:
            iter(keys)
            # a string or bytes instance can be iterated, but indicates
            # keys wasn't passed as a list
            if isinstance(keys, (str, bytes)):
                keys = [keys]
            else:
                keys = list(keys)
        except TypeError:
            keys = [keys]
        if args:
            keys.extend(args)
        return keys



