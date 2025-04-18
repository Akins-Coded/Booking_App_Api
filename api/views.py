from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import IsAdminOrManager, IsAdmin, IsAdminOrSelf
from django.contrib.auth import get_user_model
from booking.models import Organisation, Hub, Workspace, Booking

from .serializers import (
    AdminUserSerializer,
    EmployeeUserSerializer,
    UserSelfSerializer,
    BaseUserSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer,
)


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        elif self.action in ['list', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]  # Only admin can list or delete
        elif self.action in ['update', 'partial_update', 'retrieve']:
            return [IsAuthenticated(), IsAdminOrSelf()]  # Admin or self can update
        elif self.action in ['change_password', 'me']:
            return [IsAuthenticated()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return UserUpdateSerializer
        elif self.action == 'change_password':
            return ChangePasswordSerializer
        elif self.action in ['retrieve', 'list']:
            role = self.request.user.role if self.request.user.is_authenticated else None
            if role == 'admin':
                return AdminUserSerializer
            elif role == 'employee':
                return EmployeeUserSerializer
            elif role == 'user':
                return UserSelfSerializer
        return BaseUserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return User.objects.all()
        elif user.role == 'employee':
            return User.objects.exclude(role='admin')
        elif user.role == 'user':
            return User.objects.filter(id=user.id)
        return User.objects.none()

    @action(detail=False, methods=['get'], url_path='me', permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='change-password', permission_classes=[IsAuthenticated])
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Booking Views




from .serializers import (
    OrganisationSerializer,
    HubSerializer,
    WorkspaceSerializer,
    BookingSerializer
)

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign owner to the authenticated user
        serializer.save(owner=self.request.user)


class HubViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class WorkspaceViewSet(viewsets.ModelViewSet):
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign booking to current user
        serializer.save(user=self.request.user)
