"Main interface for s3 service ServiceResource"
from datetime import datetime
import sys
from typing import Any, Callable, Dict, IO, List, Union
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from boto3.s3.transfer import TransferConfig
from botocore.client import BaseClient

# pylint: disable=import-self
import mypy_boto3_s3.service_resource as service_resource_scope
from mypy_boto3_s3.type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccessControlPolicyTypeDef,
    BucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusTypeDef,
    CORSConfigurationTypeDef,
    CompleteMultipartUploadOutputTypeDef,
    CompletedMultipartUploadTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    CreateMultipartUploadOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteTypeDef,
    GetObjectOutputTypeDef,
    HeadObjectOutputTypeDef,
    LifecycleConfigurationTypeDef,
    NotificationConfigurationTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectOutputTypeDef,
    RequestPaymentConfigurationTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    TaggingTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "S3ServiceResource",
    "Bucket",
    "BucketAcl",
    "BucketCors",
    "BucketLifecycle",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "BucketNotification",
    "BucketPolicy",
    "BucketRequestPayment",
    "BucketTagging",
    "BucketVersioning",
    "BucketWebsite",
    "MultipartUpload",
    "MultipartUploadPart",
    "Object",
    "ObjectAcl",
    "ObjectSummary",
    "ObjectVersion",
    "ServiceResourceBucketsCollection",
    "BucketMultipartUploadsCollection",
    "BucketObjectVersionsCollection",
    "BucketObjectsCollection",
    "MultipartUploadPartsCollection",
)


class S3ServiceResource(Boto3ServiceResource):
    """
    [S3.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource)
    """

    buckets: service_resource_scope.ServiceResourceBucketsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Bucket(self, name: str) -> service_resource_scope.Bucket:
        """
        [ServiceResource.Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.Bucket)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketAcl(self, bucket_name: str) -> service_resource_scope.BucketAcl:
        """
        [ServiceResource.BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketCors(self, bucket_name: str) -> service_resource_scope.BucketCors:
        """
        [ServiceResource.BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketCors)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketLifecycle(self, bucket_name: str) -> service_resource_scope.BucketLifecycle:
        """
        [ServiceResource.BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketLifecycleConfiguration(
        self, bucket_name: str
    ) -> service_resource_scope.BucketLifecycleConfiguration:
        """
        [ServiceResource.BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketLogging(self, bucket_name: str) -> service_resource_scope.BucketLogging:
        """
        [ServiceResource.BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketNotification(self, bucket_name: str) -> service_resource_scope.BucketNotification:
        """
        [ServiceResource.BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketPolicy(self, bucket_name: str) -> service_resource_scope.BucketPolicy:
        """
        [ServiceResource.BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketRequestPayment(self, bucket_name: str) -> service_resource_scope.BucketRequestPayment:
        """
        [ServiceResource.BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketTagging(self, bucket_name: str) -> service_resource_scope.BucketTagging:
        """
        [ServiceResource.BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketVersioning(self, bucket_name: str) -> service_resource_scope.BucketVersioning:
        """
        [ServiceResource.BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def BucketWebsite(self, bucket_name: str) -> service_resource_scope.BucketWebsite:
        """
        [ServiceResource.BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MultipartUpload(
        self, bucket_name: str, object_key: str, id: str
    ) -> service_resource_scope.MultipartUpload:
        """
        [ServiceResource.MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> service_resource_scope.MultipartUploadPart:
        """
        [ServiceResource.MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Object(self, bucket_name: str, key: str) -> service_resource_scope.Object:
        """
        [ServiceResource.Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.Object)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ObjectAcl(self, bucket_name: str, object_key: str) -> service_resource_scope.ObjectAcl:
        """
        [ServiceResource.ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ObjectSummary(self, bucket_name: str, key: str) -> service_resource_scope.ObjectSummary:
        """
        [ServiceResource.ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ObjectVersion(
        self, bucket_name: str, object_key: str, id: str
    ) -> service_resource_scope.ObjectVersion:
        """
        [ServiceResource.ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_bucket(
        self,
        Bucket: str,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> CreateBucketOutputTypeDef:
        """
        [ServiceResource.create_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.create_bucket)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        """


class Bucket(Boto3ServiceResource):
    """
    [Bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.Bucket)
    """

    creation_date: datetime
    name: str
    multipart_uploads: service_resource_scope.BucketMultipartUploadsCollection
    object_versions: service_resource_scope.BucketObjectVersionsCollection
    objects: service_resource_scope.BucketObjectsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy(
        self,
        CopySource: CopySourceTypeDef,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        ObjectLockEnabledForBucket: bool = None,
    ) -> CreateBucketOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_objects(
        self,
        Delete: DeleteTypeDef,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectsOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_file(
        self,
        Key: str,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_fileobj(
        self,
        Key: str,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_object(
        self,
        Key: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_file(
        self,
        Filename: str,
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        Key: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_not_exists(self) -> None:
        pass


class BucketAcl(Boto3ServiceResource):
    """
    [BucketAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(
        self,
        ACL: Literal["private", "public-read", "public-read-write", "authenticated-read"] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketCors(Boto3ServiceResource):
    """
    [BucketCors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketCors)
    """

    cors_rules: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, CORSConfiguration: CORSConfigurationTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketLifecycle(Boto3ServiceResource):
    """
    [BucketLifecycle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    """

    rules: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, LifecycleConfiguration: LifecycleConfigurationTypeDef = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketLifecycleConfiguration(Boto3ServiceResource):
    """
    [BucketLifecycleConfiguration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    """

    rules: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, LifecycleConfiguration: BucketLifecycleConfigurationTypeDef = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketLogging(Boto3ServiceResource):
    """
    [BucketLogging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    """

    logging_enabled: Dict[str, Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, BucketLoggingStatus: BucketLoggingStatusTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketNotification(Boto3ServiceResource):
    """
    [BucketNotification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    """

    topic_configurations: List[Any]
    queue_configurations: List[Any]
    lambda_function_configurations: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, NotificationConfiguration: NotificationConfigurationTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketPolicy(Boto3ServiceResource):
    """
    [BucketPolicy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    """

    policy: str
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, Policy: str, ConfirmRemoveSelfBucketAccess: bool = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketRequestPayment(Boto3ServiceResource):
    """
    [BucketRequestPayment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    """

    payer: str
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketTagging(Boto3ServiceResource):
    """
    [BucketTagging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    """

    tag_set: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, Tagging: TaggingTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class BucketVersioning(Boto3ServiceResource):
    """
    [BucketVersioning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    """

    status: str
    mfa_delete: str
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable(
        self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def suspend(
        self, VersioningConfiguration: VersioningConfigurationTypeDef, MFA: str = None
    ) -> None:
        pass


class BucketWebsite(Boto3ServiceResource):
    """
    [BucketWebsite documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    """

    redirect_all_requests_to: Dict[str, Any]
    index_document: Dict[str, Any]
    error_document: Dict[str, Any]
    routing_rules: List[Any]
    bucket_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, WebsiteConfiguration: WebsiteConfigurationTypeDef) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class MultipartUpload(Boto3ServiceResource):
    """
    [MultipartUpload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    """

    upload_id: str
    key: str
    initiated: datetime
    storage_class: str
    owner: Dict[str, Any]
    initiator: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str
    parts: service_resource_scope.MultipartUploadPartsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def abort(self, RequestPayer: Literal["requester"] = None) -> AbortMultipartUploadOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def complete(
        self,
        MultipartUpload: CompletedMultipartUploadTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> CompleteMultipartUploadOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass


class MultipartUploadPart(Boto3ServiceResource):
    """
    [MultipartUploadPart documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    """

    last_modified: datetime
    e_tag: str
    size: int
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_from(
        self,
        CopySource: str,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        CopySourceRange: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
    ) -> UploadPartCopyOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload(
        self,
        Body: Union[bytes, IO] = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
    ) -> UploadPartOutputTypeDef:
        pass


class Object(Boto3ServiceResource):
    """
    [Object documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.Object)
    """

    delete_marker: bool
    accept_ranges: str
    expiration: str
    restore: str
    last_modified: datetime
    content_length: int
    e_tag: str
    missing_meta: int
    version_id: str
    cache_control: str
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    expires: datetime
    website_redirect_location: str
    server_side_encryption: str
    metadata: Dict[str, Any]
    sse_customer_algorithm: str
    sse_customer_key_md5: str
    ssekms_key_id: str
    storage_class: str
    request_charged: str
    replication_status: str
    parts_count: int
    object_lock_mode: str
    object_lock_retain_until_date: datetime
    object_lock_legal_hold_status: str
    bucket_name: str
    key: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy(
        self,
        CopySource: CopySourceTypeDef,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        SourceClient: BaseClient = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_from(
        self,
        CopySource: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: Literal["COPY", "REPLACE"] = None,
        TaggingDirective: Literal["COPY", "REPLACE"] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CopyObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def download_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_multipart_upload(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CreateMultipartUploadOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> RestoreObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_file(
        self,
        Filename: str,
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def upload_fileobj(
        self,
        Fileobj: IO[Any],
        ExtraArgs: Dict[str, Any] = None,
        Callback: Callable[..., Any] = None,
        Config: TransferConfig = None,
    ) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_not_exists(self) -> None:
        pass


class ObjectAcl(Boto3ServiceResource):
    """
    [ObjectAcl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    """

    owner: Dict[str, Any]
    grants: List[Any]
    request_charged: str
    bucket_name: str
    object_key: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        AccessControlPolicy: AccessControlPolicyTypeDef = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWrite: str = None,
        GrantWriteACP: str = None,
        RequestPayer: Literal["requester"] = None,
        VersionId: str = None,
    ) -> PutObjectAclOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass


class ObjectSummary(Boto3ServiceResource):
    """
    [ObjectSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    """

    last_modified: datetime
    e_tag: str
    size: int
    storage_class: str
    owner: Dict[str, Any]
    bucket_name: str
    key: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def copy_from(
        self,
        CopySource: str,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        CopySourceIfMatch: str = None,
        CopySourceIfModifiedSince: datetime = None,
        CopySourceIfNoneMatch: str = None,
        CopySourceIfUnmodifiedSince: datetime = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        MetadataDirective: Literal["COPY", "REPLACE"] = None,
        TaggingDirective: Literal["COPY", "REPLACE"] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        CopySourceSSECustomerAlgorithm: str = None,
        CopySourceSSECustomerKey: str = None,
        CopySourceSSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CopyObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(
        self,
        MFA: str = None,
        VersionId: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        VersionId: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def initiate_multipart_upload(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> CreateMultipartUploadOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(
        self,
        ACL: Literal[
            "private",
            "public-read",
            "public-read-write",
            "authenticated-read",
            "aws-exec-read",
            "bucket-owner-read",
            "bucket-owner-full-control",
        ] = None,
        Body: Union[bytes, IO] = None,
        CacheControl: str = None,
        ContentDisposition: str = None,
        ContentEncoding: str = None,
        ContentLanguage: str = None,
        ContentLength: int = None,
        ContentMD5: str = None,
        ContentType: str = None,
        Expires: datetime = None,
        GrantFullControl: str = None,
        GrantRead: str = None,
        GrantReadACP: str = None,
        GrantWriteACP: str = None,
        Metadata: Dict[str, str] = None,
        ServerSideEncryption: Literal["AES256", "aws:kms"] = None,
        StorageClass: Literal[
            "STANDARD",
            "REDUCED_REDUNDANCY",
            "STANDARD_IA",
            "ONEZONE_IA",
            "INTELLIGENT_TIERING",
            "GLACIER",
            "DEEP_ARCHIVE",
        ] = None,
        WebsiteRedirectLocation: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        SSEKMSKeyId: str = None,
        SSEKMSEncryptionContext: str = None,
        RequestPayer: Literal["requester"] = None,
        Tagging: str = None,
        ObjectLockMode: Literal["GOVERNANCE", "COMPLIANCE"] = None,
        ObjectLockRetainUntilDate: datetime = None,
        ObjectLockLegalHoldStatus: Literal["ON", "OFF"] = None,
    ) -> PutObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def restore_object(
        self,
        VersionId: str = None,
        RestoreRequest: RestoreRequestTypeDef = None,
        RequestPayer: Literal["requester"] = None,
    ) -> RestoreObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_exists(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait_until_not_exists(self) -> None:
        pass


class ObjectVersion(Boto3ServiceResource):
    """
    [ObjectVersion documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    """

    e_tag: str
    size: int
    storage_class: str
    key: str
    version_id: str
    is_latest: bool
    last_modified: datetime
    owner: Dict[str, Any]
    bucket_name: str
    object_key: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(
        self,
        MFA: str = None,
        RequestPayer: Literal["requester"] = None,
        BypassGovernanceRetention: bool = None,
    ) -> DeleteObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        ResponseCacheControl: str = None,
        ResponseContentDisposition: str = None,
        ResponseContentEncoding: str = None,
        ResponseContentLanguage: str = None,
        ResponseContentType: str = None,
        ResponseExpires: datetime = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> GetObjectOutputTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def head(
        self,
        IfMatch: str = None,
        IfModifiedSince: datetime = None,
        IfNoneMatch: str = None,
        IfUnmodifiedSince: datetime = None,
        Range: str = None,
        SSECustomerAlgorithm: str = None,
        SSECustomerKey: str = None,
        SSECustomerKeyMD5: str = None,
        RequestPayer: Literal["requester"] = None,
        PartNumber: int = None,
    ) -> HeadObjectOutputTypeDef:
        pass


class ServiceResourceBucketsCollection(ResourceCollection):
    """
    [ServiceResource.buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.ServiceResource.buckets)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceBucketsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.ServiceResourceBucketsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceBucketsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceBucketsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Bucket]:
        pass


class BucketMultipartUploadsCollection(ResourceCollection):
    """
    [Bucket.multipart_uploads documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.Bucket.multipart_uploads)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.BucketMultipartUploadsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.BucketMultipartUploadsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.BucketMultipartUploadsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.BucketMultipartUploadsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.MultipartUpload]:
        pass


class BucketObjectVersionsCollection(ResourceCollection):
    """
    [Bucket.object_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.Bucket.object_versions)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.BucketObjectVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.BucketObjectVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.BucketObjectVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.BucketObjectVersionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.ObjectVersion]:
        pass


class BucketObjectsCollection(ResourceCollection):
    """
    [Bucket.objects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.Bucket.objects)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.BucketObjectsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.BucketObjectsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.BucketObjectsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.BucketObjectsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.ObjectSummary]:
        pass


class MultipartUploadPartsCollection(ResourceCollection):
    """
    [MultipartUpload.parts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/s3.html#S3.MultipartUpload.parts)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.MultipartUploadPartsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        cls,
        Delimiter: str = None,
        EncodingType: str = None,
        KeyMarker: str = None,
        MaxUploads: int = None,
        Prefix: str = None,
        UploadIdMarker: str = None,
    ) -> service_resource_scope.MultipartUploadPartsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.MultipartUploadPartsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.MultipartUploadPartsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.MultipartUploadPart]:
        pass
