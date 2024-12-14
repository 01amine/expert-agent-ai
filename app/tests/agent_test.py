from app.data.agents import marketing, finance
from app.services.agent_service import generate_single_interaction_response
from app.utils.record import save_interaction

prompt = "What is the best marketing strategy for my startup based on my financial budget?"

alex_response = generate_single_interaction_response(marketing, prompt)
save_interaction(marketing, prompt, alex_response)

sarah_response = generate_single_interaction_response(finance, prompt)
save_interaction(finance, prompt, sarah_response)