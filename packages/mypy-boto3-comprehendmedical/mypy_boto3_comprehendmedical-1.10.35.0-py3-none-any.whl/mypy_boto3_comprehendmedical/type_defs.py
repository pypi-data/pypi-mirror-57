"Main interface for comprehendmedical service type defs"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


ComprehendMedicalAsyncJobFilterTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict("_RequiredInputDataConfigTypeDef", {"S3Bucket": str})
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef", {"S3Key": str}, total=False
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


_RequiredOutputDataConfigTypeDef = TypedDict("_RequiredOutputDataConfigTypeDef", {"S3Bucket": str})
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef", {"S3Key": str}, total=False
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


ComprehendMedicalAsyncJobPropertiesTypeDef = TypedDict(
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "PARTIAL_SUCCESS",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "ExpirationTime": datetime,
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "LanguageCode": Literal["en"],
        "DataAccessRoleArn": str,
        "ManifestFilePath": str,
        "KMSKey": str,
        "ModelVersion": str,
    },
    total=False,
)

DescribeEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef},
    total=False,
)

DescribePHIDetectionJobResponseTypeDef = TypedDict(
    "DescribePHIDetectionJobResponseTypeDef",
    {"ComprehendMedicalAsyncJobProperties": ComprehendMedicalAsyncJobPropertiesTypeDef},
    total=False,
)

TraitTypeDef = TypedDict(
    "TraitTypeDef",
    {"Name": Literal["SIGN", "SYMPTOM", "DIAGNOSIS", "NEGATION"], "Score": float},
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List[TraitTypeDef],
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Type": Literal[
            "NAME",
            "DOSAGE",
            "ROUTE_OR_MODE",
            "FORM",
            "FREQUENCY",
            "DURATION",
            "GENERIC_NAME",
            "BRAND_NAME",
            "STRENGTH",
            "RATE",
            "ACUITY",
            "TEST_NAME",
            "TEST_VALUE",
            "TEST_UNITS",
            "PROCEDURE_NAME",
            "TREATMENT_NAME",
            "DATE",
            "AGE",
            "CONTACT_POINT",
            "EMAIL",
            "IDENTIFIER",
            "URL",
            "ADDRESS",
            "PROFESSION",
            "SYSTEM_ORGAN_SITE",
            "DIRECTION",
            "QUALITY",
            "QUANTITY",
        ],
        "Traits": List[TraitTypeDef],
        "Attributes": List[AttributeTypeDef],
    },
    total=False,
)

UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef",
    {
        "Type": Literal[
            "MEDICATION",
            "MEDICAL_CONDITION",
            "PROTECTED_HEALTH_INFORMATION",
            "TEST_TREATMENT_PROCEDURE",
            "ANATOMY",
        ],
        "Attribute": AttributeTypeDef,
    },
    total=False,
)

_RequiredDetectEntitiesResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesResponseTypeDef", {"Entities": List[EntityTypeDef], "ModelVersion": str}
)
_OptionalDetectEntitiesResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesResponseTypeDef",
    {"UnmappedAttributes": List[UnmappedAttributeTypeDef], "PaginationToken": str},
    total=False,
)


class DetectEntitiesResponseTypeDef(
    _RequiredDetectEntitiesResponseTypeDef, _OptionalDetectEntitiesResponseTypeDef
):
    pass


_RequiredDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_RequiredDetectEntitiesV2ResponseTypeDef",
    {"Entities": List[EntityTypeDef], "ModelVersion": str},
)
_OptionalDetectEntitiesV2ResponseTypeDef = TypedDict(
    "_OptionalDetectEntitiesV2ResponseTypeDef",
    {"UnmappedAttributes": List[UnmappedAttributeTypeDef], "PaginationToken": str},
    total=False,
)


class DetectEntitiesV2ResponseTypeDef(
    _RequiredDetectEntitiesV2ResponseTypeDef, _OptionalDetectEntitiesV2ResponseTypeDef
):
    pass


_RequiredDetectPHIResponseTypeDef = TypedDict(
    "_RequiredDetectPHIResponseTypeDef", {"Entities": List[EntityTypeDef], "ModelVersion": str}
)
_OptionalDetectPHIResponseTypeDef = TypedDict(
    "_OptionalDetectPHIResponseTypeDef", {"PaginationToken": str}, total=False
)


class DetectPHIResponseTypeDef(
    _RequiredDetectPHIResponseTypeDef, _OptionalDetectPHIResponseTypeDef
):
    pass


ListEntitiesDetectionV2JobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

ListPHIDetectionJobsResponseTypeDef = TypedDict(
    "ListPHIDetectionJobsResponseTypeDef",
    {
        "ComprehendMedicalAsyncJobPropertiesList": List[ComprehendMedicalAsyncJobPropertiesTypeDef],
        "NextToken": str,
    },
    total=False,
)

StartEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

StartPHIDetectionJobResponseTypeDef = TypedDict(
    "StartPHIDetectionJobResponseTypeDef", {"JobId": str}, total=False
)

StopEntitiesDetectionV2JobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionV2JobResponseTypeDef", {"JobId": str}, total=False
)

StopPHIDetectionJobResponseTypeDef = TypedDict(
    "StopPHIDetectionJobResponseTypeDef", {"JobId": str}, total=False
)
