from uuid import UUID, uuid4
from eventsourcing.application import Application

from karp.domain.resource import Resource


class KarpApplication(Application):
    def get_resource(self, resource_id: UUID):
        raise ResourceNotFound(resource_id)

    def create_resource(self, *, name: str):
        resource = Resource.create(
            name=name,
        )
        return resource.id

    def list_resource(self):
        return []


class ResourceNotFound(Exception):
    pass
