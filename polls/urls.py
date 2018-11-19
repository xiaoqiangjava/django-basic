from django.urls import path
from . import views


# 为了是URL和view关联起来, Django使用了URLconfs来配置, URLconf将URL模式映射到视图
# python中使用<int:question_id>来匹配URL, question_id是必须与参数名称匹配
# 在模板中可以使用name来代替URL, 但是当一个project中包含很多个APP时, 可能每个APP有相同的name, 这个时候就
# 需要给URL指定命名空间, 在templates中使用时用'polls:detail'来指定URL的命名空间
app_name = "polls"  # 指定URL的命名空间为polls, 当指定了URL的命名空间后必须使用
urlpatterns = [
    path('index.html', views.index, name='index'),
    path('index_v2.html', views.index_v2, name="index_v2"),
    path('<int:question_id>', views.detail, name='detail'),
    path('v2/<int:question_id>', views.detail_v2, name="detail_v2"),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
