import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from mbc.domain.model.registry import Registry
from mbc.entrypoints.api.main import app

client = TestClient(app)


class TestRegistryEndpoint(unittest.TestCase):

    @patch('mbc.adapters.dynamodb_query_service.DynamoDBRegistryQueryService.create_registry')
    def test_create_registry(self, mock_create_registry):
        registry = Registry(id="123", name="Test Registry", description="This is a test registry",
                            created_at=1234567890.1234567890)
        mock_create_registry.return_value = registry
        response = client.post("/v1/registry", json={
            "name": "Test Registry",
            "description": "This is a test registry"
        })
        assert response.status_code == 200
        assert Registry(**response.json()) == registry

    @patch('mbc.adapters.dynamodb_query_service.DynamoDBRegistryQueryService.get_registry')
    def test_get_registry(self, mock_get_registry):
        registry = Registry(id="123", name="Test Registry", description="This is a test registry",
                            created_at=1234567890.1234567890)
        mock_get_registry.return_value = registry
        response = client.get("/v1/registry/123")
        assert response.status_code == 200
        assert Registry(**response.json()) == registry

    @patch('mbc.adapters.dynamodb_query_service.DynamoDBRegistryQueryService.update_registry')
    def test_update_registry(self, mock_update_registry):
        registry = Registry(id="123", name="Test Registry", description="This is a test registry",
                            created_at=1234567890.1234567890)
        mock_update_registry.return_value = registry
        response = client.put("/v1/registry/123", json={
            "name": "Test Registry",
            "description": "This is a test registry"
        })
        assert response.status_code == 200
