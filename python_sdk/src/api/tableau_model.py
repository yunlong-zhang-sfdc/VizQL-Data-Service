from pydantic import BaseModel, ConfigDict

class TableauModel(BaseModel):
    model_config = ConfigDict(
        extra='forbid',
        populate_by_name=True,
        exclude_none=True,
        exclude_unset=True,
    )
