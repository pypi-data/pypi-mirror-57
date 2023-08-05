"Helper functions for es service"

from typing import Any, Dict, Union
import boto3
from boto3.session import Session
from botocore.config import Config
from mypy_boto3_es.client import Client
from mypy_boto3_es.paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
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
    Equivalent of `boto3.client('es')`, returns a correct type.
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
        return session.client("es", **kwargs)
    return boto3.client("es", **kwargs)


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_elasticsearch_instance_offerings_paginator(
    client: Client,
) -> DescribeReservedElasticsearchInstanceOfferingsPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_elasticsearch_instance_offerings')`,
    returns a correct type.
    """
    return client.get_paginator("describe_reserved_elasticsearch_instance_offerings")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_describe_reserved_elasticsearch_instances_paginator(
    client: Client,
) -> DescribeReservedElasticsearchInstancesPaginator:
    """
    Equivalent of `client.get_paginator('describe_reserved_elasticsearch_instances')`, returns a
    correct type.
    """
    return client.get_paginator("describe_reserved_elasticsearch_instances")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_get_upgrade_history_paginator(client: Client) -> GetUpgradeHistoryPaginator:
    """
    Equivalent of `client.get_paginator('get_upgrade_history')`, returns a correct type.
    """
    return client.get_paginator("get_upgrade_history")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_elasticsearch_instance_types_paginator(
    client: Client,
) -> ListElasticsearchInstanceTypesPaginator:
    """
    Equivalent of `client.get_paginator('list_elasticsearch_instance_types')`, returns a correct
    type.
    """
    return client.get_paginator("list_elasticsearch_instance_types")


# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
def get_list_elasticsearch_versions_paginator(client: Client) -> ListElasticsearchVersionsPaginator:
    """
    Equivalent of `client.get_paginator('list_elasticsearch_versions')`, returns a correct type.
    """
    return client.get_paginator("list_elasticsearch_versions")
