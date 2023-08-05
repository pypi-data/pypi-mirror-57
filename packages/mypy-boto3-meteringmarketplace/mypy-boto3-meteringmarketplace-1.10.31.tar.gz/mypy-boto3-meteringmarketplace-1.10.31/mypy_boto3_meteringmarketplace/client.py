"Main interface for meteringmarketplace service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_meteringmarketplace.client as client_scope
from mypy_boto3_meteringmarketplace.type_defs import (
    ClientBatchMeterUsageResponseTypeDef,
    ClientBatchMeterUsageUsageRecordsTypeDef,
    ClientMeterUsageResponseTypeDef,
    ClientRegisterUsageResponseTypeDef,
    ClientResolveCustomerResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def batch_meter_usage(
        self, UsageRecords: List[ClientBatchMeterUsageUsageRecordsTypeDef], ProductCode: str
    ) -> ClientBatchMeterUsageResponseTypeDef:
        """
        BatchMeterUsage is called from a SaaS application listed on the AWS Marketplace to post
        metering records for a set of customers.

        For identical requests, the API is idempotent; requests can be retried with the same records
        or a subset of the input records.

        Every request to BatchMeterUsage is for one product. If you need to meter usage for multiple
        products, you must make multiple calls to BatchMeterUsage.

        BatchMeterUsage can process up to 25 UsageRecords at a time.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/BatchMeterUsage>`_

        **Request Syntax**
        ::

          response = client.batch_meter_usage(
              UsageRecords=[
                  {
                      'Timestamp': datetime(2015, 1, 1),
                      'CustomerIdentifier': 'string',
                      'Dimension': 'string',
                      'Quantity': 123
                  },
              ],
              ProductCode='string'
          )
        :type UsageRecords: list
        :param UsageRecords: **[REQUIRED]**

          The set of UsageRecords to submit. BatchMeterUsage accepts up to 25 UsageRecords at a
          time.

          - *(dict) --*

            A UsageRecord indicates a quantity of usage for a given product, customer, dimension and
            time.

            Multiple requests with the same UsageRecords as input will be deduplicated to prevent
            double charges.

            - **Timestamp** *(datetime) --* **[REQUIRED]**

              Timestamp, in UTC, for which the usage is being reported.

              Your application can meter usage for up to one hour in the past. Make sure the
              timestamp value is not before the start of the software usage.

            - **CustomerIdentifier** *(string) --* **[REQUIRED]**

              The CustomerIdentifier is obtained through the ResolveCustomer operation and
              represents an individual buyer in your application.

            - **Dimension** *(string) --* **[REQUIRED]**

              During the process of registering a product on AWS Marketplace, up to eight dimensions
              are specified. These represent different units of value in your application.

            - **Quantity** *(integer) --*

              The quantity of usage consumed by the customer for the given dimension and time.
              Defaults to ``0`` if not specified.

        :type ProductCode: string
        :param ProductCode: **[REQUIRED]**

          Product code is used to uniquely identify a product in AWS Marketplace. The product code
          should be the same as the one used during the publishing of a new product.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Results': [
                    {
                        'UsageRecord': {
                            'Timestamp': datetime(2015, 1, 1),
                            'CustomerIdentifier': 'string',
                            'Dimension': 'string',
                            'Quantity': 123
                        },
                        'MeteringRecordId': 'string',
                        'Status': 'Success'|'CustomerNotSubscribed'|'DuplicateRecord'
                    },
                ],
                'UnprocessedRecords': [
                    {
                        'Timestamp': datetime(2015, 1, 1),
                        'CustomerIdentifier': 'string',
                        'Dimension': 'string',
                        'Quantity': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            Contains the UsageRecords processed by BatchMeterUsage and any records that have failed
            due to transient error.

            - **Results** *(list) --*

              Contains all UsageRecords processed by BatchMeterUsage. These records were either
              honored by AWS Marketplace Metering Service or were invalid.

              - *(dict) --*

                A UsageRecordResult indicates the status of a given UsageRecord processed by
                BatchMeterUsage.

                - **UsageRecord** *(dict) --*

                  The UsageRecord that was part of the BatchMeterUsage request.

                  - **Timestamp** *(datetime) --*

                    Timestamp, in UTC, for which the usage is being reported.

                    Your application can meter usage for up to one hour in the past. Make sure the
                    timestamp value is not before the start of the software usage.

                  - **CustomerIdentifier** *(string) --*

                    The CustomerIdentifier is obtained through the ResolveCustomer operation and
                    represents an individual buyer in your application.

                  - **Dimension** *(string) --*

                    During the process of registering a product on AWS Marketplace, up to eight
                    dimensions are specified. These represent different units of value in your
                    application.

                  - **Quantity** *(integer) --*

                    The quantity of usage consumed by the customer for the given dimension and time.
                    Defaults to ``0`` if not specified.

                - **MeteringRecordId** *(string) --*

                  The MeteringRecordId is a unique identifier for this metering event.

                - **Status** *(string) --*

                  The UsageRecordResult Status indicates the status of an individual UsageRecord
                  processed by BatchMeterUsage.

                  * *Success* - The UsageRecord was accepted and honored by BatchMeterUsage.

                  * *CustomerNotSubscribed* - The CustomerIdentifier specified is not subscribed to
                  your product. The UsageRecord was not honored. Future UsageRecords for this
                  customer will fail until the customer subscribes to your product.

                  * *DuplicateRecord* - Indicates that the UsageRecord was invalid and not honored.
                  A previously metered UsageRecord had the same customer, dimension, and time, but a
                  different quantity.

            - **UnprocessedRecords** *(list) --*

              Contains all UsageRecords that were not processed by BatchMeterUsage. This is a list
              of UsageRecords. You can retry the failed request by making another BatchMeterUsage
              call with this list as input in the BatchMeterUsageRequest.

              - *(dict) --*

                A UsageRecord indicates a quantity of usage for a given product, customer, dimension
                and time.

                Multiple requests with the same UsageRecords as input will be deduplicated to
                prevent double charges.

                - **Timestamp** *(datetime) --*

                  Timestamp, in UTC, for which the usage is being reported.

                  Your application can meter usage for up to one hour in the past. Make sure the
                  timestamp value is not before the start of the software usage.

                - **CustomerIdentifier** *(string) --*

                  The CustomerIdentifier is obtained through the ResolveCustomer operation and
                  represents an individual buyer in your application.

                - **Dimension** *(string) --*

                  During the process of registering a product on AWS Marketplace, up to eight
                  dimensions are specified. These represent different units of value in your
                  application.

                - **Quantity** *(integer) --*

                  The quantity of usage consumed by the customer for the given dimension and time.
                  Defaults to ``0`` if not specified.
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
    def meter_usage(
        self,
        ProductCode: str,
        Timestamp: datetime,
        UsageDimension: str,
        UsageQuantity: int = None,
        DryRun: bool = None,
    ) -> ClientMeterUsageResponseTypeDef:
        """
        API to emit metering records. For identical requests, the API is idempotent. It simply
        returns the metering record ID.

        MeterUsage is authenticated on the buyer's AWS account using credentials from the EC2
        instance, ECS task, or EKS pod.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/MeterUsage>`_

        **Request Syntax**
        ::

          response = client.meter_usage(
              ProductCode='string',
              Timestamp=datetime(2015, 1, 1),
              UsageDimension='string',
              UsageQuantity=123,
              DryRun=True|False
          )
        :type ProductCode: string
        :param ProductCode: **[REQUIRED]**

          Product code is used to uniquely identify a product in AWS Marketplace. The product code
          should be the same as the one used during the publishing of a new product.

        :type Timestamp: datetime
        :param Timestamp: **[REQUIRED]**

          Timestamp, in UTC, for which the usage is being reported. Your application can meter usage
          for up to one hour in the past. Make sure the timestamp value is not before the start of
          the software usage.

        :type UsageDimension: string
        :param UsageDimension: **[REQUIRED]**

          It will be one of the fcp dimension name provided during the publishing of the product.

        :type UsageQuantity: integer
        :param UsageQuantity:

          Consumption value for the hour. Defaults to ``0`` if not specified.

        :type DryRun: boolean
        :param DryRun:

          Checks whether you have the permissions required for the action, but does not make the
          request. If you have the permissions, the request returns DryRunOperation; otherwise, it
          returns UnauthorizedException. Defaults to ``false`` if not specified.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MeteringRecordId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **MeteringRecordId** *(string) --*

              Metering record id.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_usage(
        self, ProductCode: str, PublicKeyVersion: int, Nonce: str = None
    ) -> ClientRegisterUsageResponseTypeDef:
        """
        Paid container software products sold through AWS Marketplace must integrate with the AWS
        Marketplace Metering Service and call the RegisterUsage operation for software entitlement
        and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren't required to call
        RegisterUsage, but you may choose to do so if you would like to receive usage data in your
        seller reports. The sections below explain the behavior of RegisterUsage. RegisterUsage
        performs two primary functions: metering and entitlement.

        * *Entitlement* : RegisterUsage allows you to verify that the customer running your paid
        software is subscribed to your product on AWS Marketplace, enabling you to guard against
        unauthorized use. Your container image that integrates with RegisterUsage is only required
        to guard against unauthorized use at container startup, as such a
        CustomerNotSubscribedException/PlatformNotSupportedException will only be thrown on the
        initial call to RegisterUsage. Subsequent calls from the same Amazon ECS task instance (e.g.
        task-id) or Amazon EKS pod will not throw a CustomerNotSubscribedException, even if the
        customer unsubscribes while the Amazon ECS task or Amazon EKS pod is still running.

        * *Metering* : RegisterUsage meters software use per ECS task, per hour, or per pod for
        Amazon EKS with usage prorated to the second. A minimum of 1 minute of usage applies to
        tasks that are short lived. For example, if a customer has a 10 node Amazon ECS or Amazon
        EKS cluster and a service configured as a Daemon Set, then Amazon ECS or Amazon EKS will
        launch a task on all 10 cluster nodes and the customer will be charged: (10 * hourly_rate).
        Metering for software use is automatically handled by the AWS Marketplace Metering Control
        Plane -- your software is not required to perform any metering specific actions, other than
        call RegisterUsage once for metering of software use to commence. The AWS Marketplace
        Metering Control Plane will also continue to bill customers for running ECS tasks and Amazon
        EKS pods, regardless of the customers subscription state, removing the need for your
        software to perform entitlement checks at runtime.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/RegisterUsage>`_

        **Request Syntax**
        ::

          response = client.register_usage(
              ProductCode='string',
              PublicKeyVersion=123,
              Nonce='string'
          )
        :type ProductCode: string
        :param ProductCode: **[REQUIRED]**

          Product code is used to uniquely identify a product in AWS Marketplace. The product code
          should be the same as the one used during the publishing of a new product.

        :type PublicKeyVersion: integer
        :param PublicKeyVersion: **[REQUIRED]**

          Public Key Version provided by AWS Marketplace

        :type Nonce: string
        :param Nonce:

          (Optional) To scope down the registration to a specific running software instance and
          guard against replay attacks.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PublicKeyRotationTimestamp': datetime(2015, 1, 1),
                'Signature': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **PublicKeyRotationTimestamp** *(datetime) --*

              (Optional) Only included when public key version has expired

            - **Signature** *(string) --*

              JWT Token
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resolve_customer(self, RegistrationToken: str) -> ClientResolveCustomerResponseTypeDef:
        """
        ResolveCustomer is called by a SaaS application during the registration process. When a
        buyer visits your website during the registration process, the buyer submits a registration
        token through their browser. The registration token is resolved through this API to obtain a
        CustomerIdentifier and product code.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/ResolveCustomer>`_

        **Request Syntax**
        ::

          response = client.resolve_customer(
              RegistrationToken='string'
          )
        :type RegistrationToken: string
        :param RegistrationToken: **[REQUIRED]**

          When a buyer visits your website during the registration process, the buyer submits a
          registration token through the browser. The registration token is resolved to obtain a
          CustomerIdentifier and product code.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CustomerIdentifier': 'string',
                'ProductCode': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The result of the ResolveCustomer operation. Contains the CustomerIdentifier and product
            code.

            - **CustomerIdentifier** *(string) --*

              The CustomerIdentifier is used to identify an individual customer in your application.
              Calls to BatchMeterUsage require CustomerIdentifiers for each UsageRecord.

            - **ProductCode** *(string) --*

              The product code is returned to confirm that the buyer is registering for your
              product. Subsequent BatchMeterUsage calls should be made using this product code.
        """


class Exceptions:
    ClientError: Boto3ClientError
    CustomerNotEntitledException: Boto3ClientError
    DisabledApiException: Boto3ClientError
    DuplicateRequestException: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    InternalServiceErrorException: Boto3ClientError
    InvalidCustomerIdentifierException: Boto3ClientError
    InvalidEndpointRegionException: Boto3ClientError
    InvalidProductCodeException: Boto3ClientError
    InvalidPublicKeyVersionException: Boto3ClientError
    InvalidRegionException: Boto3ClientError
    InvalidTokenException: Boto3ClientError
    InvalidUsageDimensionException: Boto3ClientError
    PlatformNotSupportedException: Boto3ClientError
    ThrottlingException: Boto3ClientError
    TimestampOutOfBoundsException: Boto3ClientError
