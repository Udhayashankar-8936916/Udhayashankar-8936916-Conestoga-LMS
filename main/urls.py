from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('logout/', views.logout_user, name = "logout"),
    path('issue book/', views.issue_books, name = "issue_book"),
    path('issue book1/', views.issue_books1, name = "issue_book1"),
    path('new book/', views.add_new_book, name = 'new_book'),
    path('view books/', views.view_books, name = "view_books"),
    path('remove issue/', views.remove_issue, name = 'remove_issue'),
    path('remove issue1/', views.remove_issue1, name = 'remove_issue1'),
    path('available books/', views.available_books,  name = "av_book"),
    path('update profile/', views.update_profile_pic, name = 'update_profile'),
    path('update profile1/', views.update_profile_pic1, name = 'update_profile1'),
    path('remove book/', views.remove_issue1, name = 'remove_issue'),
    path('remove book/1', views.remove_issue1, name='remove_book'),    
    path('slist/', views.view_student, name = 'slist'),
]