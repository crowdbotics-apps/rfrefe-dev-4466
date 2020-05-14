from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    HomePageViewSet,
    R123ViewSet,
    R456ViewSet,
    RFFFFViewSet,
    RFFFFFViewSet,
    RFFFFFddViewSet,
    RVBBViewSet,
    RVVVVViewSet,
    VGGGGViewSet,
    VVVVVViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("r456", R456ViewSet)
router.register("r123", R123ViewSet)
router.register("rfffff", RFFFFFViewSet)
router.register("rvbb", RVBBViewSet)
router.register("rvvvv", RVVVVViewSet)
router.register("rffff", RFFFFViewSet)
router.register("vgggg", VGGGGViewSet)
router.register("vvvvv", VVVVVViewSet)
router.register("rfffffdd", RFFFFFddViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
