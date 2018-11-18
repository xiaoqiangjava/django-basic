"""django_basic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    # path参数: 第一个route, 第二个view是必须参数, 第三个kwargs和第四个name是可选参数
    # name参数的作用: 为URL取名, 能够使你的URL在Django的任何地方唯一的使用, 尤其是在模板中.
    path('polls/index.html', include('polls.urls')),    # 函数include()允许引入其他的URLconfs
    path('admin/', admin.site.urls),        # 当URLconf中包含其他URLconf时, 应该总是使用include()函数
]
