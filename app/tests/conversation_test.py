from app.services.conversation_service import initialize_conversation, run_conversation
from app.utils.record import save_conversation

from app.data.relation import rh, docs
from app.data import finance

topic = "register commerce"
# agents = [ceo, business, it, design]
agents = [docs, rh]

conversation = initialize_conversation(agents)
run_conversation(conversation)
save_conversation(conversation, topic)