# -*- coding: utf-8 -*-

from rest_framework import mixins, viewsets

# from .utils import get_status


class BaseGenericViewSet(viewsets.GenericViewSet):
    """Custom API response format."""

    pass


class BaseModelViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericViewSet,
):
    """Custom API response format."""

    pass


class BaseCreateViewSet(mixins.CreateModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseCreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseCreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseCreateListRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    BaseGenericViewSet,
):
    """Custom API response format."""

    pass


class BaseCreateListRetrieveDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    BaseGenericViewSet,
):
    """Custom API response format."""

    pass


class BaseListViewSet(mixins.ListModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseListUpdateViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseListRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseRetrieveUpdateViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseRetrieveViewSet(mixins.RetrieveModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseUpdateViewSet(mixins.UpdateModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass


class BaseCreateUpdateViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, BaseGenericViewSet):
    """Custom API response format."""

    pass
