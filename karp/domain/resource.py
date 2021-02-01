from uuid import uuid4

from eventsourcing.domain import Aggregate


class Resource(Aggregate):
    @classmethod
    def create(cls):
        return cls._create_(
            event_class=cls.Created,
            id=uuid4(),
        )
