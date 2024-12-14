from app.data.agents import marketing, it, finance, rh, docs

from app.models.agent.conversational_agent import ConversationalAgent

from app.models.relation.relation import Relation, Hierarchy, Style, Intent

marketing = ConversationalAgent(**marketing.model_dump(), relations=[
    Relation(
        other=rh,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    ),
    Relation(
        other=it,
        hierarchy=Hierarchy.mentorship,
        style=Style.professional,
        intent=Intent.cooperative
    ),
    Relation(
        other=finance,
        hierarchy=Hierarchy.mentorship,
        style=Style.professional,
        intent=Intent.cooperative
    ),
], goal="Brainstorm innovative ideas based on the user startup's idea.")

finance = ConversationalAgent(**finance.model_dump(), relations=[
    Relation(
        other=marketing,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    )
], goal="Help the user's startup with business strategies and opportunities for the startup's next steps.")

it = ConversationalAgent(**it.model_dump(), relations=[
    Relation(
        other=marketing,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    ), 
    Relation(
        other=finance,
        hierarchy=Hierarchy.partnership,
        style=Style.neutral,
        intent=Intent.cooperative
    ), 
], goal="Help with the technical aspects concerning any suggestions about the startup next project and how to implement them.")

rh = ConversationalAgent(**rh.model_dump(), relations=[
    Relation(
        other=rh,
        hierarchy=Hierarchy.mentorship,
        style=Style.professional,
        intent=Intent.cooperative
    ), 
    Relation(
        other=it,
        hierarchy=Hierarchy.unknown,
        style=Style.neutral,
        intent=Intent.cooperative
    ), 
    Relation(
        other=finance,
        hierarchy=Hierarchy.mentorship,
        style=Style.friendly,
        intent=Intent.cooperative
    ),
], goal="Deliver the most creative and out-of-the-box ideas for the startup's next project steps")

docs = ConversationalAgent(**docs.model_dump(), relations=[
    Relation(
        other= rh,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    )
    ],
    goal="Help the user knows which Commerce Register to create(based on the theme, each theme has its own register code), and then help him with all the documents he needs in order to create the register"
)