from django.contrib import admin
from django.urls import path,include
from first_task import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base_page, name='basepage'),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
