# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import provider
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Provider(GenericRedoxAbstractModel):
    _redox_module = provider


class Activate(_Provider):

    Meta: generic.Meta = Field(...)
    Providers: List[generic.Provider] = Field(...)


class Deactivate(_Provider):

    Meta: generic.Meta = Field(...)
    Providers: List[generic.Provider] = Field(...)


class New(_Provider):

    Meta: generic.Meta = Field(...)
    Providers: List[generic.Provider] = Field(...)


class ProviderQuery(_Provider):

    Meta: generic.Meta = Field(...)
    Provider: generic.Provider = Field(None)


class ProviderQueryResponse(_Provider):

    Meta: generic.Meta = Field(...)
    Providers: List[generic.Provider] = Field(...)


class Update(_Provider):

    Meta: generic.Meta = Field(...)
    Providers: List[generic.Provider] = Field(...)
