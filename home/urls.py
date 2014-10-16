from django.conf.urls import patterns, url, include

from home.views import HomeView, TodoList, TodoDetail


urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home_page'),
    url(r'^todos/$', TodoList.as_view(), name="todos_list"),
	url(r'^todos/(?P<pk>[0-9]+)/$', TodoDetail.as_view(), name="todos_update"),
)