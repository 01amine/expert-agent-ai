from app.services.llm_service import generate_response_text

prompt = "im thinking about starting a tech startup, what do you think?"

response = generate_response_text(prompt)
print(response)