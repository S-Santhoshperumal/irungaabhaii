from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User
from .serializers import RegisterSerializer, LoginSerializer

class RegisterUserAPIView(APIView):
    """User Registration API View."""
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=RegisterSerializer, responses={201: "User created successfully"})
    def post(self, request):
        """Register a new user."""
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "User registered successfully",
                "user": serializer.data
            })
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "errors": serializer.errors
        })

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="user_id",
                in_=openapi.IN_QUERY,
                description="User ID to fetch user details",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={200: RegisterSerializer()}
    )
    def get(self, request):
        """Retrieve user details using user_id."""
        user_id = request.query_params.get("user_id")
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
            serializer = RegisterSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(APIView):
    """User Login API View."""
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: "JWT tokens returned"})
    def post(self, request):
        """Authenticate user and return JWT tokens."""
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(username=serializer.validated_data["username"])
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": status.HTTP_200_OK,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user_id": user.id,
                "message": "Login successful"
            })

        return Response({
            "status": status.HTTP_401_UNAUTHORIZED,
            "message": "Invalid credentials"
        })
