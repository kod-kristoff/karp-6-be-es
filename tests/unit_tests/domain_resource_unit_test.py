from eventsourcing.domain import Aggregate
from karp.domain.resource import Resource


def test_resource_is_aggregate():
    resource = Resource.create()

    assert isinstance(resource, Resource)
    assert isinstance(resource, Aggregate)
