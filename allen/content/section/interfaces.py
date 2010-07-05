""" Section interfaces
"""
from zope import schema
from allen.content.core.interfaces import IContent

class ISection(IContent):
    """ Section content-type
    """
    title = schema.TextLine(title=u'Title', required=True)
    description = schema.Text(title=u'Description', required=False)
    order = schema.Int(title=u'Order in container', default=10)
    tags = schema.List(title=u'Tags', value_type=schema.TextLine())
    max_items = schema.Int(title=u'Max items', default=15)
