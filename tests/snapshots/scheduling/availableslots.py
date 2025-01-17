# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class AvailableSlots(EventTypeAbstractModel):

    EndDateTime: Union[str, None] = Field(None)
    Meta: "AvailableSlotsMeta" = Field(...)
    Patient: "AvailableSlotsPatient" = Field(None)
    StartDateTime: str = Field(...)
    Visit: "AvailableSlotsVisit" = Field(None)


class AvailableSlotsMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["AvailableSlotsMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["AvailableSlotsMetaLog"] = Field(None)
    Message: "AvailableSlotsMetaMessage" = Field(None)
    Source: "AvailableSlotsMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "AvailableSlotsMetaTransmission" = Field(None)


class AvailableSlotsMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AvailableSlotsMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class AvailableSlotsMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AvailableSlotsMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class AvailableSlotsMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class AvailableSlotsPatient(RedoxAbstractModel):

    Demographics: "AvailableSlotsPatientDemographics" = Field(None)
    Diagnoses: List["AvailableSlotsPatientDiagnosis"] = Field(None)
    Identifiers: List["AvailableSlotsPatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class AvailableSlotsPatientDemographics(RedoxAbstractModel):

    Address: "AvailableSlotsPatientDemographicsAddress" = Field(None)
    Citizenship: List[str] = Field(None)
    DOB: Union[str, None] = Field(None)
    DeathDateTime: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    IsDeceased: Union[bool, None] = Field(None)
    IsHispanic: Union[bool, None] = Field(None)
    Language: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MaritalStatus: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "AvailableSlotsPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class AvailableSlotsPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AvailableSlotsPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class AvailableSlotsPatientDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AvailableSlotsPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class AvailableSlotsVisit(RedoxAbstractModel):

    AttendingProviders: List["AvailableSlotsVisitAttendingProvider"] = Field(None)
    Locations: List["AvailableSlotsVisitLocation"] = Field(None)
    Reasons: List[str] = Field(None)
    VisitPreference: List["AvailableSlotsVisitVisitPreference"] = Field(None)
    VisitType: List["AvailableSlotsVisitVisitType"] = Field(None)


class AvailableSlotsVisitAttendingProvider(RedoxAbstractModel):

    Address: "AvailableSlotsVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "AvailableSlotsVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "AvailableSlotsVisitAttendingProviderPhoneNumber" = Field(None)


class AvailableSlotsVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class AvailableSlotsVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class AvailableSlotsVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class AvailableSlotsVisitLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    SpecialtyDepartment: "AvailableSlotsVisitLocationSpecialtyDepartment" = Field(None)
    Type: Union[str, None] = Field(None)


class AvailableSlotsVisitLocationSpecialtyDepartment(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class AvailableSlotsVisitVisitPreference(RedoxAbstractModel):

    Day: List[str] = Field(None)
    Duration: Union[str, None] = Field(None)
    DurationUnit: Union[str, None] = Field(None)
    Time: List[str] = Field(None)


class AvailableSlotsVisitVisitType(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


AvailableSlots.update_forward_refs()
AvailableSlotsMeta.update_forward_refs()
AvailableSlotsPatient.update_forward_refs()
AvailableSlotsPatientDemographics.update_forward_refs()
AvailableSlotsVisit.update_forward_refs()
AvailableSlotsVisitAttendingProvider.update_forward_refs()
AvailableSlotsVisitLocation.update_forward_refs()
