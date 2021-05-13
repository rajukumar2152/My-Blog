from django.urls import path


from . import views

urlpatterns = [
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path("category/<int:cid>/" , views.showcat, name='catview'),
    path('catlist', views.catlist, name='catlist')    
    # path('category', views.showcat, name='catview') 
    # path('raju' ,views.ccet , name='raju'),
   
    
] 