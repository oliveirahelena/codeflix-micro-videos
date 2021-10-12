from seedwork.domain import Entity, UUID


class Category(Entity):
    _name: str

    @property
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if name is None or name == "":
            raise ValueError("You must provide a name")
        self._name = name


class NewCategory:
    @classmethod
    def get_category(cls, *args) -> Category:
        if len(args) < 1:
            return Category()
        elif len(args) == 1:
            category = Category()
            if isinstance(args[0], str):
                category.set_id(category._generate_uuid())
                category.set_name(args[0])
            elif isinstance(args[0], UUID):
                category.set_id(args[0])
            return category
        else:
            category = Category()
            category.set_id(args[0])
            category.set_name(args[1])
            return category
