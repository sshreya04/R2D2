from django.conf.urls import url,include
from django.contrib import admin


from rest_framework import routers
from movies import views

router = routers.DefaultRouter()
router.register(r'detail', views.DetailViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'data/', include('movies.urls')),
]

