from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'crud'
urlpatterns = [
    path('goods_create/', login_required(views.GoodsCreate.as_view()), name='goods_create'),
    path('goods_list/', login_required(views.GoodsList.as_view()), name='goods_list'),
    path('goods_detail/<int:pk>/', login_required(views.GoodsDetail.as_view()), name='goods_detail'),
]
