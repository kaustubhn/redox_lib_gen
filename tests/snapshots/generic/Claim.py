# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from pyredox import claim
from ..abstract_base import GenericRedoxAbstractModel
from . import types as generic


class _Claim(GenericRedoxAbstractModel):
    _redox_module = claim


class Payment(_Claim):

    Meta: generic.Meta = Field(...)
    Payee: generic.Payee = Field(None)
    Payer: generic.Payer = Field(None)
    Payments: List[generic.Payment] = Field(...)
    Transaction: generic.Transaction = Field(None)


class PaymentBatch(_Claim):

    Meta: generic.Meta = Field(...)
    Transactions: List[generic.Transaction] = Field(None)


class Submission(_Claim):

    BillingProvider: generic.BillingProvider = Field(None)
    Claims: List[generic.Claim] = Field(None)
    Meta: generic.Meta = Field(...)
    Patient: generic.Patient = Field(None)
    Subscriber: generic.Subscriber = Field(None)
    Transaction: generic.Transaction = Field(None)


class SubmissionBatch(_Claim):

    Meta: generic.Meta = Field(...)
    Transactions: List[generic.Transaction] = Field(None)
