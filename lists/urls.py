from django.conf.urls import url
from .views import home_page
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
]