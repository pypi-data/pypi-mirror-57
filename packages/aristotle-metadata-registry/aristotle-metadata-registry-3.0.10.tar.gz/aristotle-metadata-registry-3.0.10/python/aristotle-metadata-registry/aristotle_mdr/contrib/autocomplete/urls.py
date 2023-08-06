from django.conf.urls import url
from aristotle_mdr.contrib.autocomplete import views

urlpatterns = [
    url(
        r'^concept/(?:(?P<app_name>[a-z_]+)-(?P<model_name>[a-z_]+))?$',
        views.GenericConceptAutocomplete.as_view(),
        name='concept',
    ),
    url(
        r'^user$',
        views.UserAutocomplete.as_view(),
        name='user',
    ),
    url(
        r'^workgroup',
        views.WorkgroupAutocomplete.as_view(),
        name='workgroup',
    ),
    url(
        r'^framework/(?:(?P<app_name>[a-z_]+)-(?P<model_name>[a-z_]+))?$',
        views.FrameworkDimensionsAutocomplete.as_view(),
        name='framework'
    )

]
