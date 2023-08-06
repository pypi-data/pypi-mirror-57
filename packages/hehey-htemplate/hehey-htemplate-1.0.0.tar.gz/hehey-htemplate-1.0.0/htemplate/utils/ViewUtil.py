
import importlib,re,os

class ViewUtil:

    # 获取类或对象的自定义属性
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def setAttrs(cls, object, attrDict={}):
        for attr in attrDict:
            setattr(object, attr, attrDict[attr])

    @classmethod
    def ucfirst(self, str):

        return str[0].upper() + str[1:]

    # 获取上一级目录
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def dirname(cls, clazz):

        packageClass = clazz.rsplit('.', 1)

        return packageClass[0];

    # 获取类或对象的自定义属性
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def getModuleMeta(cls, clazz):
        if type(clazz) == str:
            packageClass = clazz.rsplit('.', 1)
            try:
                packageMeta = importlib.import_module(packageClass[0])
            except Exception as e:
                raise e
                pass
            return getattr(packageMeta, packageClass[1])
        else:
            return clazz

    # 获取指定文件的扩展名
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def getFileExt(self,filename):

        filelist = os.path.splitext(filename)
        ext = filelist[len(filelist) - 1]
        if ext:
            ext = ext[1:]

        return ext

    # 获取类或对象的自定义属性
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def getFuncMeta(cls, func):
        if type(func) == str:
            packageFunc = func.rsplit('.', 1)
            try:
                packageMeta = importlib.import_module(packageFunc[0])
            except Exception as e:
                raise e
                pass
            return getattr(packageMeta, packageFunc[1])
        else:
            return func

    # 统计左边空格数量
    # <B> 说明： </B>
    # <pre>
    # 略
    # </pre>
    @classmethod
    def countlstrip(cls,chars):

        reg = '^(\s*)\w+'
        result = re.match(reg,chars)
        if result:
            count = result.group(1).count(' ')
            return count
        else:
            return False


