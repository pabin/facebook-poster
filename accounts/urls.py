from django.urls import path

from .views import (
    UserLoginView,
    user_logout,
    FacebookPageIDAddView,
    FacebookAccessTokenAddView,
    FacebookAccessTokenUpdateView,
    FacebookPageListView,
)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('logout/', user_logout, name='logout'),
    path('facebook-page/add/', FacebookPageIDAddView.as_view(), name='facebook_page_add'),
    path('access-token/add/', FacebookAccessTokenAddView.as_view(), name='access_token_add'),
    path('access-token/update/<int:access_token_id>/', FacebookAccessTokenUpdateView.as_view(), name='access_token_update'),
    path('facebook-page/list/', FacebookPageListView.as_view(), name='facebook_page_list'),

]
