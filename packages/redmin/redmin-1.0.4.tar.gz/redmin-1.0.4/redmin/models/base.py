from django.db import models
from django.db.models.base import ModelBase
from django.urls import reverse

from redmin.utils import attr


def merge(name, attrs, meta_name, base_meta):
    meta = attrs.pop(meta_name, None)
    if not meta:
        meta = type(meta_name, (base_meta,), dict(
            __module__=f'{attrs.get("__module__")}.{name}'
        ))
    attributes = vars(meta)
    for key, value in vars(base_meta).items():
        if ("__init__" == key or not key.startswith("_")) and "abstract" != key and key not in attributes:
            setattr(meta, key, value)
    return meta


class BaseMeta(ModelBase):
    def __new__(mcs, name, bases, attrs, **kwargs):
        if name != 'RedminModel':
            attrs["Meta"] = merge(name, attrs, "Meta", getattr(RedminModel, "Meta"))
        return ModelBase.__new__(mcs, name, bases, attrs, **kwargs)


class RedminModel(models.Model, metaclass=BaseMeta):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        abstract = True

    def get_absolute_url(self):
        return reverse(self.__class__.__name__ + "-update", kwargs={"pk": self.pk})

    @property
    def css_color(self):
        return "black"

    @property
    def instance_permission(self):
        from .permission import Permission
        request = attr(self, "_request")
        if request:
            return Permission.get_permission(request.user, self.__class__).to_instance_permission()
        else:
            return Permission()

    @classmethod
    def get_domain_key(cls):
        app = cls.__module__.split(".")[0]
        name = cls.__name__
        return app + "_" + name

    def clone(self):
        cls = self.__class__
        instance = cls()
        for field in cls._meta.fields:
            setattr(instance, field.name, getattr(self, field.name))
        return instance
