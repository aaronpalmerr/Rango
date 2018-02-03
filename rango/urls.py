
from django.conf.urls import url
from rango import views

urlpatterns = [

    # add home page
    url(r'^$', views.index, name='index'),

    # add about page
    url(r'^about/$', views.about, name="about"),

    # add new category page
    url(r'^add_category/$', views.add_category, name='add_category'),

    # add page page
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),

    # add slugified category page
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
]
