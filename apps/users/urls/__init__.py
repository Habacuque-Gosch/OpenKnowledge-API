from .urls_auth import urlpatterns as auth_urls
# from .urls_profile import urlpatterns as profile_urls

# app_name = 'users'

urlpatterns = [
    *auth_urls,
    # *profile_urls,
]