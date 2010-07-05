from zope.formlib.form import Fields, PageEditForm
from interfaces import ISection

class Edit(PageEditForm):
    form_fields = Fields(ISection)
