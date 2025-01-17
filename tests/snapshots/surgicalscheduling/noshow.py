# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class NoShow(EventTypeAbstractModel):

    Meta: "NoShowMeta" = Field(...)
    Patient: "NoShowPatient" = Field(...)
    Procedures: List["NoShowProcedure"] = Field(...)
    SurgeryStaff: List["NoShowSurgeryStaff"] = Field(None)
    SurgicalCase: "NoShowSurgicalCase" = Field(None)
    SurgicalInfo: List["NoShowSurgicalInfo"] = Field(None)
    Visit: "NoShowVisit" = Field(...)


class NoShowMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["NoShowMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["NoShowMetaLog"] = Field(None)
    Message: "NoShowMetaMessage" = Field(None)
    Source: "NoShowMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "NoShowMetaTransmission" = Field(None)


class NoShowMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NoShowMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class NoShowMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NoShowMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class NoShowMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class NoShowPatient(RedoxAbstractModel):

    Demographics: "NoShowPatientDemographics" = Field(None)
    Identifiers: List["NoShowPatientIdentifier"] = Field(...)
    Notes: List[str] = Field(None)


class NoShowPatientDemographics(RedoxAbstractModel):

    Address: "NoShowPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "NoShowPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class NoShowPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NoShowPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class NoShowPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class NoShowProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DateTime: str = Field(...)
    Description: Union[str, None] = Field(None)
    Duration: Number = Field(...)
    ProcedureInfo: List["NoShowProcedureProcedureInfo"] = Field(None)


class NoShowProcedureProcedureInfo(RedoxAbstractModel):

    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NoShowSurgeryStaff(RedoxAbstractModel):

    Address: "NoShowSurgeryStaffAddress" = Field(None)
    Credentials: List[str] = Field(None)
    Duration: Union[Number, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NoShowSurgeryStaffLocation" = Field(None)
    PhoneNumber: "NoShowSurgeryStaffPhoneNumber" = Field(None)
    Role: "NoShowSurgeryStaffRole" = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class NoShowSurgeryStaffAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NoShowSurgeryStaffLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NoShowSurgeryStaffPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NoShowSurgeryStaffRole(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)


class NoShowSurgicalCase(RedoxAbstractModel):

    Number: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)


class NoShowSurgicalInfo(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class NoShowVisit(RedoxAbstractModel):

    AccountNumber: Union[str, None] = Field(None)
    AttendingProvider: "NoShowVisitAttendingProvider" = Field(None)
    Diagnoses: List["NoShowVisitDiagnosis"] = Field(None)
    Duration: Union[Number, None] = Field(None)
    Equipment: List["NoShowVisitEquipment"] = Field(None)
    Location: "NoShowVisitLocation" = Field(...)
    NoShowReason: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    PatientClass: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    VisitDateTime: Union[str, None] = Field(None)
    VisitNumber: str = Field(...)


class NoShowVisitAttendingProvider(RedoxAbstractModel):

    Address: "NoShowVisitAttendingProviderAddress" = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "NoShowVisitAttendingProviderLocation" = Field(None)
    PhoneNumber: "NoShowVisitAttendingProviderPhoneNumber" = Field(None)


class NoShowVisitAttendingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class NoShowVisitAttendingProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NoShowVisitAttendingProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class NoShowVisitDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class NoShowVisitEquipment(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Duration: Union[Number, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class NoShowVisitLocation(RedoxAbstractModel):

    Bed: Union[str, None] = Field(None)
    Department: str = Field(...)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


NoShow.update_forward_refs()
NoShowMeta.update_forward_refs()
NoShowPatient.update_forward_refs()
NoShowPatientDemographics.update_forward_refs()
NoShowProcedure.update_forward_refs()
NoShowSurgeryStaff.update_forward_refs()
NoShowVisit.update_forward_refs()
NoShowVisitAttendingProvider.update_forward_refs()
