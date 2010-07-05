from zope.interface import implements
from interfaces import ISection

from zope.dublincore.property import DCProperty
from allen.content.core.model import Content

class Section(Content):
    """ Section content-type
    """
    implements(ISection)

    title = DCProperty('title')
    description = DCProperty('description')
    tags = ()
    max_items = 15
    order = 10
