from django.urls import path
from .views import (ShopView,AllProductsView,ProductDetailsView,UserRegisterView,SigninView,
Userlogout,ChangePassView,ProfileChange,AddressView,EditAddress,DeleteAddress,ShowCartView,AddTCartView,
PlusQuantity,MinuseQuantity,RemoveItem,ClearCart,CheckoutView,PlaceorderView,OrdersView,Banglesbanner,
MaincateFilter,SubcateFilter)
from .form import PassResetForm,SetNewPassForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',ShopView,name='shop'),
    path('bb',Banglesbanner,name='bb'),
    path('allproducts/',AllProductsView,name='allproducts'),
    path('productdetails/<int:id>/',ProductDetailsView,name='productdetails'),
    path('showcart/',ShowCartView,name='showcart'),
    path('addcart/<int:id>/',AddTCartView,name='addcart'),
    path('plusqua/<int:id>/',PlusQuantity,name='plusqua'),
    path('minusequa/<int:id>/',MinuseQuantity,name='minusequa'),
    path('removeitem/<int:id>/',RemoveItem,name='removeitem'),
    path('clearcart',ClearCart,name='clearcart'),
    path('checkout/',CheckoutView,name='checkout'),
    path('placeorder/',PlaceorderView,name='placeorder'),
    path('orders/',OrdersView,name='orders'),
    
    # Filter by Main Category
    path('mancatefilter/<str:mcate>/',MaincateFilter,name='mancatefilter'),
    # Filter by Sub Category
    path('subcatefilter/<str:scate>/',SubcateFilter,name='subcatefilter'),

    # Auth url------------------------------------------
    path('signup/',UserRegisterView,name='signup'),
    path('signin/',SigninView,name='signin'),
    path('uout/',Userlogout,name='uout'),
    path('passchange/',ChangePassView,name='passchange'),
    path('prochange/',ProfileChange,name='prochange'),
    path('addview/',AddressView,name='addview'),
    path('addedit/<int:id>/',EditAddress,name='addedit'),
    path('adddelete/<int:id>/',DeleteAddress,name='adddelete'),


    #Password Reset
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=PassResetForm), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=SetNewPassForm), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),






    
]
