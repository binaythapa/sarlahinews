from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', article, name='article'),  
    path('<int:id>/',article_detail, name='article_detail'),
    path('delete/<int:id>/',article_delete, name='article_delete'),
    path('edit/<int:id>/', edit_article, name='edit_article'),

    path('category/', category, name='category'),  
    path('category/<int:id>',category_detail, name='category_detail'),
    path('category/delete/<int:id>',category_delete, name='category_delete'),

    path('tag/', tag, name='tag'),  
    path('tag/<int:id>',tag_detail, name='tag_detail'),
    path('tag/delete/<int:id>',tag_delete, name='tag_delete'),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)