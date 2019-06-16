from django.urls import path

from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('logout/', user_logout, name='logout'),
    path('facebook-page/add/', FacebookPageIDAddView.as_view(), name='facebook_page_add'),
    path('access-token/add/', FacebookAccessTokenAddView.as_view(), name='access_token_add'),
    path('access-token/update/<int:access_token_id>/', FacebookAccessTokenUpdateView.as_view(), name='access_token_update'),
    path('facebook-page/list/', FacebookPageListView.as_view(), name='facebook_page_list'),
    path('fb-page-/delete/<int:page_id>/', FacebookPageDeleteView.as_view(), name='fb_page_delete'),
    path('fb-page-/disable/<int:page_id>/', FacebookPageDisableView.as_view(), name='fb_page_disable'),
    path('fb-page-/enable/<int:page_id>/', FacebookPageEnableView.as_view(), name='fb_page_enable'),

]
