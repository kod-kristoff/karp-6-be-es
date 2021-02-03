from dataclasses import dataclass
from uuid import uuid4

from eventsourcing.domain import Aggregate


class Resource(Aggregate):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    @classmethod
    def create(cls, name: str):
        return cls._create_(
            event_class=cls.Created,
            id=uuid4(),
            name=name,
        )

    @dataclass(frozen=True)
    class Created(Aggregate.Created):
        name: str
