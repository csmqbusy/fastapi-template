from sqlalchemy.orm import Mapped, mapped_column


class IdIntPKMixin(object):
    id: Mapped[int] = mapped_column(primary_key=True)
