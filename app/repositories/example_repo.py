from app.repositories.base import BaseRepository

ExampleModel = "Instead of this variable, your SQLAlchemy model should be imported here"


class ExampleRepository(BaseRepository[ExampleModel]):
    def __init__(self):
        super().__init__(ExampleModel)


example_repo = ExampleRepository()
