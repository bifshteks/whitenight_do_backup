from django.conf.urls import url
import main.views as mv

urlpatterns = [
    url(r'^$', mv.Index.as_view(), name="index"),
    url(r'^catalog/$', mv.Catalog.as_view(), name="catalog"),
    url(r'^catalog/(?P<pk>\d+)/$', mv.ItemDetails.as_view(), name="item"),
    url(r'^contacts/$', mv.Contacts.as_view(), name="contacts"),
    # url(r'^thanks/$', mv.Thanks.as_view(), name="thanks"),
    # url(r'^catalogf/$', mv.FakeCatalog.as_view(), name="fake_catalog"),
    # url(r'^contact', mv.FakeContacts.as_view(), name="fake_contacts"),
]