try:
    # pylint: disable=wildcard-import, unused-wildcard-import
    from mypy_boto3_dynamodb.client import *
except ImportError:
    raise ImportError("Install boto3-stubs[dynamodb] to use dynamodb Client annotations")
