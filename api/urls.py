from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from .views import UserViewSet, OrganisationViewSet, HubViewSet, WorkspaceViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'organisations', OrganisationViewSet)
router.register(r'hubs', HubViewSet)
router.register(r'workspaces', WorkspaceViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    
    path('', include(router.urls)),  # UserViewSet endpoints

    # JWT token generation and refreshing routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Additional custom route for getting the authenticated user's own data (optional)
    # You can add more custom routes if required for your logic.
    # For example, a route for changing the password:
    path('users/me/change-password/', UserViewSet.as_view({'post': 'change_password'}), name='change_password'),
]
