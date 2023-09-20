
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('reg/',views.reg),
    path('log/',views.log),

    path('addproduct/',views.addproduct),
    path('productdetails/',views.productdetails),
    path('update/',views.update),
    path('remove/',views.removep), 
    path('updateid/',views.updateid),
    path('sthetscope/',views.steth),
    path('probe/',views.probe),
    path('multimkit/',views.multimkit),
    path('product_id/',views.product_id),
    path('shop/',views.shop),
 

  
  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    