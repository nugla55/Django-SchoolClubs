from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clubs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#    path('login/', views.LoginView.as_view(), name='login'),
#    path('logout/', views.LogoutView.as_view(), name='logout'),
#
#    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
#
#   path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#   path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#   path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#   path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]
