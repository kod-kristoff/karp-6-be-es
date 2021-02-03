from uuid import UUID, uuid4

import pytest

from karp.application import KarpApplication, ResourceNotFound


def test_karp_application():
    app = KarpApplication()

    with pytest.raises(ResourceNotFound):
        app.get_resource(uuid4())

    # Create a resource
    resource_id1 = app.create_resource(name="Saldo")

    assert isinstance(resource_id1, UUID)

    assert resource_id1 in app.list_resource()
