from django.urls import path
from . import views

urlpatterns = [
    path('SignUp/',views.SignUp,name="signup"),
    path('login/',views.user_login,name="login"),
    path('Home/',views.home,name="home"),
    path('logout/',views.logout_view,name="logout"),
    path('Student_list/',views.view_student,name="student_list"),
    path('User_delete/<int:id>/',views.user_delete,name="user_delete"),
    path('User_list/',views.view_users,name="user_list"),
]
