"Main interface for sns service ServiceResource"
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

# pylint: disable=import-self
import mypy_boto3_sns.service_resource as service_resource_scope
from mypy_boto3_sns.type_defs import (
    ConfirmSubscriptionResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreatePlatformApplicationResponseTypeDef,
    CreateTopicResponseTypeDef,
    MessageAttributeValueTypeDef,
    PublishResponseTypeDef,
    SubscribeResponseTypeDef,
    TagTypeDef,
)


__all__ = (
    "SNSServiceResource",
    "PlatformApplication",
    "PlatformEndpoint",
    "Subscription",
    "Topic",
    "ServiceResourcePlatformApplicationsCollection",
    "ServiceResourceSubscriptionsCollection",
    "ServiceResourceTopicsCollection",
    "PlatformApplicationEndpointsCollection",
    "TopicSubscriptionsCollection",
)


class SNSServiceResource(Boto3ServiceResource):
    """
    [SNS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource)
    """

    platform_applications: service_resource_scope.ServiceResourcePlatformApplicationsCollection
    subscriptions: service_resource_scope.ServiceResourceSubscriptionsCollection
    topics: service_resource_scope.ServiceResourceTopicsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlatformApplication(self, arn: str) -> service_resource_scope.PlatformApplication:
        """
        [ServiceResource.PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PlatformEndpoint(self, arn: str) -> service_resource_scope.PlatformEndpoint:
        """
        [ServiceResource.PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Subscription(self, arn: str) -> service_resource_scope.Subscription:
        """
        [ServiceResource.Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.Subscription)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Topic(self, arn: str) -> service_resource_scope.Topic:
        """
        [ServiceResource.Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.Topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> CreatePlatformApplicationResponseTypeDef:
        """
        [ServiceResource.create_platform_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.create_platform_application)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_topic(
        self, Name: str, Attributes: Dict[str, str] = None, Tags: List[TagTypeDef] = None
    ) -> CreateTopicResponseTypeDef:
        """
        [ServiceResource.create_topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.create_topic)
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.get_available_subresources)
        """


class PlatformApplication(Boto3ServiceResource):
    """
    [PlatformApplication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.PlatformApplication)
    """

    attributes: Dict[str, Any]
    arn: str
    endpoints: service_resource_scope.PlatformApplicationEndpointsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_endpoint(
        self, Token: str, CustomUserData: str = None, Attributes: Dict[str, str] = None
    ) -> CreateEndpointResponseTypeDef:
        pass

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
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        pass


class PlatformEndpoint(Boto3ServiceResource):
    """
    [PlatformEndpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.PlatformEndpoint)
    """

    attributes: Dict[str, Any]
    arn: str

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
    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    ) -> PublishResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, Attributes: Dict[str, str]) -> None:
        pass


class Subscription(Boto3ServiceResource):
    """
    [Subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.Subscription)
    """

    attributes: Dict[str, Any]
    arn: str

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
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass


class Topic(Boto3ServiceResource):
    """
    [Topic documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.Topic)
    """

    attributes: Dict[str, Any]
    arn: str
    subscriptions: service_resource_scope.TopicSubscriptionsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(self, Label: str, AWSAccountId: List[str], ActionName: List[str]) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_subscription(
        self, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ConfirmSubscriptionResponseTypeDef:
        pass

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
    def publish(
        self,
        Message: str,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
    ) -> PublishResponseTypeDef:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, Label: str) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_attributes(self, AttributeName: str, AttributeValue: str = None) -> None:
        pass

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe(
        self,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> SubscribeResponseTypeDef:
        pass


class ServiceResourcePlatformApplicationsCollection(ResourceCollection):
    """
    [ServiceResource.platform_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.platform_applications)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourcePlatformApplicationsCollection:
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
    ) -> service_resource_scope.ServiceResourcePlatformApplicationsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(
        cls, count: int
    ) -> service_resource_scope.ServiceResourcePlatformApplicationsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(
        cls, count: int
    ) -> service_resource_scope.ServiceResourcePlatformApplicationsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.PlatformApplication]:
        pass


class ServiceResourceSubscriptionsCollection(ResourceCollection):
    """
    [ServiceResource.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.subscriptions)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceSubscriptionsCollection:
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
    ) -> service_resource_scope.ServiceResourceSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Subscription]:
        pass


class ServiceResourceTopicsCollection(ResourceCollection):
    """
    [ServiceResource.topics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.ServiceResource.topics)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.ServiceResourceTopicsCollection:
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
    ) -> service_resource_scope.ServiceResourceTopicsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.ServiceResourceTopicsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.ServiceResourceTopicsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Topic]:
        pass


class PlatformApplicationEndpointsCollection(ResourceCollection):
    """
    [PlatformApplication.endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.PlatformApplication.endpoints)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.PlatformApplicationEndpointsCollection:
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
    ) -> service_resource_scope.PlatformApplicationEndpointsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.PlatformApplicationEndpointsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.PlatformApplicationEndpointsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.PlatformEndpoint]:
        pass


class TopicSubscriptionsCollection(ResourceCollection):
    """
    [Topic.subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.39/reference/services/sns.html#SNS.Topic.subscriptions)
    """

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(cls) -> service_resource_scope.TopicSubscriptionsCollection:
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
    ) -> service_resource_scope.TopicSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(cls, count: int) -> service_resource_scope.TopicSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(cls, count: int) -> service_resource_scope.TopicSubscriptionsCollection:
        pass

    @classmethod
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(cls) -> List[service_resource_scope.Subscription]:
        pass
