"Main interface for lambda service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, IO, List, Union
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_lambda.client as client_scope

# pylint: disable=import-self
import mypy_boto3_lambda.paginator as paginator_scope
from mypy_boto3_lambda.type_defs import (
    ClientAddLayerVersionPermissionResponseTypeDef,
    ClientAddPermissionResponseTypeDef,
    ClientCreateAliasResponseTypeDef,
    ClientCreateAliasRoutingConfigTypeDef,
    ClientCreateEventSourceMappingDestinationConfigTypeDef,
    ClientCreateEventSourceMappingResponseTypeDef,
    ClientCreateFunctionCodeTypeDef,
    ClientCreateFunctionDeadLetterConfigTypeDef,
    ClientCreateFunctionEnvironmentTypeDef,
    ClientCreateFunctionResponseTypeDef,
    ClientCreateFunctionTracingConfigTypeDef,
    ClientCreateFunctionVpcConfigTypeDef,
    ClientDeleteEventSourceMappingResponseTypeDef,
    ClientGetAccountSettingsResponseTypeDef,
    ClientGetAliasResponseTypeDef,
    ClientGetEventSourceMappingResponseTypeDef,
    ClientGetFunctionConcurrencyResponseTypeDef,
    ClientGetFunctionConfigurationResponseTypeDef,
    ClientGetFunctionEventInvokeConfigResponseTypeDef,
    ClientGetFunctionResponseTypeDef,
    ClientGetLayerVersionByArnResponseTypeDef,
    ClientGetLayerVersionPolicyResponseTypeDef,
    ClientGetLayerVersionResponseTypeDef,
    ClientGetPolicyResponseTypeDef,
    ClientGetProvisionedConcurrencyConfigResponseTypeDef,
    ClientInvokeAsyncResponseTypeDef,
    ClientInvokeResponseTypeDef,
    ClientListAliasesResponseTypeDef,
    ClientListEventSourceMappingsResponseTypeDef,
    ClientListFunctionEventInvokeConfigsResponseTypeDef,
    ClientListFunctionsResponseTypeDef,
    ClientListLayerVersionsResponseTypeDef,
    ClientListLayersResponseTypeDef,
    ClientListProvisionedConcurrencyConfigsResponseTypeDef,
    ClientListTagsResponseTypeDef,
    ClientListVersionsByFunctionResponseTypeDef,
    ClientPublishLayerVersionContentTypeDef,
    ClientPublishLayerVersionResponseTypeDef,
    ClientPublishVersionResponseTypeDef,
    ClientPutFunctionConcurrencyResponseTypeDef,
    ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef,
    ClientPutFunctionEventInvokeConfigResponseTypeDef,
    ClientPutProvisionedConcurrencyConfigResponseTypeDef,
    ClientUpdateAliasResponseTypeDef,
    ClientUpdateAliasRoutingConfigTypeDef,
    ClientUpdateEventSourceMappingDestinationConfigTypeDef,
    ClientUpdateEventSourceMappingResponseTypeDef,
    ClientUpdateFunctionCodeResponseTypeDef,
    ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef,
    ClientUpdateFunctionConfigurationEnvironmentTypeDef,
    ClientUpdateFunctionConfigurationResponseTypeDef,
    ClientUpdateFunctionConfigurationTracingConfigTypeDef,
    ClientUpdateFunctionConfigurationVpcConfigTypeDef,
    ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef,
    ClientUpdateFunctionEventInvokeConfigResponseTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_lambda.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_layer_version_permission(
        self,
        LayerName: str,
        VersionNumber: int,
        StatementId: str,
        Action: str,
        Principal: str,
        OrganizationId: str = None,
        RevisionId: str = None,
    ) -> ClientAddLayerVersionPermissionResponseTypeDef:
        """
        Adds permissions to the resource-based policy of a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ . Use this
        action to grant layer usage permission to other accounts. You can grant permission to a
        single account, all AWS accounts, or all accounts in an organization.

        To revoke permission, call  RemoveLayerVersionPermission with the statement ID that you
        specified when you added it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/AddLayerVersionPermission>`_

        **Request Syntax**
        ::

          response = client.add_layer_version_permission(
              LayerName='string',
              VersionNumber=123,
              StatementId='string',
              Action='string',
              Principal='string',
              OrganizationId='string',
              RevisionId='string'
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type VersionNumber: integer
        :param VersionNumber: **[REQUIRED]**

          The version number.

        :type StatementId: string
        :param StatementId: **[REQUIRED]**

          An identifier that distinguishes the policy from others on the same layer version.

        :type Action: string
        :param Action: **[REQUIRED]**

          The API action that grants access to the layer. For example, ``lambda:GetLayerVersion`` .

        :type Principal: string
        :param Principal: **[REQUIRED]**

          An account ID, or ``*`` to grant permission to all AWS accounts.

        :type OrganizationId: string
        :param OrganizationId:

          With the principal set to ``*`` , grant permission to all accounts in the specified
          organization.

        :type RevisionId: string
        :param RevisionId:

          Only update the policy if the revision ID matches the ID specified. Use this option to
          avoid modifying a policy that has changed since you last read it.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Statement': 'string',
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Statement** *(string) --*

              The permission statement.

            - **RevisionId** *(string) --*

              A unique identifier for the current revision of the policy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_permission(
        self,
        FunctionName: str,
        StatementId: str,
        Action: str,
        Principal: str,
        SourceArn: str = None,
        SourceAccount: str = None,
        EventSourceToken: str = None,
        Qualifier: str = None,
        RevisionId: str = None,
    ) -> ClientAddPermissionResponseTypeDef:
        """
        Grants an AWS service or another account permission to use a function. You can apply the
        policy at the function level, or specify a qualifier to restrict access to a single version
        or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN)
        of that version or alias to invoke the function.

        To grant permission to another account, specify the account ID as the ``Principal`` . For
        AWS services, the principal is a domain-style identifier defined by the service, like
        ``s3.amazonaws.com`` or ``sns.amazonaws.com`` . For AWS services, you can also specify the
        ARN or owning account of the associated resource as the ``SourceArn`` or ``SourceAccount`` .
        If you grant permission to a service principal without specifying the source, other accounts
        could potentially configure resources in their account to invoke your Lambda function.

        This action adds a statement to a resource-based permissions policy for the function. For
        more information about function policies, see `Lambda Function Policies
        <https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/AddPermission>`_

        **Request Syntax**
        ::

          response = client.add_permission(
              FunctionName='string',
              StatementId='string',
              Action='string',
              Principal='string',
              SourceArn='string',
              SourceAccount='string',
              EventSourceToken='string',
              Qualifier='string',
              RevisionId='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type StatementId: string
        :param StatementId: **[REQUIRED]**

          A statement identifier that differentiates the statement from others in the same policy.

        :type Action: string
        :param Action: **[REQUIRED]**

          The action that the principal can use on the function. For example,
          ``lambda:InvokeFunction`` or ``lambda:GetFunction`` .

        :type Principal: string
        :param Principal: **[REQUIRED]**

          The AWS service or account that invokes the function. If you specify a service, use
          ``SourceArn`` or ``SourceAccount`` to limit who can invoke the function through that
          service.

        :type SourceArn: string
        :param SourceArn:

          For AWS services, the ARN of the AWS resource that invokes the function. For example, an
          Amazon S3 bucket or Amazon SNS topic.

        :type SourceAccount: string
        :param SourceAccount:

          For AWS services, the ID of the account that owns the resource. Use this instead of
          ``SourceArn`` to grant permission to resources that are owned by another account (for
          example, all of an account's Amazon S3 buckets). Or use it together with ``SourceArn`` to
          ensure that the resource is owned by the specified account. For example, an Amazon S3
          bucket could be deleted by its owner and recreated by another account.

        :type EventSourceToken: string
        :param EventSourceToken:

          For Alexa Smart Home functions, a token that must be supplied by the invoker.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to add permissions to a published version of the function.

        :type RevisionId: string
        :param RevisionId:

          Only update the policy if the revision ID matches the ID that's specified. Use this option
          to avoid modifying a policy that has changed since you last read it.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Statement': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Statement** *(string) --*

              The permission statement that's added to the function policy.
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
    def create_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str,
        Description: str = None,
        RoutingConfig: ClientCreateAliasRoutingConfigTypeDef = None,
    ) -> ClientCreateAliasResponseTypeDef:
        """
        Creates an `alias <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__
        for a Lambda function version. Use aliases to provide clients with a function identifier
        that you can update to invoke a different version.

        You can also map an alias to split invocation requests between two versions. Use the
        ``RoutingConfig`` parameter to specify a second version and the percentage of invocation
        requests that it receives.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateAlias>`_

        **Request Syntax**
        ::

          response = client.create_alias(
              FunctionName='string',
              Name='string',
              FunctionVersion='string',
              Description='string',
              RoutingConfig={
                  'AdditionalVersionWeights': {
                      'string': 123.0
                  }
              }
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the alias.

        :type FunctionVersion: string
        :param FunctionVersion: **[REQUIRED]**

          The function version that the alias invokes.

        :type Description: string
        :param Description:

          A description of the alias.

        :type RoutingConfig: dict
        :param RoutingConfig:

          The `routing configuration
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
          of the alias.

          - **AdditionalVersionWeights** *(dict) --*

            The name of the second alias, and the percentage of traffic that's routed to it.

            - *(string) --*

              - *(float) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AliasArn': 'string',
                'Name': 'string',
                'FunctionVersion': 'string',
                'Description': 'string',
                'RoutingConfig': {
                    'AdditionalVersionWeights': {
                        'string': 123.0
                    }
                },
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Provides configuration information about a Lambda function `alias
            <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

            - **AliasArn** *(string) --*

              The Amazon Resource Name (ARN) of the alias.

            - **Name** *(string) --*

              The name of the alias.

            - **FunctionVersion** *(string) --*

              The function version that the alias invokes.

            - **Description** *(string) --*

              A description of the alias.

            - **RoutingConfig** *(dict) --*

              The `routing configuration
              <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
              of the alias.

              - **AdditionalVersionWeights** *(dict) --*

                The name of the second alias, and the percentage of traffic that's routed to it.

                - *(string) --*

                  - *(float) --*

            - **RevisionId** *(string) --*

              A unique identifier that changes when you update the alias.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_event_source_mapping(
        self,
        EventSourceArn: str,
        FunctionName: str,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        ParallelizationFactor: int = None,
        StartingPosition: Literal["TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"] = None,
        StartingPositionTimestamp: datetime = None,
        DestinationConfig: ClientCreateEventSourceMappingDestinationConfigTypeDef = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
    ) -> ClientCreateEventSourceMappingResponseTypeDef:
        """
        Creates a mapping between an event source and an AWS Lambda function. Lambda reads items
        from the event source and triggers the function.

        For details about each event source type, see the following topics.

        * `Using AWS Lambda with Amazon DynamoDB
        <https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html>`__

        * `Using AWS Lambda with Amazon Kinesis
        <https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html>`__

        * `Using AWS Lambda with Amazon SQS
        <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html>`__

        The following error handling options are only available for stream sources (DynamoDB and
        Kinesis):

        * ``BisectBatchOnFunctionError`` - If the function returns an error, split the batch in two
        and retry.

        * ``DestinationConfig`` - Send discarded records to an Amazon SQS queue or Amazon SNS topic.

        * ``MaximumRecordAgeInSeconds`` - Discard records older than the specified age.

        * ``MaximumRetryAttempts`` - Discard records after the specified number of retries.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateEventSourceMapping>`_

        **Request Syntax**
        ::

          response = client.create_event_source_mapping(
              EventSourceArn='string',
              FunctionName='string',
              Enabled=True|False,
              BatchSize=123,
              MaximumBatchingWindowInSeconds=123,
              ParallelizationFactor=123,
              StartingPosition='TRIM_HORIZON'|'LATEST'|'AT_TIMESTAMP',
              StartingPositionTimestamp=datetime(2015, 1, 1),
              DestinationConfig={
                  'OnSuccess': {
                      'Destination': 'string'
                  },
                  'OnFailure': {
                      'Destination': 'string'
                  }
              },
              MaximumRecordAgeInSeconds=123,
              BisectBatchOnFunctionError=True|False,
              MaximumRetryAttempts=123
          )
        :type EventSourceArn: string
        :param EventSourceArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the event source.

          * **Amazon Kinesis** - The ARN of the data stream or a stream consumer.

          * **Amazon DynamoDB Streams** - The ARN of the stream.

          * **Amazon Simple Queue Service** - The ARN of the queue.

        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Version or Alias ARN** -
          ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it's limited to 64 characters in length.

        :type Enabled: boolean
        :param Enabled:

          Disables the event source mapping to pause polling and invocation.

        :type BatchSize: integer
        :param BatchSize:

          The maximum number of items to retrieve in a single batch.

          * **Amazon Kinesis** - Default 100. Max 10,000.

          * **Amazon DynamoDB Streams** - Default 100. Max 1,000.

          * **Amazon Simple Queue Service** - Default 10. Max 10.

        :type MaximumBatchingWindowInSeconds: integer
        :param MaximumBatchingWindowInSeconds:

          The maximum amount of time to gather records before invoking the function, in seconds.

        :type ParallelizationFactor: integer
        :param ParallelizationFactor:

          (Streams) The number of batches to process from each shard concurrently.

        :type StartingPosition: string
        :param StartingPosition:

          The position in a stream from which to start reading. Required for Amazon Kinesis and
          Amazon DynamoDB Streams sources. ``AT_TIMESTAMP`` is only supported for Amazon Kinesis
          streams.

        :type StartingPositionTimestamp: datetime
        :param StartingPositionTimestamp:

          With ``StartingPosition`` set to ``AT_TIMESTAMP`` , the time from which to start reading.

        :type DestinationConfig: dict
        :param DestinationConfig:

          (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

          - **OnSuccess** *(dict) --*

            The destination configuration for successful invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

          - **OnFailure** *(dict) --*

            The destination configuration for failed invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

        :type MaximumRecordAgeInSeconds: integer
        :param MaximumRecordAgeInSeconds:

          (Streams) The maximum age of a record that Lambda sends to a function for processing.

        :type BisectBatchOnFunctionError: boolean
        :param BisectBatchOnFunctionError:

          (Streams) If the function returns an error, split the batch in two and retry.

        :type MaximumRetryAttempts: integer
        :param MaximumRetryAttempts:

          (Streams) The maximum number of times to retry when the function returns an error.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UUID': 'string',
                'BatchSize': 123,
                'MaximumBatchingWindowInSeconds': 123,
                'ParallelizationFactor': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string',
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                },
                'MaximumRecordAgeInSeconds': 123,
                'BisectBatchOnFunctionError': True|False,
                'MaximumRetryAttempts': 123
            }
          **Response Structure**

          - *(dict) --*

            A mapping between an AWS resource and an AWS Lambda function. See
            CreateEventSourceMapping for details.

            - **UUID** *(string) --*

              The identifier of the event source mapping.

            - **BatchSize** *(integer) --*

              The maximum number of items to retrieve in a single batch.

            - **MaximumBatchingWindowInSeconds** *(integer) --*

              The maximum amount of time to gather records before invoking the function, in seconds.

            - **ParallelizationFactor** *(integer) --*

              (Streams) The number of batches to process from each shard concurrently.

            - **EventSourceArn** *(string) --*

              The Amazon Resource Name (ARN) of the event source.

            - **FunctionArn** *(string) --*

              The ARN of the Lambda function.

            - **LastModified** *(datetime) --*

              The date that the event source mapping was last updated, or its state changed.

            - **LastProcessingResult** *(string) --*

              The result of the last AWS Lambda invocation of your Lambda function.

            - **State** *(string) --*

              The state of the event source mapping. It can be one of the following: ``Creating`` ,
              ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
              ``Deleting`` .

            - **StateTransitionReason** *(string) --*

              Indicates whether the last change to the event source mapping was made by a user, or
              by the Lambda service.

            - **DestinationConfig** *(dict) --*

              (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

            - **MaximumRecordAgeInSeconds** *(integer) --*

              (Streams) The maximum age of a record that Lambda sends to a function for processing.

            - **BisectBatchOnFunctionError** *(boolean) --*

              (Streams) If the function returns an error, split the batch in two and retry.

            - **MaximumRetryAttempts** *(integer) --*

              (Streams) The maximum number of times to retry when the function returns an error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_function(
        self,
        FunctionName: str,
        Runtime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ],
        Role: str,
        Handler: str,
        Code: ClientCreateFunctionCodeTypeDef,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        Publish: bool = None,
        VpcConfig: ClientCreateFunctionVpcConfigTypeDef = None,
        DeadLetterConfig: ClientCreateFunctionDeadLetterConfigTypeDef = None,
        Environment: ClientCreateFunctionEnvironmentTypeDef = None,
        KMSKeyArn: str = None,
        TracingConfig: ClientCreateFunctionTracingConfigTypeDef = None,
        Tags: Dict[str, str] = None,
        Layers: List[str] = None,
    ) -> ClientCreateFunctionResponseTypeDef:
        """
        Creates a Lambda function. To create a function, you need a `deployment package
        <https://docs.aws.amazon.com/lambda/latest/dg/deployment-package-v2.html>`__ and an
        `execution role
        <https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html#lambda-intro-execution-role>`__
        . The deployment package contains your function code. The execution role grants the function
        permission to use AWS services, such as Amazon CloudWatch Logs for log streaming and AWS
        X-Ray for request tracing.

        When you create a function, Lambda provisions an instance of the function and its supporting
        resources. If your function connects to a VPC, this process can take a minute or so. During
        this time, you can't invoke or modify the function. The ``State`` , ``StateReason`` , and
        ``StateReasonCode`` fields in the response from  GetFunctionConfiguration indicate when the
        function is ready to invoke. For more information, see `Function States
        <https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html>`__ .

        A function has an unpublished version, and can have published versions and aliases. The
        unpublished version changes when you update your function's code and configuration. A
        published version is a snapshot of your function code and configuration that can't be
        changed. An alias is a named resource that maps to a version, and can be changed to map to a
        different version. Use the ``Publish`` parameter to create version ``1`` of your function
        from its initial configuration.

        The other parameters let you configure version-specific and function-level settings. You can
        modify version-specific settings later with  UpdateFunctionConfiguration . Function-level
        settings apply to both the unpublished and published versions of the function, and include
        tags ( TagResource ) and per-function concurrency limits ( PutFunctionConcurrency ).

        If another account or an AWS service invokes your function, use  AddPermission to grant
        permission by creating a resource-based IAM policy. You can grant permissions at the
        function level, on a version, or on an alias.

        To invoke your function directly, use  Invoke . To invoke your function in response to
        events in other AWS services, create an event source mapping ( CreateEventSourceMapping ),
        or configure a function trigger in the other service. For more information, see `Invoking
        Functions <https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/CreateFunction>`_

        **Request Syntax**
        ::

          response = client.create_function(
              FunctionName='string',
              Runtime=
                  'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                  |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                  |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              Role='string',
              Handler='string',
              Code={
                  'ZipFile': b'bytes',
                  'S3Bucket': 'string',
                  'S3Key': 'string',
                  'S3ObjectVersion': 'string'
              },
              Description='string',
              Timeout=123,
              MemorySize=123,
              Publish=True|False,
              VpcConfig={
                  'SubnetIds': [
                      'string',
                  ],
                  'SecurityGroupIds': [
                      'string',
                  ]
              },
              DeadLetterConfig={
                  'TargetArn': 'string'
              },
              Environment={
                  'Variables': {
                      'string': 'string'
                  }
              },
              KMSKeyArn='string',
              TracingConfig={
                  'Mode': 'Active'|'PassThrough'
              },
              Tags={
                  'string': 'string'
              },
              Layers=[
                  'string',
              ]
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Runtime: string
        :param Runtime: **[REQUIRED]**

          The identifier of the function's `runtime
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>`__ .

        :type Role: string
        :param Role: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the function's execution role.

        :type Handler: string
        :param Handler: **[REQUIRED]**

          The name of the method within your code that Lambda calls to execute your function. The
          format includes the file name. It can also include namespaces and other qualifiers,
          depending on the runtime. For more information, see `Programming Model
          <https://docs.aws.amazon.com/lambda/latest/dg/programming-model-v2.html>`__ .

        :type Code: dict
        :param Code: **[REQUIRED]**

          The code for the function.

          - **ZipFile** *(bytes) --*

            The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients
            handle the encoding for you.

          - **S3Bucket** *(string) --*

            An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a
            different AWS account.

          - **S3Key** *(string) --*

            The Amazon S3 key of the deployment package.

          - **S3ObjectVersion** *(string) --*

            For versioned objects, the version of the deployment package object to use.

        :type Description: string
        :param Description:

          A description of the function.

        :type Timeout: integer
        :param Timeout:

          The amount of time that Lambda allows a function to run before stopping it. The default is
          3 seconds. The maximum allowed value is 900 seconds.

        :type MemorySize: integer
        :param MemorySize:

          The amount of memory that your function has access to. Increasing the function's memory
          also increases its CPU allocation. The default value is 128 MB. The value must be a
          multiple of 64 MB.

        :type Publish: boolean
        :param Publish:

          Set to true to publish the first version of the function during creation.

        :type VpcConfig: dict
        :param VpcConfig:

          For network connectivity to AWS resources in a VPC, specify a list of security groups and
          subnets in the VPC. When you connect a function to a VPC, it can only access resources and
          the internet through that VPC. For more information, see `VPC Settings
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html>`__ .

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

        :type DeadLetterConfig: dict
        :param DeadLetterConfig:

          A dead letter queue configuration that specifies the queue or topic where Lambda sends
          asynchronous events when they fail processing. For more information, see `Dead Letter
          Queues <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq>`__ .

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        :type Environment: dict
        :param Environment:

          Environment variables that are accessible from function code during execution.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

        :type KMSKeyArn: string
        :param KMSKeyArn:

          The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your
          function's environment variables. If it's not provided, AWS Lambda uses a default service
          key.

        :type TracingConfig: dict
        :param TracingConfig:

          Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS
          X-Ray.

          - **Mode** *(string) --*

            The tracing mode.

        :type Tags: dict
        :param Tags:

          A list of `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ to apply to
          the function.

          - *(string) --*

            - *(string) --*

        :type Layers: list
        :param Layers:

          A list of `function layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ to add to the
          function's execution environment. Specify each layer by its ARN, including the version.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime':
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'
                |'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode':
                'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                |'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'
                |'SubnetOutOfIPAddresses',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode':
                'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'
                |'InternalError'
            }
          **Response Structure**

          - *(dict) --*

            Details about a function's configuration.

            - **FunctionName** *(string) --*

              The name of the function.

            - **FunctionArn** *(string) --*

              The function's Amazon Resource Name (ARN).

            - **Runtime** *(string) --*

              The runtime environment for the Lambda function.

            - **Role** *(string) --*

              The function's execution role.

            - **Handler** *(string) --*

              The function that Lambda calls to begin executing your function.

            - **CodeSize** *(integer) --*

              The size of the function's deployment package, in bytes.

            - **Description** *(string) --*

              The function's description.

            - **Timeout** *(integer) --*

              The amount of time that Lambda allows a function to run before stopping it.

            - **MemorySize** *(integer) --*

              The memory that's allocated to the function.

            - **LastModified** *(string) --*

              The date and time that the function was last updated, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **CodeSha256** *(string) --*

              The SHA256 hash of the function's deployment package.

            - **Version** *(string) --*

              The version of the Lambda function.

            - **VpcConfig** *(dict) --*

              The function's networking configuration.

              - **SubnetIds** *(list) --*

                A list of VPC subnet IDs.

                - *(string) --*

              - **SecurityGroupIds** *(list) --*

                A list of VPC security groups IDs.

                - *(string) --*

              - **VpcId** *(string) --*

                The ID of the VPC.

            - **DeadLetterConfig** *(dict) --*

              The function's dead letter queue.

              - **TargetArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

            - **Environment** *(dict) --*

              The function's environment variables.

              - **Variables** *(dict) --*

                Environment variable key-value pairs.

                - *(string) --*

                  - *(string) --*

              - **Error** *(dict) --*

                Error messages for environment variables that couldn't be applied.

                - **ErrorCode** *(string) --*

                  The error code.

                - **Message** *(string) --*

                  The error message.

            - **KMSKeyArn** *(string) --*

              The KMS key that's used to encrypt the function's environment variables. This key is
              only returned if you've configured a customer managed CMK.

            - **TracingConfig** *(dict) --*

              The function's AWS X-Ray tracing configuration.

              - **Mode** *(string) --*

                The tracing mode.

            - **MasterArn** *(string) --*

              For Lambda@Edge functions, the ARN of the master function.

            - **RevisionId** *(string) --*

              The latest updated revision of the function or alias.

            - **Layers** *(list) --*

              The function's `layers
              <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

              - *(dict) --*

                An `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **CodeSize** *(integer) --*

                  The size of the layer archive in bytes.

            - **State** *(string) --*

              The current state of the function. When the state is ``Inactive`` , you can reactivate
              the function by invoking it.

            - **StateReason** *(string) --*

              The reason for the function's current state.

            - **StateReasonCode** *(string) --*

              The reason code for the function's current state. When the code is ``Creating`` , you
              can't invoke or modify the function.

            - **LastUpdateStatus** *(string) --*

              The status of the last update that was performed on the function.

            - **LastUpdateStatusReason** *(string) --*

              The reason for the last update that was performed on the function.

            - **LastUpdateStatusReasonCode** *(string) --*

              The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, FunctionName: str, Name: str) -> None:
        """
        Deletes a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteAlias>`_

        **Request Syntax**
        ::

          response = client.delete_alias(
              FunctionName='string',
              Name='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the alias.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_event_source_mapping(
        self, UUID: str
    ) -> ClientDeleteEventSourceMappingResponseTypeDef:
        """
        Deletes an `event source mapping
        <https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html>`__ . You can get
        the identifier of a mapping from the output of  ListEventSourceMappings .

        When you delete an event source mapping, it enters a ``Deleting`` state and might not be
        completely deleted for several seconds.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteEventSourceMapping>`_

        **Request Syntax**
        ::

          response = client.delete_event_source_mapping(
              UUID='string'
          )
        :type UUID: string
        :param UUID: **[REQUIRED]**

          The identifier of the event source mapping.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UUID': 'string',
                'BatchSize': 123,
                'MaximumBatchingWindowInSeconds': 123,
                'ParallelizationFactor': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string',
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                },
                'MaximumRecordAgeInSeconds': 123,
                'BisectBatchOnFunctionError': True|False,
                'MaximumRetryAttempts': 123
            }
          **Response Structure**

          - *(dict) --*

            A mapping between an AWS resource and an AWS Lambda function. See
            CreateEventSourceMapping for details.

            - **UUID** *(string) --*

              The identifier of the event source mapping.

            - **BatchSize** *(integer) --*

              The maximum number of items to retrieve in a single batch.

            - **MaximumBatchingWindowInSeconds** *(integer) --*

              The maximum amount of time to gather records before invoking the function, in seconds.

            - **ParallelizationFactor** *(integer) --*

              (Streams) The number of batches to process from each shard concurrently.

            - **EventSourceArn** *(string) --*

              The Amazon Resource Name (ARN) of the event source.

            - **FunctionArn** *(string) --*

              The ARN of the Lambda function.

            - **LastModified** *(datetime) --*

              The date that the event source mapping was last updated, or its state changed.

            - **LastProcessingResult** *(string) --*

              The result of the last AWS Lambda invocation of your Lambda function.

            - **State** *(string) --*

              The state of the event source mapping. It can be one of the following: ``Creating`` ,
              ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
              ``Deleting`` .

            - **StateTransitionReason** *(string) --*

              Indicates whether the last change to the event source mapping was made by a user, or
              by the Lambda service.

            - **DestinationConfig** *(dict) --*

              (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

            - **MaximumRecordAgeInSeconds** *(integer) --*

              (Streams) The maximum age of a record that Lambda sends to a function for processing.

            - **BisectBatchOnFunctionError** *(boolean) --*

              (Streams) If the function returns an error, split the batch in two and retry.

            - **MaximumRetryAttempts** *(integer) --*

              (Streams) The maximum number of times to retry when the function returns an error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        Deletes a Lambda function. To delete a specific function version, use the ``Qualifier``
        parameter. Otherwise, all versions and aliases are deleted.

        To delete Lambda event source mappings that invoke a function, use  DeleteEventSourceMapping
        . For AWS services and resources that invoke your function directly, delete the trigger in
        the service where you originally configured it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunction>`_

        **Request Syntax**
        ::

          response = client.delete_function(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function or version.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:1`` (with version).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          Specify a version to delete. You can't delete a version that's referenced by an alias.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_concurrency(self, FunctionName: str) -> None:
        """
        Removes a concurrent execution limit from a function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunctionConcurrency>`_

        **Request Syntax**
        ::

          response = client.delete_function_concurrency(
              FunctionName='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_function_event_invoke_config(self, FunctionName: str, Qualifier: str = None) -> None:
        """
        Deletes the configuration for asynchronous invocation for a function, version, or alias.

        To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteFunctionEventInvokeConfig>`_

        **Request Syntax**
        ::

          response = client.delete_function_event_invoke_config(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          A version number or alias name.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_layer_version(self, LayerName: str, VersionNumber: int) -> None:
        """
        Deletes a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ . Deleted
        versions can no longer be viewed or added to functions. To avoid breaking functions, a copy
        of the version remains in Lambda until no functions refer to it.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteLayerVersion>`_

        **Request Syntax**
        ::

          response = client.delete_layer_version(
              LayerName='string',
              VersionNumber=123
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type VersionNumber: integer
        :param VersionNumber: **[REQUIRED]**

          The version number.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_provisioned_concurrency_config(self, FunctionName: str, Qualifier: str) -> None:
        """
        Deletes the provisioned concurrency configuration for a function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/DeleteProvisionedConcurrencyConfig>`_

        **Request Syntax**
        ::

          response = client.delete_provisioned_concurrency_config(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Qualifier: string
        :param Qualifier: **[REQUIRED]**

          The version number or alias name.

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
    def get_account_settings(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetAccountSettingsResponseTypeDef:
        """
        Retrieves details about your account's `limits
        <https://docs.aws.amazon.com/lambda/latest/dg/limits.html>`__ and usage in an AWS Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAccountSettings>`_

        **Request Syntax**
        ::

          response = client.get_account_settings()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AccountLimit': {
                    'TotalCodeSize': 123,
                    'CodeSizeUnzipped': 123,
                    'CodeSizeZipped': 123,
                    'ConcurrentExecutions': 123,
                    'UnreservedConcurrentExecutions': 123
                },
                'AccountUsage': {
                    'TotalCodeSize': 123,
                    'FunctionCount': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **AccountLimit** *(dict) --*

              Limits that are related to concurrency and code storage.

              - **TotalCodeSize** *(integer) --*

                The amount of storage space that you can use for all deployment packages and layer
                archives.

              - **CodeSizeUnzipped** *(integer) --*

                The maximum size of a function's deployment package and layers when they're
                extracted.

              - **CodeSizeZipped** *(integer) --*

                The maximum size of a deployment package when it's uploaded directly to AWS Lambda.
                Use Amazon S3 for larger files.

              - **ConcurrentExecutions** *(integer) --*

                The maximum number of simultaneous function executions.

              - **UnreservedConcurrentExecutions** *(integer) --*

                The maximum number of simultaneous function executions, minus the capacity that's
                reserved for individual functions with  PutFunctionConcurrency .

            - **AccountUsage** *(dict) --*

              The number of functions and amount of storage in use.

              - **TotalCodeSize** *(integer) --*

                The amount of storage space, in bytes, that's being used by deployment packages and
                layer archives.

              - **FunctionCount** *(integer) --*

                The number of Lambda functions.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_alias(self, FunctionName: str, Name: str) -> ClientGetAliasResponseTypeDef:
        """
        Returns details about a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetAlias>`_

        **Request Syntax**
        ::

          response = client.get_alias(
              FunctionName='string',
              Name='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the alias.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AliasArn': 'string',
                'Name': 'string',
                'FunctionVersion': 'string',
                'Description': 'string',
                'RoutingConfig': {
                    'AdditionalVersionWeights': {
                        'string': 123.0
                    }
                },
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Provides configuration information about a Lambda function `alias
            <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

            - **AliasArn** *(string) --*

              The Amazon Resource Name (ARN) of the alias.

            - **Name** *(string) --*

              The name of the alias.

            - **FunctionVersion** *(string) --*

              The function version that the alias invokes.

            - **Description** *(string) --*

              A description of the alias.

            - **RoutingConfig** *(dict) --*

              The `routing configuration
              <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
              of the alias.

              - **AdditionalVersionWeights** *(dict) --*

                The name of the second alias, and the percentage of traffic that's routed to it.

                - *(string) --*

                  - *(float) --*

            - **RevisionId** *(string) --*

              A unique identifier that changes when you update the alias.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_event_source_mapping(self, UUID: str) -> ClientGetEventSourceMappingResponseTypeDef:
        """
        Returns details about an event source mapping. You can get the identifier of a mapping from
        the output of  ListEventSourceMappings .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetEventSourceMapping>`_

        **Request Syntax**
        ::

          response = client.get_event_source_mapping(
              UUID='string'
          )
        :type UUID: string
        :param UUID: **[REQUIRED]**

          The identifier of the event source mapping.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UUID': 'string',
                'BatchSize': 123,
                'MaximumBatchingWindowInSeconds': 123,
                'ParallelizationFactor': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string',
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                },
                'MaximumRecordAgeInSeconds': 123,
                'BisectBatchOnFunctionError': True|False,
                'MaximumRetryAttempts': 123
            }
          **Response Structure**

          - *(dict) --*

            A mapping between an AWS resource and an AWS Lambda function. See
            CreateEventSourceMapping for details.

            - **UUID** *(string) --*

              The identifier of the event source mapping.

            - **BatchSize** *(integer) --*

              The maximum number of items to retrieve in a single batch.

            - **MaximumBatchingWindowInSeconds** *(integer) --*

              The maximum amount of time to gather records before invoking the function, in seconds.

            - **ParallelizationFactor** *(integer) --*

              (Streams) The number of batches to process from each shard concurrently.

            - **EventSourceArn** *(string) --*

              The Amazon Resource Name (ARN) of the event source.

            - **FunctionArn** *(string) --*

              The ARN of the Lambda function.

            - **LastModified** *(datetime) --*

              The date that the event source mapping was last updated, or its state changed.

            - **LastProcessingResult** *(string) --*

              The result of the last AWS Lambda invocation of your Lambda function.

            - **State** *(string) --*

              The state of the event source mapping. It can be one of the following: ``Creating`` ,
              ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
              ``Deleting`` .

            - **StateTransitionReason** *(string) --*

              Indicates whether the last change to the event source mapping was made by a user, or
              by the Lambda service.

            - **DestinationConfig** *(dict) --*

              (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

            - **MaximumRecordAgeInSeconds** *(integer) --*

              (Streams) The maximum age of a record that Lambda sends to a function for processing.

            - **BisectBatchOnFunctionError** *(boolean) --*

              (Streams) If the function returns an error, split the batch in two and retry.

            - **MaximumRetryAttempts** *(integer) --*

              (Streams) The maximum number of times to retry when the function returns an error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function(
        self, FunctionName: str, Qualifier: str = None
    ) -> ClientGetFunctionResponseTypeDef:
        """
        Returns information about the function or function version, with a link to download the
        deployment package that's valid for 10 minutes. If you specify a function version, only
        details that are specific to that version are returned.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunction>`_

        **Request Syntax**
        ::

          response = client.get_function(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to get details about a published version of the function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Configuration': {
                    'FunctionName': 'string',
                    'FunctionArn': 'string',
                    'Runtime':
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'
                    |'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'
                    |'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'
                    |'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                    'Role': 'string',
                    'Handler': 'string',
                    'CodeSize': 123,
                    'Description': 'string',
                    'Timeout': 123,
                    'MemorySize': 123,
                    'LastModified': 'string',
                    'CodeSha256': 'string',
                    'Version': 'string',
                    'VpcConfig': {
                        'SubnetIds': [
                            'string',
                        ],
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'VpcId': 'string'
                    },
                    'DeadLetterConfig': {
                        'TargetArn': 'string'
                    },
                    'Environment': {
                        'Variables': {
                            'string': 'string'
                        },
                        'Error': {
                            'ErrorCode': 'string',
                            'Message': 'string'
                        }
                    },
                    'KMSKeyArn': 'string',
                    'TracingConfig': {
                        'Mode': 'Active'|'PassThrough'
                    },
                    'MasterArn': 'string',
                    'RevisionId': 'string',
                    'Layers': [
                        {
                            'Arn': 'string',
                            'CodeSize': 123
                        },
                    ],
                    'State': 'Pending'|'Active'|'Inactive'|'Failed',
                    'StateReason': 'string',
                    'StateReasonCode':
                    'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                    |'InsufficientRolePermissions'|'InvalidConfiguration'
                    |'InternalError'|'SubnetOutOfIPAddresses',
                    'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                    'LastUpdateStatusReason': 'string',
                    'LastUpdateStatusReasonCode':
                    'EniLimitExceeded'|'InsufficientRolePermissions'
                    |'InvalidConfiguration'|'InternalError'
                },
                'Code': {
                    'RepositoryType': 'string',
                    'Location': 'string'
                },
                'Tags': {
                    'string': 'string'
                },
                'Concurrency': {
                    'ReservedConcurrentExecutions': 123
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Configuration** *(dict) --*

              The configuration of the function or version.

              - **FunctionName** *(string) --*

                The name of the function.

              - **FunctionArn** *(string) --*

                The function's Amazon Resource Name (ARN).

              - **Runtime** *(string) --*

                The runtime environment for the Lambda function.

              - **Role** *(string) --*

                The function's execution role.

              - **Handler** *(string) --*

                The function that Lambda calls to begin executing your function.

              - **CodeSize** *(integer) --*

                The size of the function's deployment package, in bytes.

              - **Description** *(string) --*

                The function's description.

              - **Timeout** *(integer) --*

                The amount of time that Lambda allows a function to run before stopping it.

              - **MemorySize** *(integer) --*

                The memory that's allocated to the function.

              - **LastModified** *(string) --*

                The date and time that the function was last updated, in `ISO-8601 format
                <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

              - **CodeSha256** *(string) --*

                The SHA256 hash of the function's deployment package.

              - **Version** *(string) --*

                The version of the Lambda function.

              - **VpcConfig** *(dict) --*

                The function's networking configuration.

                - **SubnetIds** *(list) --*

                  A list of VPC subnet IDs.

                  - *(string) --*

                - **SecurityGroupIds** *(list) --*

                  A list of VPC security groups IDs.

                  - *(string) --*

                - **VpcId** *(string) --*

                  The ID of the VPC.

              - **DeadLetterConfig** *(dict) --*

                The function's dead letter queue.

                - **TargetArn** *(string) --*

                  The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

              - **Environment** *(dict) --*

                The function's environment variables.

                - **Variables** *(dict) --*

                  Environment variable key-value pairs.

                  - *(string) --*

                    - *(string) --*

                - **Error** *(dict) --*

                  Error messages for environment variables that couldn't be applied.

                  - **ErrorCode** *(string) --*

                    The error code.

                  - **Message** *(string) --*

                    The error message.

              - **KMSKeyArn** *(string) --*

                The KMS key that's used to encrypt the function's environment variables. This key is
                only returned if you've configured a customer managed CMK.

              - **TracingConfig** *(dict) --*

                The function's AWS X-Ray tracing configuration.

                - **Mode** *(string) --*

                  The tracing mode.

              - **MasterArn** *(string) --*

                For Lambda@Edge functions, the ARN of the master function.

              - **RevisionId** *(string) --*

                The latest updated revision of the function or alias.

              - **Layers** *(list) --*

                The function's `layers
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - *(dict) --*

                  An `AWS Lambda layer
                  <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                  - **Arn** *(string) --*

                    The Amazon Resource Name (ARN) of the function layer.

                  - **CodeSize** *(integer) --*

                    The size of the layer archive in bytes.

              - **State** *(string) --*

                The current state of the function. When the state is ``Inactive`` , you can
                reactivate the function by invoking it.

              - **StateReason** *(string) --*

                The reason for the function's current state.

              - **StateReasonCode** *(string) --*

                The reason code for the function's current state. When the code is ``Creating`` ,
                you can't invoke or modify the function.

              - **LastUpdateStatus** *(string) --*

                The status of the last update that was performed on the function.

              - **LastUpdateStatusReason** *(string) --*

                The reason for the last update that was performed on the function.

              - **LastUpdateStatusReasonCode** *(string) --*

                The reason code for the last update that was performed on the function.

            - **Code** *(dict) --*

              The deployment package of the function or version.

              - **RepositoryType** *(string) --*

                The service that's hosting the file.

              - **Location** *(string) --*

                A presigned URL that you can use to download the deployment package.

            - **Tags** *(dict) --*

              The function's `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ .

              - *(string) --*

                - *(string) --*

            - **Concurrency** *(dict) --*

              The function's `reserved concurrency
              <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .

              - **ReservedConcurrentExecutions** *(integer) --*

                The number of concurrent executions that are reserved for this function. For more
                information, see `Managing Concurrency
                <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_concurrency(
        self, FunctionName: str
    ) -> ClientGetFunctionConcurrencyResponseTypeDef:
        """
        Returns details about the concurrency configuration for a function. To set a concurrency
        limit for a function, use  PutFunctionConcurrency .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunctionConcurrency>`_

        **Request Syntax**
        ::

          response = client.get_function_concurrency(
              FunctionName='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReservedConcurrentExecutions': 123
            }
          **Response Structure**

          - *(dict) --*

            - **ReservedConcurrentExecutions** *(integer) --*

              The number of simultaneous executions that are reserved for the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_configuration(
        self, FunctionName: str, Qualifier: str = None
    ) -> ClientGetFunctionConfigurationResponseTypeDef:
        """
        Returns the version-specific settings of a Lambda function or version. The output includes
        only options that can vary between versions of a function. To modify these settings, use
        UpdateFunctionConfiguration .

        To get all of a function's details, including function-level settings, use  GetFunction .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunctionConfiguration>`_

        **Request Syntax**
        ::

          response = client.get_function_configuration(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to get details about a published version of the function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime':
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'
                |'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode':
                'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                |'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'
                |'SubnetOutOfIPAddresses',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode':
                'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'
                |'InternalError'
            }
          **Response Structure**

          - *(dict) --*

            Details about a function's configuration.

            - **FunctionName** *(string) --*

              The name of the function.

            - **FunctionArn** *(string) --*

              The function's Amazon Resource Name (ARN).

            - **Runtime** *(string) --*

              The runtime environment for the Lambda function.

            - **Role** *(string) --*

              The function's execution role.

            - **Handler** *(string) --*

              The function that Lambda calls to begin executing your function.

            - **CodeSize** *(integer) --*

              The size of the function's deployment package, in bytes.

            - **Description** *(string) --*

              The function's description.

            - **Timeout** *(integer) --*

              The amount of time that Lambda allows a function to run before stopping it.

            - **MemorySize** *(integer) --*

              The memory that's allocated to the function.

            - **LastModified** *(string) --*

              The date and time that the function was last updated, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **CodeSha256** *(string) --*

              The SHA256 hash of the function's deployment package.

            - **Version** *(string) --*

              The version of the Lambda function.

            - **VpcConfig** *(dict) --*

              The function's networking configuration.

              - **SubnetIds** *(list) --*

                A list of VPC subnet IDs.

                - *(string) --*

              - **SecurityGroupIds** *(list) --*

                A list of VPC security groups IDs.

                - *(string) --*

              - **VpcId** *(string) --*

                The ID of the VPC.

            - **DeadLetterConfig** *(dict) --*

              The function's dead letter queue.

              - **TargetArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

            - **Environment** *(dict) --*

              The function's environment variables.

              - **Variables** *(dict) --*

                Environment variable key-value pairs.

                - *(string) --*

                  - *(string) --*

              - **Error** *(dict) --*

                Error messages for environment variables that couldn't be applied.

                - **ErrorCode** *(string) --*

                  The error code.

                - **Message** *(string) --*

                  The error message.

            - **KMSKeyArn** *(string) --*

              The KMS key that's used to encrypt the function's environment variables. This key is
              only returned if you've configured a customer managed CMK.

            - **TracingConfig** *(dict) --*

              The function's AWS X-Ray tracing configuration.

              - **Mode** *(string) --*

                The tracing mode.

            - **MasterArn** *(string) --*

              For Lambda@Edge functions, the ARN of the master function.

            - **RevisionId** *(string) --*

              The latest updated revision of the function or alias.

            - **Layers** *(list) --*

              The function's `layers
              <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

              - *(dict) --*

                An `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **CodeSize** *(integer) --*

                  The size of the layer archive in bytes.

            - **State** *(string) --*

              The current state of the function. When the state is ``Inactive`` , you can reactivate
              the function by invoking it.

            - **StateReason** *(string) --*

              The reason for the function's current state.

            - **StateReasonCode** *(string) --*

              The reason code for the function's current state. When the code is ``Creating`` , you
              can't invoke or modify the function.

            - **LastUpdateStatus** *(string) --*

              The status of the last update that was performed on the function.

            - **LastUpdateStatusReason** *(string) --*

              The reason for the last update that was performed on the function.

            - **LastUpdateStatusReasonCode** *(string) --*

              The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_function_event_invoke_config(
        self, FunctionName: str, Qualifier: str = None
    ) -> ClientGetFunctionEventInvokeConfigResponseTypeDef:
        """
        Retrieves the configuration for asynchronous invocation for a function, version, or alias.

        To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetFunctionEventInvokeConfig>`_

        **Request Syntax**
        ::

          response = client.get_function_event_invoke_config(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          A version number or alias name.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LastModified': datetime(2015, 1, 1),
                'FunctionArn': 'string',
                'MaximumRetryAttempts': 123,
                'MaximumEventAgeInSeconds': 123,
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LastModified** *(datetime) --*

              The date and time that the configuration was last updated.

            - **FunctionArn** *(string) --*

              The Amazon Resource Name (ARN) of the function.

            - **MaximumRetryAttempts** *(integer) --*

              The maximum number of times to retry when the function returns an error.

            - **MaximumEventAgeInSeconds** *(integer) --*

              The maximum age of a request that Lambda sends to a function for processing.

            - **DestinationConfig** *(dict) --*

              A destination for events after they have been sent to a function for processing.

               **Destinations**

              * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

              * **Queue** - The ARN of an SQS queue.

              * **Topic** - The ARN of an SNS topic.

              * **Event Bus** - The ARN of an Amazon EventBridge event bus.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version(
        self, LayerName: str, VersionNumber: int
    ) -> ClientGetLayerVersionResponseTypeDef:
        """
        Returns information about a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ , with a link to
        download the layer archive that's valid for 10 minutes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetLayerVersion>`_

        **Request Syntax**
        ::

          response = client.get_layer_version(
              LayerName='string',
              VersionNumber=123
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type VersionNumber: integer
        :param VersionNumber: **[REQUIRED]**

          The version number.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Content': {
                    'Location': 'string',
                    'CodeSha256': 'string',
                    'CodeSize': 123
                },
                'LayerArn': 'string',
                'LayerVersionArn': 'string',
                'Description': 'string',
                'CreatedDate': 'string',
                'Version': 123,
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                    |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                    |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                ],
                'LicenseInfo': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Content** *(dict) --*

              Details about the layer version.

              - **Location** *(string) --*

                A link to the layer archive in Amazon S3 that is valid for 10 minutes.

              - **CodeSha256** *(string) --*

                The SHA-256 hash of the layer archive.

              - **CodeSize** *(integer) --*

                The size of the layer archive in bytes.

            - **LayerArn** *(string) --*

              The ARN of the layer.

            - **LayerVersionArn** *(string) --*

              The ARN of the layer version.

            - **Description** *(string) --*

              The description of the version.

            - **CreatedDate** *(string) --*

              The date that the layer version was created, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **Version** *(integer) --*

              The version number.

            - **CompatibleRuntimes** *(list) --*

              The layer's compatible runtimes.

              - *(string) --*

            - **LicenseInfo** *(string) --*

              The layer's software license.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version_by_arn(self, Arn: str) -> ClientGetLayerVersionByArnResponseTypeDef:
        """
        Returns information about a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ , with a link to
        download the layer archive that's valid for 10 minutes.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetLayerVersionByArn>`_

        **Request Syntax**
        ::

          response = client.get_layer_version_by_arn(
              Arn='string'
          )
        :type Arn: string
        :param Arn: **[REQUIRED]**

          The ARN of the layer version.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Content': {
                    'Location': 'string',
                    'CodeSha256': 'string',
                    'CodeSize': 123
                },
                'LayerArn': 'string',
                'LayerVersionArn': 'string',
                'Description': 'string',
                'CreatedDate': 'string',
                'Version': 123,
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                    |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                    |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                ],
                'LicenseInfo': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Content** *(dict) --*

              Details about the layer version.

              - **Location** *(string) --*

                A link to the layer archive in Amazon S3 that is valid for 10 minutes.

              - **CodeSha256** *(string) --*

                The SHA-256 hash of the layer archive.

              - **CodeSize** *(integer) --*

                The size of the layer archive in bytes.

            - **LayerArn** *(string) --*

              The ARN of the layer.

            - **LayerVersionArn** *(string) --*

              The ARN of the layer version.

            - **Description** *(string) --*

              The description of the version.

            - **CreatedDate** *(string) --*

              The date that the layer version was created, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **Version** *(integer) --*

              The version number.

            - **CompatibleRuntimes** *(list) --*

              The layer's compatible runtimes.

              - *(string) --*

            - **LicenseInfo** *(string) --*

              The layer's software license.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_layer_version_policy(
        self, LayerName: str, VersionNumber: int
    ) -> ClientGetLayerVersionPolicyResponseTypeDef:
        """
        Returns the permission policy for a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ . For more
        information, see  AddLayerVersionPermission .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetLayerVersionPolicy>`_

        **Request Syntax**
        ::

          response = client.get_layer_version_policy(
              LayerName='string',
              VersionNumber=123
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type VersionNumber: integer
        :param VersionNumber: **[REQUIRED]**

          The version number.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string',
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              The policy document.

            - **RevisionId** *(string) --*

              A unique identifier for the current revision of the policy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_policy(
        self, FunctionName: str, Qualifier: str = None
    ) -> ClientGetPolicyResponseTypeDef:
        """
        Returns the `resource-based IAM policy
        <https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html>`__ for a
        function, version, or alias.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetPolicy>`_

        **Request Syntax**
        ::

          response = client.get_policy(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to get the policy for that resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string',
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              The resource-based policy.

            - **RevisionId** *(string) --*

              A unique identifier for the current revision of the policy.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str
    ) -> ClientGetProvisionedConcurrencyConfigResponseTypeDef:
        """
        Retrieves the provisioned concurrency configuration for a function's alias or version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/GetProvisionedConcurrencyConfig>`_

        **Request Syntax**
        ::

          response = client.get_provisioned_concurrency_config(
              FunctionName='string',
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Qualifier: string
        :param Qualifier: **[REQUIRED]**

          The version number or alias name.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestedProvisionedConcurrentExecutions': 123,
                'AvailableProvisionedConcurrentExecutions': 123,
                'AllocatedProvisionedConcurrentExecutions': 123,
                'Status': 'IN_PROGRESS'|'READY'|'FAILED',
                'StatusReason': 'string',
                'LastModified': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestedProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency requested.

            - **AvailableProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency available.

            - **AllocatedProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency allocated.

            - **Status** *(string) --*

              The status of the allocation process.

            - **StatusReason** *(string) --*

              For failed allocations, the reason that provisioned concurrency could not be
              allocated.

            - **LastModified** *(string) --*

              The date and time that a user last updated the configuration, in `ISO 8601 format
              <https://www.iso.org/iso-8601-date-and-time-format.html>`__ .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke(
        self,
        FunctionName: str,
        InvocationType: Literal["Event", "RequestResponse", "DryRun"] = None,
        LogType: Literal["None", "Tail"] = None,
        ClientContext: str = None,
        Payload: Union[bytes, IO] = None,
        Qualifier: str = None,
    ) -> ClientInvokeResponseTypeDef:
        """
        Invokes a Lambda function. You can invoke a function synchronously (and wait for the
        response), or asynchronously. To invoke a function asynchronously, set ``InvocationType`` to
        ``Event`` .

        For `synchronous invocation
        <https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html>`__ , details about the
        function response, including errors, are included in the response body and headers. For
        either invocation type, you can find more information in the `execution log
        <https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions.html>`__ and `trace
        <https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html>`__ .

        When an error occurs, your function may be invoked multiple times. Retry behavior varies by
        error type, client, event source, and invocation type. For example, if you invoke a function
        asynchronously and it returns an error, Lambda executes the function up to two more times.
        For more information, see `Retry Behavior
        <https://docs.aws.amazon.com/lambda/latest/dg/retries-on-errors.html>`__ .

        For `asynchronous invocation
        <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html>`__ , Lambda adds events
        to a queue before sending them to your function. If your function does not have enough
        capacity to keep up with the queue, events may be lost. Occasionally, your function may
        receive the same event multiple times, even if no error occurs. To retain events that were
        not processed, configure your function with a `dead-letter queue
        <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq>`__ .

        The status code in the API response doesn't reflect function errors. Error codes are
        reserved for errors that prevent your function from executing, such as permissions errors,
        `limit errors <https://docs.aws.amazon.com/lambda/latest/dg/limits.html>`__ , or issues with
        your function's code and configuration. For example, Lambda returns
        ``TooManyRequestsException`` if executing the function would cause you to exceed a
        concurrency limit at either the account level (``ConcurrentInvocationLimitExceeded`` ) or
        function level (``ReservedFunctionConcurrentInvocationLimitExceeded`` ).

        For functions with a long timeout, your client might be disconnected during synchronous
        invocation while it waits for a response. Configure your HTTP client, SDK, firewall, proxy,
        or operating system to allow for long connections with timeout or keep-alive settings.

        This operation requires permission for the ``lambda:InvokeFunction`` action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/Invoke>`_

        **Request Syntax**
        ::

          response = client.invoke(
              FunctionName='string',
              InvocationType='Event'|'RequestResponse'|'DryRun',
              LogType='None'|'Tail',
              ClientContext='string',
              Payload=b'bytes'|file,
              Qualifier='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type InvocationType: string
        :param InvocationType:

          Choose from the following options.

          * ``RequestResponse`` (default) - Invoke the function synchronously. Keep the connection
          open until the function returns a response or times out. The API response includes the
          function response and additional data.

          * ``Event`` - Invoke the function asynchronously. Send events that fail multiple times to
          the function's dead-letter queue (if it's configured). The API response only includes a
          status code.

          * ``DryRun`` - Validate parameter values and verify that the user or role has permission
          to invoke the function.

        :type LogType: string
        :param LogType:

          Set to ``Tail`` to include the execution log in the response.

        :type ClientContext: string
        :param ClientContext:

          Up to 3583 bytes of base64-encoded data about the invoking client to pass to the function
          in the context object.

        :type Payload: bytes or seekable file-like object
        :param Payload:

          The JSON that you want to provide to your Lambda function as input.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to invoke a published version of the function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'StatusCode': 123,
                'FunctionError': 'string',
                'LogResult': 'string',
                'Payload': StreamingBody(),
                'ExecutedVersion': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **StatusCode** *(integer) --*

              The HTTP status code is in the 200 range for a successful request. For the
              ``RequestResponse`` invocation type, this status code is 200. For the ``Event``
              invocation type, this status code is 202. For the ``DryRun`` invocation type, the
              status code is 204.

            - **FunctionError** *(string) --*

              If present, indicates that an error occurred during function execution. Details about
              the error are included in the response payload.

              * ``Handled`` - The runtime caught an error thrown by the function and formatted it
              into a JSON document.

              * ``Unhandled`` - The runtime didn't handle the error. For example, the function ran
              out of memory or timed out.

            - **LogResult** *(string) --*

              The last 4 KB of the execution log, which is base64 encoded.

            - **Payload** (:class:`.StreamingBody`) --

              The response from the function, or an error object.

            - **ExecutedVersion** *(string) --*

              The version of the function that executed. When you invoke a function with an alias,
              this indicates which version the alias resolved to.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def invoke_async(
        self, FunctionName: str, InvokeArgs: Union[bytes, IO]
    ) -> ClientInvokeAsyncResponseTypeDef:
        """
        .. warning::

          For asynchronous function invocation, use  Invoke .

        Invokes a function asynchronously.

        .. danger::

            This operation is deprecated and may not function as expected. This operation should not
            be used going forward and is only kept for the purpose of backwards compatiblity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/InvokeAsync>`_

        **Request Syntax**
        ::

          response = client.invoke_async(
              FunctionName='string',
              InvokeArgs=b'bytes'|file
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type InvokeArgs: bytes or seekable file-like object
        :param InvokeArgs: **[REQUIRED]**

          The JSON that you want to provide to your Lambda function as input.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Status': 123
            }
          **Response Structure**

          - *(dict) --*

            A success response (``202 Accepted`` ) indicates that the request is queued for
            invocation.

            - **Status** *(integer) --*

              The status code.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListAliasesResponseTypeDef:
        """
        Returns a list of `aliases
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ for a Lambda
        function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListAliases>`_

        **Request Syntax**
        ::

          response = client.list_aliases(
              FunctionName='string',
              FunctionVersion='string',
              Marker='string',
              MaxItems=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type FunctionVersion: string
        :param FunctionVersion:

          Specify a function version to only list aliases that invoke that version.

        :type Marker: string
        :param Marker:

          Specify the pagination token that's returned by a previous request to retrieve the next
          page of results.

        :type MaxItems: integer
        :param MaxItems:

          Limit the number of aliases returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'Aliases': [
                    {
                        'AliasArn': 'string',
                        'Name': 'string',
                        'FunctionVersion': 'string',
                        'Description': 'string',
                        'RoutingConfig': {
                            'AdditionalVersionWeights': {
                                'string': 123.0
                            }
                        },
                        'RevisionId': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextMarker** *(string) --*

              The pagination token that's included if more results are available.

            - **Aliases** *(list) --*

              A list of aliases.

              - *(dict) --*

                Provides configuration information about a Lambda function `alias
                <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

                - **AliasArn** *(string) --*

                  The Amazon Resource Name (ARN) of the alias.

                - **Name** *(string) --*

                  The name of the alias.

                - **FunctionVersion** *(string) --*

                  The function version that the alias invokes.

                - **Description** *(string) --*

                  A description of the alias.

                - **RoutingConfig** *(dict) --*

                  The `routing configuration
                  <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
                  of the alias.

                  - **AdditionalVersionWeights** *(dict) --*

                    The name of the second alias, and the percentage of traffic that's routed to it.

                    - *(string) --*

                      - *(float) --*

                - **RevisionId** *(string) --*

                  A unique identifier that changes when you update the alias.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_event_source_mappings(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListEventSourceMappingsResponseTypeDef:
        """
        Lists event source mappings. Specify an ``EventSourceArn`` to only show event source
        mappings for a single event source.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListEventSourceMappings>`_

        **Request Syntax**
        ::

          response = client.list_event_source_mappings(
              EventSourceArn='string',
              FunctionName='string',
              Marker='string',
              MaxItems=123
          )
        :type EventSourceArn: string
        :param EventSourceArn:

          The Amazon Resource Name (ARN) of the event source.

          * **Amazon Kinesis** - The ARN of the data stream or a stream consumer.

          * **Amazon DynamoDB Streams** - The ARN of the stream.

          * **Amazon Simple Queue Service** - The ARN of the queue.

        :type FunctionName: string
        :param FunctionName:

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Version or Alias ARN** -
          ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it's limited to 64 characters in length.

        :type Marker: string
        :param Marker:

          A pagination token returned by a previous call.

        :type MaxItems: integer
        :param MaxItems:

          The maximum number of event source mappings to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'EventSourceMappings': [
                    {
                        'UUID': 'string',
                        'BatchSize': 123,
                        'MaximumBatchingWindowInSeconds': 123,
                        'ParallelizationFactor': 123,
                        'EventSourceArn': 'string',
                        'FunctionArn': 'string',
                        'LastModified': datetime(2015, 1, 1),
                        'LastProcessingResult': 'string',
                        'State': 'string',
                        'StateTransitionReason': 'string',
                        'DestinationConfig': {
                            'OnSuccess': {
                                'Destination': 'string'
                            },
                            'OnFailure': {
                                'Destination': 'string'
                            }
                        },
                        'MaximumRecordAgeInSeconds': 123,
                        'BisectBatchOnFunctionError': True|False,
                        'MaximumRetryAttempts': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextMarker** *(string) --*

              A pagination token that's returned when the response doesn't contain all event source
              mappings.

            - **EventSourceMappings** *(list) --*

              A list of event source mappings.

              - *(dict) --*

                A mapping between an AWS resource and an AWS Lambda function. See
                CreateEventSourceMapping for details.

                - **UUID** *(string) --*

                  The identifier of the event source mapping.

                - **BatchSize** *(integer) --*

                  The maximum number of items to retrieve in a single batch.

                - **MaximumBatchingWindowInSeconds** *(integer) --*

                  The maximum amount of time to gather records before invoking the function, in
                  seconds.

                - **ParallelizationFactor** *(integer) --*

                  (Streams) The number of batches to process from each shard concurrently.

                - **EventSourceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the event source.

                - **FunctionArn** *(string) --*

                  The ARN of the Lambda function.

                - **LastModified** *(datetime) --*

                  The date that the event source mapping was last updated, or its state changed.

                - **LastProcessingResult** *(string) --*

                  The result of the last AWS Lambda invocation of your Lambda function.

                - **State** *(string) --*

                  The state of the event source mapping. It can be one of the following:
                  ``Creating`` , ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` ,
                  ``Updating`` , or ``Deleting`` .

                - **StateTransitionReason** *(string) --*

                  Indicates whether the last change to the event source mapping was made by a user,
                  or by the Lambda service.

                - **DestinationConfig** *(dict) --*

                  (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded
                  records.

                  - **OnSuccess** *(dict) --*

                    The destination configuration for successful invocations.

                    - **Destination** *(string) --*

                      The Amazon Resource Name (ARN) of the destination resource.

                  - **OnFailure** *(dict) --*

                    The destination configuration for failed invocations.

                    - **Destination** *(string) --*

                      The Amazon Resource Name (ARN) of the destination resource.

                - **MaximumRecordAgeInSeconds** *(integer) --*

                  (Streams) The maximum age of a record that Lambda sends to a function for
                  processing.

                - **BisectBatchOnFunctionError** *(boolean) --*

                  (Streams) If the function returns an error, split the batch in two and retry.

                - **MaximumRetryAttempts** *(integer) --*

                  (Streams) The maximum number of times to retry when the function returns an error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_function_event_invoke_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListFunctionEventInvokeConfigsResponseTypeDef:
        """
        Retrieves a list of configurations for asynchronous invocation for a function.

        To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctionEventInvokeConfigs>`_

        **Request Syntax**
        ::

          response = client.list_function_event_invoke_configs(
              FunctionName='string',
              Marker='string',
              MaxItems=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Marker: string
        :param Marker:

          Specify the pagination token that's returned by a previous request to retrieve the next
          page of results.

        :type MaxItems: integer
        :param MaxItems:

          The maximum number of configurations to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionEventInvokeConfigs': [
                    {
                        'LastModified': datetime(2015, 1, 1),
                        'FunctionArn': 'string',
                        'MaximumRetryAttempts': 123,
                        'MaximumEventAgeInSeconds': 123,
                        'DestinationConfig': {
                            'OnSuccess': {
                                'Destination': 'string'
                            },
                            'OnFailure': {
                                'Destination': 'string'
                            }
                        }
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **FunctionEventInvokeConfigs** *(list) --*

              A list of configurations.

              - *(dict) --*

                - **LastModified** *(datetime) --*

                  The date and time that the configuration was last updated.

                - **FunctionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the function.

                - **MaximumRetryAttempts** *(integer) --*

                  The maximum number of times to retry when the function returns an error.

                - **MaximumEventAgeInSeconds** *(integer) --*

                  The maximum age of a request that Lambda sends to a function for processing.

                - **DestinationConfig** *(dict) --*

                  A destination for events after they have been sent to a function for processing.

                   **Destinations**

                  * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

                  * **Queue** - The ARN of an SQS queue.

                  * **Topic** - The ARN of an SNS topic.

                  * **Event Bus** - The ARN of an Amazon EventBridge event bus.

                  - **OnSuccess** *(dict) --*

                    The destination configuration for successful invocations.

                    - **Destination** *(string) --*

                      The Amazon Resource Name (ARN) of the destination resource.

                  - **OnFailure** *(dict) --*

                    The destination configuration for failed invocations.

                    - **Destination** *(string) --*

                      The Amazon Resource Name (ARN) of the destination resource.

            - **NextMarker** *(string) --*

              The pagination token that's included if more results are available.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_functions(
        self,
        MasterRegion: str = None,
        FunctionVersion: str = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListFunctionsResponseTypeDef:
        """
        Returns a list of Lambda functions, with the version-specific configuration of each.

        Set ``FunctionVersion`` to ``ALL`` to include all published versions of each function in
        addition to the unpublished version. To get more information about a function or version,
        use  GetFunction .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListFunctions>`_

        **Request Syntax**
        ::

          response = client.list_functions(
              MasterRegion='string',
              FunctionVersion='ALL',
              Marker='string',
              MaxItems=123
          )
        :type MasterRegion: string
        :param MasterRegion:

          For Lambda@Edge functions, the AWS Region of the master function. For example,
          ``us-east-2`` or ``ALL`` . If specified, you must set ``FunctionVersion`` to ``ALL`` .

        :type FunctionVersion: string
        :param FunctionVersion:

          Set to ``ALL`` to include entries for all published versions of each function.

        :type Marker: string
        :param Marker:

          Specify the pagination token that's returned by a previous request to retrieve the next
          page of results.

        :type MaxItems: integer
        :param MaxItems:

          Specify a value between 1 and 50 to limit the number of functions in the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'Functions': [
                    {
                        'FunctionName': 'string',
                        'FunctionArn': 'string',
                        'Runtime':
                        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'
                        |'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'
                        |'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'
                        |'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'
                        |'provided',
                        'Role': 'string',
                        'Handler': 'string',
                        'CodeSize': 123,
                        'Description': 'string',
                        'Timeout': 123,
                        'MemorySize': 123,
                        'LastModified': 'string',
                        'CodeSha256': 'string',
                        'Version': 'string',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'VpcId': 'string'
                        },
                        'DeadLetterConfig': {
                            'TargetArn': 'string'
                        },
                        'Environment': {
                            'Variables': {
                                'string': 'string'
                            },
                            'Error': {
                                'ErrorCode': 'string',
                                'Message': 'string'
                            }
                        },
                        'KMSKeyArn': 'string',
                        'TracingConfig': {
                            'Mode': 'Active'|'PassThrough'
                        },
                        'MasterArn': 'string',
                        'RevisionId': 'string',
                        'Layers': [
                            {
                                'Arn': 'string',
                                'CodeSize': 123
                            },
                        ],
                        'State': 'Pending'|'Active'|'Inactive'|'Failed',
                        'StateReason': 'string',
                        'StateReasonCode':
                        'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                        |'InsufficientRolePermissions'|'InvalidConfiguration'
                        |'InternalError'|'SubnetOutOfIPAddresses',
                        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                        'LastUpdateStatusReason': 'string',
                        'LastUpdateStatusReasonCode':
                        'EniLimitExceeded'|'InsufficientRolePermissions'
                        |'InvalidConfiguration'|'InternalError'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            A list of Lambda functions.

            - **NextMarker** *(string) --*

              The pagination token that's included if more results are available.

            - **Functions** *(list) --*

              A list of Lambda functions.

              - *(dict) --*

                Details about a function's configuration.

                - **FunctionName** *(string) --*

                  The name of the function.

                - **FunctionArn** *(string) --*

                  The function's Amazon Resource Name (ARN).

                - **Runtime** *(string) --*

                  The runtime environment for the Lambda function.

                - **Role** *(string) --*

                  The function's execution role.

                - **Handler** *(string) --*

                  The function that Lambda calls to begin executing your function.

                - **CodeSize** *(integer) --*

                  The size of the function's deployment package, in bytes.

                - **Description** *(string) --*

                  The function's description.

                - **Timeout** *(integer) --*

                  The amount of time that Lambda allows a function to run before stopping it.

                - **MemorySize** *(integer) --*

                  The memory that's allocated to the function.

                - **LastModified** *(string) --*

                  The date and time that the function was last updated, in `ISO-8601 format
                  <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

                - **CodeSha256** *(string) --*

                  The SHA256 hash of the function's deployment package.

                - **Version** *(string) --*

                  The version of the Lambda function.

                - **VpcConfig** *(dict) --*

                  The function's networking configuration.

                  - **SubnetIds** *(list) --*

                    A list of VPC subnet IDs.

                    - *(string) --*

                  - **SecurityGroupIds** *(list) --*

                    A list of VPC security groups IDs.

                    - *(string) --*

                  - **VpcId** *(string) --*

                    The ID of the VPC.

                - **DeadLetterConfig** *(dict) --*

                  The function's dead letter queue.

                  - **TargetArn** *(string) --*

                    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

                - **Environment** *(dict) --*

                  The function's environment variables.

                  - **Variables** *(dict) --*

                    Environment variable key-value pairs.

                    - *(string) --*

                      - *(string) --*

                  - **Error** *(dict) --*

                    Error messages for environment variables that couldn't be applied.

                    - **ErrorCode** *(string) --*

                      The error code.

                    - **Message** *(string) --*

                      The error message.

                - **KMSKeyArn** *(string) --*

                  The KMS key that's used to encrypt the function's environment variables. This key
                  is only returned if you've configured a customer managed CMK.

                - **TracingConfig** *(dict) --*

                  The function's AWS X-Ray tracing configuration.

                  - **Mode** *(string) --*

                    The tracing mode.

                - **MasterArn** *(string) --*

                  For Lambda@Edge functions, the ARN of the master function.

                - **RevisionId** *(string) --*

                  The latest updated revision of the function or alias.

                - **Layers** *(list) --*

                  The function's `layers
                  <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                  - *(dict) --*

                    An `AWS Lambda layer
                    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                    - **Arn** *(string) --*

                      The Amazon Resource Name (ARN) of the function layer.

                    - **CodeSize** *(integer) --*

                      The size of the layer archive in bytes.

                - **State** *(string) --*

                  The current state of the function. When the state is ``Inactive`` , you can
                  reactivate the function by invoking it.

                - **StateReason** *(string) --*

                  The reason for the function's current state.

                - **StateReasonCode** *(string) --*

                  The reason code for the function's current state. When the code is ``Creating`` ,
                  you can't invoke or modify the function.

                - **LastUpdateStatus** *(string) --*

                  The status of the last update that was performed on the function.

                - **LastUpdateStatusReason** *(string) --*

                  The reason for the last update that was performed on the function.

                - **LastUpdateStatusReasonCode** *(string) --*

                  The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_layer_versions(
        self,
        LayerName: str,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListLayerVersionsResponseTypeDef:
        """
        Lists the versions of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ . Versions that
        have been deleted aren't listed. Specify a `runtime identifier
        <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>`__ to list only versions
        that indicate that they're compatible with that runtime.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListLayerVersions>`_

        **Request Syntax**
        ::

          response = client.list_layer_versions(
              CompatibleRuntime=
                  'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                  |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                  |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              LayerName='string',
              Marker='string',
              MaxItems=123
          )
        :type CompatibleRuntime: string
        :param CompatibleRuntime:

          A runtime identifier. For example, ``go1.x`` .

        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type Marker: string
        :param Marker:

          A pagination token returned by a previous call.

        :type MaxItems: integer
        :param MaxItems:

          The maximum number of versions to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'LayerVersions': [
                    {
                        'LayerVersionArn': 'string',
                        'Version': 123,
                        'Description': 'string',
                        'CreatedDate': 'string',
                        'CompatibleRuntimes': [
                            'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                            |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                            |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'
                            |'go1.x'|'ruby2.5'|'provided',
                        ],
                        'LicenseInfo': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextMarker** *(string) --*

              A pagination token returned when the response doesn't contain all versions.

            - **LayerVersions** *(list) --*

              A list of versions.

              - *(dict) --*

                Details about a version of an `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **LayerVersionArn** *(string) --*

                  The ARN of the layer version.

                - **Version** *(integer) --*

                  The version number.

                - **Description** *(string) --*

                  The description of the version.

                - **CreatedDate** *(string) --*

                  The date that the version was created, in ISO 8601 format. For example,
                  ``2018-11-27T15:10:45.123+0000`` .

                - **CompatibleRuntimes** *(list) --*

                  The layer's compatible runtimes.

                  - *(string) --*

                - **LicenseInfo** *(string) --*

                  The layer's open-source license.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_layers(
        self,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> ClientListLayersResponseTypeDef:
        """
        Lists `AWS Lambda layers
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ and shows
        information about the latest version of each. Specify a `runtime identifier
        <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>`__ to list only layers
        that indicate that they're compatible with that runtime.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListLayers>`_

        **Request Syntax**
        ::

          response = client.list_layers(
              CompatibleRuntime=
                  'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                  |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                  |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              Marker='string',
              MaxItems=123
          )
        :type CompatibleRuntime: string
        :param CompatibleRuntime:

          A runtime identifier. For example, ``go1.x`` .

        :type Marker: string
        :param Marker:

          A pagination token returned by a previous call.

        :type MaxItems: integer
        :param MaxItems:

          The maximum number of layers to return.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'Layers': [
                    {
                        'LayerName': 'string',
                        'LayerArn': 'string',
                        'LatestMatchingVersion': {
                            'LayerVersionArn': 'string',
                            'Version': 123,
                            'Description': 'string',
                            'CreatedDate': 'string',
                            'CompatibleRuntimes': [
                                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'
                                |'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'
                                |'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'
                                |'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                            ],
                            'LicenseInfo': 'string'
                        }
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextMarker** *(string) --*

              A pagination token returned when the response doesn't contain all layers.

            - **Layers** *(list) --*

              A list of function layers.

              - *(dict) --*

                Details about an `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **LayerName** *(string) --*

                  The name of the layer.

                - **LayerArn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **LatestMatchingVersion** *(dict) --*

                  The newest version of the layer.

                  - **LayerVersionArn** *(string) --*

                    The ARN of the layer version.

                  - **Version** *(integer) --*

                    The version number.

                  - **Description** *(string) --*

                    The description of the version.

                  - **CreatedDate** *(string) --*

                    The date that the version was created, in ISO 8601 format. For example,
                    ``2018-11-27T15:10:45.123+0000`` .

                  - **CompatibleRuntimes** *(list) --*

                    The layer's compatible runtimes.

                    - *(string) --*

                  - **LicenseInfo** *(string) --*

                    The layer's open-source license.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_provisioned_concurrency_configs(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListProvisionedConcurrencyConfigsResponseTypeDef:
        """
        Retrieves a list of provisioned concurrency configurations for a function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListProvisionedConcurrencyConfigs>`_

        **Request Syntax**
        ::

          response = client.list_provisioned_concurrency_configs(
              FunctionName='string',
              Marker='string',
              MaxItems=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Marker: string
        :param Marker:

          Specify the pagination token that's returned by a previous request to retrieve the next
          page of results.

        :type MaxItems: integer
        :param MaxItems:

          Specify a number to limit the number of configurations returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ProvisionedConcurrencyConfigs': [
                    {
                        'FunctionArn': 'string',
                        'RequestedProvisionedConcurrentExecutions': 123,
                        'AvailableProvisionedConcurrentExecutions': 123,
                        'AllocatedProvisionedConcurrentExecutions': 123,
                        'Status': 'IN_PROGRESS'|'READY'|'FAILED',
                        'StatusReason': 'string',
                        'LastModified': 'string'
                    },
                ],
                'NextMarker': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ProvisionedConcurrencyConfigs** *(list) --*

              A list of provisioned concurrency configurations.

              - *(dict) --*

                Details about the provisioned concurrency configuration for a function alias or
                version.

                - **FunctionArn** *(string) --*

                  The Amazon Resource Name (ARN) of the alias or version.

                - **RequestedProvisionedConcurrentExecutions** *(integer) --*

                  The amount of provisioned concurrency requested.

                - **AvailableProvisionedConcurrentExecutions** *(integer) --*

                  The amount of provisioned concurrency available.

                - **AllocatedProvisionedConcurrentExecutions** *(integer) --*

                  The amount of provisioned concurrency allocated.

                - **Status** *(string) --*

                  The status of the allocation process.

                - **StatusReason** *(string) --*

                  For failed allocations, the reason that provisioned concurrency could not be
                  allocated.

                - **LastModified** *(string) --*

                  The date and time that a user last updated the configuration, in `ISO 8601 format
                  <https://www.iso.org/iso-8601-date-and-time-format.html>`__ .

            - **NextMarker** *(string) --*

              The pagination token that's included if more results are available.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags(self, Resource: str) -> ClientListTagsResponseTypeDef:
        """
        Returns a function's `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ .
        You can also view tags with  GetFunction .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListTags>`_

        **Request Syntax**
        ::

          response = client.list_tags(
              Resource='string'
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The function's Amazon Resource Name (ARN).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': {
                    'string': 'string'
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(dict) --*

              The function's tags.

              - *(string) --*

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_versions_by_function(
        self, FunctionName: str, Marker: str = None, MaxItems: int = None
    ) -> ClientListVersionsByFunctionResponseTypeDef:
        """
        Returns a list of `versions
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ , with the
        version-specific configuration of each.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/ListVersionsByFunction>`_

        **Request Syntax**
        ::

          response = client.list_versions_by_function(
              FunctionName='string',
              Marker='string',
              MaxItems=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Marker: string
        :param Marker:

          Specify the pagination token that's returned by a previous request to retrieve the next
          page of results.

        :type MaxItems: integer
        :param MaxItems:

          Limit the number of versions that are returned.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextMarker': 'string',
                'Versions': [
                    {
                        'FunctionName': 'string',
                        'FunctionArn': 'string',
                        'Runtime':
                        'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'
                        |'nodejs12.x'|'java8'|'java11'|'python2.7'|'python3.6'
                        |'python3.7'|'python3.8'|'dotnetcore1.0'|'dotnetcore2.0'
                        |'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'
                        |'provided',
                        'Role': 'string',
                        'Handler': 'string',
                        'CodeSize': 123,
                        'Description': 'string',
                        'Timeout': 123,
                        'MemorySize': 123,
                        'LastModified': 'string',
                        'CodeSha256': 'string',
                        'Version': 'string',
                        'VpcConfig': {
                            'SubnetIds': [
                                'string',
                            ],
                            'SecurityGroupIds': [
                                'string',
                            ],
                            'VpcId': 'string'
                        },
                        'DeadLetterConfig': {
                            'TargetArn': 'string'
                        },
                        'Environment': {
                            'Variables': {
                                'string': 'string'
                            },
                            'Error': {
                                'ErrorCode': 'string',
                                'Message': 'string'
                            }
                        },
                        'KMSKeyArn': 'string',
                        'TracingConfig': {
                            'Mode': 'Active'|'PassThrough'
                        },
                        'MasterArn': 'string',
                        'RevisionId': 'string',
                        'Layers': [
                            {
                                'Arn': 'string',
                                'CodeSize': 123
                            },
                        ],
                        'State': 'Pending'|'Active'|'Inactive'|'Failed',
                        'StateReason': 'string',
                        'StateReasonCode':
                        'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                        |'InsufficientRolePermissions'|'InvalidConfiguration'
                        |'InternalError'|'SubnetOutOfIPAddresses',
                        'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                        'LastUpdateStatusReason': 'string',
                        'LastUpdateStatusReasonCode':
                        'EniLimitExceeded'|'InsufficientRolePermissions'
                        |'InvalidConfiguration'|'InternalError'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextMarker** *(string) --*

              The pagination token that's included if more results are available.

            - **Versions** *(list) --*

              A list of Lambda function versions.

              - *(dict) --*

                Details about a function's configuration.

                - **FunctionName** *(string) --*

                  The name of the function.

                - **FunctionArn** *(string) --*

                  The function's Amazon Resource Name (ARN).

                - **Runtime** *(string) --*

                  The runtime environment for the Lambda function.

                - **Role** *(string) --*

                  The function's execution role.

                - **Handler** *(string) --*

                  The function that Lambda calls to begin executing your function.

                - **CodeSize** *(integer) --*

                  The size of the function's deployment package, in bytes.

                - **Description** *(string) --*

                  The function's description.

                - **Timeout** *(integer) --*

                  The amount of time that Lambda allows a function to run before stopping it.

                - **MemorySize** *(integer) --*

                  The memory that's allocated to the function.

                - **LastModified** *(string) --*

                  The date and time that the function was last updated, in `ISO-8601 format
                  <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

                - **CodeSha256** *(string) --*

                  The SHA256 hash of the function's deployment package.

                - **Version** *(string) --*

                  The version of the Lambda function.

                - **VpcConfig** *(dict) --*

                  The function's networking configuration.

                  - **SubnetIds** *(list) --*

                    A list of VPC subnet IDs.

                    - *(string) --*

                  - **SecurityGroupIds** *(list) --*

                    A list of VPC security groups IDs.

                    - *(string) --*

                  - **VpcId** *(string) --*

                    The ID of the VPC.

                - **DeadLetterConfig** *(dict) --*

                  The function's dead letter queue.

                  - **TargetArn** *(string) --*

                    The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

                - **Environment** *(dict) --*

                  The function's environment variables.

                  - **Variables** *(dict) --*

                    Environment variable key-value pairs.

                    - *(string) --*

                      - *(string) --*

                  - **Error** *(dict) --*

                    Error messages for environment variables that couldn't be applied.

                    - **ErrorCode** *(string) --*

                      The error code.

                    - **Message** *(string) --*

                      The error message.

                - **KMSKeyArn** *(string) --*

                  The KMS key that's used to encrypt the function's environment variables. This key
                  is only returned if you've configured a customer managed CMK.

                - **TracingConfig** *(dict) --*

                  The function's AWS X-Ray tracing configuration.

                  - **Mode** *(string) --*

                    The tracing mode.

                - **MasterArn** *(string) --*

                  For Lambda@Edge functions, the ARN of the master function.

                - **RevisionId** *(string) --*

                  The latest updated revision of the function or alias.

                - **Layers** *(list) --*

                  The function's `layers
                  <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                  - *(dict) --*

                    An `AWS Lambda layer
                    <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                    - **Arn** *(string) --*

                      The Amazon Resource Name (ARN) of the function layer.

                    - **CodeSize** *(integer) --*

                      The size of the layer archive in bytes.

                - **State** *(string) --*

                  The current state of the function. When the state is ``Inactive`` , you can
                  reactivate the function by invoking it.

                - **StateReason** *(string) --*

                  The reason for the function's current state.

                - **StateReasonCode** *(string) --*

                  The reason code for the function's current state. When the code is ``Creating`` ,
                  you can't invoke or modify the function.

                - **LastUpdateStatus** *(string) --*

                  The status of the last update that was performed on the function.

                - **LastUpdateStatusReason** *(string) --*

                  The reason for the last update that was performed on the function.

                - **LastUpdateStatusReasonCode** *(string) --*

                  The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish_layer_version(
        self,
        LayerName: str,
        Content: ClientPublishLayerVersionContentTypeDef,
        Description: str = None,
        CompatibleRuntimes: List[
            Literal[
                "nodejs",
                "nodejs4.3",
                "nodejs6.10",
                "nodejs8.10",
                "nodejs10.x",
                "nodejs12.x",
                "java8",
                "java11",
                "python2.7",
                "python3.6",
                "python3.7",
                "python3.8",
                "dotnetcore1.0",
                "dotnetcore2.0",
                "dotnetcore2.1",
                "nodejs4.3-edge",
                "go1.x",
                "ruby2.5",
                "provided",
            ]
        ] = None,
        LicenseInfo: str = None,
    ) -> ClientPublishLayerVersionResponseTypeDef:
        """
        Creates an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ from a ZIP
        archive. Each time you call ``PublishLayerVersion`` with the same layer name, a new version
        is created.

        Add layers to your function with  CreateFunction or  UpdateFunctionConfiguration .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PublishLayerVersion>`_

        **Request Syntax**
        ::

          response = client.publish_layer_version(
              LayerName='string',
              Description='string',
              Content={
                  'S3Bucket': 'string',
                  'S3Key': 'string',
                  'S3ObjectVersion': 'string',
                  'ZipFile': b'bytes'
              },
              CompatibleRuntimes=[
                  'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                  |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                  |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              ],
              LicenseInfo='string'
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type Description: string
        :param Description:

          The description of the version.

        :type Content: dict
        :param Content: **[REQUIRED]**

          The function layer archive.

          - **S3Bucket** *(string) --*

            The Amazon S3 bucket of the layer archive.

          - **S3Key** *(string) --*

            The Amazon S3 key of the layer archive.

          - **S3ObjectVersion** *(string) --*

            For versioned objects, the version of the layer archive object to use.

          - **ZipFile** *(bytes) --*

            The base64-encoded contents of the layer archive. AWS SDK and AWS CLI clients handle the
            encoding for you.

        :type CompatibleRuntimes: list
        :param CompatibleRuntimes:

          A list of compatible `function runtimes
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>`__ . Used for
          filtering with  ListLayers and  ListLayerVersions .

          - *(string) --*

        :type LicenseInfo: string
        :param LicenseInfo:

          The layer's software license. It can be any of the following:

          * An `SPDX license identifier <https://spdx.org/licenses/>`__ . For example, ``MIT`` .

          * The URL of a license hosted on the internet. For example,
          ``https://opensource.org/licenses/MIT`` .

          * The full text of the license.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Content': {
                    'Location': 'string',
                    'CodeSha256': 'string',
                    'CodeSize': 123
                },
                'LayerArn': 'string',
                'LayerVersionArn': 'string',
                'Description': 'string',
                'CreatedDate': 'string',
                'Version': 123,
                'CompatibleRuntimes': [
                    'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                    |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                    |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
                ],
                'LicenseInfo': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Content** *(dict) --*

              Details about the layer version.

              - **Location** *(string) --*

                A link to the layer archive in Amazon S3 that is valid for 10 minutes.

              - **CodeSha256** *(string) --*

                The SHA-256 hash of the layer archive.

              - **CodeSize** *(integer) --*

                The size of the layer archive in bytes.

            - **LayerArn** *(string) --*

              The ARN of the layer.

            - **LayerVersionArn** *(string) --*

              The ARN of the layer version.

            - **Description** *(string) --*

              The description of the version.

            - **CreatedDate** *(string) --*

              The date that the layer version was created, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **Version** *(integer) --*

              The version number.

            - **CompatibleRuntimes** *(list) --*

              The layer's compatible runtimes.

              - *(string) --*

            - **LicenseInfo** *(string) --*

              The layer's software license.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def publish_version(
        self,
        FunctionName: str,
        CodeSha256: str = None,
        Description: str = None,
        RevisionId: str = None,
    ) -> ClientPublishVersionResponseTypeDef:
        """
        Creates a `version <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__
        from the current code and configuration of a function. Use versions to create a snapshot of
        your function code and configuration that doesn't change.

        AWS Lambda doesn't publish a version if the function's configuration and code haven't
        changed since the last version. Use  UpdateFunctionCode or  UpdateFunctionConfiguration to
        update the function before publishing a version.

        Clients can invoke versions directly or with an alias. To create an alias, use  CreateAlias
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PublishVersion>`_

        **Request Syntax**
        ::

          response = client.publish_version(
              FunctionName='string',
              CodeSha256='string',
              Description='string',
              RevisionId='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type CodeSha256: string
        :param CodeSha256:

          Only publish a version if the hash value matches the value that's specified. Use this
          option to avoid publishing a version if the function code has changed since you last
          updated it. You can get the hash for the version that you uploaded from the output of
          UpdateFunctionCode .

        :type Description: string
        :param Description:

          A description for the version to override the description in the function configuration.

        :type RevisionId: string
        :param RevisionId:

          Only update the function if the revision ID matches the ID that's specified. Use this
          option to avoid publishing a version if the function configuration has changed since you
          last updated it.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime':
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'
                |'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode':
                'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                |'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'
                |'SubnetOutOfIPAddresses',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode':
                'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'
                |'InternalError'
            }
          **Response Structure**

          - *(dict) --*

            Details about a function's configuration.

            - **FunctionName** *(string) --*

              The name of the function.

            - **FunctionArn** *(string) --*

              The function's Amazon Resource Name (ARN).

            - **Runtime** *(string) --*

              The runtime environment for the Lambda function.

            - **Role** *(string) --*

              The function's execution role.

            - **Handler** *(string) --*

              The function that Lambda calls to begin executing your function.

            - **CodeSize** *(integer) --*

              The size of the function's deployment package, in bytes.

            - **Description** *(string) --*

              The function's description.

            - **Timeout** *(integer) --*

              The amount of time that Lambda allows a function to run before stopping it.

            - **MemorySize** *(integer) --*

              The memory that's allocated to the function.

            - **LastModified** *(string) --*

              The date and time that the function was last updated, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **CodeSha256** *(string) --*

              The SHA256 hash of the function's deployment package.

            - **Version** *(string) --*

              The version of the Lambda function.

            - **VpcConfig** *(dict) --*

              The function's networking configuration.

              - **SubnetIds** *(list) --*

                A list of VPC subnet IDs.

                - *(string) --*

              - **SecurityGroupIds** *(list) --*

                A list of VPC security groups IDs.

                - *(string) --*

              - **VpcId** *(string) --*

                The ID of the VPC.

            - **DeadLetterConfig** *(dict) --*

              The function's dead letter queue.

              - **TargetArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

            - **Environment** *(dict) --*

              The function's environment variables.

              - **Variables** *(dict) --*

                Environment variable key-value pairs.

                - *(string) --*

                  - *(string) --*

              - **Error** *(dict) --*

                Error messages for environment variables that couldn't be applied.

                - **ErrorCode** *(string) --*

                  The error code.

                - **Message** *(string) --*

                  The error message.

            - **KMSKeyArn** *(string) --*

              The KMS key that's used to encrypt the function's environment variables. This key is
              only returned if you've configured a customer managed CMK.

            - **TracingConfig** *(dict) --*

              The function's AWS X-Ray tracing configuration.

              - **Mode** *(string) --*

                The tracing mode.

            - **MasterArn** *(string) --*

              For Lambda@Edge functions, the ARN of the master function.

            - **RevisionId** *(string) --*

              The latest updated revision of the function or alias.

            - **Layers** *(list) --*

              The function's `layers
              <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

              - *(dict) --*

                An `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **CodeSize** *(integer) --*

                  The size of the layer archive in bytes.

            - **State** *(string) --*

              The current state of the function. When the state is ``Inactive`` , you can reactivate
              the function by invoking it.

            - **StateReason** *(string) --*

              The reason for the function's current state.

            - **StateReasonCode** *(string) --*

              The reason code for the function's current state. When the code is ``Creating`` , you
              can't invoke or modify the function.

            - **LastUpdateStatus** *(string) --*

              The status of the last update that was performed on the function.

            - **LastUpdateStatusReason** *(string) --*

              The reason for the last update that was performed on the function.

            - **LastUpdateStatusReasonCode** *(string) --*

              The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_function_concurrency(
        self, FunctionName: str, ReservedConcurrentExecutions: int
    ) -> ClientPutFunctionConcurrencyResponseTypeDef:
        """
        Sets the maximum number of simultaneous executions for a function, and reserves capacity for
        that concurrency level.

        Concurrency settings apply to the function as a whole, including all published versions and
        the unpublished version. Reserving concurrency both ensures that your function has capacity
        to process the specified number of events simultaneously, and prevents it from scaling
        beyond that level. Use  GetFunction to see the current setting for a function.

        Use  GetAccountSettings to see your Regional concurrency limit. You can reserve concurrency
        for as many functions as you like, as long as you leave at least 100 simultaneous executions
        unreserved for functions that aren't configured with a per-function limit. For more
        information, see `Managing Concurrency
        <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PutFunctionConcurrency>`_

        **Request Syntax**
        ::

          response = client.put_function_concurrency(
              FunctionName='string',
              ReservedConcurrentExecutions=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type ReservedConcurrentExecutions: integer
        :param ReservedConcurrentExecutions: **[REQUIRED]**

          The number of simultaneous executions to reserve for the function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ReservedConcurrentExecutions': 123
            }
          **Response Structure**

          - *(dict) --*

            - **ReservedConcurrentExecutions** *(integer) --*

              The number of concurrent executions that are reserved for this function. For more
              information, see `Managing Concurrency
              <https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html>`__ .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: ClientPutFunctionEventInvokeConfigDestinationConfigTypeDef = None,
    ) -> ClientPutFunctionEventInvokeConfigResponseTypeDef:
        """
        Configures options for `asynchronous invocation
        <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html>`__ on a function,
        version, or alias.

        By default, Lambda retries an asynchronous invocation twice if the function returns an
        error. It retains events in a queue for up to six hours. When an event fails all processing
        attempts or stays in the asynchronous invocation queue for too long, Lambda discards it. To
        retain discarded events, configure a dead-letter queue with  UpdateFunctionConfiguration .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PutFunctionEventInvokeConfig>`_

        **Request Syntax**
        ::

          response = client.put_function_event_invoke_config(
              FunctionName='string',
              Qualifier='string',
              MaximumRetryAttempts=123,
              MaximumEventAgeInSeconds=123,
              DestinationConfig={
                  'OnSuccess': {
                      'Destination': 'string'
                  },
                  'OnFailure': {
                      'Destination': 'string'
                  }
              }
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          A version number or alias name.

        :type MaximumRetryAttempts: integer
        :param MaximumRetryAttempts:

          The maximum number of times to retry when the function returns an error.

        :type MaximumEventAgeInSeconds: integer
        :param MaximumEventAgeInSeconds:

          The maximum age of a request that Lambda sends to a function for processing.

        :type DestinationConfig: dict
        :param DestinationConfig:

          A destination for events after they have been sent to a function for processing.

           **Destinations**

          * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

          * **Queue** - The ARN of an SQS queue.

          * **Topic** - The ARN of an SNS topic.

          * **Event Bus** - The ARN of an Amazon EventBridge event bus.

          - **OnSuccess** *(dict) --*

            The destination configuration for successful invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

          - **OnFailure** *(dict) --*

            The destination configuration for failed invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LastModified': datetime(2015, 1, 1),
                'FunctionArn': 'string',
                'MaximumRetryAttempts': 123,
                'MaximumEventAgeInSeconds': 123,
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LastModified** *(datetime) --*

              The date and time that the configuration was last updated.

            - **FunctionArn** *(string) --*

              The Amazon Resource Name (ARN) of the function.

            - **MaximumRetryAttempts** *(integer) --*

              The maximum number of times to retry when the function returns an error.

            - **MaximumEventAgeInSeconds** *(integer) --*

              The maximum age of a request that Lambda sends to a function for processing.

            - **DestinationConfig** *(dict) --*

              A destination for events after they have been sent to a function for processing.

               **Destinations**

              * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

              * **Queue** - The ARN of an SQS queue.

              * **Topic** - The ARN of an SNS topic.

              * **Event Bus** - The ARN of an Amazon EventBridge event bus.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_provisioned_concurrency_config(
        self, FunctionName: str, Qualifier: str, ProvisionedConcurrentExecutions: int
    ) -> ClientPutProvisionedConcurrencyConfigResponseTypeDef:
        """
        Adds a provisioned concurrency configuration to a function's alias or version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/PutProvisionedConcurrencyConfig>`_

        **Request Syntax**
        ::

          response = client.put_provisioned_concurrency_config(
              FunctionName='string',
              Qualifier='string',
              ProvisionedConcurrentExecutions=123
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Qualifier: string
        :param Qualifier: **[REQUIRED]**

          The version number or alias name.

        :type ProvisionedConcurrentExecutions: integer
        :param ProvisionedConcurrentExecutions: **[REQUIRED]**

          The amount of provisioned concurrency to allocate for the version or alias.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'RequestedProvisionedConcurrentExecutions': 123,
                'AvailableProvisionedConcurrentExecutions': 123,
                'AllocatedProvisionedConcurrentExecutions': 123,
                'Status': 'IN_PROGRESS'|'READY'|'FAILED',
                'StatusReason': 'string',
                'LastModified': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **RequestedProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency requested.

            - **AvailableProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency available.

            - **AllocatedProvisionedConcurrentExecutions** *(integer) --*

              The amount of provisioned concurrency allocated.

            - **Status** *(string) --*

              The status of the allocation process.

            - **StatusReason** *(string) --*

              For failed allocations, the reason that provisioned concurrency could not be
              allocated.

            - **LastModified** *(string) --*

              The date and time that a user last updated the configuration, in `ISO 8601 format
              <https://www.iso.org/iso-8601-date-and-time-format.html>`__ .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_layer_version_permission(
        self, LayerName: str, VersionNumber: int, StatementId: str, RevisionId: str = None
    ) -> None:
        """
        Removes a statement from the permissions policy for a version of an `AWS Lambda layer
        <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ . For more
        information, see  AddLayerVersionPermission .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/RemoveLayerVersionPermission>`_

        **Request Syntax**
        ::

          response = client.remove_layer_version_permission(
              LayerName='string',
              VersionNumber=123,
              StatementId='string',
              RevisionId='string'
          )
        :type LayerName: string
        :param LayerName: **[REQUIRED]**

          The name or Amazon Resource Name (ARN) of the layer.

        :type VersionNumber: integer
        :param VersionNumber: **[REQUIRED]**

          The version number.

        :type StatementId: string
        :param StatementId: **[REQUIRED]**

          The identifier that was specified when the statement was added.

        :type RevisionId: string
        :param RevisionId:

          Only update the policy if the revision ID matches the ID specified. Use this option to
          avoid modifying a policy that has changed since you last read it.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_permission(
        self, FunctionName: str, StatementId: str, Qualifier: str = None, RevisionId: str = None
    ) -> None:
        """
        Revokes function-use permission from an AWS service or another account. You can get the ID
        of the statement from the output of  GetPolicy .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/RemovePermission>`_

        **Request Syntax**
        ::

          response = client.remove_permission(
              FunctionName='string',
              StatementId='string',
              Qualifier='string',
              RevisionId='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type StatementId: string
        :param StatementId: **[REQUIRED]**

          Statement ID of the permission to remove.

        :type Qualifier: string
        :param Qualifier:

          Specify a version or alias to remove permissions from a published version of the function.

        :type RevisionId: string
        :param RevisionId:

          Only update the policy if the revision ID matches the ID that's specified. Use this option
          to avoid modifying a policy that has changed since you last read it.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, Resource: str, Tags: Dict[str, str]) -> None:
        """
        Adds `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ to a function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              Resource='string',
              Tags={
                  'string': 'string'
              }
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The function's Amazon Resource Name (ARN).

        :type Tags: dict
        :param Tags: **[REQUIRED]**

          A list of tags to apply to the function.

          - *(string) --*

            - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, Resource: str, TagKeys: List[str]) -> None:
        """
        Removes `tags <https://docs.aws.amazon.com/lambda/latest/dg/tagging.html>`__ from a
        function.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              Resource='string',
              TagKeys=[
                  'string',
              ]
          )
        :type Resource: string
        :param Resource: **[REQUIRED]**

          The function's Amazon Resource Name (ARN).

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          A list of tag keys to remove from the function.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_alias(
        self,
        FunctionName: str,
        Name: str,
        FunctionVersion: str = None,
        Description: str = None,
        RoutingConfig: ClientUpdateAliasRoutingConfigTypeDef = None,
        RevisionId: str = None,
    ) -> ClientUpdateAliasResponseTypeDef:
        """
        Updates the configuration of a Lambda function `alias
        <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateAlias>`_

        **Request Syntax**
        ::

          response = client.update_alias(
              FunctionName='string',
              Name='string',
              FunctionVersion='string',
              Description='string',
              RoutingConfig={
                  'AdditionalVersionWeights': {
                      'string': 123.0
                  }
              },
              RevisionId='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the alias.

        :type FunctionVersion: string
        :param FunctionVersion:

          The function version that the alias invokes.

        :type Description: string
        :param Description:

          A description of the alias.

        :type RoutingConfig: dict
        :param RoutingConfig:

          The `routing configuration
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
          of the alias.

          - **AdditionalVersionWeights** *(dict) --*

            The name of the second alias, and the percentage of traffic that's routed to it.

            - *(string) --*

              - *(float) --*

        :type RevisionId: string
        :param RevisionId:

          Only update the alias if the revision ID matches the ID that's specified. Use this option
          to avoid modifying an alias that has changed since you last read it.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AliasArn': 'string',
                'Name': 'string',
                'FunctionVersion': 'string',
                'Description': 'string',
                'RoutingConfig': {
                    'AdditionalVersionWeights': {
                        'string': 123.0
                    }
                },
                'RevisionId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Provides configuration information about a Lambda function `alias
            <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>`__ .

            - **AliasArn** *(string) --*

              The Amazon Resource Name (ARN) of the alias.

            - **Name** *(string) --*

              The name of the alias.

            - **FunctionVersion** *(string) --*

              The function version that the alias invokes.

            - **Description** *(string) --*

              A description of the alias.

            - **RoutingConfig** *(dict) --*

              The `routing configuration
              <https://docs.aws.amazon.com/lambda/latest/dg/lambda-traffic-shifting-using-aliases.html>`__
              of the alias.

              - **AdditionalVersionWeights** *(dict) --*

                The name of the second alias, and the percentage of traffic that's routed to it.

                - *(string) --*

                  - *(float) --*

            - **RevisionId** *(string) --*

              A unique identifier that changes when you update the alias.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_event_source_mapping(
        self,
        UUID: str,
        FunctionName: str = None,
        Enabled: bool = None,
        BatchSize: int = None,
        MaximumBatchingWindowInSeconds: int = None,
        DestinationConfig: ClientUpdateEventSourceMappingDestinationConfigTypeDef = None,
        MaximumRecordAgeInSeconds: int = None,
        BisectBatchOnFunctionError: bool = None,
        MaximumRetryAttempts: int = None,
        ParallelizationFactor: int = None,
    ) -> ClientUpdateEventSourceMappingResponseTypeDef:
        """
        Updates an event source mapping. You can change the function that AWS Lambda invokes, or
        pause invocation and resume later from the same location.

        The following error handling options are only available for stream sources (DynamoDB and
        Kinesis):

        * ``BisectBatchOnFunctionError`` - If the function returns an error, split the batch in two
        and retry.

        * ``DestinationConfig`` - Send discarded records to an Amazon SQS queue or Amazon SNS topic.

        * ``MaximumRecordAgeInSeconds`` - Discard records older than the specified age.

        * ``MaximumRetryAttempts`` - Discard records after the specified number of retries.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateEventSourceMapping>`_

        **Request Syntax**
        ::

          response = client.update_event_source_mapping(
              UUID='string',
              FunctionName='string',
              Enabled=True|False,
              BatchSize=123,
              MaximumBatchingWindowInSeconds=123,
              DestinationConfig={
                  'OnSuccess': {
                      'Destination': 'string'
                  },
                  'OnFailure': {
                      'Destination': 'string'
                  }
              },
              MaximumRecordAgeInSeconds=123,
              BisectBatchOnFunctionError=True|False,
              MaximumRetryAttempts=123,
              ParallelizationFactor=123
          )
        :type UUID: string
        :param UUID: **[REQUIRED]**

          The identifier of the event source mapping.

        :type FunctionName: string
        :param FunctionName:

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``MyFunction`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction`` .

          * **Version or Alias ARN** -
          ``arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD`` .

          * **Partial ARN** - ``123456789012:function:MyFunction`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it's limited to 64 characters in length.

        :type Enabled: boolean
        :param Enabled:

          Disables the event source mapping to pause polling and invocation.

        :type BatchSize: integer
        :param BatchSize:

          The maximum number of items to retrieve in a single batch.

          * **Amazon Kinesis** - Default 100. Max 10,000.

          * **Amazon DynamoDB Streams** - Default 100. Max 1,000.

          * **Amazon Simple Queue Service** - Default 10. Max 10.

        :type MaximumBatchingWindowInSeconds: integer
        :param MaximumBatchingWindowInSeconds:

          The maximum amount of time to gather records before invoking the function, in seconds.

        :type DestinationConfig: dict
        :param DestinationConfig:

          (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

          - **OnSuccess** *(dict) --*

            The destination configuration for successful invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

          - **OnFailure** *(dict) --*

            The destination configuration for failed invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

        :type MaximumRecordAgeInSeconds: integer
        :param MaximumRecordAgeInSeconds:

          (Streams) The maximum age of a record that Lambda sends to a function for processing.

        :type BisectBatchOnFunctionError: boolean
        :param BisectBatchOnFunctionError:

          (Streams) If the function returns an error, split the batch in two and retry.

        :type MaximumRetryAttempts: integer
        :param MaximumRetryAttempts:

          (Streams) The maximum number of times to retry when the function returns an error.

        :type ParallelizationFactor: integer
        :param ParallelizationFactor:

          (Streams) The number of batches to process from each shard concurrently.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UUID': 'string',
                'BatchSize': 123,
                'MaximumBatchingWindowInSeconds': 123,
                'ParallelizationFactor': 123,
                'EventSourceArn': 'string',
                'FunctionArn': 'string',
                'LastModified': datetime(2015, 1, 1),
                'LastProcessingResult': 'string',
                'State': 'string',
                'StateTransitionReason': 'string',
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                },
                'MaximumRecordAgeInSeconds': 123,
                'BisectBatchOnFunctionError': True|False,
                'MaximumRetryAttempts': 123
            }
          **Response Structure**

          - *(dict) --*

            A mapping between an AWS resource and an AWS Lambda function. See
            CreateEventSourceMapping for details.

            - **UUID** *(string) --*

              The identifier of the event source mapping.

            - **BatchSize** *(integer) --*

              The maximum number of items to retrieve in a single batch.

            - **MaximumBatchingWindowInSeconds** *(integer) --*

              The maximum amount of time to gather records before invoking the function, in seconds.

            - **ParallelizationFactor** *(integer) --*

              (Streams) The number of batches to process from each shard concurrently.

            - **EventSourceArn** *(string) --*

              The Amazon Resource Name (ARN) of the event source.

            - **FunctionArn** *(string) --*

              The ARN of the Lambda function.

            - **LastModified** *(datetime) --*

              The date that the event source mapping was last updated, or its state changed.

            - **LastProcessingResult** *(string) --*

              The result of the last AWS Lambda invocation of your Lambda function.

            - **State** *(string) --*

              The state of the event source mapping. It can be one of the following: ``Creating`` ,
              ``Enabling`` , ``Enabled`` , ``Disabling`` , ``Disabled`` , ``Updating`` , or
              ``Deleting`` .

            - **StateTransitionReason** *(string) --*

              Indicates whether the last change to the event source mapping was made by a user, or
              by the Lambda service.

            - **DestinationConfig** *(dict) --*

              (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

            - **MaximumRecordAgeInSeconds** *(integer) --*

              (Streams) The maximum age of a record that Lambda sends to a function for processing.

            - **BisectBatchOnFunctionError** *(boolean) --*

              (Streams) If the function returns an error, split the batch in two and retry.

            - **MaximumRetryAttempts** *(integer) --*

              (Streams) The maximum number of times to retry when the function returns an error.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_code(
        self,
        FunctionName: str,
        ZipFile: bytes = None,
        S3Bucket: str = None,
        S3Key: str = None,
        S3ObjectVersion: str = None,
        Publish: bool = None,
        DryRun: bool = None,
        RevisionId: str = None,
    ) -> ClientUpdateFunctionCodeResponseTypeDef:
        """
        Updates a Lambda function's code.

        The function's code is locked when you publish a version. You can't modify the code of a
        published version, only the unpublished version.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionCode>`_

        **Request Syntax**
        ::

          response = client.update_function_code(
              FunctionName='string',
              ZipFile=b'bytes',
              S3Bucket='string',
              S3Key='string',
              S3ObjectVersion='string',
              Publish=True|False,
              DryRun=True|False,
              RevisionId='string'
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type ZipFile: bytes
        :param ZipFile:

          The base64-encoded contents of the deployment package. AWS SDK and AWS CLI clients handle
          the encoding for you.

            **This value will be base64 encoded automatically. Do not base64 encode this value prior
            to performing the operation.**

        :type S3Bucket: string
        :param S3Bucket:

          An Amazon S3 bucket in the same AWS Region as your function. The bucket can be in a
          different AWS account.

        :type S3Key: string
        :param S3Key:

          The Amazon S3 key of the deployment package.

        :type S3ObjectVersion: string
        :param S3ObjectVersion:

          For versioned objects, the version of the deployment package object to use.

        :type Publish: boolean
        :param Publish:

          Set to true to publish a new version of the function after updating the code. This has the
          same effect as calling  PublishVersion separately.

        :type DryRun: boolean
        :param DryRun:

          Set to true to validate the request parameters and access permissions without modifying
          the function code.

        :type RevisionId: string
        :param RevisionId:

          Only update the function if the revision ID matches the ID that's specified. Use this
          option to avoid modifying a function that has changed since you last read it.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime':
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'
                |'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode':
                'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                |'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'
                |'SubnetOutOfIPAddresses',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode':
                'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'
                |'InternalError'
            }
          **Response Structure**

          - *(dict) --*

            Details about a function's configuration.

            - **FunctionName** *(string) --*

              The name of the function.

            - **FunctionArn** *(string) --*

              The function's Amazon Resource Name (ARN).

            - **Runtime** *(string) --*

              The runtime environment for the Lambda function.

            - **Role** *(string) --*

              The function's execution role.

            - **Handler** *(string) --*

              The function that Lambda calls to begin executing your function.

            - **CodeSize** *(integer) --*

              The size of the function's deployment package, in bytes.

            - **Description** *(string) --*

              The function's description.

            - **Timeout** *(integer) --*

              The amount of time that Lambda allows a function to run before stopping it.

            - **MemorySize** *(integer) --*

              The memory that's allocated to the function.

            - **LastModified** *(string) --*

              The date and time that the function was last updated, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **CodeSha256** *(string) --*

              The SHA256 hash of the function's deployment package.

            - **Version** *(string) --*

              The version of the Lambda function.

            - **VpcConfig** *(dict) --*

              The function's networking configuration.

              - **SubnetIds** *(list) --*

                A list of VPC subnet IDs.

                - *(string) --*

              - **SecurityGroupIds** *(list) --*

                A list of VPC security groups IDs.

                - *(string) --*

              - **VpcId** *(string) --*

                The ID of the VPC.

            - **DeadLetterConfig** *(dict) --*

              The function's dead letter queue.

              - **TargetArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

            - **Environment** *(dict) --*

              The function's environment variables.

              - **Variables** *(dict) --*

                Environment variable key-value pairs.

                - *(string) --*

                  - *(string) --*

              - **Error** *(dict) --*

                Error messages for environment variables that couldn't be applied.

                - **ErrorCode** *(string) --*

                  The error code.

                - **Message** *(string) --*

                  The error message.

            - **KMSKeyArn** *(string) --*

              The KMS key that's used to encrypt the function's environment variables. This key is
              only returned if you've configured a customer managed CMK.

            - **TracingConfig** *(dict) --*

              The function's AWS X-Ray tracing configuration.

              - **Mode** *(string) --*

                The tracing mode.

            - **MasterArn** *(string) --*

              For Lambda@Edge functions, the ARN of the master function.

            - **RevisionId** *(string) --*

              The latest updated revision of the function or alias.

            - **Layers** *(list) --*

              The function's `layers
              <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

              - *(dict) --*

                An `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **CodeSize** *(integer) --*

                  The size of the layer archive in bytes.

            - **State** *(string) --*

              The current state of the function. When the state is ``Inactive`` , you can reactivate
              the function by invoking it.

            - **StateReason** *(string) --*

              The reason for the function's current state.

            - **StateReasonCode** *(string) --*

              The reason code for the function's current state. When the code is ``Creating`` , you
              can't invoke or modify the function.

            - **LastUpdateStatus** *(string) --*

              The status of the last update that was performed on the function.

            - **LastUpdateStatusReason** *(string) --*

              The reason for the last update that was performed on the function.

            - **LastUpdateStatusReasonCode** *(string) --*

              The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_configuration(
        self,
        FunctionName: str,
        Role: str = None,
        Handler: str = None,
        Description: str = None,
        Timeout: int = None,
        MemorySize: int = None,
        VpcConfig: ClientUpdateFunctionConfigurationVpcConfigTypeDef = None,
        Environment: ClientUpdateFunctionConfigurationEnvironmentTypeDef = None,
        Runtime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "provided",
        ] = None,
        DeadLetterConfig: ClientUpdateFunctionConfigurationDeadLetterConfigTypeDef = None,
        KMSKeyArn: str = None,
        TracingConfig: ClientUpdateFunctionConfigurationTracingConfigTypeDef = None,
        RevisionId: str = None,
        Layers: List[str] = None,
    ) -> ClientUpdateFunctionConfigurationResponseTypeDef:
        """
        Modify the version-specific settings of a Lambda function.

        When you update a function, Lambda provisions an instance of the function and its supporting
        resources. If your function connects to a VPC, this process can take a minute. During this
        time, you can't modify the function, but you can still invoke it. The ``LastUpdateStatus`` ,
        ``LastUpdateStatusReason`` , and ``LastUpdateStatusReasonCode`` fields in the response from
        GetFunctionConfiguration indicate when the update is complete and the function is processing
        events with the new configuration. For more information, see `Function States
        <https://docs.aws.amazon.com/lambda/latest/dg/functions-states.html>`__ .

        These settings can vary between versions of a function and are locked when you publish a
        version. You can't modify the configuration of a published version, only the unpublished
        version.

        To configure function concurrency, use  PutFunctionConcurrency . To grant invoke permissions
        to an account or AWS service, use  AddPermission .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionConfiguration>`_

        **Request Syntax**
        ::

          response = client.update_function_configuration(
              FunctionName='string',
              Role='string',
              Handler='string',
              Description='string',
              Timeout=123,
              MemorySize=123,
              VpcConfig={
                  'SubnetIds': [
                      'string',
                  ],
                  'SecurityGroupIds': [
                      'string',
                  ]
              },
              Environment={
                  'Variables': {
                      'string': 'string'
                  }
              },
              Runtime=
                  'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'|'java8'
                  |'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'|'dotnetcore1.0'
                  |'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'|'ruby2.5'|'provided',
              DeadLetterConfig={
                  'TargetArn': 'string'
              },
              KMSKeyArn='string',
              TracingConfig={
                  'Mode': 'Active'|'PassThrough'
              },
              RevisionId='string',
              Layers=[
                  'string',
              ]
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function.

           **Name formats**

          * **Function name** - ``my-function`` .

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          The length constraint applies only to the full ARN. If you specify only the function name,
          it is limited to 64 characters in length.

        :type Role: string
        :param Role:

          The Amazon Resource Name (ARN) of the function's execution role.

        :type Handler: string
        :param Handler:

          The name of the method within your code that Lambda calls to execute your function. The
          format includes the file name. It can also include namespaces and other qualifiers,
          depending on the runtime. For more information, see `Programming Model
          <https://docs.aws.amazon.com/lambda/latest/dg/programming-model-v2.html>`__ .

        :type Description: string
        :param Description:

          A description of the function.

        :type Timeout: integer
        :param Timeout:

          The amount of time that Lambda allows a function to run before stopping it. The default is
          3 seconds. The maximum allowed value is 900 seconds.

        :type MemorySize: integer
        :param MemorySize:

          The amount of memory that your function has access to. Increasing the function's memory
          also increases its CPU allocation. The default value is 128 MB. The value must be a
          multiple of 64 MB.

        :type VpcConfig: dict
        :param VpcConfig:

          For network connectivity to AWS resources in a VPC, specify a list of security groups and
          subnets in the VPC. When you connect a function to a VPC, it can only access resources and
          the internet through that VPC. For more information, see `VPC Settings
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html>`__ .

          - **SubnetIds** *(list) --*

            A list of VPC subnet IDs.

            - *(string) --*

          - **SecurityGroupIds** *(list) --*

            A list of VPC security groups IDs.

            - *(string) --*

        :type Environment: dict
        :param Environment:

          Environment variables that are accessible from function code during execution.

          - **Variables** *(dict) --*

            Environment variable key-value pairs.

            - *(string) --*

              - *(string) --*

        :type Runtime: string
        :param Runtime:

          The identifier of the function's `runtime
          <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html>`__ .

        :type DeadLetterConfig: dict
        :param DeadLetterConfig:

          A dead letter queue configuration that specifies the queue or topic where Lambda sends
          asynchronous events when they fail processing. For more information, see `Dead Letter
          Queues <https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq>`__ .

          - **TargetArn** *(string) --*

            The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

        :type KMSKeyArn: string
        :param KMSKeyArn:

          The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your
          function's environment variables. If it's not provided, AWS Lambda uses a default service
          key.

        :type TracingConfig: dict
        :param TracingConfig:

          Set ``Mode`` to ``Active`` to sample and trace a subset of incoming requests with AWS
          X-Ray.

          - **Mode** *(string) --*

            The tracing mode.

        :type RevisionId: string
        :param RevisionId:

          Only update the function if the revision ID matches the ID that's specified. Use this
          option to avoid modifying a function that has changed since you last read it.

        :type Layers: list
        :param Layers:

          A list of `function layers
          <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ to add to the
          function's execution environment. Specify each layer by its ARN, including the version.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'FunctionName': 'string',
                'FunctionArn': 'string',
                'Runtime':
                'nodejs'|'nodejs4.3'|'nodejs6.10'|'nodejs8.10'|'nodejs10.x'|'nodejs12.x'
                |'java8'|'java11'|'python2.7'|'python3.6'|'python3.7'|'python3.8'
                |'dotnetcore1.0'|'dotnetcore2.0'|'dotnetcore2.1'|'nodejs4.3-edge'|'go1.x'
                |'ruby2.5'|'provided',
                'Role': 'string',
                'Handler': 'string',
                'CodeSize': 123,
                'Description': 'string',
                'Timeout': 123,
                'MemorySize': 123,
                'LastModified': 'string',
                'CodeSha256': 'string',
                'Version': 'string',
                'VpcConfig': {
                    'SubnetIds': [
                        'string',
                    ],
                    'SecurityGroupIds': [
                        'string',
                    ],
                    'VpcId': 'string'
                },
                'DeadLetterConfig': {
                    'TargetArn': 'string'
                },
                'Environment': {
                    'Variables': {
                        'string': 'string'
                    },
                    'Error': {
                        'ErrorCode': 'string',
                        'Message': 'string'
                    }
                },
                'KMSKeyArn': 'string',
                'TracingConfig': {
                    'Mode': 'Active'|'PassThrough'
                },
                'MasterArn': 'string',
                'RevisionId': 'string',
                'Layers': [
                    {
                        'Arn': 'string',
                        'CodeSize': 123
                    },
                ],
                'State': 'Pending'|'Active'|'Inactive'|'Failed',
                'StateReason': 'string',
                'StateReasonCode':
                'Idle'|'Creating'|'Restoring'|'EniLimitExceeded'
                |'InsufficientRolePermissions'|'InvalidConfiguration'|'InternalError'
                |'SubnetOutOfIPAddresses',
                'LastUpdateStatus': 'Successful'|'Failed'|'InProgress',
                'LastUpdateStatusReason': 'string',
                'LastUpdateStatusReasonCode':
                'EniLimitExceeded'|'InsufficientRolePermissions'|'InvalidConfiguration'
                |'InternalError'
            }
          **Response Structure**

          - *(dict) --*

            Details about a function's configuration.

            - **FunctionName** *(string) --*

              The name of the function.

            - **FunctionArn** *(string) --*

              The function's Amazon Resource Name (ARN).

            - **Runtime** *(string) --*

              The runtime environment for the Lambda function.

            - **Role** *(string) --*

              The function's execution role.

            - **Handler** *(string) --*

              The function that Lambda calls to begin executing your function.

            - **CodeSize** *(integer) --*

              The size of the function's deployment package, in bytes.

            - **Description** *(string) --*

              The function's description.

            - **Timeout** *(integer) --*

              The amount of time that Lambda allows a function to run before stopping it.

            - **MemorySize** *(integer) --*

              The memory that's allocated to the function.

            - **LastModified** *(string) --*

              The date and time that the function was last updated, in `ISO-8601 format
              <https://www.w3.org/TR/NOTE-datetime>`__ (YYYY-MM-DDThh:mm:ss.sTZD).

            - **CodeSha256** *(string) --*

              The SHA256 hash of the function's deployment package.

            - **Version** *(string) --*

              The version of the Lambda function.

            - **VpcConfig** *(dict) --*

              The function's networking configuration.

              - **SubnetIds** *(list) --*

                A list of VPC subnet IDs.

                - *(string) --*

              - **SecurityGroupIds** *(list) --*

                A list of VPC security groups IDs.

                - *(string) --*

              - **VpcId** *(string) --*

                The ID of the VPC.

            - **DeadLetterConfig** *(dict) --*

              The function's dead letter queue.

              - **TargetArn** *(string) --*

                The Amazon Resource Name (ARN) of an Amazon SQS queue or Amazon SNS topic.

            - **Environment** *(dict) --*

              The function's environment variables.

              - **Variables** *(dict) --*

                Environment variable key-value pairs.

                - *(string) --*

                  - *(string) --*

              - **Error** *(dict) --*

                Error messages for environment variables that couldn't be applied.

                - **ErrorCode** *(string) --*

                  The error code.

                - **Message** *(string) --*

                  The error message.

            - **KMSKeyArn** *(string) --*

              The KMS key that's used to encrypt the function's environment variables. This key is
              only returned if you've configured a customer managed CMK.

            - **TracingConfig** *(dict) --*

              The function's AWS X-Ray tracing configuration.

              - **Mode** *(string) --*

                The tracing mode.

            - **MasterArn** *(string) --*

              For Lambda@Edge functions, the ARN of the master function.

            - **RevisionId** *(string) --*

              The latest updated revision of the function or alias.

            - **Layers** *(list) --*

              The function's `layers
              <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

              - *(dict) --*

                An `AWS Lambda layer
                <https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html>`__ .

                - **Arn** *(string) --*

                  The Amazon Resource Name (ARN) of the function layer.

                - **CodeSize** *(integer) --*

                  The size of the layer archive in bytes.

            - **State** *(string) --*

              The current state of the function. When the state is ``Inactive`` , you can reactivate
              the function by invoking it.

            - **StateReason** *(string) --*

              The reason for the function's current state.

            - **StateReasonCode** *(string) --*

              The reason code for the function's current state. When the code is ``Creating`` , you
              can't invoke or modify the function.

            - **LastUpdateStatus** *(string) --*

              The status of the last update that was performed on the function.

            - **LastUpdateStatusReason** *(string) --*

              The reason for the last update that was performed on the function.

            - **LastUpdateStatusReasonCode** *(string) --*

              The reason code for the last update that was performed on the function.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_function_event_invoke_config(
        self,
        FunctionName: str,
        Qualifier: str = None,
        MaximumRetryAttempts: int = None,
        MaximumEventAgeInSeconds: int = None,
        DestinationConfig: ClientUpdateFunctionEventInvokeConfigDestinationConfigTypeDef = None,
    ) -> ClientUpdateFunctionEventInvokeConfigResponseTypeDef:
        """
        Updates the configuration for asynchronous invocation for a function, version, or alias.

        To configure options for asynchronous invocation, use  PutFunctionEventInvokeConfig .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateFunctionEventInvokeConfig>`_

        **Request Syntax**
        ::

          response = client.update_function_event_invoke_config(
              FunctionName='string',
              Qualifier='string',
              MaximumRetryAttempts=123,
              MaximumEventAgeInSeconds=123,
              DestinationConfig={
                  'OnSuccess': {
                      'Destination': 'string'
                  },
                  'OnFailure': {
                      'Destination': 'string'
                  }
              }
          )
        :type FunctionName: string
        :param FunctionName: **[REQUIRED]**

          The name of the Lambda function, version, or alias.

           **Name formats**

          * **Function name** - ``my-function`` (name-only), ``my-function:v1`` (with alias).

          * **Function ARN** - ``arn:aws:lambda:us-west-2:123456789012:function:my-function`` .

          * **Partial ARN** - ``123456789012:function:my-function`` .

          You can append a version number or alias to any of the formats. The length constraint
          applies only to the full ARN. If you specify only the function name, it is limited to 64
          characters in length.

        :type Qualifier: string
        :param Qualifier:

          A version number or alias name.

        :type MaximumRetryAttempts: integer
        :param MaximumRetryAttempts:

          The maximum number of times to retry when the function returns an error.

        :type MaximumEventAgeInSeconds: integer
        :param MaximumEventAgeInSeconds:

          The maximum age of a request that Lambda sends to a function for processing.

        :type DestinationConfig: dict
        :param DestinationConfig:

          A destination for events after they have been sent to a function for processing.

           **Destinations**

          * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

          * **Queue** - The ARN of an SQS queue.

          * **Topic** - The ARN of an SNS topic.

          * **Event Bus** - The ARN of an Amazon EventBridge event bus.

          - **OnSuccess** *(dict) --*

            The destination configuration for successful invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

          - **OnFailure** *(dict) --*

            The destination configuration for failed invocations.

            - **Destination** *(string) --*

              The Amazon Resource Name (ARN) of the destination resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'LastModified': datetime(2015, 1, 1),
                'FunctionArn': 'string',
                'MaximumRetryAttempts': 123,
                'MaximumEventAgeInSeconds': 123,
                'DestinationConfig': {
                    'OnSuccess': {
                        'Destination': 'string'
                    },
                    'OnFailure': {
                        'Destination': 'string'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **LastModified** *(datetime) --*

              The date and time that the configuration was last updated.

            - **FunctionArn** *(string) --*

              The Amazon Resource Name (ARN) of the function.

            - **MaximumRetryAttempts** *(integer) --*

              The maximum number of times to retry when the function returns an error.

            - **MaximumEventAgeInSeconds** *(integer) --*

              The maximum age of a request that Lambda sends to a function for processing.

            - **DestinationConfig** *(dict) --*

              A destination for events after they have been sent to a function for processing.

               **Destinations**

              * **Function** - The Amazon Resource Name (ARN) of a Lambda function.

              * **Queue** - The ARN of an SQS queue.

              * **Topic** - The ARN of an SNS topic.

              * **Event Bus** - The ARN of an Amazon EventBridge event bus.

              - **OnSuccess** *(dict) --*

                The destination configuration for successful invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.

              - **OnFailure** *(dict) --*

                The destination configuration for failed invocations.

                - **Destination** *(string) --*

                  The Amazon Resource Name (ARN) of the destination resource.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        Get Paginator for `list_aliases` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_event_source_mappings"]
    ) -> paginator_scope.ListEventSourceMappingsPaginator:
        """
        Get Paginator for `list_event_source_mappings` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_function_event_invoke_configs"]
    ) -> paginator_scope.ListFunctionEventInvokeConfigsPaginator:
        """
        Get Paginator for `list_function_event_invoke_configs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_functions"]
    ) -> paginator_scope.ListFunctionsPaginator:
        """
        Get Paginator for `list_functions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_layer_versions"]
    ) -> paginator_scope.ListLayerVersionsPaginator:
        """
        Get Paginator for `list_layer_versions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_layers"]
    ) -> paginator_scope.ListLayersPaginator:
        """
        Get Paginator for `list_layers` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_provisioned_concurrency_configs"]
    ) -> paginator_scope.ListProvisionedConcurrencyConfigsPaginator:
        """
        Get Paginator for `list_provisioned_concurrency_configs` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_versions_by_function"]
    ) -> paginator_scope.ListVersionsByFunctionPaginator:
        """
        Get Paginator for `list_versions_by_function` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_active"]
    ) -> waiter_scope.FunctionActiveWaiter:
        """
        Get Waiter `function_active`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_exists"]
    ) -> waiter_scope.FunctionExistsWaiter:
        """
        Get Waiter `function_exists`.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["function_updated"]
    ) -> waiter_scope.FunctionUpdatedWaiter:
        """
        Get Waiter `function_updated`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    ClientError: Boto3ClientError
    CodeStorageExceededException: Boto3ClientError
    EC2AccessDeniedException: Boto3ClientError
    EC2ThrottledException: Boto3ClientError
    EC2UnexpectedException: Boto3ClientError
    ENILimitReachedException: Boto3ClientError
    InvalidParameterValueException: Boto3ClientError
    InvalidRequestContentException: Boto3ClientError
    InvalidRuntimeException: Boto3ClientError
    InvalidSecurityGroupIDException: Boto3ClientError
    InvalidSubnetIDException: Boto3ClientError
    InvalidZipFileException: Boto3ClientError
    KMSAccessDeniedException: Boto3ClientError
    KMSDisabledException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KMSNotFoundException: Boto3ClientError
    PolicyLengthExceededException: Boto3ClientError
    PreconditionFailedException: Boto3ClientError
    ProvisionedConcurrencyConfigNotFoundException: Boto3ClientError
    RequestTooLargeException: Boto3ClientError
    ResourceConflictException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    ResourceNotReadyException: Boto3ClientError
    ServiceException: Boto3ClientError
    SubnetIPAddressLimitReachedException: Boto3ClientError
    TooManyRequestsException: Boto3ClientError
    UnsupportedMediaTypeException: Boto3ClientError
