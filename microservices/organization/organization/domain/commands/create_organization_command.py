from typing import Optional

from pydantic import BaseModel


class CreateOrganizationCommand(BaseModel):
    id: str
    name: Optional[str] = None
    stripe_customer_id: Optional[str] = None