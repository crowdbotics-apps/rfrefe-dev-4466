from rest_framework import viewsets
from rest_framework import authentication
from .serializers import (
    CustomTextSerializer,
    HomePageSerializer,
    R123Serializer,
    R456Serializer,
    RFFFFSerializer,
    RFFFFFSerializer,
    RFFFFFddSerializer,
    RVBBSerializer,
    RVVVVSerializer,
    VGGGGSerializer,
    VVVVVSerializer,
)
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home.api.v1.serializers import (
    SignupSerializer,
    CustomTextSerializer,
    HomePageSerializer,
    UserSerializer,
)
from home.models import (
    CustomText,
    HomePage,
    R123,
    R456,
    RFFFF,
    RFFFFF,
    RFFFFFdd,
    RVBB,
    RVVVV,
    VGGGG,
    VVVVV,
)


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class LoginViewSet(ViewSet):
    """Based on rest_framework.authtoken.views.ObtainAuthToken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})


class CustomTextViewSet(ModelViewSet):
    serializer_class = CustomTextSerializer
    queryset = CustomText.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class HomePageViewSet(ModelViewSet):
    serializer_class = HomePageSerializer
    queryset = HomePage.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "put", "patch"]


class R456ViewSet(viewsets.ModelViewSet):
    serializer_class = R456Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = R456.objects.all()


class R123ViewSet(viewsets.ModelViewSet):
    serializer_class = R123Serializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = R123.objects.all()


class RFFFFFViewSet(viewsets.ModelViewSet):
    serializer_class = RFFFFFSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RFFFFF.objects.all()


class RVBBViewSet(viewsets.ModelViewSet):
    serializer_class = RVBBSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RVBB.objects.all()


class RVVVVViewSet(viewsets.ModelViewSet):
    serializer_class = RVVVVSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RVVVV.objects.all()


class RFFFFViewSet(viewsets.ModelViewSet):
    serializer_class = RFFFFSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RFFFF.objects.all()


class VGGGGViewSet(viewsets.ModelViewSet):
    serializer_class = VGGGGSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VGGGG.objects.all()


class VVVVVViewSet(viewsets.ModelViewSet):
    serializer_class = VVVVVSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VVVVV.objects.all()


class RFFFFFddViewSet(viewsets.ModelViewSet):
    serializer_class = RFFFFFddSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = RFFFFFdd.objects.all()
