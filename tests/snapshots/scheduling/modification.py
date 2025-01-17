# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Modification(EventTypeAbstractModel):

    AppointmentInfo: List["ModificationAppointmentInfo"] = Field(None)
    Meta: "ModificationMeta" = Field(...)
    Patient: "ModificationPatient" = Field(None)
    Visit: "ModificationVisit" = Field(...)


class ModificationAppointmentInfo(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class ModificationMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["ModificationMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["ModificationMetaLog"] = Field(None)
    Message: "ModificationMetaMessage" = Field(None)
    Source: "ModificationMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "ModificationMetaTransmission" = Field(None)


class ModificationMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class ModificationMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class ModificationMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class ModificationMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class ModificationMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class ModificationPatient(RedoxAbstractModel):

    Demographics: "ModificationPatientDemographics" = Field(None)
    Identifiers: List["ModificationPatientIdentifier"] = Field(None)
    Notes: List[str] = Field(None)


class ModificationPatientDemographics(RedoxAbstractModel):

    Address: "ModificationPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "ModificationPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class ModificationPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class ModificationPatientIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class ModificationVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AdditionalStaff: List["ModificationVisitAdditionalStaff"] = Field(None)
    AttendingProvider: "ModificationVisitAttendingProvider" = Field(None)
    ConsultingProvider: "ModificationVisitConsultingProvider" = Field(None)
    Diagnoses: List["ModificationVisitDiagnosis"] = Field(None)
    Duration: Number = Field(...)
    Equipment: List["ModificationVisitEquipment"] = Field(None)
    Instructions: List[str] = Field(None)
    Location: "ModificationVisitLocation" = Field(...)
    PatientClass: Union[str, None] = Field(None)
    Reason: Union[str, None] = Field(None)
    ReferringProvider: "ModificationVisitReferringProvider" = Field(None)
    Status: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    VisitDateTime: str = Field(...)
    VisitNumber: str = Field(...)
    VisitProvider: "ModificationVisitVisitProvider" = Field(None)


class ModificationVisitAdditionalStaff(RedoxAbstractModel):

    Address: "ModificationVisitAdditionalStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    Duration: Union[Number, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "ModificationVisitAdditionalStaffLocation" = Field(None)
    PhoneNumber: "ModificationVisitAdditionalStaffPhoneNumber" = Field(None)
    Role: "ModificationVisitAdditionalStaffRole" = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class ModificationVisitAdditionalStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationVisitAdditionalStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitAdditionalStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class ModificationVisitAdditionalStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class ModificationVisitAttendingProvider(RedoxAbstractModel):

    Address: "ModificationVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "ModificationVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "ModificationVisitAttendingProviderPhoneNumber" = Field(None)


class ModificationVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class ModificationVisitConsultingProvider(RedoxAbstractModel):

    Address: "ModificationVisitConsultingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "ModificationVisitConsultingProviderLocation" = Field(None)
    PhoneNumber: "ModificationVisitConsultingProviderPhoneNumber" = Field(None)


class ModificationVisitConsultingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationVisitConsultingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitConsultingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class ModificationVisitDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitEquipment(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class ModificationVisitLocation(RedoxAbstractModel):

    Department: str = Field(...)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitReferringProvider(RedoxAbstractModel):

    Address: "ModificationVisitReferringProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "ModificationVisitReferringProviderLocation" = Field(None)
    PhoneNumber: "ModificationVisitReferringProviderPhoneNumber" = Field(None)


class ModificationVisitReferringProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationVisitReferringProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitReferringProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class ModificationVisitVisitProvider(RedoxAbstractModel):

    Address: "ModificationVisitVisitProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "ModificationVisitVisitProviderLocation" = Field(None)
    PhoneNumber: "ModificationVisitVisitProviderPhoneNumber" = Field(None)


class ModificationVisitVisitProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class ModificationVisitVisitProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class ModificationVisitVisitProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


Modification.update_forward_refs()
ModificationMeta.update_forward_refs()
ModificationPatient.update_forward_refs()
ModificationPatientDemographics.update_forward_refs()
ModificationVisit.update_forward_refs()
ModificationVisitAdditionalStaff.update_forward_refs()
ModificationVisitAttendingProvider.update_forward_refs()
ModificationVisitConsultingProvider.update_forward_refs()
ModificationVisitReferringProvider.update_forward_refs()
ModificationVisitVisitProvider.update_forward_refs()
