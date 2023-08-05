"Main interface for application-autoscaling service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_application_autoscaling.client as client_scope

# pylint: disable=import-self
import mypy_boto3_application_autoscaling.paginator as paginator_scope
from mypy_boto3_application_autoscaling.type_defs import (
    ClientDescribeScalableTargetsResponseTypeDef,
    ClientDescribeScalingActivitiesResponseTypeDef,
    ClientDescribeScalingPoliciesResponseTypeDef,
    ClientDescribeScheduledActionsResponseTypeDef,
    ClientPutScalingPolicyResponseTypeDef,
    ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef,
    ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef,
    ClientPutScheduledActionScalableTargetActionTypeDef,
    ClientRegisterScalableTargetSuspendedStateTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

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
    def delete_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
    ) -> Dict[str, Any]:
        """
        Deletes the specified scaling policy for an Application Auto Scaling scalable target.

        Deleting a step scaling policy deletes the underlying alarm action, but does not delete the
        CloudWatch alarm associated with the scaling policy, even if it no longer has an associated
        action.

        For more information, see `Delete a Step Scaling Policy
        <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html#delete-step-scaling-policy>`__
        and `Delete a Target Tracking Scaling Policy
        <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html#delete-target-tracking-policy>`__
        in the *Application Auto Scaling User Guide* .

        To create a scaling policy or update an existing one, see  PutScalingPolicy .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DeleteScalingPolicy>`_

        **Request Syntax**
        ::

          response = client.delete_scaling_policy(
              PolicyName='string',
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency'
          )
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The name of the scaling policy.

        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource associated with the scalable target. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_scheduled_action(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
    ) -> Dict[str, Any]:
        """
        Deletes the specified scheduled action for an Application Auto Scaling scalable target.

        For more information, see `Delete a Scheduled Action
        <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.html#delete-scheduled-action>`__
        in the *Application Auto Scaling User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DeleteScheduledAction>`_

        **Request Syntax**
        ::

          response = client.delete_scheduled_action(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ScheduledActionName='string',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency'
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ScheduledActionName: string
        :param ScheduledActionName: **[REQUIRED]**

          The name of the scheduled action.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource associated with the scheduled action. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_scalable_target(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
    ) -> Dict[str, Any]:
        """
        Deregisters an Application Auto Scaling scalable target.

        Deregistering a scalable target deletes the scaling policies that are associated with it.

        To create a scalable target or update an existing one, see  RegisterScalableTarget .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DeregisterScalableTarget>`_

        **Request Syntax**
        ::

          response = client.deregister_scalable_target(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency'
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource associated with the scalable target. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension associated with the scalable target. This string consists of the
          service namespace, resource type, and scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scalable_targets(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceIds: List[str] = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalableTargetsResponseTypeDef:
        """
        Gets information about the scalable targets in the specified namespace.

        You can filter the results using ``ResourceIds`` and ``ScalableDimension`` .

        To create a scalable target or update an existing one, see  RegisterScalableTarget . If you
        are no longer using a scalable target, you can deregister it using  DeregisterScalableTarget
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalableTargets>`_

        **Request Syntax**
        ::

          response = client.describe_scalable_targets(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceIds=[
                  'string',
              ],
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              MaxResults=123,
              NextToken='string'
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceIds: list
        :param ResourceIds:

          The identifier of the resource associated with the scalable target. This string consists
          of the resource type and unique identifier. If you specify a scalable dimension, you must
          also specify a resource ID.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

          - *(string) --*

        :type ScalableDimension: string
        :param ScalableDimension:

          The scalable dimension associated with the scalable target. This string consists of the
          service namespace, resource type, and scaling property. If you specify a scalable
          dimension, you must also specify a resource ID.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of scalable targets. This value can be between 1 and 50. The default
          value is 50.

          If this parameter is used, the operation returns up to ``MaxResults`` results at a time,
          along with a ``NextToken`` value. To get the next set of results, include the
          ``NextToken`` value in a subsequent call. If this parameter is not used, the operation
          returns up to 50 results and a ``NextToken`` value, if applicable.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ScalableTargets': [
                    {
                        'ServiceNamespace':
                        'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'
                        |'sagemaker'|'custom-resource'|'comprehend'|'lambda',
                        'ResourceId': 'string',
                        'ScalableDimension':
                        'ecs:service:DesiredCount'
                        |'ec2:spot-fleet-request:TargetCapacity'
                        |'elasticmapreduce:instancegroup:InstanceCount'
                        |'appstream:fleet:DesiredCapacity'
                        |'dynamodb:table:ReadCapacityUnits'
                        |'dynamodb:table:WriteCapacityUnits'
                        |'dynamodb:index:ReadCapacityUnits'
                        |'dynamodb:index:WriteCapacityUnits'
                        |'rds:cluster:ReadReplicaCount'
                        |'sagemaker:variant:DesiredInstanceCount'
                        |'custom-resource:ResourceType:Property'
                        |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                        |'lambda:function:ProvisionedConcurrency',
                        'MinCapacity': 123,
                        'MaxCapacity': 123,
                        'RoleARN': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'SuspendedState': {
                            'DynamicScalingInSuspended': True|False,
                            'DynamicScalingOutSuspended': True|False,
                            'ScheduledScalingSuspended': True|False
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ScalableTargets** *(list) --*

              The scalable targets that match the request parameters.

              - *(dict) --*

                Represents a scalable target.

                - **ServiceNamespace** *(string) --*

                  The namespace of the AWS service that provides the resource or ``custom-resource``
                  for a resource provided by your own application or service. For more information,
                  see `AWS Service Namespaces
                  <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
                  in the *Amazon Web Services General Reference* .

                - **ResourceId** *(string) --*

                  The identifier of the resource associated with the scalable target. This string
                  consists of the resource type and unique identifier.

                  * ECS service - The resource type is ``service`` and the unique identifier is the
                  cluster name and service name. Example: ``service/default/sample-webapp`` .

                  * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
                  identifier is the Spot Fleet request ID. Example:
                  ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier
                  is the cluster ID and instance group ID. Example:
                  ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier
                  is the fleet name. Example: ``fleet/sample-fleet`` .

                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the
                  table name. Example: ``table/my-table`` .

                  * DynamoDB global secondary index - The resource type is ``index`` and the unique
                  identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier
                  is the cluster name. Example: ``cluster:my-db-cluster`` .

                  * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the
                  unique identifier is the resource ID. Example:
                  ``endpoint/my-end-point/variant/KMeansClustering`` .

                  * Custom resources are not supported with a resource type. This parameter must
                  specify the ``OutputValue`` from the CloudFormation template stack used to access
                  the resources. The unique identifier is defined by the service provider. More
                  information is available in our `GitHub repository
                  <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

                  * Amazon Comprehend document classification endpoint - The resource type and
                  unique identifier are specified using the endpoint ARN. Example:
                  ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``
                  .

                  * Lambda provisioned concurrency - The resource type is ``function`` and the
                  unique identifier is the function name with a function version or alias name
                  suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or
                  ``function:my-function:1`` .

                - **ScalableDimension** *(string) --*

                  The scalable dimension associated with the scalable target. This string consists
                  of the service namespace, resource type, and scaling property.

                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
                  request.

                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
                  Instance Group.

                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0
                  fleet.

                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB table.

                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB table.

                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB global secondary index.

                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB global secondary index.

                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
                  cluster. Available for Aurora MySQL-compatible edition and Aurora
                  PostgreSQL-compatible edition.

                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an
                  Amazon SageMaker model endpoint variant.

                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
                  resource provided by your own application or service.

                  * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number
                  of inference units for an Amazon Comprehend document classification endpoint.

                  * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a
                  Lambda function.

                - **MinCapacity** *(integer) --*

                  The minimum value to scale to in response to a scale-in event.

                - **MaxCapacity** *(integer) --*

                  The maximum value to scale to in response to a scale-out event.

                - **RoleARN** *(string) --*

                  The ARN of an IAM role that allows Application Auto Scaling to modify the scalable
                  target on your behalf.

                - **CreationTime** *(datetime) --*

                  The Unix timestamp for when the scalable target was created.

                - **SuspendedState** *(dict) --*

                  Specifies whether the scaling activities for a scalable target are in a suspended
                  state.

                  - **DynamicScalingInSuspended** *(boolean) --*

                    Whether scale in by a target tracking scaling policy or a step scaling policy is
                    suspended. Set the value to ``true`` if you don't want Application Auto Scaling
                    to remove capacity when a scaling policy is triggered. The default is ``false``
                    .

                  - **DynamicScalingOutSuspended** *(boolean) --*

                    Whether scale out by a target tracking scaling policy or a step scaling policy
                    is suspended. Set the value to ``true`` if you don't want Application Auto
                    Scaling to add capacity when a scaling policy is triggered. The default is
                    ``false`` .

                  - **ScheduledScalingSuspended** *(boolean) --*

                    Whether scheduled scaling is suspended. Set the value to ``true`` if you don't
                    want Application Auto Scaling to add or remove capacity by initiating scheduled
                    actions. The default is ``false`` .

            - **NextToken** *(string) --*

              The token required to get the next set of results. This value is ``null`` if there are
              no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scaling_activities(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalingActivitiesResponseTypeDef:
        """
        Provides descriptive information about the scaling activities in the specified namespace
        from the previous six weeks.

        You can filter the results using ``ResourceId`` and ``ScalableDimension`` .

        Scaling activities are triggered by CloudWatch alarms that are associated with scaling
        policies. To view the scaling policies for a service namespace, see  DescribeScalingPolicies
        . To create a scaling policy or update an existing one, see  PutScalingPolicy .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalingActivities>`_

        **Request Syntax**
        ::

          response = client.describe_scaling_activities(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              MaxResults=123,
              NextToken='string'
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId:

          The identifier of the resource associated with the scaling activity. This string consists
          of the resource type and unique identifier. If you specify a scalable dimension, you must
          also specify a resource ID.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension:

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property. If you specify a scalable dimension, you must also specify a resource
          ID.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of scalable targets. This value can be between 1 and 50. The default
          value is 50.

          If this parameter is used, the operation returns up to ``MaxResults`` results at a time,
          along with a ``NextToken`` value. To get the next set of results, include the
          ``NextToken`` value in a subsequent call. If this parameter is not used, the operation
          returns up to 50 results and a ``NextToken`` value, if applicable.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ScalingActivities': [
                    {
                        'ActivityId': 'string',
                        'ServiceNamespace':
                        'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'
                        |'sagemaker'|'custom-resource'|'comprehend'|'lambda',
                        'ResourceId': 'string',
                        'ScalableDimension':
                        'ecs:service:DesiredCount'
                        |'ec2:spot-fleet-request:TargetCapacity'
                        |'elasticmapreduce:instancegroup:InstanceCount'
                        |'appstream:fleet:DesiredCapacity'
                        |'dynamodb:table:ReadCapacityUnits'
                        |'dynamodb:table:WriteCapacityUnits'
                        |'dynamodb:index:ReadCapacityUnits'
                        |'dynamodb:index:WriteCapacityUnits'
                        |'rds:cluster:ReadReplicaCount'
                        |'sagemaker:variant:DesiredInstanceCount'
                        |'custom-resource:ResourceType:Property'
                        |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                        |'lambda:function:ProvisionedConcurrency',
                        'Description': 'string',
                        'Cause': 'string',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'StatusCode':
                        'Pending'|'InProgress'|'Successful'|'Overridden'
                        |'Unfulfilled'|'Failed',
                        'StatusMessage': 'string',
                        'Details': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ScalingActivities** *(list) --*

              A list of scaling activity objects.

              - *(dict) --*

                Represents a scaling activity.

                - **ActivityId** *(string) --*

                  The unique identifier of the scaling activity.

                - **ServiceNamespace** *(string) --*

                  The namespace of the AWS service that provides the resource or ``custom-resource``
                  for a resource provided by your own application or service. For more information,
                  see `AWS Service Namespaces
                  <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
                  in the *Amazon Web Services General Reference* .

                - **ResourceId** *(string) --*

                  The identifier of the resource associated with the scaling activity. This string
                  consists of the resource type and unique identifier.

                  * ECS service - The resource type is ``service`` and the unique identifier is the
                  cluster name and service name. Example: ``service/default/sample-webapp`` .

                  * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
                  identifier is the Spot Fleet request ID. Example:
                  ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier
                  is the cluster ID and instance group ID. Example:
                  ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier
                  is the fleet name. Example: ``fleet/sample-fleet`` .

                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the
                  table name. Example: ``table/my-table`` .

                  * DynamoDB global secondary index - The resource type is ``index`` and the unique
                  identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier
                  is the cluster name. Example: ``cluster:my-db-cluster`` .

                  * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the
                  unique identifier is the resource ID. Example:
                  ``endpoint/my-end-point/variant/KMeansClustering`` .

                  * Custom resources are not supported with a resource type. This parameter must
                  specify the ``OutputValue`` from the CloudFormation template stack used to access
                  the resources. The unique identifier is defined by the service provider. More
                  information is available in our `GitHub repository
                  <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

                  * Amazon Comprehend document classification endpoint - The resource type and
                  unique identifier are specified using the endpoint ARN. Example:
                  ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``
                  .

                  * Lambda provisioned concurrency - The resource type is ``function`` and the
                  unique identifier is the function name with a function version or alias name
                  suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or
                  ``function:my-function:1`` .

                - **ScalableDimension** *(string) --*

                  The scalable dimension. This string consists of the service namespace, resource
                  type, and scaling property.

                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
                  request.

                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
                  Instance Group.

                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0
                  fleet.

                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB table.

                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB table.

                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB global secondary index.

                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB global secondary index.

                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
                  cluster. Available for Aurora MySQL-compatible edition and Aurora
                  PostgreSQL-compatible edition.

                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an
                  Amazon SageMaker model endpoint variant.

                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
                  resource provided by your own application or service.

                  * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number
                  of inference units for an Amazon Comprehend document classification endpoint.

                  * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a
                  Lambda function.

                - **Description** *(string) --*

                  A simple description of what action the scaling activity intends to accomplish.

                - **Cause** *(string) --*

                  A simple description of what caused the scaling activity to happen.

                - **StartTime** *(datetime) --*

                  The Unix timestamp for when the scaling activity began.

                - **EndTime** *(datetime) --*

                  The Unix timestamp for when the scaling activity ended.

                - **StatusCode** *(string) --*

                  Indicates the status of the scaling activity.

                - **StatusMessage** *(string) --*

                  A simple message about the current status of the scaling activity.

                - **Details** *(string) --*

                  The details about the scaling activity.

            - **NextToken** *(string) --*

              The token required to get the next set of results. This value is ``null`` if there are
              no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scaling_policies(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        PolicyNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScalingPoliciesResponseTypeDef:
        """
        Describes the Application Auto Scaling scaling policies for the specified service namespace.

        You can filter the results using ``ResourceId`` , ``ScalableDimension`` , and
        ``PolicyNames`` .

        To create a scaling policy or update an existing one, see  PutScalingPolicy . If you are no
        longer using a scaling policy, you can delete it using  DeleteScalingPolicy .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScalingPolicies>`_

        **Request Syntax**
        ::

          response = client.describe_scaling_policies(
              PolicyNames=[
                  'string',
              ],
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              MaxResults=123,
              NextToken='string'
          )
        :type PolicyNames: list
        :param PolicyNames:

          The names of the scaling policies to describe.

          - *(string) --*

        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId:

          The identifier of the resource associated with the scaling policy. This string consists of
          the resource type and unique identifier. If you specify a scalable dimension, you must
          also specify a resource ID.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension:

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property. If you specify a scalable dimension, you must also specify a resource
          ID.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of scalable targets. This value can be between 1 and 50. The default
          value is 50.

          If this parameter is used, the operation returns up to ``MaxResults`` results at a time,
          along with a ``NextToken`` value. To get the next set of results, include the
          ``NextToken`` value in a subsequent call. If this parameter is not used, the operation
          returns up to 50 results and a ``NextToken`` value, if applicable.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ScalingPolicies': [
                    {
                        'PolicyARN': 'string',
                        'PolicyName': 'string',
                        'ServiceNamespace':
                        'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'
                        |'sagemaker'|'custom-resource'|'comprehend'|'lambda',
                        'ResourceId': 'string',
                        'ScalableDimension':
                        'ecs:service:DesiredCount'
                        |'ec2:spot-fleet-request:TargetCapacity'
                        |'elasticmapreduce:instancegroup:InstanceCount'
                        |'appstream:fleet:DesiredCapacity'
                        |'dynamodb:table:ReadCapacityUnits'
                        |'dynamodb:table:WriteCapacityUnits'
                        |'dynamodb:index:ReadCapacityUnits'
                        |'dynamodb:index:WriteCapacityUnits'
                        |'rds:cluster:ReadReplicaCount'
                        |'sagemaker:variant:DesiredInstanceCount'
                        |'custom-resource:ResourceType:Property'
                        |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                        |'lambda:function:ProvisionedConcurrency',
                        'PolicyType': 'StepScaling'|'TargetTrackingScaling',
                        'StepScalingPolicyConfiguration': {
                            'AdjustmentType':
                            'ChangeInCapacity'|'PercentChangeInCapacity'
                            |'ExactCapacity',
                            'StepAdjustments': [
                                {
                                    'MetricIntervalLowerBound': 123.0,
                                    'MetricIntervalUpperBound': 123.0,
                                    'ScalingAdjustment': 123
                                },
                            ],
                            'MinAdjustmentMagnitude': 123,
                            'Cooldown': 123,
                            'MetricAggregationType': 'Average'|'Minimum'|'Maximum'
                        },
                        'TargetTrackingScalingPolicyConfiguration': {
                            'TargetValue': 123.0,
                            'PredefinedMetricSpecification': {
                                'PredefinedMetricType':
                                'DynamoDBReadCapacityUtilization'
                                |'DynamoDBWriteCapacityUtilization'
                                |'ALBRequestCountPerTarget'
                                |'RDSReaderAverageCPUUtilization'
                                |'RDSReaderAverageDatabaseConnections'
                                |'EC2SpotFleetRequestAverageCPUUtilization'
                                |'EC2SpotFleetRequestAverageNetworkIn'
                                |'EC2SpotFleetRequestAverageNetworkOut'
                                |'SageMakerVariantInvocationsPerInstance'
                                |'ECSServiceAverageCPUUtilization'
                                |'ECSServiceAverageMemoryUtilization'
                                |'AppStreamAverageCapacityUtilization'
                                |'ComprehendInferenceUtilization'
                                |'LambdaProvisionedConcurrencyUtilization',
                                'ResourceLabel': 'string'
                            },
                            'CustomizedMetricSpecification': {
                                'MetricName': 'string',
                                'Namespace': 'string',
                                'Dimensions': [
                                    {
                                        'Name': 'string',
                                        'Value': 'string'
                                    },
                                ],
                                'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                                'Unit': 'string'
                            },
                            'ScaleOutCooldown': 123,
                            'ScaleInCooldown': 123,
                            'DisableScaleIn': True|False
                        },
                        'Alarms': [
                            {
                                'AlarmName': 'string',
                                'AlarmARN': 'string'
                            },
                        ],
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ScalingPolicies** *(list) --*

              Information about the scaling policies.

              - *(dict) --*

                Represents a scaling policy to use with Application Auto Scaling.

                - **PolicyARN** *(string) --*

                  The Amazon Resource Name (ARN) of the scaling policy.

                - **PolicyName** *(string) --*

                  The name of the scaling policy.

                - **ServiceNamespace** *(string) --*

                  The namespace of the AWS service that provides the resource or ``custom-resource``
                  for a resource provided by your own application or service. For more information,
                  see `AWS Service Namespaces
                  <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
                  in the *Amazon Web Services General Reference* .

                - **ResourceId** *(string) --*

                  The identifier of the resource associated with the scaling policy. This string
                  consists of the resource type and unique identifier.

                  * ECS service - The resource type is ``service`` and the unique identifier is the
                  cluster name and service name. Example: ``service/default/sample-webapp`` .

                  * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
                  identifier is the Spot Fleet request ID. Example:
                  ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier
                  is the cluster ID and instance group ID. Example:
                  ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier
                  is the fleet name. Example: ``fleet/sample-fleet`` .

                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the
                  table name. Example: ``table/my-table`` .

                  * DynamoDB global secondary index - The resource type is ``index`` and the unique
                  identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier
                  is the cluster name. Example: ``cluster:my-db-cluster`` .

                  * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the
                  unique identifier is the resource ID. Example:
                  ``endpoint/my-end-point/variant/KMeansClustering`` .

                  * Custom resources are not supported with a resource type. This parameter must
                  specify the ``OutputValue`` from the CloudFormation template stack used to access
                  the resources. The unique identifier is defined by the service provider. More
                  information is available in our `GitHub repository
                  <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

                  * Amazon Comprehend document classification endpoint - The resource type and
                  unique identifier are specified using the endpoint ARN. Example:
                  ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``
                  .

                  * Lambda provisioned concurrency - The resource type is ``function`` and the
                  unique identifier is the function name with a function version or alias name
                  suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or
                  ``function:my-function:1`` .

                - **ScalableDimension** *(string) --*

                  The scalable dimension. This string consists of the service namespace, resource
                  type, and scaling property.

                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
                  request.

                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
                  Instance Group.

                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0
                  fleet.

                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB table.

                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB table.

                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB global secondary index.

                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB global secondary index.

                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
                  cluster. Available for Aurora MySQL-compatible edition and Aurora
                  PostgreSQL-compatible edition.

                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an
                  Amazon SageMaker model endpoint variant.

                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
                  resource provided by your own application or service.

                  * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number
                  of inference units for an Amazon Comprehend document classification endpoint.

                  * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a
                  Lambda function.

                - **PolicyType** *(string) --*

                  The scaling policy type.

                - **StepScalingPolicyConfiguration** *(dict) --*

                  A step scaling policy.

                  - **AdjustmentType** *(string) --*

                    Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an
                    absolute number or a percentage of the current capacity.

                  - **StepAdjustments** *(list) --*

                    A set of adjustments that enable you to scale based on the size of the alarm
                    breach.

                    - *(dict) --*

                      Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes
                      an adjustment based on the difference between the value of the aggregated
                      CloudWatch metric and the breach threshold that you've defined for the alarm.

                      For the following examples, suppose that you have an alarm with a breach
                      threshold of 50:

                      * To trigger the adjustment when the metric is greater than or equal to 50 and
                      less than 60, specify a lower bound of 0 and an upper bound of 10.

                      * To trigger the adjustment when the metric is greater than 40 and less than
                      or equal to 50, specify a lower bound of -10 and an upper bound of 0.

                      There are a few rules for the step adjustments for your step policy:

                      * The ranges of your step adjustments can't overlap or have a gap.

                      * At most one step adjustment can have a null lower bound. If one step
                      adjustment has a negative lower bound, then there must be a step adjustment
                      with a null lower bound.

                      * At most one step adjustment can have a null upper bound. If one step
                      adjustment has a positive upper bound, then there must be a step adjustment
                      with a null upper bound.

                      * The upper and lower bound can't be null in the same step adjustment.

                      - **MetricIntervalLowerBound** *(float) --*

                        The lower bound for the difference between the alarm threshold and the
                        CloudWatch metric. If the metric value is above the breach threshold, the
                        lower bound is inclusive (the metric must be greater than or equal to the
                        threshold plus the lower bound). Otherwise, it is exclusive (the metric must
                        be greater than the threshold plus the lower bound). A null value indicates
                        negative infinity.

                      - **MetricIntervalUpperBound** *(float) --*

                        The upper bound for the difference between the alarm threshold and the
                        CloudWatch metric. If the metric value is above the breach threshold, the
                        upper bound is exclusive (the metric must be less than the threshold plus
                        the upper bound). Otherwise, it is inclusive (the metric must be less than
                        or equal to the threshold plus the upper bound). A null value indicates
                        positive infinity.

                        The upper bound must be greater than the lower bound.

                      - **ScalingAdjustment** *(integer) --*

                        The amount by which to scale, based on the specified adjustment type. A
                        positive value adds to the current scalable dimension while a negative
                        number removes from the current scalable dimension.

                  - **MinAdjustmentMagnitude** *(integer) --*

                    The minimum number to adjust your scalable dimension as a result of a scaling
                    activity. If the adjustment type is ``PercentChangeInCapacity`` , the scaling
                    policy changes the scalable dimension of the scalable target by this amount.

                    For example, suppose that you create a step scaling policy to scale out an
                    Amazon ECS service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of
                    2. If the service has 4 tasks and the scaling policy is performed, 25 percent of
                    4 is 1. However, because you specified a ``MinAdjustmentMagnitude`` of 2,
                    Application Auto Scaling scales out the service by 2 tasks.

                  - **Cooldown** *(integer) --*

                    The amount of time, in seconds, after a scaling activity completes where
                    previous trigger-related scaling activities can influence future scaling events.

                    For scale-out policies, while the cooldown period is in effect, the capacity
                    that has been added by the previous scale-out event that initiated the cooldown
                    is calculated as part of the desired capacity for the next scale out. The
                    intention is to continuously (but not excessively) scale out. For example, an
                    alarm triggers a step scaling policy to scale out an Amazon ECS service by 2
                    tasks, the scaling activity completes successfully, and a cooldown period of 5
                    minutes starts. During the cooldown period, if the alarm triggers the same
                    policy again but at a more aggressive step adjustment to scale out the service
                    by 3 tasks, the 2 tasks that were added in the previous scale-out event are
                    considered part of that capacity and only 1 additional task is added to the
                    desired count.

                    For scale-in policies, the cooldown period is used to block subsequent scale-in
                    requests until it has expired. The intention is to scale in conservatively to
                    protect your application's availability. However, if another alarm triggers a
                    scale-out policy during the cooldown period after a scale-in, Application Auto
                    Scaling scales out your scalable target immediately.

                  - **MetricAggregationType** *(string) --*

                    The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
                    ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is
                    treated as ``Average`` .

                - **TargetTrackingScalingPolicyConfiguration** *(dict) --*

                  A target tracking scaling policy.

                  - **TargetValue** *(float) --*

                    The target value for the metric. The range is 8.515920e-109 to 1.174271e+108
                    (Base 10) or 2e-360 to 2e360 (Base 2).

                  - **PredefinedMetricSpecification** *(dict) --*

                    A predefined metric. You can specify either a predefined metric or a customized
                    metric.

                    - **PredefinedMetricType** *(string) --*

                      The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to
                      Spot Fleet requests and ECS services.

                    - **ResourceLabel** *(string) --*

                      Identifies the resource associated with the metric type. You can't specify a
                      resource label unless the metric type is ``ALBRequestCountPerTarget`` and
                      there is a target group attached to the Spot Fleet request or ECS service.

                      The format is
                      app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
                      where:

                      * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
                      balancer ARN

                      * targetgroup/<target-group-name>/<target-group-id> is the final portion of
                      the target group ARN.

                  - **CustomizedMetricSpecification** *(dict) --*

                    A customized metric. You can specify either a predefined metric or a customized
                    metric.

                    - **MetricName** *(string) --*

                      The name of the metric.

                    - **Namespace** *(string) --*

                      The namespace of the metric.

                    - **Dimensions** *(list) --*

                      The dimensions of the metric.

                      Conditional: If you published your metric with dimensions, you must specify
                      the same dimensions in your scaling policy.

                      - *(dict) --*

                        Describes the dimension names and values associated with a metric.

                        - **Name** *(string) --*

                          The name of the dimension.

                        - **Value** *(string) --*

                          The value of the dimension.

                    - **Statistic** *(string) --*

                      The statistic of the metric.

                    - **Unit** *(string) --*

                      The unit of the metric.

                  - **ScaleOutCooldown** *(integer) --*

                    The amount of time, in seconds, after a scale-out activity completes before
                    another scale-out activity can start.

                    While the cooldown period is in effect, the capacity that has been added by the
                    previous scale-out event that initiated the cooldown is calculated as part of
                    the desired capacity for the next scale out. The intention is to continuously
                    (but not excessively) scale out.

                  - **ScaleInCooldown** *(integer) --*

                    The amount of time, in seconds, after a scale-in activity completes before
                    another scale in activity can start.

                    The cooldown period is used to block subsequent scale-in requests until it has
                    expired. The intention is to scale in conservatively to protect your
                    application's availability. However, if another alarm triggers a scale-out
                    policy during the cooldown period after a scale-in, Application Auto Scaling
                    scales out your scalable target immediately.

                  - **DisableScaleIn** *(boolean) --*

                    Indicates whether scale in by the target tracking scaling policy is disabled. If
                    the value is ``true`` , scale in is disabled and the target tracking scaling
                    policy won't remove capacity from the scalable resource. Otherwise, scale in is
                    enabled and the target tracking scaling policy can remove capacity from the
                    scalable resource. The default value is ``false`` .

                - **Alarms** *(list) --*

                  The CloudWatch alarms associated with the scaling policy.

                  - *(dict) --*

                    Represents a CloudWatch alarm associated with a scaling policy.

                    - **AlarmName** *(string) --*

                      The name of the alarm.

                    - **AlarmARN** *(string) --*

                      The Amazon Resource Name (ARN) of the alarm.

                - **CreationTime** *(datetime) --*

                  The Unix timestamp for when the scaling policy was created.

            - **NextToken** *(string) --*

              The token required to get the next set of results. This value is ``null`` if there are
              no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_scheduled_actions(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ScheduledActionNames: List[str] = None,
        ResourceId: str = None,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ClientDescribeScheduledActionsResponseTypeDef:
        """
        Describes the Application Auto Scaling scheduled actions for the specified service
        namespace.

        You can filter the results using the ``ResourceId`` , ``ScalableDimension`` , and
        ``ScheduledActionNames`` parameters.

        To create a scheduled action or update an existing one, see  PutScheduledAction . If you are
        no longer using a scheduled action, you can delete it using  DeleteScheduledAction .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/DescribeScheduledActions>`_

        **Request Syntax**
        ::

          response = client.describe_scheduled_actions(
              ScheduledActionNames=[
                  'string',
              ],
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              MaxResults=123,
              NextToken='string'
          )
        :type ScheduledActionNames: list
        :param ScheduledActionNames:

          The names of the scheduled actions to describe.

          - *(string) --*

        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId:

          The identifier of the resource associated with the scheduled action. This string consists
          of the resource type and unique identifier. If you specify a scalable dimension, you must
          also specify a resource ID.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension:

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property. If you specify a scalable dimension, you must also specify a resource
          ID.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of scheduled action results. This value can be between 1 and 50. The
          default value is 50.

          If this parameter is used, the operation returns up to ``MaxResults`` results at a time,
          along with a ``NextToken`` value. To get the next set of results, include the
          ``NextToken`` value in a subsequent call. If this parameter is not used, the operation
          returns up to 50 results and a ``NextToken`` value, if applicable.

        :type NextToken: string
        :param NextToken:

          The token for the next set of results.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ScheduledActions': [
                    {
                        'ScheduledActionName': 'string',
                        'ScheduledActionARN': 'string',
                        'ServiceNamespace':
                        'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'
                        |'sagemaker'|'custom-resource'|'comprehend'|'lambda',
                        'Schedule': 'string',
                        'ResourceId': 'string',
                        'ScalableDimension':
                        'ecs:service:DesiredCount'
                        |'ec2:spot-fleet-request:TargetCapacity'
                        |'elasticmapreduce:instancegroup:InstanceCount'
                        |'appstream:fleet:DesiredCapacity'
                        |'dynamodb:table:ReadCapacityUnits'
                        |'dynamodb:table:WriteCapacityUnits'
                        |'dynamodb:index:ReadCapacityUnits'
                        |'dynamodb:index:WriteCapacityUnits'
                        |'rds:cluster:ReadReplicaCount'
                        |'sagemaker:variant:DesiredInstanceCount'
                        |'custom-resource:ResourceType:Property'
                        |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                        |'lambda:function:ProvisionedConcurrency',
                        'StartTime': datetime(2015, 1, 1),
                        'EndTime': datetime(2015, 1, 1),
                        'ScalableTargetAction': {
                            'MinCapacity': 123,
                            'MaxCapacity': 123
                        },
                        'CreationTime': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ScheduledActions** *(list) --*

              Information about the scheduled actions.

              - *(dict) --*

                Represents a scheduled action.

                - **ScheduledActionName** *(string) --*

                  The name of the scheduled action.

                - **ScheduledActionARN** *(string) --*

                  The Amazon Resource Name (ARN) of the scheduled action.

                - **ServiceNamespace** *(string) --*

                  The namespace of the AWS service that provides the resource or ``custom-resource``
                  for a resource provided by your own application or service. For more information,
                  see `AWS Service Namespaces
                  <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
                  in the *Amazon Web Services General Reference* .

                - **Schedule** *(string) --*

                  The schedule for this action. The following formats are supported:

                  * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

                  * Rate expressions - "``rate(*value*  *unit* )`` "

                  * Cron expressions - "``cron(*fields* )`` "

                  At expressions are useful for one-time schedules. Specify the time, in UTC.

                  For rate expressions, *value* is a positive integer and *unit* is ``minute``
                  |
                  ``minutes`` | ``hour`` | ``hours`` | ``day`` | ``days`` .

                  For more information about cron expressions, see `Cron Expressions
                  <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
                  in the *Amazon CloudWatch Events User Guide* .

                - **ResourceId** *(string) --*

                  The identifier of the resource associated with the scaling policy. This string
                  consists of the resource type and unique identifier.

                  * ECS service - The resource type is ``service`` and the unique identifier is the
                  cluster name and service name. Example: ``service/default/sample-webapp`` .

                  * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
                  identifier is the Spot Fleet request ID. Example:
                  ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

                  * EMR cluster - The resource type is ``instancegroup`` and the unique identifier
                  is the cluster ID and instance group ID. Example:
                  ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

                  * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier
                  is the fleet name. Example: ``fleet/sample-fleet`` .

                  * DynamoDB table - The resource type is ``table`` and the unique identifier is the
                  table name. Example: ``table/my-table`` .

                  * DynamoDB global secondary index - The resource type is ``index`` and the unique
                  identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

                  * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier
                  is the cluster name. Example: ``cluster:my-db-cluster`` .

                  * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the
                  unique identifier is the resource ID. Example:
                  ``endpoint/my-end-point/variant/KMeansClustering`` .

                  * Custom resources are not supported with a resource type. This parameter must
                  specify the ``OutputValue`` from the CloudFormation template stack used to access
                  the resources. The unique identifier is defined by the service provider. More
                  information is available in our `GitHub repository
                  <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

                  * Amazon Comprehend document classification endpoint - The resource type and
                  unique identifier are specified using the endpoint ARN. Example:
                  ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE``
                  .

                  * Lambda provisioned concurrency - The resource type is ``function`` and the
                  unique identifier is the function name with a function version or alias name
                  suffix that is not ``$LATEST`` . Example: ``function:my-function:prod`` or
                  ``function:my-function:1`` .

                - **ScalableDimension** *(string) --*

                  The scalable dimension. This string consists of the service namespace, resource
                  type, and scaling property.

                  * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

                  * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet
                  request.

                  * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR
                  Instance Group.

                  * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0
                  fleet.

                  * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB table.

                  * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB table.

                  * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a
                  DynamoDB global secondary index.

                  * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a
                  DynamoDB global secondary index.

                  * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB
                  cluster. Available for Aurora MySQL-compatible edition and Aurora
                  PostgreSQL-compatible edition.

                  * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an
                  Amazon SageMaker model endpoint variant.

                  * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom
                  resource provided by your own application or service.

                  * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number
                  of inference units for an Amazon Comprehend document classification endpoint.

                  * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a
                  Lambda function.

                - **StartTime** *(datetime) --*

                  The date and time that the action is scheduled to begin.

                - **EndTime** *(datetime) --*

                  The date and time that the action is scheduled to end.

                - **ScalableTargetAction** *(dict) --*

                  The new minimum and maximum capacity. You can set both values or just one. During
                  the scheduled time, if the current capacity is below the minimum capacity,
                  Application Auto Scaling scales out to the minimum capacity. If the current
                  capacity is above the maximum capacity, Application Auto Scaling scales in to the
                  maximum capacity.

                  - **MinCapacity** *(integer) --*

                    The minimum capacity.

                  - **MaxCapacity** *(integer) --*

                    The maximum capacity.

                - **CreationTime** *(datetime) --*

                  The date and time that the scheduled action was created.

            - **NextToken** *(string) --*

              The token required to get the next set of results. This value is ``null`` if there are
              no more results to return.
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
    def put_scaling_policy(
        self,
        PolicyName: str,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        PolicyType: Literal["StepScaling", "TargetTrackingScaling"] = None,
        StepScalingPolicyConfiguration: ClientPutScalingPolicyStepScalingPolicyConfigurationTypeDef = None,
        TargetTrackingScalingPolicyConfiguration: ClientPutScalingPolicyTargetTrackingScalingPolicyConfigurationTypeDef = None,
    ) -> ClientPutScalingPolicyResponseTypeDef:
        """
        Creates or updates a policy for an Application Auto Scaling scalable target.

        Each scalable target is identified by a service namespace, resource ID, and scalable
        dimension. A scaling policy applies to the scalable target identified by those three
        attributes. You cannot create a scaling policy until you have registered the resource as a
        scalable target using  RegisterScalableTarget .

        To update a policy, specify its policy name and the parameters that you want to change. Any
        parameters that you don't specify are not changed by this update request.

        You can view the scaling policies for a service namespace using  DescribeScalingPolicies .
        If you are no longer using a scaling policy, you can delete it using  DeleteScalingPolicy .

        Multiple scaling policies can be in force at the same time for the same scalable target. You
        can have one or more target tracking scaling policies, one or more step scaling policies, or
        both. However, there is a chance that multiple policies could conflict, instructing the
        scalable target to scale out or in at the same time. Application Auto Scaling gives
        precedence to the policy that provides the largest capacity for both scale out and scale in.
        For example, if one policy increases capacity by 3, another policy increases capacity by 200
        percent, and the current capacity is 10, Application Auto Scaling uses the policy with the
        highest calculated capacity (200% of 10 = 20) and scales out to 30.

        Learn more about how to work with scaling policies in the `Application Auto Scaling User
        Guide
        <https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/PutScalingPolicy>`_

        **Request Syntax**
        ::

          response = client.put_scaling_policy(
              PolicyName='string',
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              PolicyType='StepScaling'|'TargetTrackingScaling',
              StepScalingPolicyConfiguration={
                  'AdjustmentType': 'ChangeInCapacity'|'PercentChangeInCapacity'|'ExactCapacity',
                  'StepAdjustments': [
                      {
                          'MetricIntervalLowerBound': 123.0,
                          'MetricIntervalUpperBound': 123.0,
                          'ScalingAdjustment': 123
                      },
                  ],
                  'MinAdjustmentMagnitude': 123,
                  'Cooldown': 123,
                  'MetricAggregationType': 'Average'|'Minimum'|'Maximum'
              },
              TargetTrackingScalingPolicyConfiguration={
                  'TargetValue': 123.0,
                  'PredefinedMetricSpecification': {
                      'PredefinedMetricType':
                      'DynamoDBReadCapacityUtilization'
                      |'DynamoDBWriteCapacityUtilization'|'ALBRequestCountPerTarget'
                      |'RDSReaderAverageCPUUtilization'
                      |'RDSReaderAverageDatabaseConnections'
                      |'EC2SpotFleetRequestAverageCPUUtilization'
                      |'EC2SpotFleetRequestAverageNetworkIn'
                      |'EC2SpotFleetRequestAverageNetworkOut'
                      |'SageMakerVariantInvocationsPerInstance'
                      |'ECSServiceAverageCPUUtilization'
                      |'ECSServiceAverageMemoryUtilization'
                      |'AppStreamAverageCapacityUtilization'
                      |'ComprehendInferenceUtilization'
                      |'LambdaProvisionedConcurrencyUtilization',
                      'ResourceLabel': 'string'
                  },
                  'CustomizedMetricSpecification': {
                      'MetricName': 'string',
                      'Namespace': 'string',
                      'Dimensions': [
                          {
                              'Name': 'string',
                              'Value': 'string'
                          },
                      ],
                      'Statistic': 'Average'|'Minimum'|'Maximum'|'SampleCount'|'Sum',
                      'Unit': 'string'
                  },
                  'ScaleOutCooldown': 123,
                  'ScaleInCooldown': 123,
                  'DisableScaleIn': True|False
              }
          )
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The name of the scaling policy.

        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource associated with the scaling policy. This string consists of
          the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type PolicyType: string
        :param PolicyType:

          The policy type. This parameter is required if you are creating a scaling policy.

          The following policy types are supported:

           ``TargetTrackingScaling`` —Not supported for Amazon EMR

           ``StepScaling`` —Not supported for DynamoDB, Amazon Comprehend, or AWS Lambda

          For more information, see `Target Tracking Scaling Policies
          <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html>`__
          and `Step Scaling Policies
          <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html>`__
          in the *Application Auto Scaling User Guide* .

        :type StepScalingPolicyConfiguration: dict
        :param StepScalingPolicyConfiguration:

          A step scaling policy.

          This parameter is required if you are creating a policy and the policy type is
          ``StepScaling`` .

          - **AdjustmentType** *(string) --*

            Specifies whether the ``ScalingAdjustment`` value in a  StepAdjustment is an absolute
            number or a percentage of the current capacity.

          - **StepAdjustments** *(list) --*

            A set of adjustments that enable you to scale based on the size of the alarm breach.

            - *(dict) --*

              Represents a step adjustment for a  StepScalingPolicyConfiguration . Describes an
              adjustment based on the difference between the value of the aggregated CloudWatch
              metric and the breach threshold that you've defined for the alarm.

              For the following examples, suppose that you have an alarm with a breach threshold of
              50:

              * To trigger the adjustment when the metric is greater than or equal to 50 and less
              than 60, specify a lower bound of 0 and an upper bound of 10.

              * To trigger the adjustment when the metric is greater than 40 and less than or equal
              to 50, specify a lower bound of -10 and an upper bound of 0.

              There are a few rules for the step adjustments for your step policy:

              * The ranges of your step adjustments can't overlap or have a gap.

              * At most one step adjustment can have a null lower bound. If one step adjustment has
              a negative lower bound, then there must be a step adjustment with a null lower bound.

              * At most one step adjustment can have a null upper bound. If one step adjustment has
              a positive upper bound, then there must be a step adjustment with a null upper bound.

              * The upper and lower bound can't be null in the same step adjustment.

              - **MetricIntervalLowerBound** *(float) --*

                The lower bound for the difference between the alarm threshold and the CloudWatch
                metric. If the metric value is above the breach threshold, the lower bound is
                inclusive (the metric must be greater than or equal to the threshold plus the lower
                bound). Otherwise, it is exclusive (the metric must be greater than the threshold
                plus the lower bound). A null value indicates negative infinity.

              - **MetricIntervalUpperBound** *(float) --*

                The upper bound for the difference between the alarm threshold and the CloudWatch
                metric. If the metric value is above the breach threshold, the upper bound is
                exclusive (the metric must be less than the threshold plus the upper bound).
                Otherwise, it is inclusive (the metric must be less than or equal to the threshold
                plus the upper bound). A null value indicates positive infinity.

                The upper bound must be greater than the lower bound.

              - **ScalingAdjustment** *(integer) --* **[REQUIRED]**

                The amount by which to scale, based on the specified adjustment type. A positive
                value adds to the current scalable dimension while a negative number removes from
                the current scalable dimension.

          - **MinAdjustmentMagnitude** *(integer) --*

            The minimum number to adjust your scalable dimension as a result of a scaling activity.
            If the adjustment type is ``PercentChangeInCapacity`` , the scaling policy changes the
            scalable dimension of the scalable target by this amount.

            For example, suppose that you create a step scaling policy to scale out an Amazon ECS
            service by 25 percent and you specify a ``MinAdjustmentMagnitude`` of 2. If the service
            has 4 tasks and the scaling policy is performed, 25 percent of 4 is 1. However, because
            you specified a ``MinAdjustmentMagnitude`` of 2, Application Auto Scaling scales out the
            service by 2 tasks.

          - **Cooldown** *(integer) --*

            The amount of time, in seconds, after a scaling activity completes where previous
            trigger-related scaling activities can influence future scaling events.

            For scale-out policies, while the cooldown period is in effect, the capacity that has
            been added by the previous scale-out event that initiated the cooldown is calculated as
            part of the desired capacity for the next scale out. The intention is to continuously
            (but not excessively) scale out. For example, an alarm triggers a step scaling policy to
            scale out an Amazon ECS service by 2 tasks, the scaling activity completes successfully,
            and a cooldown period of 5 minutes starts. During the cooldown period, if the alarm
            triggers the same policy again but at a more aggressive step adjustment to scale out the
            service by 3 tasks, the 2 tasks that were added in the previous scale-out event are
            considered part of that capacity and only 1 additional task is added to the desired
            count.

            For scale-in policies, the cooldown period is used to block subsequent scale-in requests
            until it has expired. The intention is to scale in conservatively to protect your
            application's availability. However, if another alarm triggers a scale-out policy during
            the cooldown period after a scale-in, Application Auto Scaling scales out your scalable
            target immediately.

          - **MetricAggregationType** *(string) --*

            The aggregation type for the CloudWatch metrics. Valid values are ``Minimum`` ,
            ``Maximum`` , and ``Average`` . If the aggregation type is null, the value is treated as
            ``Average`` .

        :type TargetTrackingScalingPolicyConfiguration: dict
        :param TargetTrackingScalingPolicyConfiguration:

          A target tracking scaling policy. Includes support for predefined or customized metrics.

          This parameter is required if you are creating a policy and the policy type is
          ``TargetTrackingScaling`` .

          - **TargetValue** *(float) --* **[REQUIRED]**

            The target value for the metric. The range is 8.515920e-109 to 1.174271e+108 (Base 10)
            or 2e-360 to 2e360 (Base 2).

          - **PredefinedMetricSpecification** *(dict) --*

            A predefined metric. You can specify either a predefined metric or a customized metric.

            - **PredefinedMetricType** *(string) --* **[REQUIRED]**

              The metric type. The ``ALBRequestCountPerTarget`` metric type applies only to Spot
              Fleet requests and ECS services.

            - **ResourceLabel** *(string) --*

              Identifies the resource associated with the metric type. You can't specify a resource
              label unless the metric type is ``ALBRequestCountPerTarget`` and there is a target
              group attached to the Spot Fleet request or ECS service.

              The format is
              app/<load-balancer-name>/<load-balancer-id>/targetgroup/<target-group-name>/<target-group-id>,
              where:

              * app/<load-balancer-name>/<load-balancer-id> is the final portion of the load
              balancer ARN

              * targetgroup/<target-group-name>/<target-group-id> is the final portion of the target
              group ARN.

          - **CustomizedMetricSpecification** *(dict) --*

            A customized metric. You can specify either a predefined metric or a customized metric.

            - **MetricName** *(string) --* **[REQUIRED]**

              The name of the metric.

            - **Namespace** *(string) --* **[REQUIRED]**

              The namespace of the metric.

            - **Dimensions** *(list) --*

              The dimensions of the metric.

              Conditional: If you published your metric with dimensions, you must specify the same
              dimensions in your scaling policy.

              - *(dict) --*

                Describes the dimension names and values associated with a metric.

                - **Name** *(string) --* **[REQUIRED]**

                  The name of the dimension.

                - **Value** *(string) --* **[REQUIRED]**

                  The value of the dimension.

            - **Statistic** *(string) --* **[REQUIRED]**

              The statistic of the metric.

            - **Unit** *(string) --*

              The unit of the metric.

          - **ScaleOutCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-out activity completes before another
            scale-out activity can start.

            While the cooldown period is in effect, the capacity that has been added by the previous
            scale-out event that initiated the cooldown is calculated as part of the desired
            capacity for the next scale out. The intention is to continuously (but not excessively)
            scale out.

          - **ScaleInCooldown** *(integer) --*

            The amount of time, in seconds, after a scale-in activity completes before another scale
            in activity can start.

            The cooldown period is used to block subsequent scale-in requests until it has expired.
            The intention is to scale in conservatively to protect your application's availability.
            However, if another alarm triggers a scale-out policy during the cooldown period after a
            scale-in, Application Auto Scaling scales out your scalable target immediately.

          - **DisableScaleIn** *(boolean) --*

            Indicates whether scale in by the target tracking scaling policy is disabled. If the
            value is ``true`` , scale in is disabled and the target tracking scaling policy won't
            remove capacity from the scalable resource. Otherwise, scale in is enabled and the
            target tracking scaling policy can remove capacity from the scalable resource. The
            default value is ``false`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyARN': 'string',
                'Alarms': [
                    {
                        'AlarmName': 'string',
                        'AlarmARN': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyARN** *(string) --*

              The Amazon Resource Name (ARN) of the resulting scaling policy.

            - **Alarms** *(list) --*

              The CloudWatch alarms created for the target tracking scaling policy.

              - *(dict) --*

                Represents a CloudWatch alarm associated with a scaling policy.

                - **AlarmName** *(string) --*

                  The name of the alarm.

                - **AlarmARN** *(string) --*

                  The Amazon Resource Name (ARN) of the alarm.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_scheduled_action(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ScheduledActionName: str,
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        Schedule: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        ScalableTargetAction: ClientPutScheduledActionScalableTargetActionTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Creates or updates a scheduled action for an Application Auto Scaling scalable target.

        Each scalable target is identified by a service namespace, resource ID, and scalable
        dimension. A scheduled action applies to the scalable target identified by those three
        attributes. You cannot create a scheduled action until you have registered the resource as a
        scalable target using  RegisterScalableTarget .

        To update an action, specify its name and the parameters that you want to change. If you
        don't specify start and end times, the old values are deleted. Any other parameters that you
        don't specify are not changed by this update request.

        You can view the scheduled actions using  DescribeScheduledActions . If you are no longer
        using a scheduled action, you can delete it using  DeleteScheduledAction .

        Learn more about how to work with scheduled actions in the `Application Auto Scaling User
        Guide
        <https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/PutScheduledAction>`_

        **Request Syntax**
        ::

          response = client.put_scheduled_action(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              Schedule='string',
              ScheduledActionName='string',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              ScalableTargetAction={
                  'MinCapacity': 123,
                  'MaxCapacity': 123
              }
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type Schedule: string
        :param Schedule:

          The schedule for this action. The following formats are supported:

          * At expressions - "``at(*yyyy* -*mm* -*dd* T*hh* :*mm* :*ss* )`` "

          * Rate expressions - "``rate(*value*  *unit* )`` "

          * Cron expressions - "``cron(*fields* )`` "

          At expressions are useful for one-time schedules. Specify the time, in UTC.

          For rate expressions, *value* is a positive integer and *unit* is ``minute``
          | ``minutes``
          | ``hour`` | ``hours`` | ``day`` | ``days`` .

          For more information about cron expressions, see `Cron Expressions
          <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions>`__
          in the *Amazon CloudWatch Events User Guide* .

        :type ScheduledActionName: string
        :param ScheduledActionName: **[REQUIRED]**

          The name of the scheduled action.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource associated with the scheduled action. This string consists
          of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension. This string consists of the service namespace, resource type, and
          scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type StartTime: datetime
        :param StartTime:

          The date and time for the scheduled action to start.

        :type EndTime: datetime
        :param EndTime:

          The date and time for the scheduled action to end.

        :type ScalableTargetAction: dict
        :param ScalableTargetAction:

          The new minimum and maximum capacity. You can set both values or just one. During the
          scheduled time, if the current capacity is below the minimum capacity, Application Auto
          Scaling scales out to the minimum capacity. If the current capacity is above the maximum
          capacity, Application Auto Scaling scales in to the maximum capacity.

          - **MinCapacity** *(integer) --*

            The minimum capacity.

          - **MaxCapacity** *(integer) --*

            The maximum capacity.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_scalable_target(
        self,
        ServiceNamespace: Literal[
            "ecs",
            "elasticmapreduce",
            "ec2",
            "appstream",
            "dynamodb",
            "rds",
            "sagemaker",
            "custom-resource",
            "comprehend",
            "lambda",
        ],
        ResourceId: str,
        ScalableDimension: Literal[
            "ecs:service:DesiredCount",
            "ec2:spot-fleet-request:TargetCapacity",
            "elasticmapreduce:instancegroup:InstanceCount",
            "appstream:fleet:DesiredCapacity",
            "dynamodb:table:ReadCapacityUnits",
            "dynamodb:table:WriteCapacityUnits",
            "dynamodb:index:ReadCapacityUnits",
            "dynamodb:index:WriteCapacityUnits",
            "rds:cluster:ReadReplicaCount",
            "sagemaker:variant:DesiredInstanceCount",
            "custom-resource:ResourceType:Property",
            "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
            "lambda:function:ProvisionedConcurrency",
        ],
        MinCapacity: int = None,
        MaxCapacity: int = None,
        RoleARN: str = None,
        SuspendedState: ClientRegisterScalableTargetSuspendedStateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Registers or updates a scalable target. A scalable target is a resource that Application
        Auto Scaling can scale out and scale in. Scalable targets are uniquely identified by the
        combination of resource ID, scalable dimension, and namespace.

        When you register a new scalable target, you must specify values for minimum and maximum
        capacity. Application Auto Scaling will not scale capacity to values that are outside of
        this range.

        To update a scalable target, specify the parameter that you want to change as well as the
        following parameters that identify the scalable target: resource ID, scalable dimension, and
        namespace. Any parameters that you don't specify are not changed by this update request.

        After you register a scalable target, you do not need to register it again to use other
        Application Auto Scaling operations. To see which resources have been registered, use
        DescribeScalableTargets . You can also view the scaling policies for a service namespace by
        using  DescribeScalableTargets .

        If you no longer need a scalable target, you can deregister it by using
        DeregisterScalableTarget .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/application-autoscaling-2016-02-06/RegisterScalableTarget>`_

        **Request Syntax**
        ::

          response = client.register_scalable_target(
              ServiceNamespace=
                  'ecs'|'elasticmapreduce'|'ec2'|'appstream'|'dynamodb'|'rds'|'sagemaker'
                  |'custom-resource'|'comprehend'|'lambda',
              ResourceId='string',
              ScalableDimension=
                  'ecs:service:DesiredCount'|'ec2:spot-fleet-request:TargetCapacity'
                  |'elasticmapreduce:instancegroup:InstanceCount'|'appstream:fleet:DesiredCapacity'
                  |'dynamodb:table:ReadCapacityUnits'|'dynamodb:table:WriteCapacityUnits'
                  |'dynamodb:index:ReadCapacityUnits'|'dynamodb:index:WriteCapacityUnits'
                  |'rds:cluster:ReadReplicaCount'|'sagemaker:variant:DesiredInstanceCount'
                  |'custom-resource:ResourceType:Property'
                  |'comprehend:document-classifier-endpoint:DesiredInferenceUnits'
                  |'lambda:function:ProvisionedConcurrency',
              MinCapacity=123,
              MaxCapacity=123,
              RoleARN='string',
              SuspendedState={
                  'DynamicScalingInSuspended': True|False,
                  'DynamicScalingOutSuspended': True|False,
                  'ScheduledScalingSuspended': True|False
              }
          )
        :type ServiceNamespace: string
        :param ServiceNamespace: **[REQUIRED]**

          The namespace of the AWS service that provides the resource or ``custom-resource`` for a
          resource provided by your own application or service. For more information, see `AWS
          Service Namespaces
          <http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces>`__
          in the *Amazon Web Services General Reference* .

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource that is associated with the scalable target. This string
          consists of the resource type and unique identifier.

          * ECS service - The resource type is ``service`` and the unique identifier is the cluster
          name and service name. Example: ``service/default/sample-webapp`` .

          * Spot Fleet request - The resource type is ``spot-fleet-request`` and the unique
          identifier is the Spot Fleet request ID. Example:
          ``spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`` .

          * EMR cluster - The resource type is ``instancegroup`` and the unique identifier is the
          cluster ID and instance group ID. Example:
          ``instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0`` .

          * AppStream 2.0 fleet - The resource type is ``fleet`` and the unique identifier is the
          fleet name. Example: ``fleet/sample-fleet`` .

          * DynamoDB table - The resource type is ``table`` and the unique identifier is the table
          name. Example: ``table/my-table`` .

          * DynamoDB global secondary index - The resource type is ``index`` and the unique
          identifier is the index name. Example: ``table/my-table/index/my-table-index`` .

          * Aurora DB cluster - The resource type is ``cluster`` and the unique identifier is the
          cluster name. Example: ``cluster:my-db-cluster`` .

          * Amazon SageMaker endpoint variant - The resource type is ``variant`` and the unique
          identifier is the resource ID. Example: ``endpoint/my-end-point/variant/KMeansClustering``
          .

          * Custom resources are not supported with a resource type. This parameter must specify the
          ``OutputValue`` from the CloudFormation template stack used to access the resources. The
          unique identifier is defined by the service provider. More information is available in our
          `GitHub repository <https://github.com/aws/aws-auto-scaling-custom-resource>`__ .

          * Amazon Comprehend document classification endpoint - The resource type and unique
          identifier are specified using the endpoint ARN. Example:
          ``arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE`` .

          * Lambda provisioned concurrency - The resource type is ``function`` and the unique
          identifier is the function name with a function version or alias name suffix that is not
          ``$LATEST`` . Example: ``function:my-function:prod`` or ``function:my-function:1`` .

        :type ScalableDimension: string
        :param ScalableDimension: **[REQUIRED]**

          The scalable dimension associated with the scalable target. This string consists of the
          service namespace, resource type, and scaling property.

          * ``ecs:service:DesiredCount`` - The desired task count of an ECS service.

          * ``ec2:spot-fleet-request:TargetCapacity`` - The target capacity of a Spot Fleet request.

          * ``elasticmapreduce:instancegroup:InstanceCount`` - The instance count of an EMR Instance
          Group.

          * ``appstream:fleet:DesiredCapacity`` - The desired capacity of an AppStream 2.0 fleet.

          * ``dynamodb:table:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          table.

          * ``dynamodb:table:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          table.

          * ``dynamodb:index:ReadCapacityUnits`` - The provisioned read capacity for a DynamoDB
          global secondary index.

          * ``dynamodb:index:WriteCapacityUnits`` - The provisioned write capacity for a DynamoDB
          global secondary index.

          * ``rds:cluster:ReadReplicaCount`` - The count of Aurora Replicas in an Aurora DB cluster.
          Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.

          * ``sagemaker:variant:DesiredInstanceCount`` - The number of EC2 instances for an Amazon
          SageMaker model endpoint variant.

          * ``custom-resource:ResourceType:Property`` - The scalable dimension for a custom resource
          provided by your own application or service.

          * ``comprehend:document-classifier-endpoint:DesiredInferenceUnits`` - The number of
          inference units for an Amazon Comprehend document classification endpoint.

          * ``lambda:function:ProvisionedConcurrency`` - The provisioned concurrency for a Lambda
          function.

        :type MinCapacity: integer
        :param MinCapacity:

          The minimum value to scale to in response to a scale-in event. ``MinCapacity`` is required
          to register a scalable target.

        :type MaxCapacity: integer
        :param MaxCapacity:

          The maximum value to scale to in response to a scale-out event. ``MaxCapacity`` is
          required to register a scalable target.

        :type RoleARN: string
        :param RoleARN:

          Application Auto Scaling creates a service-linked role that grants it permissions to
          modify the scalable target on your behalf. For more information, see `Service-Linked Roles
          for Application Auto Scaling
          <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html>`__
          .

          For Amazon EMR, this parameter is required, and it must specify the ARN of an IAM role
          that allows Application Auto Scaling to modify the scalable target on your behalf.

        :type SuspendedState: dict
        :param SuspendedState:

          An embedded object that contains attributes and attribute values that are used to suspend
          and resume automatic scaling. Setting the value of an attribute to ``true`` suspends the
          specified scaling activities. Setting it to ``false`` (default) resumes the specified
          scaling activities.

           **Suspension Outcomes**

          * For ``DynamicScalingInSuspended`` , while a suspension is in effect, all scale-in
          activities that are triggered by a scaling policy are suspended.

          * For ``DynamicScalingOutSuspended`` , while a suspension is in effect, all scale-out
          activities that are triggered by a scaling policy are suspended.

          * For ``ScheduledScalingSuspended`` , while a suspension is in effect, all scaling
          activities that involve scheduled actions are suspended.

          For more information, see `Suspending and Resuming Scaling
          <https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.html>`__
          in the *Application Auto Scaling User Guide* .

          - **DynamicScalingInSuspended** *(boolean) --*

            Whether scale in by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to
            remove capacity when a scaling policy is triggered. The default is ``false`` .

          - **DynamicScalingOutSuspended** *(boolean) --*

            Whether scale out by a target tracking scaling policy or a step scaling policy is
            suspended. Set the value to ``true`` if you don't want Application Auto Scaling to add
            capacity when a scaling policy is triggered. The default is ``false`` .

          - **ScheduledScalingSuspended** *(boolean) --*

            Whether scheduled scaling is suspended. Set the value to ``true`` if you don't want
            Application Auto Scaling to add or remove capacity by initiating scheduled actions. The
            default is ``false`` .

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
        self, operation_name: Literal["describe_scalable_targets"]
    ) -> paginator_scope.DescribeScalableTargetsPaginator:
        """
        Get Paginator for `describe_scalable_targets` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scaling_activities"]
    ) -> paginator_scope.DescribeScalingActivitiesPaginator:
        """
        Get Paginator for `describe_scaling_activities` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scaling_policies"]
    ) -> paginator_scope.DescribeScalingPoliciesPaginator:
        """
        Get Paginator for `describe_scaling_policies` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_actions"]
    ) -> paginator_scope.DescribeScheduledActionsPaginator:
        """
        Get Paginator for `describe_scheduled_actions` operation.
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
    ClientError: Boto3ClientError
    ConcurrentUpdateException: Boto3ClientError
    FailedResourceAccessException: Boto3ClientError
    InternalServiceException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    ObjectNotFoundException: Boto3ClientError
    ValidationException: Boto3ClientError
