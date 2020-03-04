from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('login/',views.login,name="Login"),
    path('register/',views.register,name="Register"),
    path('check/',views.check,name="Check"),
   
    
    
    
    path('admin/create-user',views.create_user,name="Create-user"),
    path('admin/delete-user/<id>', views.delete_user,name="Delete-user"),
    path('admin/create-blog', views.create_blog,name="createblog"),
    path('admin/view-posts/<slug>/<table_id>',views.show_news, name="view-posts"),
    path('admin/delete-content/<slug>/<id>',views.delete_content,name="delete-content"),
    path('login/admin',views.admin_login_check,name="admin-login"),
    path('admin/dashboard/', views.admin_dashboard,name="admin-dashboard"),
    path('admin-logout', views.admin_logout,name="admin-logout"),
    path('admin/view-content/<slug>/<id>',views.view_content,name="admin-view-content"),
    
    
    path('user/create-post',views.create_user_blog,name="create-user-blog"),
    path('user/logout',views.user_logout,name="user-logout"),
    path('user/dashboard/',views.check,name="user-dashboard"),
    path('user/update-post/<slug>/<id>',views.update_content,name="user-update")
    
    
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)