
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

    # add register url
    url(r'^register/$', views.register, name='register'),

    # add login url
    url(r'^login/$', views.user_login, name='login'),

    url(r'^restricted/$', views.restricted, name='restricted'),

    url(r'^logout/$', views.user_logout, name='logout'),

]
