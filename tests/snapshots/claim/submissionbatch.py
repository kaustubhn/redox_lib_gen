# -*- coding: utf-8 -*-
# ----  AUTO-GENERATED BY redox_lib_gen. DO NOT MODIFY MANUALLY!!  ---- #

from typing import List, Union

from pydantic import Field

from ..abstract_base import EventTypeAbstractModel, RedoxAbstractModel
from ..field_types import Number


class SubmissionBatch(EventTypeAbstractModel):

    Meta: "SubmissionBatchMeta" = Field(...)
    Transactions: List["SubmissionBatchTransaction"] = Field(None)


class SubmissionBatchMeta(RedoxAbstractModel):

    DataModel: str = Field(...)
    Destinations: List["SubmissionBatchMetaDestination"] = Field(None)
    EventDateTime: Union[str, None] = Field(None)
    EventType: str = Field(...)
    FacilityCode: Union[str, None] = Field(None)
    Logs: List["SubmissionBatchMetaLog"] = Field(None)
    Message: "SubmissionBatchMetaMessage" = Field(None)
    Source: "SubmissionBatchMetaSource" = Field(None)
    Test: Union[bool, None] = Field(None)
    Transmission: "SubmissionBatchMetaTransmission" = Field(None)


class SubmissionBatchMetaDestination(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SubmissionBatchMetaLog(RedoxAbstractModel):

    AttemptID: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class SubmissionBatchMetaMessage(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class SubmissionBatchMetaSource(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)


class SubmissionBatchMetaTransmission(RedoxAbstractModel):

    ID: Union[Number, None] = Field(None)


class SubmissionBatchTransaction(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Receiver: "SubmissionBatchTransactionReceiver" = Field(None)
    Submissions: List["SubmissionBatchTransactionSubmission"] = Field(None)
    Submitter: "SubmissionBatchTransactionSubmitter" = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionReceiver(RedoxAbstractModel):

    Address: "SubmissionBatchTransactionReceiverAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    Identifiers: List["SubmissionBatchTransactionReceiverIdentifier"] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "SubmissionBatchTransactionReceiverPhoneNumber" = Field(None)


class SubmissionBatchTransactionReceiverAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionReceiverIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionReceiverPhoneNumber(RedoxAbstractModel):

    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmission(RedoxAbstractModel):

    BillingProvider: "SubmissionBatchTransactionSubmissionBillingProvider" = Field(None)
    Subscribers: List["SubmissionBatchTransactionSubmissionSubscriber"] = Field(None)


class SubmissionBatchTransactionSubmissionBillingProvider(RedoxAbstractModel):

    Address: "SubmissionBatchTransactionSubmissionBillingProviderAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    Identifiers: List[
        "SubmissionBatchTransactionSubmissionBillingProviderIdentifier"
    ] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "SubmissionBatchTransactionSubmissionBillingProviderPhoneNumber" = (
        Field(None)
    )
    Specialty: "SubmissionBatchTransactionSubmissionBillingProviderSpecialty" = Field(
        None
    )


class SubmissionBatchTransactionSubmissionBillingProviderAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionBillingProviderIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionBillingProviderPhoneNumber(
    RedoxAbstractModel
):

    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionBillingProviderSpecialty(RedoxAbstractModel):

    Description: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriber(RedoxAbstractModel):

    Demographics: "SubmissionBatchTransactionSubmissionSubscriberDemographics" = Field(
        None
    )
    Identifiers: List[
        "SubmissionBatchTransactionSubmissionSubscriberIdentifier"
    ] = Field(None)
    Insurance: "SubmissionBatchTransactionSubmissionSubscriberInsurance" = Field(None)
    OrganizationName: Union[str, None] = Field(None)
    Patients: List["SubmissionBatchTransactionSubmissionSubscriberPatient"] = Field(
        None
    )
    ResponsibilityLevel: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberDemographics(RedoxAbstractModel):

    Address: "SubmissionBatchTransactionSubmissionSubscriberDemographicsAddress" = (
        Field(None)
    )
    DOB: Union[str, None] = Field(None)
    FirstName: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    MiddleName: Union[str, None] = Field(None)
    PhoneNumber: "SubmissionBatchTransactionSubmissionSubscriberDemographicsPhoneNumber" = Field(
        None
    )
    Sex: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberDemographicsAddress(
    RedoxAbstractModel
):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberDemographicsPhoneNumber(
    RedoxAbstractModel
):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberInsurance(RedoxAbstractModel):

    AgreementType: Union[str, None] = Field(None)
    Company: "SubmissionBatchTransactionSubmissionSubscriberInsuranceCompany" = Field(
        None
    )
    CoverageType: Union[str, None] = Field(None)
    EffectiveDate: Union[str, None] = Field(None)
    ExpirationDate: Union[str, None] = Field(None)
    GroupName: Union[str, None] = Field(None)
    GroupNumber: Union[str, None] = Field(None)
    MemberNumber: Union[str, None] = Field(None)
    Plan: "SubmissionBatchTransactionSubmissionSubscriberInsurancePlan" = Field(None)
    PolicyNumber: Union[str, None] = Field(None)
    Priority: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberInsuranceCompany(
    RedoxAbstractModel
):

    Address: "SubmissionBatchTransactionSubmissionSubscriberInsuranceCompanyAddress" = (
        Field(None)
    )
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberInsuranceCompanyAddress(
    RedoxAbstractModel
):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberInsurancePlan(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    Name: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatient(RedoxAbstractModel):

    Claims: List["SubmissionBatchTransactionSubmissionSubscriberPatientClaim"] = Field(
        None
    )
    Demographics: "SubmissionBatchTransactionSubmissionSubscriberPatientDemographics" = Field(
        None
    )
    Identifiers: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientIdentifier"
    ] = Field(None)
    Notes: List[str] = Field(None)
    RelationToSubscriber: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaim(RedoxAbstractModel):

    AdditionalDates: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimAdditionalDate"
    ] = Field(None)
    BenefitsAssignmentCode: Union[bool, None] = Field(None)
    CopayAmount: Union[str, None] = Field(None)
    Diagnoses: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimDiagnosis"
    ] = Field(None)
    DiagnosisRelatedGroup: Union[str, None] = Field(None)
    IsProviderSignatureOnFile: Union[bool, None] = Field(None)
    IsReleaseOfInformationOnFile: Union[bool, None] = Field(None)
    ProviderAcceptanceCode: Union[str, None] = Field(None)
    Providers: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimProvider"
    ] = Field(None)
    ReferenceNumbers: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimReferenceNumber"
    ] = Field(None)
    Services: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimService"
    ] = Field(None)
    SubmissionNumber: Union[str, None] = Field(None)
    TotalAmount: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)
    Visit: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisit" = Field(
        None
    )


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimAdditionalDate(
    RedoxAbstractModel
):

    DateTime: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimDiagnosis(
    RedoxAbstractModel
):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimProvider(
    RedoxAbstractModel
):

    Address: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderAddress" = Field(
        None
    )
    Credentials: List[str] = Field(None)
    EmailAddresses: List[str] = Field(None)
    FirstName: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)
    LastName: Union[str, None] = Field(None)
    Location: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderLocation" = Field(
        None
    )
    PhoneNumber: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderPhoneNumber" = Field(
        None
    )
    Role: Union[str, None] = Field(None)
    Specialty: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderSpecialty" = Field(
        None
    )


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderAddress(
    RedoxAbstractModel
):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderLocation(
    RedoxAbstractModel
):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderPhoneNumber(
    RedoxAbstractModel
):

    Office: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimProviderSpecialty(
    RedoxAbstractModel
):

    Description: Union[str, None] = Field(None)
    ID: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimReferenceNumber(
    RedoxAbstractModel
):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimService(
    RedoxAbstractModel
):

    Amount: Union[str, None] = Field(None)
    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Diagnoses: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDiagnosis"
    ] = Field(None)
    Drug: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDrug" = (
        Field(None)
    )
    EndDateTime: Union[str, None] = Field(None)
    IsEmergency: Union[bool, None] = Field(None)
    Modifiers: List[str] = Field(None)
    Notes: Union[str, None] = Field(None)
    Quantity: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceQuantity" = Field(
        None
    )
    ReferenceNumbers: List[
        "SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceReferenceNumber"
    ] = Field(None)
    RevenueCode: Union[str, None] = Field(None)
    StartDateTime: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDiagnosis(
    RedoxAbstractModel
):

    Code: Union[str, None] = Field(None)
    Codeset: Union[str, None] = Field(None)
    Description: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDrug(
    RedoxAbstractModel
):

    NDC: Union[str, None] = Field(None)
    PrescriptionID: Union[str, None] = Field(None)
    Quantity: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDrugQuantity" = Field(
        None
    )


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDrugQuantity(
    RedoxAbstractModel
):

    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceQuantity(
    RedoxAbstractModel
):

    Units: Union[str, None] = Field(None)
    Value: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceReferenceNumber(
    RedoxAbstractModel
):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisit(
    RedoxAbstractModel
):

    DateTime: Union[str, None] = Field(None)
    DischargeDateTime: Union[str, None] = Field(None)
    Location: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisitLocation" = Field(
        None
    )
    PreviousLocation: "SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisitPreviousLocation" = Field(
        None
    )
    Type: Union[str, None] = Field(None)
    VisitNumber: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisitLocation(
    RedoxAbstractModel
):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisitPreviousLocation(
    RedoxAbstractModel
):

    Department: Union[str, None] = Field(None)
    Facility: Union[str, None] = Field(None)
    Room: Union[str, None] = Field(None)
    Type: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientDemographics(
    RedoxAbstractModel
):

    Address: "SubmissionBatchTransactionSubmissionSubscriberPatientDemographicsAddress" = Field(
        None
    )
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
    PhoneNumber: "SubmissionBatchTransactionSubmissionSubscriberPatientDemographicsPhoneNumber" = Field(
        None
    )
    Race: Union[str, None] = Field(None)
    Religion: Union[str, None] = Field(None)
    SSN: Union[str, None] = Field(None)
    Sex: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientDemographicsAddress(
    RedoxAbstractModel
):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientDemographicsPhoneNumber(
    RedoxAbstractModel
):

    Home: Union[str, None] = Field(None)
    Mobile: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmissionSubscriberPatientIdentifier(
    RedoxAbstractModel
):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmitter(RedoxAbstractModel):

    Address: "SubmissionBatchTransactionSubmitterAddress" = Field(None)
    EmailAddress: Union[str, None] = Field(None)
    Identifiers: List["SubmissionBatchTransactionSubmitterIdentifier"] = Field(None)
    Name: Union[str, None] = Field(None)
    PhoneNumber: "SubmissionBatchTransactionSubmitterPhoneNumber" = Field(None)


class SubmissionBatchTransactionSubmitterAddress(RedoxAbstractModel):

    City: Union[str, None] = Field(None)
    Country: Union[str, None] = Field(None)
    County: Union[str, None] = Field(None)
    State: Union[str, None] = Field(None)
    StreetAddress: Union[str, None] = Field(None)
    ZIP: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmitterIdentifier(RedoxAbstractModel):

    ID: Union[str, None] = Field(None)
    IDType: Union[str, None] = Field(None)


class SubmissionBatchTransactionSubmitterPhoneNumber(RedoxAbstractModel):

    Fax: Union[str, None] = Field(None)
    Office: Union[str, None] = Field(None)


SubmissionBatch.update_forward_refs()
SubmissionBatchMeta.update_forward_refs()
SubmissionBatchTransaction.update_forward_refs()
SubmissionBatchTransactionReceiver.update_forward_refs()
SubmissionBatchTransactionSubmission.update_forward_refs()
SubmissionBatchTransactionSubmissionBillingProvider.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriber.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberDemographics.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberInsurance.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberInsuranceCompany.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatient.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientClaim.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientClaimProvider.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientClaimService.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientClaimServiceDrug.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientClaimVisit.update_forward_refs()
SubmissionBatchTransactionSubmissionSubscriberPatientDemographics.update_forward_refs()
SubmissionBatchTransactionSubmitter.update_forward_refs()
