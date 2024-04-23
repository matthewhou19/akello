from typing import Optional

from mypy_boto3_dynamodb import client

from user.domain.model.user import User
from user.domain.ports.inbound import user_query_service


class DynamoDBOrganizationQueryService(user_query_service.UserQueryService):

    def __init__(self, table_name: str, dynamodb_client: client.DynamoDBClient):
        self._table_name = table_name
        self._dynamodb_client = dynamodb_client

    def get(self, user_id: str) -> Optional[User]:
        """Gets a user from the DynamoDB table."""

        resp = self._dynamodb_client.get_item(
            TableName=self._table_name,
            Key={
                'partition_key': user_id,
                'sort_key': 'meta'
            }
        )

        if 'Item' in resp:
            return User.parse_obj(resp['Item'])

    def create(self, user: User) -> None:
        self._dynamodb_client.put_item(
            TableName=self._table_name,
            Item={
                'partition_key': user.id,
                'sort_key': 'meta',
                **user.dict()
            }
        )

    def set(self, user: User) -> None:
        self._dynamodb_client.put_item(
            TableName=self._table_name,
            Item={
                'partition_key': user.id,
                'sort_key': 'meta',
                **user.dict()
            }
        )