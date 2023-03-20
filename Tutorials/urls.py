from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepageviews,name="homepage"),
   
    path('create/',views.createpageviews,name="createpage"),
    path('add-town/',views.addtownpageviews,name="add-town-page"),
    path('edit/<str:pk>/',views.editpageviews,name="editpage"),
    path('delete/<str:pk>/',views.deletepageviews,name="deletepage"),
    path('detail/<str:pk>/',views.detailpageviews,name="detailpage"),
    path('eachtown/<str:pk>/',views.eachtownpageviews,name="eachtownpage"),

    # accounts url
    path('register/',views.register,name="registerpage"),
    path('login/',views.loginpageviews,name="loginpage"),
    path('logout/',views.logoutpageviews,name="logoutpage"),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
