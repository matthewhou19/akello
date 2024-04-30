from typing import Optional

from mbc.adapters.dynamodb_query_service import DynamoDBRegistryQueryService
from mbc.domain.commands.get_user_from_registry_command import GetUserFromRegistryCommand
from mbc.domain.model.registry import RegistryUser


def handle_get_user_from_registry_command(
        command: GetUserFromRegistryCommand,
        patient_query_service: DynamoDBRegistryQueryService,
) -> Optional[RegistryUser]:
    return patient_query_service.get_registry_user(command.registry_id, command.user_id)
