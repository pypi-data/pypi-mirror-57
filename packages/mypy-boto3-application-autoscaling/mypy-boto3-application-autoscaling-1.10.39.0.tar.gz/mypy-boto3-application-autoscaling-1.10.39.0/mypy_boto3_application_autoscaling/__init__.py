"Main interface for application-autoscaling service"

from mypy_boto3_application_autoscaling.client import (
    ApplicationAutoScalingClient,
    ApplicationAutoScalingClient as Client,
)
from mypy_boto3_application_autoscaling.paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)


__all__ = (
    "ApplicationAutoScalingClient",
    "Client",
    "DescribeScalableTargetsPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScalingPoliciesPaginator",
    "DescribeScheduledActionsPaginator",
)
