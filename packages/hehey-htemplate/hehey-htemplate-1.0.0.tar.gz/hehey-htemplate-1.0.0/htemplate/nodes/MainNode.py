from .BaseNode import BaseNode

"""
 * 主节点
 *<B>说明：</B>
 *<pre>
 *  用于节点解析入口，与TemplateCompiler 对象直接对接
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
class MainNode(BaseNode):

    def __init__(self,body,attrs = {}):

        super().__init__(body,attrs)

        self.startNode = self;

    def start(self):
        funcNode = self.makeFuncNode(self.body)
        self.body = ''
        self.writeFunc('fetch', funcNode);

        pass
