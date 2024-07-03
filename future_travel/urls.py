from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403, handler400
from blog import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"), name="blog-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("allauth.urls")),
]

handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
handler403 = 'blog.views.handler403'
handler405 = 'blog.views.handler405'
 
