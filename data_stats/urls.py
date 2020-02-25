from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('login/',views.login,name="Login"),
    path('register/',views.register,name="Register"),
    path('check/',views.check,name="Check"),
    path('logout/',views.logout,name="Logout"),
    
    
    
    path('admin/create-user',views.create_user,name="Create-user"),
    path('admin/delete-user/<id>', views.delete_user,name="Delete-user"),
    path('admin/create-blog', views.create_blog,name="createblog"),
    path('admin/view-posts/<slug>/<table_id>',views.show_news, name="view-posts"),
    path('admin/delete-content/<slug>/<id>',views.delete_content,name="delete-content"),
    
    
    
    path('user/create-post',views.create_user_blog,name="create-user-blog"),
    path('user/logout',views.user_logout,name="user-logout"),
    path('user/dashboard/',views.check,name="user-dashboard"),
    
    
    
    
    
]
