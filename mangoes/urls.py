from django.urls import path

from .views import home,signup,Login,Logout,profile,html_to_pdf_view,delivery_for_salers,list_to_buy,sell,single_page,my_sells,update_product,delete_product,create_for_buy,my_buys,single_buy,change_delivery
from django.contrib.auth import views as auth_views
from django.urls import path,include

urlpatterns = [
   
    path('account/login/',Login , name='login'),
    path('account/signin/',signup, name='signin'),
    path('account/logout/',Logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')),
# path("account/password_reset",auth_views.password_reset,name='password_reset'),
# path("password_reset/done/", auth_views.password_reset_done, name='password_reset_done'),
# path("account/password_change/",auth_views.password_change,name='password_change'),
# path("account/password_change/done/",auth_views.password_change_done,name='password_change_done'),
# path("account/reset/<uidb64>/<token>/",auth_views.password_reset_confirm,name='password_reset_confirm'),
# path("account/reset/done/",auth_views.password_reset_complete,name='password_reset_complete') ,
 
    path('accounts/', include('allauth.urls')), # <--

    path('',home,name='index'),
    path('profile/',profile,name='profile'),
    path('list_to_buy/',list_to_buy,name='list_to_buy'),
    path('sell/',sell,name='sell'),
    path('single_page/<int:id>/',single_page,name='single_page'),
    path('my_sells/',my_sells,name="my_sells"),
    path('update_product/<int:id>/',update_product,name="update_product"),
    path('delete_product/<int:id>/',delete_product,name="delete_product"),

    path('create__for_buy/<int:id>/',create_for_buy,name="create_for_buy"),
    path('my_buys/',my_buys,name="my_buys"),
    path('single_buy/<int:id>/',single_buy,name="single_buy"),

    path('delivery_list/',delivery_for_salers,name="delivery_for_sales"),
    path('change_delivery/<int:id>/',change_delivery,name="change_delivery"),

    path('html_to_pdf/<int:id>/',html_to_pdf_view,name="pdfs"),
]