from django.db.models import QuerySet

from version_control.helpers import VersionWrapper


def decorate_queryset_method(queryset_func, new_bases: tuple):
    """
    A decorator function for extending queryset class base classes
    """

    def queryset_method(*args, **kwargs):
        queryset = queryset_func(*args, **kwargs)
        queryset_cls = queryset.__class__
        queryset.__class__ = type(
            queryset_cls.__name__, (*new_bases, *queryset_cls.__bases__), dict(queryset_cls.__dict__)
        )
        return queryset
    return queryset_method


class ModelObjectVersionGroupQuerySet(QuerySet):
    """
    A queryset-manager for "ModelObjectVersionGroup" model
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).prefetch_related('model_object_versions')


class ModelObjectVersionQuerySet(QuerySet):
    """
    A queryset-manager for "ModelObjectVersion" model
    """

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs).select_related('group')


class VersionControlQuerysetManagerMixin:
    """
    The base queryset manager mixin
    """

    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        bulk_created_objects = super().bulk_create(objs, batch_size, ignore_conflicts)
        for obj in bulk_created_objects:
            if obj.WRITE_CREATION:
                obj.handle_version()
        return bulk_created_objects

    # bulk_update uses update method

    def update(self, **kwargs):
        old_states = list(self._chain())
        rows = super().update(**kwargs)
        current_states = list(self._chain())
        chain_to_process = [
            obj for index, obj in enumerate(current_states)
            if obj.WRITE_CHANGES and VersionWrapper(obj) != VersionWrapper(old_states[index])
        ]
        for obj in chain_to_process:
            obj.handle_version()
        return rows

    # Not required to override. All deletions catching by pre_delete signal
    # def delete(self):
    #     for obj in self._chain():
    #         obj.handle_version(version_change_type=ModelObjectChangeType.OBJECT_DELETED)
    #     return super().delete()


class VersionControlModelManagerMixin(VersionControlQuerysetManagerMixin):
    """
    A queryset manager for tracking model objects versions after QuerySet manager's bulk_create/update/delete
    operations.
    """

    def _extend_queryset_methods(self, methods: list) -> None:
        for method in methods:
            method_object = getattr(self.__class__, method, None)
            if method_object:
                setattr(self.__class__, method, decorate_queryset_method(method_object,
                                                                         (VersionControlQuerysetManagerMixin,)))
