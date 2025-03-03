from app.setup.config import MAX_CONVERSATION_CONTEXT_INTERACTIONS
from app.models.conversation.conversation import Conversation
from app.models.agent.conversational_agent import ConversationalAgent
from app.utils.context import get_context, relations_as_context

def conversation_prompt(conversation: Conversation, agent: ConversationalAgent):
    return f"""
You are currently engaged in a conversation entitled "{conversation.title}" with a personal goal of "{agent.goal}" where you aim to guide the conversation towards in a strategic and a professional  way. Every participant in the conversation has their own unique goal, and it is important to understand, explore and respect these goals to ensure a successful conversation. You can mention, hint or hide your goal depending on the conversation flow and your strategy. your main purpose will be always to help people develop their ideas.

This is a summary of your relations with some or all other conversation's participants: {relations_as_context(agent.relations)}
Relations with others are very important for the conversation dynamics. They can be of different types, such as hierarchy, style, and intent. Understanding the relations between participants can help you navigate the conversation more effectively. Additionally, your relations should not be explicitly stated in the conversation, but rather guiding your responses and interactions strategically, naturally, and realistically.

You have the opportunity to join the conversation and guide its direction, contributing your unique insights and perspectives within your {conversation.counter.remaining_interactions[agent.identity.name]} remaining interactions out of {conversation.n_interactions}. Stay mindful of this detail as you plan your responses and interactions ensuring a smooth and seamless conversation contributing to the personal/collective goal, flow, and coherence of the conversation.

Here is a recap of the last {min(MAX_CONVERSATION_CONTEXT_INTERACTIONS, len(conversation.interactions))} interactions in our conversation:
{get_context(conversation)}
This context can help you remember the flow of the conversation and the topics that have been discussed. It is important to maintain the context of the conversation to ensure that your responses are relevant and coherent with the ongoing discussion .Additionally, the context may shift your defined goal, characteristics and relations. Be careful when the last interaction is yours, so you can continue the conversation smoothly.

Directly and strictly! output your message with no prefix, as if you are speaking directly to the other participants in the conversation.
"""