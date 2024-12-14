from pydantic import BaseModel

from app.models.agent.identity import Identity
from app.models.agent.expertise import Expertise

class Agent(BaseModel):
    identity: Identity
    expertise: Expertise