from uuid import UUID
from eventsourcing.application import Application


class KarpApplication(Application):
    def get_resource(self, resource_id: UUID):
        raise ResourceNotFound(resource_id)

    def create_resource(self, *, name: str):
        pass


class ResourceNotFound(Exception):
    pass
