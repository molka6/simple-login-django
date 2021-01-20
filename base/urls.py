from django.contrib import admin
from django.urls import path,include

urlpatterns = [path("admin/", admin.site.urls), 
# path("", home, name="homepage"),


# path('login',views.user_login, name='login'),
# path('index',views.index, name='index'),



path('auth/', include('login_user.urls'))

]
