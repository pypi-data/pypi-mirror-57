from .Tag import Tag
from ..nodes.BaseNode import BaseNode

"""
 * html标签库
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
class HtmlTag(Tag):

    def __init__(self,template):
        super().__init__(template)
        self.tags = [
            {'name': "css", 'close': False, 'onTag': True},
            {'name': "js", 'close': False, 'onTag': True},
            {'name': "img", 'close': False, 'onTag': True},
            {'name': "select", 'close': False,'onTag':True},
        ]


# 模板继承
    def _select(self,node_attrs,mainNode:BaseNode):
        #print(node_attrs)

        #attrs = self.parseAttr(node_attrs)
        pass

    def _css(self,node_attrs, mainNode:BaseNode):
        attrs = self.parseAttr(node_attrs)
        href = attrs['href'];
        cssFunc = 'self.call("css","{0}")'.format(href)
        attrs['href'] = '%s';
        attrsHtml = self.buildHtmlAttrs(attrs);
        codeHtml = "'<link {0} />' % ({1})".format(attrsHtml, cssFunc)

        mainNode.writeRawCode(codeHtml, True, True)

    def _js(self,node_attrs, mainNode:BaseNode):
        attrs = self.parseAttr(node_attrs)
        src = attrs['src'];
        jsFunc = 'self.call("js","{0}")'.format(src)
        attrs['src'] = '%s';
        attrsHtml = self.buildHtmlAttrs(attrs);
        codeHtml = "'<script {0} ></script>' % ({1})".format(attrsHtml, jsFunc)

        mainNode.writeRawCode(codeHtml, True, True)

    def _img(self,node_attrs, mainNode:BaseNode):
        attrs = self.parseAttr(node_attrs)
        src = attrs['src'];
        jsFunc = 'self.call("img","{0}")'.format(src)
        attrs['src'] = '%s';
        attrsHtml = self.buildHtmlAttrs(attrs);
        codeHtml = "'<img {0} >' % ({1})".format(attrsHtml, jsFunc)

        mainNode.writeRawCode(codeHtml, True, True)









