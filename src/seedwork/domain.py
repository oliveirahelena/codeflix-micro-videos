import uuid

from pydantic import BaseModel, Field

UUID = uuid.UUID
UUID_v4 = uuid.uuid4


class Entity(BaseModel):
    _id: UUID = Field(default_factory=UUID_v4)

    @property
    def get_id(self) -> UUID:
        return self._id

    def set_id(self, id: UUID) -> None:
        if id is None or not self._is_valid_uuid(str(id)):
            raise ValueError("You must provide a valid uuid")
        self._id = id

    def _is_valid_uuid(self, uuid_string) -> bool:
        try:
            UUID(uuid_string, version=4)
            return True
        except ValueError:
            return False

    def _generate_uuid(self) -> UUID:
        return UUID_v4()
