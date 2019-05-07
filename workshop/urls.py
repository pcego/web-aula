from django.contrib import admin
from django.urls import path
from workshop.core.views import home, speaker, \
    about, news, events, contact


from workshop.subscriptions.views import subscription, detail

urlpatterns = [

    path('', home),
    path('speakers/', speaker),
    path('about/', about),
    path('news/', news),
    path('events/', events),
    path('contact/', contact),
    path('subscription/', subscription),
    path('subscription/<int:pk>/', detail),

    path('admin/', admin.site.urls),
]
