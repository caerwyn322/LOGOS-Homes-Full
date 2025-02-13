"""logos_homes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('/', include('home.urls')),
    path('home/', include('home.urls')),
    path('home/Home.html', include('home.urls')),
    path('Home.html', include('home.urls')),
    path('admin/', admin.site.urls),
    path('contact_us/', include('contact_us.urls')),
    path('Contact-Us.html', include('contact_us.urls')),
    path('designs/', include('designs.urls')),
    path('designs/Designs.html', include('designs.urls')),
    path('Designs.html', include('designs.urls')),
    path(r'contact_us/Contact-Us.html', include('contact_us.urls')),
    path('abouts_us/', include('about_us.urls')),
    path('about_us/About-Us.html', include ('about_us.urls')),
    path('About-Us.html', include('about_us.urls')),
    path('gallery/', include('gallery.urls')),
    path('gallery/Gallery.html', include('gallery.urls')),
    path('Gallery.html', include('gallery.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += [
#         url(r'^media/(?P<oath>.*)$', serve,{
#             'document_root':settings.MEDIA_ROOT,
#         })
#     ]
