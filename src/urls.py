"""xiche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from customer import views as cus_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hook/$',cus_view.hook),
    
    url(r'^zk/new_session/$',cus_view.new_session),
    url(r'^zk/qr/$',cus_view.qr),
    url(r'^zk/start/$',cus_view.start),
    url(r'^zk/end/$',cus_view.end),
    
    url(r'^sms/getcode/$',cus_view.get_code),
    url(r'^sms/validatecode/',cus_view.valide_sms),
    url(r'^user/login$',cus_view.user_login)
]
