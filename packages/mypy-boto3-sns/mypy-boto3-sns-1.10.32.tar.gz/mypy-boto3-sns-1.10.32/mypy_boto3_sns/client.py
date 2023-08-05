"Main interface for sns service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_sns.client as client_scope

# pylint: disable=import-self
import mypy_boto3_sns.paginator as paginator_scope
from mypy_boto3_sns.type_defs import (
    ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef,
    ClientConfirmSubscriptionResponseTypeDef,
    ClientCreatePlatformApplicationResponseTypeDef,
    ClientCreatePlatformEndpointResponseTypeDef,
    ClientCreateTopicResponseTypeDef,
    ClientCreateTopicTagsTypeDef,
    ClientGetEndpointAttributesResponseTypeDef,
    ClientGetPlatformApplicationAttributesResponseTypeDef,
    ClientGetSmsAttributesResponseTypeDef,
    ClientGetSubscriptionAttributesResponseTypeDef,
    ClientGetTopicAttributesResponseTypeDef,
    ClientListEndpointsByPlatformApplicationResponseTypeDef,
    ClientListPhoneNumbersOptedOutResponseTypeDef,
    ClientListPlatformApplicationsResponseTypeDef,
    ClientListSubscriptionsByTopicResponseTypeDef,
    ClientListSubscriptionsResponseTypeDef,
    ClientListTagsForResourceResponseTypeDef,
    ClientListTopicsResponseTypeDef,
    ClientPublishMessageAttributesTypeDef,
    ClientPublishResponseTypeDef,
    ClientSubscribeResponseTypeDef,
    ClientTagResourceTagsTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(
        self, TopicArn: str, Label: str, AWSAccountId: List[str], ActionName: List[str]
    ) -> None:
        """
        Adds a statement to a topic's access control policy, granting access for the specified AWS
        accounts to the specified actions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/AddPermission>`_

        **Request Syntax**
        ::

          response = client.add_permission(
              TopicArn='string',
              Label='string',
              AWSAccountId=[
                  'string',
              ],
              ActionName=[
                  'string',
              ]
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic whose access control policy you wish to modify.

        :type Label: string
        :param Label: **[REQUIRED]**

          A unique identifier for the new policy statement.

        :type AWSAccountId: list
        :param AWSAccountId: **[REQUIRED]**

          The AWS account IDs of the users (principals) who will be given access to the specified
          actions. The users must have AWS accounts, but do not need to be signed up for this
          service.

          - *(string) --*

        :type ActionName: list
        :param ActionName: **[REQUIRED]**

          The action you want to allow for the specified principal(s).

          Valid values: Any Amazon SNS action name, for example ``Publish`` .

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def check_if_phone_number_is_opted_out(
        self, phoneNumber: str
    ) -> ClientCheckIfPhoneNumberIsOptedOutResponseTypeDef:
        """
        Accepts a phone number and indicates whether the phone holder has opted out of receiving SMS
        messages from your account. You cannot send SMS messages to a number that is opted out.

        To resume sending messages, you can opt in the number by using the ``OptInPhoneNumber``
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CheckIfPhoneNumberIsOptedOut>`_

        **Request Syntax**
        ::

          response = client.check_if_phone_number_is_opted_out(
              phoneNumber='string'
          )
        :type phoneNumber: string
        :param phoneNumber: **[REQUIRED]**

          The phone number for which you want to check the opt out status.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'isOptedOut': True|False
            }
          **Response Structure**

          - *(dict) --*

            The response from the ``CheckIfPhoneNumberIsOptedOut`` action.

            - **isOptedOut** *(boolean) --*

              Indicates whether the phone number is opted out:

              * ``true`` – The phone number is opted out, meaning you cannot publish SMS messages to
              it.

              * ``false`` – The phone number is opted in, meaning you can publish SMS messages to
              it.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def confirm_subscription(
        self, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ClientConfirmSubscriptionResponseTypeDef:
        """
        Verifies an endpoint owner's intent to receive messages by validating the token sent to the
        endpoint by an earlier ``Subscribe`` action. If the token is valid, the action creates a new
        subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature
        only when the ``AuthenticateOnUnsubscribe`` flag is set to "true".

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ConfirmSubscription>`_

        **Request Syntax**
        ::

          response = client.confirm_subscription(
              TopicArn='string',
              Token='string',
              AuthenticateOnUnsubscribe='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic for which you wish to confirm a subscription.

        :type Token: string
        :param Token: **[REQUIRED]**

          Short-lived token sent to an endpoint during the ``Subscribe`` action.

        :type AuthenticateOnUnsubscribe: string
        :param AuthenticateOnUnsubscribe:

          Disallows unauthenticated unsubscribes of the subscription. If the value of this parameter
          is ``true`` and the request has an AWS signature, then only the topic owner and the
          subscription owner can unsubscribe the endpoint. The unsubscribe action requires AWS
          authentication.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SubscriptionArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ConfirmSubscriptions action.

            - **SubscriptionArn** *(string) --*

              The ARN of the created subscription.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> ClientCreatePlatformApplicationResponseTypeDef:
        """
        Creates a platform application object for one of the supported push notification services,
        such as APNS and FCM, to which devices and mobile apps may register. You must specify
        PlatformPrincipal and PlatformCredential attributes when using the
        ``CreatePlatformApplication`` action. The PlatformPrincipal is received from the
        notification service. For APNS/APNS_SANDBOX, PlatformPrincipal is "SSL certificate". For
        FCM, PlatformPrincipal is not applicable. For ADM, PlatformPrincipal is "client id". The
        PlatformCredential is also received from the notification service. For WNS,
        PlatformPrincipal is "Package Security Identifier". For MPNS, PlatformPrincipal is "TLS
        certificate". For Baidu, PlatformPrincipal is "API key".

        For APNS/APNS_SANDBOX, PlatformCredential is "private key". For FCM, PlatformCredential is
        "API key". For ADM, PlatformCredential is "client secret". For WNS, PlatformCredential is
        "secret key". For MPNS, PlatformCredential is "private key". For Baidu, PlatformCredential
        is "secret key". The PlatformApplicationArn that is returned when using
        ``CreatePlatformApplication`` is then used as an attribute for the
        ``CreatePlatformEndpoint`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreatePlatformApplication>`_

        **Request Syntax**
        ::

          response = client.create_platform_application(
              Name='string',
              Platform='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          Application names must be made up of only uppercase and lowercase ASCII letters, numbers,
          underscores, hyphens, and periods, and must be between 1 and 256 characters long.

        :type Platform: string
        :param Platform: **[REQUIRED]**

          The following platforms are supported: ADM (Amazon Device Messaging), APNS (Apple Push
          Notification Service), APNS_SANDBOX, and FCM (Firebase Cloud Messaging).

        :type Attributes: dict
        :param Attributes: **[REQUIRED]**

          For a list of attributes, see `SetPlatformApplicationAttributes
          <https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html>`__

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PlatformApplicationArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response from CreatePlatformApplication action.

            - **PlatformApplicationArn** *(string) --*

              PlatformApplicationArn is returned.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_platform_endpoint(
        self,
        PlatformApplicationArn: str,
        Token: str,
        CustomUserData: str = None,
        Attributes: Dict[str, str] = None,
    ) -> ClientCreatePlatformEndpointResponseTypeDef:
        """
        Creates an endpoint for a device and mobile app on one of the supported push notification
        services, such as FCM and APNS. ``CreatePlatformEndpoint`` requires the
        PlatformApplicationArn that is returned from ``CreatePlatformApplication`` . The EndpointArn
        that is returned when using ``CreatePlatformEndpoint`` can then be used by the ``Publish``
        action to send a message to a mobile app or by the ``Subscribe`` action for subscription to
        a topic. The ``CreatePlatformEndpoint`` action is idempotent, so if the requester already
        owns an endpoint with the same device token and attributes, that endpoint's ARN is returned
        without creating a new endpoint. For more information, see `Using Amazon SNS Mobile Push
        Notifications <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        When using ``CreatePlatformEndpoint`` with Baidu, two attributes must be provided: ChannelId
        and UserId. The token field must also contain the ChannelId. For more information, see
        `Creating an Amazon SNS Endpoint for Baidu
        <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePushBaiduEndpoint.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreatePlatformEndpoint>`_

        **Request Syntax**
        ::

          response = client.create_platform_endpoint(
              PlatformApplicationArn='string',
              Token='string',
              CustomUserData='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn returned from CreatePlatformApplication is used to create a an
          endpoint.

        :type Token: string
        :param Token: **[REQUIRED]**

          Unique identifier created by the notification service for an app on a device. The specific
          name for Token will vary, depending on which notification service is being used. For
          example, when using APNS as the notification service, you need the device token.
          Alternatively, when using FCM or ADM, the device token equivalent is called the
          registration ID.

        :type CustomUserData: string
        :param CustomUserData:

          Arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The
          data must be in UTF-8 format and less than 2KB.

        :type Attributes: dict
        :param Attributes:

          For a list of attributes, see `SetEndpointAttributes
          <https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html>`__ .

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'EndpointArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response from CreateEndpoint action.

            - **EndpointArn** *(string) --*

              EndpointArn returned from CreateEndpoint action.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_topic(
        self,
        Name: str,
        Attributes: Dict[str, str] = None,
        Tags: List[ClientCreateTopicTagsTypeDef] = None,
    ) -> ClientCreateTopicResponseTypeDef:
        """
        Creates a topic to which notifications can be published. Users can create at most 100,000
        topics. For more information, see `https\\://aws.amazon.com/sns
        <http://aws.amazon.com/sns/>`__ . This action is idempotent, so if the requester already
        owns a topic with the specified name, that topic's ARN is returned without creating a new
        topic.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/CreateTopic>`_

        **Request Syntax**
        ::

          response = client.create_topic(
              Name='string',
              Attributes={
                  'string': 'string'
              },
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the topic you want to create.

          Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters,
          numbers, underscores, and hyphens, and must be between 1 and 256 characters long.

        :type Attributes: dict
        :param Attributes:

          A map of attributes with their corresponding values.

          The following lists the names, descriptions, and values of the special request parameters
          that the ``CreateTopic`` action uses:

          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to
          HTTP/S endpoints.

          * ``DisplayName`` – The display name to use for a topic with SMS subscriptions.

          * ``Policy`` – The policy that defines who can access your topic. By default, only the
          topic owner can publish or subscribe to the topic.

          The following attribute applies only to `server-side-encryption
          <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`__ :

          * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon SNS
          or a custom CMK. For more information, see `Key Terms
          <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`__
          . For more examples, see `KeyId
          <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__
          in the *AWS Key Management Service API Reference* .

          - *(string) --*

            - *(string) --*

        :type Tags: list
        :param Tags:

          The list of tags to add to a new topic.

          .. note::

            To be able to tag a topic on creation, you must have the ``sns:CreateTopic`` and
            ``sns:TagResource`` permissions.

          - *(dict) --*

            The list of tags to be added to the specified topic.

            - **Key** *(string) --* **[REQUIRED]**

              The required key portion of the tag.

            - **Value** *(string) --* **[REQUIRED]**

              The optional value portion of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'TopicArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response from CreateTopic action.

            - **TopicArn** *(string) --*

              The Amazon Resource Name (ARN) assigned to the created topic.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_endpoint(self, EndpointArn: str) -> None:
        """
        Deletes the endpoint for a device and mobile app from Amazon SNS. This action is idempotent.
        For more information, see `Using Amazon SNS Mobile Push Notifications
        <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        When you delete an endpoint that is also subscribed to a topic, then you must also
        unsubscribe the endpoint from the topic.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeleteEndpoint>`_

        **Request Syntax**
        ::

          response = client.delete_endpoint(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          EndpointArn of endpoint to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_platform_application(self, PlatformApplicationArn: str) -> None:
        """
        Deletes a platform application object for one of the supported push notification services,
        such as APNS and FCM. For more information, see `Using Amazon SNS Mobile Push Notifications
        <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeletePlatformApplication>`_

        **Request Syntax**
        ::

          response = client.delete_platform_application(
              PlatformApplicationArn='string'
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn of platform application object to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_topic(self, TopicArn: str) -> None:
        """
        Deletes a topic and all its subscriptions. Deleting a topic might prevent some messages
        previously sent to the topic from being delivered to subscribers. This action is idempotent,
        so deleting a topic that does not exist does not result in an error.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/DeleteTopic>`_

        **Request Syntax**
        ::

          response = client.delete_topic(
              TopicArn='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic you want to delete.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_endpoint_attributes(
        self, EndpointArn: str
    ) -> ClientGetEndpointAttributesResponseTypeDef:
        """
        Retrieves the endpoint attributes for a device on one of the supported push notification
        services, such as FCM and APNS. For more information, see `Using Amazon SNS Mobile Push
        Notifications <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/GetEndpointAttributes>`_

        **Request Syntax**
        ::

          response = client.get_endpoint_attributes(
              EndpointArn='string'
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          EndpointArn for GetEndpointAttributes input.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Response from GetEndpointAttributes of the EndpointArn.

            - **Attributes** *(dict) --*

              Attributes include the following:

              * ``CustomUserData`` – arbitrary user data to associate with the endpoint. Amazon SNS
              does not use this data. The data must be in UTF-8 format and less than 2KB.

              * ``Enabled`` – flag that enables/disables delivery to the endpoint. Amazon SNS will
              set this to false when a notification service indicates to Amazon SNS that the
              endpoint is invalid. Users can set it back to true, typically after updating Token.

              * ``Token`` – device token, also referred to as a registration id, for an app and
              mobile device. This is returned from the notification service when an app and mobile
              device are registered with the notification service.

              .. note::

                 The device token for the iOS platform is returned in lowercase.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_platform_application_attributes(
        self, PlatformApplicationArn: str
    ) -> ClientGetPlatformApplicationAttributesResponseTypeDef:
        """
        Retrieves the attributes of the platform application object for the supported push
        notification services, such as APNS and FCM. For more information, see `Using Amazon SNS
        Mobile Push Notifications <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/GetPlatformApplicationAttributes>`_

        **Request Syntax**
        ::

          response = client.get_platform_application_attributes(
              PlatformApplicationArn='string'
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn for GetPlatformApplicationAttributesInput.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Response for GetPlatformApplicationAttributes action.

            - **Attributes** *(dict) --*

              Attributes include the following:

              * ``EventEndpointCreated`` – Topic ARN to which EndpointCreated event notifications
              should be sent.

              * ``EventEndpointDeleted`` – Topic ARN to which EndpointDeleted event notifications
              should be sent.

              * ``EventEndpointUpdated`` – Topic ARN to which EndpointUpdate event notifications
              should be sent.

              * ``EventDeliveryFailure`` – Topic ARN to which DeliveryFailure event notifications
              should be sent upon Direct Publish delivery failure (permanent) to one of the
              application's endpoints.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_sms_attributes(
        self, attributes: List[str] = None
    ) -> ClientGetSmsAttributesResponseTypeDef:
        """
        Returns the settings for sending SMS messages from your account.

        These settings are set with the ``SetSMSAttributes`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/GetSMSAttributes>`_

        **Request Syntax**
        ::

          response = client.get_sms_attributes(
              attributes=[
                  'string',
              ]
          )
        :type attributes: list
        :param attributes:

          A list of the individual attribute names, such as ``MonthlySpendLimit`` , for which you
          want values.

          For all attribute names, see `SetSMSAttributes
          <https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html>`__ .

          If you don't use this parameter, Amazon SNS returns all SMS attributes.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            The response from the ``GetSMSAttributes`` request.

            - **attributes** *(dict) --*

              The SMS attribute names and their values.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_subscription_attributes(
        self, SubscriptionArn: str
    ) -> ClientGetSubscriptionAttributesResponseTypeDef:
        """
        Returns all of the properties of a subscription.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/GetSubscriptionAttributes>`_

        **Request Syntax**
        ::

          response = client.get_subscription_attributes(
              SubscriptionArn='string'
          )
        :type SubscriptionArn: string
        :param SubscriptionArn: **[REQUIRED]**

          The ARN of the subscription whose properties you want to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Response for GetSubscriptionAttributes action.

            - **Attributes** *(dict) --*

              A map of the subscription's attributes. Attributes in this map include the following:

              * ``ConfirmationWasAuthenticated`` – ``true`` if the subscription confirmation request
              was authenticated.

              * ``DeliveryPolicy`` – The JSON serialization of the subscription's delivery policy.

              * ``EffectiveDeliveryPolicy`` – The JSON serialization of the effective delivery
              policy that takes into account the topic delivery policy and account system defaults.

              * ``FilterPolicy`` – The filter policy JSON that is assigned to the subscription.

              * ``Owner`` – The AWS account ID of the subscription's owner.

              * ``PendingConfirmation`` – ``true`` if the subscription hasn't been confirmed. To
              confirm a pending subscription, call the ``ConfirmSubscription`` action with a
              confirmation token.

              * ``RawMessageDelivery`` – ``true`` if raw message delivery is enabled for the
              subscription. Raw messages are free of JSON formatting and can be sent to HTTP/S and
              Amazon SQS endpoints.

              * ``RedrivePolicy`` – When specified, sends undeliverable messages to the specified
              Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors
              (for example, when the subscribed endpoint is unreachable) or server errors (for
              example, when the service that powers the subscribed endpoint becomes unavailable) are
              held in the dead-letter queue for further analysis or reprocessing.

              * ``SubscriptionArn`` – The subscription's ARN.

              * ``TopicArn`` – The topic ARN that the subscription is associated with.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_topic_attributes(self, TopicArn: str) -> ClientGetTopicAttributesResponseTypeDef:
        """
        Returns all of the properties of a topic. Topic properties returned might differ based on
        the authorization of the user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/GetTopicAttributes>`_

        **Request Syntax**
        ::

          response = client.get_topic_attributes(
              TopicArn='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic whose properties you want to get.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Attributes': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            Response for GetTopicAttributes action.

            - **Attributes** *(dict) --*

              A map of the topic's attributes. Attributes in this map include the following:

              * ``DeliveryPolicy`` – The JSON serialization of the topic's delivery policy.

              * ``DisplayName`` – The human-readable name used in the ``From`` field for
              notifications to ``email`` and ``email-json`` endpoints.

              * ``Owner`` – The AWS account ID of the topic's owner.

              * ``Policy`` – The JSON serialization of the topic's access control policy.

              * ``SubscriptionsConfirmed`` – The number of confirmed subscriptions for the topic.

              * ``SubscriptionsDeleted`` – The number of deleted subscriptions for the topic.

              * ``SubscriptionsPending`` – The number of subscriptions pending confirmation for the
              topic.

              * ``TopicArn`` – The topic's ARN.

              * ``EffectiveDeliveryPolicy`` – Yhe JSON serialization of the effective delivery
              policy, taking system defaults into account.

              The following attribute applies only to `server-side-encryption
              <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`__ :

              * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon
              SNS or a custom CMK. For more information, see `Key Terms
              <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`__
              . For more examples, see `KeyId
              <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__
              in the *AWS Key Management Service API Reference* .

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_endpoints_by_platform_application(
        self, PlatformApplicationArn: str, NextToken: str = None
    ) -> ClientListEndpointsByPlatformApplicationResponseTypeDef:
        """
        Lists the endpoints and endpoint attributes for devices in a supported push notification
        service, such as FCM and APNS. The results for ``ListEndpointsByPlatformApplication`` are
        paginated and return a limited list of endpoints, up to 100. If additional records are
        available after the first page results, then a NextToken string will be returned. To receive
        the next page, you call ``ListEndpointsByPlatformApplication`` again using the NextToken
        string received from the previous call. When there are no more records to return, NextToken
        will be null. For more information, see `Using Amazon SNS Mobile Push Notifications
        <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        This action is throttled at 30 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListEndpointsByPlatformApplication>`_

        **Request Syntax**
        ::

          response = client.list_endpoints_by_platform_application(
              PlatformApplicationArn='string',
              NextToken='string'
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn for ListEndpointsByPlatformApplicationInput action.

        :type NextToken: string
        :param NextToken:

          NextToken string is used when calling ListEndpointsByPlatformApplication action to
          retrieve additional records that are available after the first page results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Endpoints': [
                    {
                        'EndpointArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ListEndpointsByPlatformApplication action.

            - **Endpoints** *(list) --*

              Endpoints returned for ListEndpointsByPlatformApplication action.

              - *(dict) --*

                Endpoint for mobile app and device.

                - **EndpointArn** *(string) --*

                  EndpointArn for mobile app and device.

                - **Attributes** *(dict) --*

                  Attributes for endpoint.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              NextToken string is returned when calling ListEndpointsByPlatformApplication action if
              additional records are available after the first page results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_phone_numbers_opted_out(
        self, nextToken: str = None
    ) -> ClientListPhoneNumbersOptedOutResponseTypeDef:
        """
        Returns a list of phone numbers that are opted out, meaning you cannot send SMS messages to
        them.

        The results for ``ListPhoneNumbersOptedOut`` are paginated, and each page returns up to 100
        phone numbers. If additional phone numbers are available after the first page of results,
        then a ``NextToken`` string will be returned. To receive the next page, you call
        ``ListPhoneNumbersOptedOut`` again using the ``NextToken`` string received from the previous
        call. When there are no more records to return, ``NextToken`` will be null.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPhoneNumbersOptedOut>`_

        **Request Syntax**
        ::

          response = client.list_phone_numbers_opted_out(
              nextToken='string'
          )
        :type nextToken: string
        :param nextToken:

          A ``NextToken`` string is used when you call the ``ListPhoneNumbersOptedOut`` action to
          retrieve additional records that are available after the first page of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'phoneNumbers': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response from the ``ListPhoneNumbersOptedOut`` action.

            - **phoneNumbers** *(list) --*

              A list of phone numbers that are opted out of receiving SMS messages. The list is
              paginated, and each page can contain up to 100 phone numbers.

              - *(string) --*

            - **nextToken** *(string) --*

              A ``NextToken`` string is returned when you call the ``ListPhoneNumbersOptedOut``
              action if additional records are available after the first page of results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_platform_applications(
        self, NextToken: str = None
    ) -> ClientListPlatformApplicationsResponseTypeDef:
        """
        Lists the platform application objects for the supported push notification services, such as
        APNS and FCM. The results for ``ListPlatformApplications`` are paginated and return a
        limited list of applications, up to 100. If additional records are available after the first
        page results, then a NextToken string will be returned. To receive the next page, you call
        ``ListPlatformApplications`` using the NextToken string received from the previous call.
        When there are no more records to return, NextToken will be null. For more information, see
        `Using Amazon SNS Mobile Push Notifications
        <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        This action is throttled at 15 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListPlatformApplications>`_

        **Request Syntax**
        ::

          response = client.list_platform_applications(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:

          NextToken string is used when calling ListPlatformApplications action to retrieve
          additional records that are available after the first page results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PlatformApplications': [
                    {
                        'PlatformApplicationArn': 'string',
                        'Attributes': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ListPlatformApplications action.

            - **PlatformApplications** *(list) --*

              Platform applications returned when calling ListPlatformApplications action.

              - *(dict) --*

                Platform application object.

                - **PlatformApplicationArn** *(string) --*

                  PlatformApplicationArn for platform application object.

                - **Attributes** *(dict) --*

                  Attributes for platform application object.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              NextToken string is returned when calling ListPlatformApplications action if
              additional records are available after the first page results.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscriptions(self, NextToken: str = None) -> ClientListSubscriptionsResponseTypeDef:
        """
        Returns a list of the requester's subscriptions. Each call returns a limited list of
        subscriptions, up to 100. If there are more subscriptions, a ``NextToken`` is also returned.
        Use the ``NextToken`` parameter in a new ``ListSubscriptions`` call to get further results.

        This action is throttled at 30 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptions>`_

        **Request Syntax**
        ::

          response = client.list_subscriptions(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:

          Token returned by the previous ``ListSubscriptions`` request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ListSubscriptions action

            - **Subscriptions** *(list) --*

              A list of subscriptions.

              - *(dict) --*

                A wrapper type for the attributes of an Amazon SNS subscription.

                - **SubscriptionArn** *(string) --*

                  The subscription's ARN.

                - **Owner** *(string) --*

                  The subscription's owner.

                - **Protocol** *(string) --*

                  The subscription's protocol.

                - **Endpoint** *(string) --*

                  The subscription's endpoint (format depends on the protocol).

                - **TopicArn** *(string) --*

                  The ARN of the subscription's topic.

            - **NextToken** *(string) --*

              Token to pass along to the next ``ListSubscriptions`` request. This element is
              returned if there are more subscriptions to retrieve.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_subscriptions_by_topic(
        self, TopicArn: str, NextToken: str = None
    ) -> ClientListSubscriptionsByTopicResponseTypeDef:
        """
        Returns a list of the subscriptions to a specific topic. Each call returns a limited list of
        subscriptions, up to 100. If there are more subscriptions, a ``NextToken`` is also returned.
        Use the ``NextToken`` parameter in a new ``ListSubscriptionsByTopic`` call to get further
        results.

        This action is throttled at 30 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListSubscriptionsByTopic>`_

        **Request Syntax**
        ::

          response = client.list_subscriptions_by_topic(
              TopicArn='string',
              NextToken='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic for which you wish to find subscriptions.

        :type NextToken: string
        :param NextToken:

          Token returned by the previous ``ListSubscriptionsByTopic`` request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Subscriptions': [
                    {
                        'SubscriptionArn': 'string',
                        'Owner': 'string',
                        'Protocol': 'string',
                        'Endpoint': 'string',
                        'TopicArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ListSubscriptionsByTopic action.

            - **Subscriptions** *(list) --*

              A list of subscriptions.

              - *(dict) --*

                A wrapper type for the attributes of an Amazon SNS subscription.

                - **SubscriptionArn** *(string) --*

                  The subscription's ARN.

                - **Owner** *(string) --*

                  The subscription's owner.

                - **Protocol** *(string) --*

                  The subscription's protocol.

                - **Endpoint** *(string) --*

                  The subscription's endpoint (format depends on the protocol).

                - **TopicArn** *(string) --*

                  The ARN of the subscription's topic.

            - **NextToken** *(string) --*

              Token to pass along to the next ``ListSubscriptionsByTopic`` request. This element is
              returned if there are more subscriptions to retrieve.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_resource(self, ResourceArn: str) -> ClientListTagsForResourceResponseTypeDef:
        """
        List all tags added to the specified Amazon SNS topic. For an overview, see `Amazon SNS Tags
        <https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html>`__ in the *Amazon Simple
        Notification Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTagsForResource>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_resource(
              ResourceArn='string'
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of the topic for which to list tags.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              The tags associated with the specified topic.

              - *(dict) --*

                The list of tags to be added to the specified topic.

                - **Key** *(string) --*

                  The required key portion of the tag.

                - **Value** *(string) --*

                  The optional value portion of the tag.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_topics(self, NextToken: str = None) -> ClientListTopicsResponseTypeDef:
        """
        Returns a list of the requester's topics. Each call returns a limited list of topics, up to
        100. If there are more topics, a ``NextToken`` is also returned. Use the ``NextToken``
        parameter in a new ``ListTopics`` call to get further results.

        This action is throttled at 30 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/ListTopics>`_

        **Request Syntax**
        ::

          response = client.list_topics(
              NextToken='string'
          )
        :type NextToken: string
        :param NextToken:

          Token returned by the previous ``ListTopics`` request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Topics': [
                    {
                        'TopicArn': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for ListTopics action.

            - **Topics** *(list) --*

              A list of topic ARNs.

              - *(dict) --*

                A wrapper type for the topic's Amazon Resource Name (ARN). To retrieve a topic's
                attributes, use ``GetTopicAttributes`` .

                - **TopicArn** *(string) --*

                  The topic's ARN.

            - **NextToken** *(string) --*

              Token to pass along to the next ``ListTopics`` request. This element is returned if
              there are additional topics to retrieve.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def opt_in_phone_number(self, phoneNumber: str) -> Dict[str, Any]:
        """
        Use this request to opt in a phone number that is opted out, which enables you to resume
        sending SMS messages to the number.

        You can opt in a phone number only once every 30 days.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/OptInPhoneNumber>`_

        **Request Syntax**
        ::

          response = client.opt_in_phone_number(
              phoneNumber='string'
          )
        :type phoneNumber: string
        :param phoneNumber: **[REQUIRED]**

          The phone number to opt in.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            The response for the OptInPhoneNumber action.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, ClientPublishMessageAttributesTypeDef] = None,
    ) -> ClientPublishResponseTypeDef:
        """
        Sends a message to an Amazon SNS topic or sends a text message (SMS message) directly to a
        phone number.

        If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is
        subscribed to the topic. The format of the message depends on the notification protocol for
        each subscribed endpoint.

        When a ``messageId`` is returned, the message has been saved and Amazon SNS will attempt to
        deliver it shortly.

        To use the ``Publish`` action for sending a message to a mobile endpoint, such as an app on
        a Kindle device or mobile phone, you must specify the EndpointArn for the TargetArn
        parameter. The EndpointArn is returned when making a call with the
        ``CreatePlatformEndpoint`` action.

        For more information about formatting messages, see `Send Custom Platform-Specific Payloads
        in Messages to Mobile Devices
        <https://docs.aws.amazon.com/sns/latest/dg/mobile-push-send-custommessage.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Publish>`_

        **Request Syntax**
        ::

          response = client.publish(
              TopicArn='string',
              TargetArn='string',
              PhoneNumber='string',
              Message='string',
              Subject='string',
              MessageStructure='string',
              MessageAttributes={
                  'string': {
                      'DataType': 'string',
                      'StringValue': 'string',
                      'BinaryValue': b'bytes'
                  }
              }
          )
        :type TopicArn: string
        :param TopicArn:

          The topic you want to publish to.

          If you don't specify a value for the ``TopicArn`` parameter, you must specify a value for
          the ``PhoneNumber`` or ``TargetArn`` parameters.

        :type TargetArn: string
        :param TargetArn:

          If you don't specify a value for the ``TargetArn`` parameter, you must specify a value for
          the ``PhoneNumber`` or ``TopicArn`` parameters.

        :type PhoneNumber: string
        :param PhoneNumber:

          The phone number to which you want to deliver an SMS message. Use E.164 format.

          If you don't specify a value for the ``PhoneNumber`` parameter, you must specify a value
          for the ``TargetArn`` or ``TopicArn`` parameters.

        :type Message: string
        :param Message: **[REQUIRED]**

          The message you want to send.

          If you are publishing to a topic and you want to send the same message to all transport
          protocols, include the text of the message as a String value. If you want to send
          different messages for each transport protocol, set the value of the ``MessageStructure``
          parameter to ``json`` and use a JSON object for the ``Message`` parameter.

          Constraints:

          * With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in
          size (262,144 bytes, not 262,144 characters).

          * For SMS, each message can contain up to 140 characters. This character limit depends on
          the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII
          characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit,
          Amazon SNS sends the message as multiple messages, each fitting within the size limit.
          Messages aren't truncated mid-word but are cut off at whole-word boundaries. The total
          size limit for a single SMS ``Publish`` action is 1,600 characters.

          JSON-specific constraints:

          * Keys in the JSON object that correspond to supported transport protocols must have
          simple JSON string values.

          * The values will be parsed (unescaped) before they are used in outgoing messages.

          * Outbound notifications are JSON encoded (meaning that the characters will be reescaped
          for sending).

          * Values have a minimum length of 0 (the empty string, "", is allowed).

          * Values have a maximum length bounded by the overall message size (so, including multiple
          protocols may limit message sizes).

          * Non-string values will cause the key to be ignored.

          * Keys that do not correspond to supported transport protocols are ignored.

          * Duplicate keys are not allowed.

          * Failure to parse or validate any key or value in the message will cause the ``Publish``
          call to return an error (no partial delivery).

        :type Subject: string
        :param Subject:

          Optional parameter to be used as the "Subject" line when the message is delivered to email
          endpoints. This field will also be included, if present, in the standard JSON messages
          delivered to other endpoints.

          Constraints: Subjects must be ASCII text that begins with a letter, number, or punctuation
          mark; must not include line breaks or control characters; and must be less than 100
          characters long.

        :type MessageStructure: string
        :param MessageStructure:

          Set ``MessageStructure`` to ``json`` if you want to send a different message for each
          protocol. For example, using one publish action, you can send a short message to your SMS
          subscribers and a longer message to your email subscribers. If you set
          ``MessageStructure`` to ``json`` , the value of the ``Message`` parameter must:

          * be a syntactically valid JSON object; and

          * contain at least a top-level JSON key of "default" with a value that is a string.

          You can define other top-level keys that define the message you want to send to a specific
          transport protocol (e.g., "http").

          Valid value: ``json``

        :type MessageAttributes: dict
        :param MessageAttributes:

          Message attributes for Publish action.

          - *(string) --*

            - *(dict) --*

              The user-specified message attribute value. For string data types, the value attribute
              has the same restrictions on the content as the message body. For more information,
              see `Publish <https://docs.aws.amazon.com/sns/latest/api/API_Publish.html>`__ .

              Name, type, and value must not be empty or null. In addition, the message body should
              not be empty or null. All parts of the message attribute, including name, type, and
              value, are included in the message size restriction, which is currently 256 KB
              (262,144 bytes). For more information, see `Using Amazon SNS Message Attributes
              <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html>`__ .

              - **DataType** *(string) --* **[REQUIRED]**

                Amazon SNS supports the following logical data types: String, String.Array, Number,
                and Binary. For more information, see `Message Attribute Data Types
                <https://docs.aws.amazon.com/sns/latest/dg/SNSMessageAttributes.html#SNSMessageAttributes.DataTypes>`__
                .

              - **StringValue** *(string) --*

                Strings are Unicode with UTF8 binary encoding. For a list of code values, see `ASCII
                Printable Characters
                <https://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters>`__ .

              - **BinaryValue** *(bytes) --*

                Binary type attributes can store any binary data, for example, compressed data,
                encrypted data, or images.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MessageId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for Publish action.

            - **MessageId** *(string) --*

              Unique identifier assigned to the published message.

              Length Constraint: Maximum 100 characters
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(self, TopicArn: str, Label: str) -> None:
        """
        Removes a statement from a topic's access control policy.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/RemovePermission>`_

        **Request Syntax**
        ::

          response = client.remove_permission(
              TopicArn='string',
              Label='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic whose access control policy you wish to modify.

        :type Label: string
        :param Label: **[REQUIRED]**

          The unique label of the statement you want to remove.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_endpoint_attributes(self, EndpointArn: str, Attributes: Dict[str, str]) -> None:
        """
        Sets the attributes for an endpoint for a device on one of the supported push notification
        services, such as FCM and APNS. For more information, see `Using Amazon SNS Mobile Push
        Notifications <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetEndpointAttributes>`_

        **Request Syntax**
        ::

          response = client.set_endpoint_attributes(
              EndpointArn='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          EndpointArn used for SetEndpointAttributes action.

        :type Attributes: dict
        :param Attributes: **[REQUIRED]**

          A map of the endpoint attributes. Attributes in this map include the following:

          * ``CustomUserData`` – arbitrary user data to associate with the endpoint. Amazon SNS does
          not use this data. The data must be in UTF-8 format and less than 2KB.

          * ``Enabled`` – flag that enables/disables delivery to the endpoint. Amazon SNS will set
          this to false when a notification service indicates to Amazon SNS that the endpoint is
          invalid. Users can set it back to true, typically after updating Token.

          * ``Token`` – device token, also referred to as a registration id, for an app and mobile
          device. This is returned from the notification service when an app and mobile device are
          registered with the notification service.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_platform_application_attributes(
        self, PlatformApplicationArn: str, Attributes: Dict[str, str]
    ) -> None:
        """
        Sets the attributes of the platform application object for the supported push notification
        services, such as APNS and FCM. For more information, see `Using Amazon SNS Mobile Push
        Notifications <https://docs.aws.amazon.com/sns/latest/dg/SNSMobilePush.html>`__ . For
        information on configuring attributes for message delivery status, see `Using Amazon SNS
        Application Attributes for Message Delivery Status
        <https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetPlatformApplicationAttributes>`_

        **Request Syntax**
        ::

          response = client.set_platform_application_attributes(
              PlatformApplicationArn='string',
              Attributes={
                  'string': 'string'
              }
          )
        :type PlatformApplicationArn: string
        :param PlatformApplicationArn: **[REQUIRED]**

          PlatformApplicationArn for SetPlatformApplicationAttributes action.

        :type Attributes: dict
        :param Attributes: **[REQUIRED]**

          A map of the platform application attributes. Attributes in this map include the
          following:

          * ``PlatformCredential`` – The credential received from the notification service. For
          APNS/APNS_SANDBOX, PlatformCredential is private key. For FCM, PlatformCredential is "API
          key". For ADM, PlatformCredential is "client secret".

          * ``PlatformPrincipal`` – The principal received from the notification service. For
          APNS/APNS_SANDBOX, PlatformPrincipal is SSL certificate. For FCM, PlatformPrincipal is not
          applicable. For ADM, PlatformPrincipal is "client id".

          * ``EventEndpointCreated`` – Topic ARN to which EndpointCreated event notifications should
          be sent.

          * ``EventEndpointDeleted`` – Topic ARN to which EndpointDeleted event notifications should
          be sent.

          * ``EventEndpointUpdated`` – Topic ARN to which EndpointUpdate event notifications should
          be sent.

          * ``EventDeliveryFailure`` – Topic ARN to which DeliveryFailure event notifications should
          be sent upon Direct Publish delivery failure (permanent) to one of the application's
          endpoints.

          * ``SuccessFeedbackRoleArn`` – IAM role ARN used to give Amazon SNS write access to use
          CloudWatch Logs on your behalf.

          * ``FailureFeedbackRoleArn`` – IAM role ARN used to give Amazon SNS write access to use
          CloudWatch Logs on your behalf.

          * ``SuccessFeedbackSampleRate`` – Sample rate percentage (0-100) of successfully delivered
          messages.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_sms_attributes(self, attributes: Dict[str, str]) -> Dict[str, Any]:
        """
        Use this request to set the default settings for sending SMS messages and receiving daily
        SMS usage reports.

        You can override some of these settings for a single message when you use the ``Publish``
        action with the ``MessageAttributes.entry.N`` parameter. For more information, see `Sending
        an SMS Message <https://docs.aws.amazon.com/sns/latest/dg/sms_publish-to-phone.html>`__ in
        the *Amazon SNS Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetSMSAttributes>`_

        **Request Syntax**
        ::

          response = client.set_sms_attributes(
              attributes={
                  'string': 'string'
              }
          )
        :type attributes: dict
        :param attributes: **[REQUIRED]**

          The default settings for sending SMS messages from your account. You can set values for
          the following attribute names:

           ``MonthlySpendLimit`` – The maximum amount in USD that you are willing to spend each
           month to send SMS messages. When Amazon SNS determines that sending an SMS message would
           incur a cost that exceeds this limit, it stops sending SMS messages within minutes.

          .. warning::

            Amazon SNS stops sending SMS messages within minutes of the limit being crossed. During
            that interval, if you continue to send SMS messages, you will incur costs that exceed
            your limit.

          By default, the spend limit is set to the maximum allowed by Amazon SNS. If you want to
          raise the limit, submit an `SNS Limit Increase case
          <https://console.aws.amazon.com/support/home#/case/create?issueType=
              service-limit-increase&limitType=service-code-sns>`__
          . For **New limit value** , enter your desired monthly spend limit. In the **Use Case
          Description** field, explain that you are requesting an SMS monthly spend limit increase.

           ``DeliveryStatusIAMRole`` – The ARN of the IAM role that allows Amazon SNS to write logs
           about SMS deliveries in CloudWatch Logs. For each SMS message that you send, Amazon SNS
           writes a log that includes the message price, the success or failure status, the reason
           for failure (if the message failed), the message dwell time, and other information.

           ``DeliveryStatusSuccessSamplingRate`` – The percentage of successful SMS deliveries for
           which Amazon SNS will write logs in CloudWatch Logs. The value can be an integer from 0 -
           100. For example, to write logs only for failed deliveries, set this value to ``0`` . To
           write logs for 10% of your successful deliveries, set it to ``10`` .

           ``DefaultSenderID`` – A string, such as your business brand, that is displayed as the
           sender on the receiving device. Support for sender IDs varies by country. The sender ID
           can be 1 - 11 alphanumeric characters, and it must contain at least one letter.

           ``DefaultSMSType`` – The type of SMS message that you will send by default. You can
           assign the following values:

          * ``Promotional`` – (Default) Noncritical messages, such as marketing messages. Amazon SNS
          optimizes the message delivery to incur the lowest cost.

          * ``Transactional`` – Critical messages that support customer transactions, such as
          one-time passcodes for multi-factor authentication. Amazon SNS optimizes the message
          delivery to achieve the highest reliability.

           ``UsageReportS3Bucket`` – The name of the Amazon S3 bucket to receive daily SMS usage
           reports from Amazon SNS. Each day, Amazon SNS will deliver a usage report as a CSV file
           to the bucket. The report includes the following information for each SMS message that
           was successfully delivered by your account:

          * Time that the message was published (in UTC)

          * Message ID

          * Destination phone number

          * Message type

          * Delivery status

          * Message price (in USD)

          * Part number (a message is split into multiple parts if it is too long for a single
          message)

          * Total number of parts

          To receive the report, the bucket must have a policy that allows the Amazon SNS service
          principle to perform the ``s3:PutObject`` and ``s3:GetBucketLocation`` actions.

          For an example bucket policy and usage report, see `Monitoring SMS Activity
          <https://docs.aws.amazon.com/sns/latest/dg/sms_stats.html>`__ in the *Amazon SNS Developer
          Guide* .

          - *(string) --*

            - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*

            The response for the SetSMSAttributes action.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_subscription_attributes(
        self, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        Allows a subscription owner to set an attribute of the subscription to a new value.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetSubscriptionAttributes>`_

        **Request Syntax**
        ::

          response = client.set_subscription_attributes(
              SubscriptionArn='string',
              AttributeName='string',
              AttributeValue='string'
          )
        :type SubscriptionArn: string
        :param SubscriptionArn: **[REQUIRED]**

          The ARN of the subscription to modify.

        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**

          A map of attributes with their corresponding values.

          The following lists the names, descriptions, and values of the special request parameters
          that the ``SetTopicAttributes`` action uses:

          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to
          HTTP/S endpoints.

          * ``FilterPolicy`` – The simple JSON object that lets your subscriber receive only a
          subset of messages, rather than receiving every message published to the topic.

          * ``RawMessageDelivery`` – When set to ``true`` , enables raw message delivery to Amazon
          SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON
          formatting, which is otherwise created for Amazon SNS metadata.

          * ``RedrivePolicy`` – When specified, sends undeliverable messages to the specified Amazon
          SQS dead-letter queue. Messages that can't be delivered due to client errors (for example,
          when the subscribed endpoint is unreachable) or server errors (for example, when the
          service that powers the subscribed endpoint becomes unavailable) are held in the
          dead-letter queue for further analysis or reprocessing.

        :type AttributeValue: string
        :param AttributeValue:

          The new value for the attribute in JSON format.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_topic_attributes(
        self, TopicArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        Allows a topic owner to set an attribute of the topic to a new value.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/SetTopicAttributes>`_

        **Request Syntax**
        ::

          response = client.set_topic_attributes(
              TopicArn='string',
              AttributeName='string',
              AttributeValue='string'
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic to modify.

        :type AttributeName: string
        :param AttributeName: **[REQUIRED]**

          A map of attributes with their corresponding values.

          The following lists the names, descriptions, and values of the special request parameters
          that the ``SetTopicAttributes`` action uses:

          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to
          HTTP/S endpoints.

          * ``DisplayName`` – The display name to use for a topic with SMS subscriptions.

          * ``Policy`` – The policy that defines who can access your topic. By default, only the
          topic owner can publish or subscribe to the topic.

          The following attribute applies only to `server-side-encryption
          <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html>`__ :

          * ``KmsMasterKeyId`` - The ID of an AWS-managed customer master key (CMK) for Amazon SNS
          or a custom CMK. For more information, see `Key Terms
          <https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms>`__
          . For more examples, see `KeyId
          <https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters>`__
          in the *AWS Key Management Service API Reference* .

        :type AttributeValue: string
        :param AttributeValue:

          The new value for the attribute.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def subscribe(
        self,
        TopicArn: str,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> ClientSubscribeResponseTypeDef:
        """
        Prepares to subscribe an endpoint by sending the endpoint a confirmation message. To
        actually create a subscription, the endpoint owner must call the ``ConfirmSubscription``
        action with the token from the confirmation message. Confirmation tokens are valid for three
        days.

        This action is throttled at 100 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Subscribe>`_

        **Request Syntax**
        ::

          response = client.subscribe(
              TopicArn='string',
              Protocol='string',
              Endpoint='string',
              Attributes={
                  'string': 'string'
              },
              ReturnSubscriptionArn=True|False
          )
        :type TopicArn: string
        :param TopicArn: **[REQUIRED]**

          The ARN of the topic you want to subscribe to.

        :type Protocol: string
        :param Protocol: **[REQUIRED]**

          The protocol you want to use. Supported protocols include:

          * ``http`` – delivery of JSON-encoded message via HTTP POST

          * ``https`` – delivery of JSON-encoded message via HTTPS POST

          * ``email`` – delivery of message via SMTP

          * ``email-json`` – delivery of JSON-encoded message via SMTP

          * ``sms`` – delivery of message via SMS

          * ``sqs`` – delivery of JSON-encoded message to an Amazon SQS queue

          * ``application`` – delivery of JSON-encoded message to an EndpointArn for a mobile app
          and device.

          * ``lambda`` – delivery of JSON-encoded message to an Amazon Lambda function.

        :type Endpoint: string
        :param Endpoint:

          The endpoint that you want to receive notifications. Endpoints vary by protocol:

          * For the ``http`` protocol, the endpoint is an URL beginning with ``http://``

          * For the ``https`` protocol, the endpoint is a URL beginning with ``https://``

          * For the ``email`` protocol, the endpoint is an email address

          * For the ``email-json`` protocol, the endpoint is an email address

          * For the ``sms`` protocol, the endpoint is a phone number of an SMS-enabled device

          * For the ``sqs`` protocol, the endpoint is the ARN of an Amazon SQS queue

          * For the ``application`` protocol, the endpoint is the EndpointArn of a mobile app and
          device.

          * For the ``lambda`` protocol, the endpoint is the ARN of an Amazon Lambda function.

        :type Attributes: dict
        :param Attributes:

          A map of attributes with their corresponding values.

          The following lists the names, descriptions, and values of the special request parameters
          that the ``SetTopicAttributes`` action uses:

          * ``DeliveryPolicy`` – The policy that defines how Amazon SNS retries failed deliveries to
          HTTP/S endpoints.

          * ``FilterPolicy`` – The simple JSON object that lets your subscriber receive only a
          subset of messages, rather than receiving every message published to the topic.

          * ``RawMessageDelivery`` – When set to ``true`` , enables raw message delivery to Amazon
          SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON
          formatting, which is otherwise created for Amazon SNS metadata.

          * ``RedrivePolicy`` – When specified, sends undeliverable messages to the specified Amazon
          SQS dead-letter queue. Messages that can't be delivered due to client errors (for example,
          when the subscribed endpoint is unreachable) or server errors (for example, when the
          service that powers the subscribed endpoint becomes unavailable) are held in the
          dead-letter queue for further analysis or reprocessing.

          - *(string) --*

            - *(string) --*

        :type ReturnSubscriptionArn: boolean
        :param ReturnSubscriptionArn:

          Sets whether the response from the ``Subscribe`` request includes the subscription ARN,
          even if the subscription is not yet confirmed.

          * If you have the subscription ARN returned, the response includes the ARN in all cases,
          even if the subscription is not yet confirmed.

          * If you don't have the subscription ARN returned, in addition to the ARN for confirmed
          subscriptions, the response also includes the ``pending subscription`` ARN value for
          subscriptions that aren't yet confirmed. A subscription becomes confirmed when the
          subscriber calls the ``ConfirmSubscription`` action with a confirmation token.

          If you set this parameter to ``true`` , .

          The default value is ``false`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SubscriptionArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Response for Subscribe action.

            - **SubscriptionArn** *(string) --*

              The ARN of the subscription if it is confirmed, or the string "pending confirmation"
              if the subscription requires confirmation. However, if the API request parameter
              ``ReturnSubscriptionArn`` is true, then the value is always the subscription ARN, even
              if the subscription requires confirmation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, ResourceArn: str, Tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Add tags to the specified Amazon SNS topic. For an overview, see `Amazon SNS Tags
        <https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html>`__ in the *Amazon SNS Developer
        Guide* .

        When you use topic tags, keep the following guidelines in mind:

        * Adding more than 50 tags to a topic isn't recommended.

        * Tags don't have any semantic meaning. Amazon SNS interprets tags as character strings.

        * Tags are case-sensitive.

        * A new tag with a key identical to that of an existing tag overwrites the existing tag.

        * Tagging actions are limited to 10 TPS per AWS account, per AWS region. If your application
        requires a higher throughput, file a `technical support request
        <https://console.aws.amazon.com/support/home#/case/create?issueType=technical>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              ResourceArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of the topic to which to add tags.

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The tags to be added to the specified topic. A tag consists of a required key and an
          optional value.

          - *(dict) --*

            The list of tags to be added to the specified topic.

            - **Key** *(string) --* **[REQUIRED]**

              The required key portion of the tag.

            - **Value** *(string) --* **[REQUIRED]**

              The optional value portion of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def unsubscribe(self, SubscriptionArn: str) -> None:
        """
        Deletes a subscription. If the subscription requires authentication for deletion, only the
        owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is
        required. If the ``Unsubscribe`` call does not require authentication and the requester is
        not the subscription owner, a final cancellation message is delivered to the endpoint, so
        that the endpoint owner can easily resubscribe to the topic if the ``Unsubscribe`` request
        was unintended.

        This action is throttled at 100 transactions per second (TPS).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/Unsubscribe>`_

        **Request Syntax**
        ::

          response = client.unsubscribe(
              SubscriptionArn='string'
          )
        :type SubscriptionArn: string
        :param SubscriptionArn: **[REQUIRED]**

          The ARN of the subscription to be deleted.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove tags from the specified Amazon SNS topic. For an overview, see `Amazon SNS Tags
        <https://docs.aws.amazon.com/sns/latest/dg/sns-tags.html>`__ in the *Amazon SNS Developer
        Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sns-2010-03-31/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              ResourceArn='string',
              TagKeys=[
                  'string',
              ]
          )
        :type ResourceArn: string
        :param ResourceArn: **[REQUIRED]**

          The ARN of the topic from which to remove tags.

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          The list of tag keys to remove from the specified topic.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_endpoints_by_platform_application"]
    ) -> paginator_scope.ListEndpointsByPlatformApplicationPaginator:
        """
        Get Paginator for `list_endpoints_by_platform_application` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_opted_out"]
    ) -> paginator_scope.ListPhoneNumbersOptedOutPaginator:
        """
        Get Paginator for `list_phone_numbers_opted_out` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_platform_applications"]
    ) -> paginator_scope.ListPlatformApplicationsPaginator:
        """
        Get Paginator for `list_platform_applications` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> paginator_scope.ListSubscriptionsPaginator:
        """
        Get Paginator for `list_subscriptions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_subscriptions_by_topic"]
    ) -> paginator_scope.ListSubscriptionsByTopicPaginator:
        """
        Get Paginator for `list_subscriptions_by_topic` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_topics"]
    ) -> paginator_scope.ListTopicsPaginator:
        """
        Get Paginator for `list_topics` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    AuthorizationErrorException: Boto3ClientError
    ClientError: Boto3ClientError
    ConcurrentAccessException: Boto3ClientError
    EndpointDisabledException: Boto3ClientError
    FilterPolicyLimitExceededException: Boto3ClientError
    InternalErrorException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidSecurityException: Boto3ClientError
    KMSAccessDeniedException: Boto3ClientError
    KMSDisabledException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KMSNotFoundException: Boto3ClientError
    KMSOptInRequired: Boto3ClientError
    KMSThrottlingException: Boto3ClientError
    NotFoundException: Boto3ClientError
    PlatformApplicationDisabledException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    StaleTagException: Boto3ClientError
    SubscriptionLimitExceededException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    ThrottledException: Boto3ClientError
    TopicLimitExceededException: Boto3ClientError
