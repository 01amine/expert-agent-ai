from app.models.agent.agent import Agent
from app.models.agent.identity import Identity
from app.models.agent.expertise import Expertise, Level


from app.utils.record import save_agent

marketing = Agent(
    identity=Identity(name="marketing"),
    expertise=Expertise(
        domain="Marketing",
        subdomains=["Digital Marketing", "Social Media Content Management"],
        level=Level.expert,
        thinking_process="Opportunist"
    )
)

it = Agent(
    identity=Identity(name="it"),
    expertise=Expertise(
        domain="Information Technology",
        subdomains=["Software Engineering", "Big Tech Companies","Algerian Tech","Algerian Tech Company"],
        level=Level.proficient,
        thinking_process="Problem-solving"
    )
)

finance = Agent(
    identity=Identity(name="finance"),
    expertise=Expertise(
        domain="Financial Consulting",
        subdomains=["Market Research", "Financial Analysis","Currency Risks","Investments"],
        level=Level.expert,
        thinking_process="Analytical"
    )
)

rh = Agent(
    identity=Identity(name="rh"),
    expertise=Expertise(
        domain="Human Resources",
        subdomains=["Human Resources", "Managing Employees","Interviewing Employees","Management"],
        level=Level.proficient,
        thinking_process="Strategic Thinking & Planning Skills"
    )
)
docs = Agent(
    identity=Identity(name="docs"),
    expertise=Expertise(
        domain="Documentation",
        subdomains=["Documentation", "Documentation Management","Documentation Creation","Documentation Review"],
        level=Level.expert,
        thinking_process="Strategic Thinking & Planning Skills"
))

save_agent(marketing, "brainstorming")
save_agent(it, "brainstorming")
save_agent(finance, "brainstorming")
save_agent(rh, "brainstorming")
save_agent(docs,"documents regulation")