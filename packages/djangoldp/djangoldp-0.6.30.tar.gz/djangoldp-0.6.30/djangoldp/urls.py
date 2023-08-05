from importlib import import_module

from django.conf import settings
from django.conf.urls import url, include

from djangoldp.models import LDPSource, Model
from djangoldp.permissions import LDPPermissions
from djangoldp.views import LDPSourceViewSet, WebFingerView
from djangoldp.views import LDPViewSet


def __clean_path(path):
    if path.startswith("/"):
        path = path[1:]
    if not path.endswith("/"):
        path = "{}/".format(path)
    return path


urlpatterns = [
    url(r'^sources/(?P<federation>\w+)/', LDPSourceViewSet.urls(model=LDPSource, fields=['federation', 'urlid'],
                                                                permission_classes=[LDPPermissions], )),
    url(r'^\.well-known/webfinger/?$', WebFingerView.as_view()),
]

for package in settings.DJANGOLDP_PACKAGES:
    try:
        import_module('{}.models'.format(package))
    except ModuleNotFoundError:
        pass

model_classes = {cls.__name__: cls for cls in Model.__subclasses__()}

for class_name in model_classes:
    model_class = model_classes[class_name]
    path = __clean_path(model_class.get_container_path())
    urls_fct = model_class.get_view_set().urls
    urlpatterns.append(url(r'^' + path, include(
        urls_fct(model=model_class,
                 lookup_field=Model.get_meta(model_class, 'lookup_field', 'pk'),
                 permission_classes=Model.get_meta(model_class, 'permission_classes', [LDPPermissions]),
                 fields=Model.get_meta(model_class, 'serializer_fields', []),
                 nested_fields=Model.get_meta(model_class, 'nested_fields', [])))))

for package in settings.DJANGOLDP_PACKAGES:
    try:
        urlpatterns.append(url(r'^', include('{}.djangoldp_urls'.format(package))))
    except ModuleNotFoundError:
        pass

if 'djangoldp_account' not in settings.DJANGOLDP_PACKAGES:
    urlpatterns.append(url(r'^users/', LDPViewSet.urls(model=settings.AUTH_USER_MODEL, permission_classes=[])))
