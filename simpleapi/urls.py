"""
URL configuration for simpleapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from usersapimixin.views import UserMixinList, UserMixinDetail, UserDetail, UserUpdate, UserCreate, UserDelete, UserDtoDetail, User

from usersapi.views import UserList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usersapi.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('allusers/', UserMixinList.as_view(), name='usermixin-list'),
    path('allusers/<int:pk>', UserMixinDetail.as_view(), name='usermixin-detail'),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('userup/<int:pk>', UserUpdate.as_view(), name='user-up'),
    path('new', UserCreate.as_view(), name='new'),
    path('delete/<int:pk>', UserDelete.as_view(), name='delete'),
    path('userdto/<int:pk>', UserDtoDetail.as_view(), name='get'),


    # path('userlist/', UserList.as_view, name='userlist'),

]
