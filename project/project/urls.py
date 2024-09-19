"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('register',views.Register),
    path('bankregister',views.bankregister),
    path('login',views.Login),
    path('userhome',views.userhome,name='userhome'),
    path('profileview',views.profileview,name='profileview'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('bankhome',views.bankhome),
    path('logout',views.Logout,name='logout'),
    path('deposit',views.deposite,name='deposit'),
    path('more',views.more),
    path('withdrow',views.withdrow,name='withdrow'),
    path('history',views.history,name='history'),
    path('viewuser',views.bankviewuser,name='viewuser'),
    path('bankuser/<int:id>',views.bankuser,name='bankuser'),
    path('viewhistory/<int:id>',views.bankuserhistory,name='viewhistory'),
    path('admin1',views.admin,name='admin1'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('index1',views.index1,name='index1'),
    path('adminuseraccept/<int:id>',views.adminuseraccept,name='adminuseraccept'),
    

    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)