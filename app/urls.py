from re import template
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,ChangePasswordForm,ResetPasswordForm,MySetPassForm
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(),name='homepage'),    
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.productDetailview.as_view(),name='product-detail'),  
    path('cart/', views.AddcartView.as_view(), name='add-to-cart'),
    path('buy/', views.BuynowView.as_view(), name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.AddressView.as_view(), name='address'),
    path('orders/', views.OdersView.as_view(), name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=ChangePasswordForm,success_url='/passwordchangedone/'), name='changepassword'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passchangedone'),
    # path('mobile/', views.mobile, name='mobile'),
    path('pass-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='reset_password_done'),
    path('pass-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=ResetPasswordForm),name='reset-password'),
    path('pass-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPassForm),name='reset-password-confirm'),
    path('pass-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='reset-password-complete'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('mobile/<slug:data>', views.MobileView.as_view(), name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustRegdView.as_view(), name='customerregistration'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
