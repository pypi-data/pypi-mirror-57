"Helper functions for pinpoint-email service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_pinpoint_email.client import Client
from mypy_boto3_pinpoint_email.paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)

# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def boto3_client(
    session: Session = None,
    region_name: str = None,
    api_version: str = None,
    use_ssl: bool = None,
    verify: Union[str, bool] = None,
    endpoint_url: str = None,
    aws_access_key_id: str = None,
    aws_secret_access_key: str = None,
    aws_session_token: str = None,
    config: Config = None,
) -> Client:
    """
    Equivalent of `boto3.client('pinpoint-email')`, returns a correct type.
    """
    kwargs: Dict[str, Any] = {}
    if region_name is not None:
        kwargs["region_name"] = region_name
    if api_version is not None:
        kwargs["api_version"] = api_version
    if use_ssl is not None:
        kwargs["use_ssl"] = use_ssl
    if verify is not None:
        kwargs["verify"] = verify
    if endpoint_url is not None:
        kwargs["endpoint_url"] = endpoint_url
    if aws_access_key_id is not None:
        kwargs["aws_access_key_id"] = aws_access_key_id
    if aws_secret_access_key is not None:
        kwargs["aws_secret_access_key"] = aws_secret_access_key
    if aws_session_token is not None:
        kwargs["aws_session_token"] = aws_session_token
    if config is not None:
        kwargs["config"] = config
    if session is not None:
        return session.client("pinpoint-email", **kwargs)
    return boto3.client("pinpoint-email", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_dedicated_ips_paginator(client: Client) -> GetDedicatedIpsPaginator:
    """
    Equivalent of `client.get_paginator('get_dedicated_ips')`, returns a correct type.
    """
    return client.get_paginator("get_dedicated_ips")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_configuration_sets_paginator(client: Client) -> ListConfigurationSetsPaginator:
    """
    Equivalent of `client.get_paginator('list_configuration_sets')`, returns a correct type.
    """
    return client.get_paginator("list_configuration_sets")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_dedicated_ip_pools_paginator(client: Client) -> ListDedicatedIpPoolsPaginator:
    """
    Equivalent of `client.get_paginator('list_dedicated_ip_pools')`, returns a correct type.
    """
    return client.get_paginator("list_dedicated_ip_pools")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_deliverability_test_reports_paginator(
    client: Client,
) -> ListDeliverabilityTestReportsPaginator:
    """
    Equivalent of `client.get_paginator('list_deliverability_test_reports')`, returns a correct
    type.
    """
    return client.get_paginator("list_deliverability_test_reports")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_email_identities_paginator(client: Client) -> ListEmailIdentitiesPaginator:
    """
    Equivalent of `client.get_paginator('list_email_identities')`, returns a correct type.
    """
    return client.get_paginator("list_email_identities")
