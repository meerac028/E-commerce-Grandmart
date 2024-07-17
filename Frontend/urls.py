from django.urls import path
from Frontend import views

urlpatterns=[
    path('home_page/', views.home_page, name="home_page"),
    path('product_page/<cate>', views.product_page, name="product_page"),
    path('about_page/', views.about_page, name="about_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('contact_save/', views.contact_save, name="contact_save"),
    path('singleproduct_page/<int:pro_id>/', views.singleproduct_page, name="singleproduct_page"),
    path('sign_in_up_page/', views.sign_in_up_page, name="sign_in_up_page"),
    path('sign_save/', views.sign_save, name="sign_save"),
    path('signup/', views.signup, name="signup"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('blog_page/', views.blog_page, name="blog_page"),
    path('cart/', views.cart, name="cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('checkout_save/', views.checkout_save, name="checkout_save"),
    path('cart_delete/<int:p_id>/', views.cart_delete, name="cart_delete"),
    ]