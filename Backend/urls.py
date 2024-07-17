from django.urls import path
from Backend import views

urlpatterns=[
    path('index_page/', views.index_page, name="index_page"),

#CATEGORY

    path('addcat_page/', views.addcat_page, name="addcat_page"),
    path('Cat_save/', views.Cat_save, name="Cat_save"),
    path('Cat_display/', views.Cat_display, name="Cat_display"),
    path('Cat_edit/<int:c_id>/', views.Cat_edit, name="Cat_edit"),
    path('cat_update/<int:c_id>/', views.cat_update, name="cat_update"),
    path('cat_delete/<int:c_id>/', views.cat_delete, name="cat_delete"),

#PRODUCT

    path('addproduct_page/', views.addproduct_page, name="addproduct_page"),
    path('product_save/', views.product_save, name="product_save"),
    path('Product_display/', views.Product_display, name="Product_display"),
    path('pro_edit/<int:p_id>/', views.pro_edit, name="pro_edit"),
    path('pro_update/<int:p_id>/', views.pro_update, name="pro_update"),
    path('pro_delete/<int:p_id>/', views.pro_delete, name="pro_delete"),

#ADMIN

    path('admin_login_page/',views.admin_login_page,name="admin_login_page"),
    path('admin_save/',views.admin_save,name="admin_save"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('delete_contact<int:d_id>/',views.delete_contact,name="delete_contact")
    ]