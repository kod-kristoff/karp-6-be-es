from uuid import uuid4

from eventsourcing.domain.model.aggregate import AggregateRoot


class Resource(AggregateRoot):
    @classmethod
    def create(cls):
        return cls.__create__(
            event_class=cls.Created,
            id=uuid4(),
        )
