"Main interface for sqs service"

from mypy_boto3_sqs.client import Client
from mypy_boto3_sqs.service_resource import ServiceResource


__all__ = ("Client", "ServiceResource")
