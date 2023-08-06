
"""
 * 模板上下文
 *<B>说明：</B>
 *<pre>
 *  使用
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
class TemplateContext:

    def __init__(self):
        self.template = None

        self.contextList = {} # 上下文定义
        pass


    def register(self,funcName, funcMeta):

        self.contextList[funcName] = funcMeta
        pass

    def getContext(self)->'list':

        data = {};
        for funcName,funcMeta in self.contextList.items():
            data.update(funcMeta())

        return data

