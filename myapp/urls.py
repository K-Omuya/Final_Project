from tkinter.font import names

from django.urls import path
from .import views
# from .views import item_list

urlpatterns=[
      path('',views.home,name='home'),

      path('about/',views.about,name='about'),
      path('services/',views.about,name='services'),

      path('contacts/',views.about,name='contacts'),


      path('',views.bloglist, name='blog_list'),
      path('<int:post_id>',views.blog_detail, name='blog_detail'),

   #
   #    path('',views.item_list,name=item_list),
   #    path('create/',views.create_item,name='create_item'),
   #
   #    path('update/<int:pk>',views.update_item,name='update_item'),
   # path('delete/<int:pk>',views.delete_item,name='delete_item'),
   #
   #
   #
   #
   #
   #
   #
   #

]