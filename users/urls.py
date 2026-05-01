from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import SignUpView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='homepage/homepage.html'), name='login'),

    path('logout/', LogoutView.as_view(next_page='/', http_method_names=['get', 'post']), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]