# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class Cancel(EventTypeAbstractModel):

    Meta: "CancelMeta" = Field(...)
    Patient: "CancelPatient" = Field(...)
    Referral: "CancelReferral" = Field(None)
    Visit: "CancelVisit" = Field(None)


class CancelMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["CancelMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["CancelMetaLog"] = Field(None)
    Message: "CancelMetaMessage" = Field(None)
    Source: "CancelMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "CancelMetaTransmission" = Field(None)


class CancelMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class CancelMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CancelMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class CancelPatient(RedoxAbstractModel):

    Contacts: List["CancelPatientContact"] = Field(None)
    Demographics: "CancelPatientDemographics" = Field(None)
    Guarantor: "CancelPatientGuarantor" = Field(None)
    Identifiers: List["CancelPatientIdentifier"] = Field(...)
    Insurances: List["CancelPatientInsurance"] = Field(None)
    Notes: List[str] = Field(None)


class CancelPatientContact(RedoxAbstractModel):

    Address: "CancelPatientContactAddress" = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "CancelPatientContactPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    Roles: List[str] = Field(None)


class CancelPatientContactAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientContactPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CancelPatientDemographics(RedoxAbstractModel):

    Address: "CancelPatientDemographicsAddress" = Field(None)
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
    PhoneNumber: "CancelPatientDemographicsPhoneNumber" = Field(None)
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class CancelPatientDemographicsAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientDemographicsPhoneNumber(RedoxAbstractModel):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class CancelPatientGuarantor(RedoxAbstractModel):

    Address: "CancelPatientGuarantorAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    EmailAddresses: List[str] = Field(None)
    Employer: "CancelPatientGuarantorEmployer" = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Number: Union[str, None] = Field(None)
    PhoneNumber: "CancelPatientGuarantorPhoneNumber" = Field(None)
    RelationToPatient: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)
    Spouse: "CancelPatientGuarantorSpouse" = Field(None)
    Type: Union[str, None] = Field(None)


class CancelPatientGuarantorAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientGuarantorEmployer(RedoxAbstractModel):

    Address: "CancelPatientGuarantorEmployerAddress" = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class CancelPatientGuarantorEmployerAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientGuarantorPhoneNumber(RedoxAbstractModel):

    Business: Union[str, None] = Field(None)
    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)


class CancelPatientGuarantorSpouse(RedoxAbstractModel):

    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)


class CancelPatientIdentifier(RedoxAbstractModel):

    ID: str = Field(...)
    IDType: str = Field(...)


class CancelPatientInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "CancelPatientInsuranceCompany" = Field(None)
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    Insured: "CancelPatientInsuranceInsured" = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "CancelPatientInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class CancelPatientInsuranceCompany(RedoxAbstractModel):

    Address: "CancelPatientInsuranceCompanyAddress" = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class CancelPatientInsuranceCompanyAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientInsuranceInsured(RedoxAbstractModel):

    Address: "CancelPatientInsuranceInsuredAddress" = Field(None)
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    Identifiers: List["CancelPatientInsuranceInsuredIdentifier"] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    Relationship: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class CancelPatientInsuranceInsuredAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelPatientInsuranceInsuredIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class CancelPatientInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelReferral(RedoxAbstractModel):

    AlternateID: Union[str, None] = Field(None)
    Authorization: "CancelReferralAuthorization" = Field(None)
    Category: Union[str, None] = Field(None)
    DateTime: Union[str, None] = Field(None)
    DepartmentSpecialty: Union[str, None] = Field(None)
    Diagnoses: List["CancelReferralDiagnosis"] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Priority: Union[str, None] = Field(None)
    Procedures: List["CancelReferralProcedure"] = Field(None)
    ProcessDateTime: Union[str, None] = Field(None)
    ProviderSpecialty: Union[str, None] = Field(None)
    Providers: List["CancelReferralProvider"] = Field(None)
    Reason: Union[str, None] = Field(None)
    Status: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Visit: "CancelReferralVisit" = Field(None)


class CancelReferralAuthorization(RedoxAbstractModel):

    AuthorizedTreatmentCount: Union[str, None] = Field(None)
    Company: "CancelReferralAuthorizationCompany" = Field(None)
    DateTime: Union[str, None] = Field(None)
    ExpirationDateTime: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Number: Union[str, None] = Field(None)
    Plan: "CancelReferralAuthorizationPlan" = Field(None)
    ReimbursementLimit: Union[str, None] = Field(None)
    RequestedTreatmentCount: Union[str, None] = Field(None)
    RequestedTreatmentUnits: Union[str, None] = Field(None)


class CancelReferralAuthorizationCompany(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelReferralAuthorizationPlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class CancelReferralDiagnosis(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    DocumentedDateTime: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Notes: List[str] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelReferralProcedure(RedoxAbstractModel):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Notes: List[str] = Field(None)
    Quantity: Union[str, None] = Field(None)
    Units: Union[str, None] = Field(None)


class CancelReferralProvider(RedoxAbstractModel):

    Address: "CancelReferralProviderAddress" = Field(None)
    ContactInfo: Union[str, None] = Field(None)
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "CancelReferralProviderLocation" = Field(None)
    PhoneNumber: "CancelReferralProviderPhoneNumber" = Field(None)
    Type: Union[str, None] = Field(None)


class CancelReferralProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class CancelReferralProviderLocation(RedoxAbstractModel):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class CancelReferralProviderPhoneNumber(RedoxAbstractModel):

    Office: Union[str, None] = Field(None)


class CancelReferralVisit(RedoxAbstractModel):

    VisitNumber: Union[str, None] = Field(None)


class CancelVisit(RedoxAbstractModel):

    VisitNumber: Union[str, None] = Field(None)


Cancel.update_forward_refs()
CancelMeta.update_forward_refs()
CancelPatient.update_forward_refs()
CancelPatientContact.update_forward_refs()
CancelPatientDemographics.update_forward_refs()
CancelPatientGuarantor.update_forward_refs()
CancelPatientGuarantorEmployer.update_forward_refs()
CancelPatientInsurance.update_forward_refs()
CancelPatientInsuranceCompany.update_forward_refs()
CancelPatientInsuranceInsured.update_forward_refs()
CancelReferral.update_forward_refs()
CancelReferralAuthorization.update_forward_refs()
CancelReferralProvider.update_forward_refs()
