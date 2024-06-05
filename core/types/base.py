from pydantic import BaseModel, ConfigDict


class DTO(BaseModel):
    """
    Base pydantic schema
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        from_attributes=True,
        extra="ignore",
    )
