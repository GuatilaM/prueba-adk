from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Un asistente presto a ayudar e informar con datos ambientales de Bogotá',
    instruction='Responder las preguntas y solicitudes de los usuarios sobre datos ambientales dentro de las posibilidades de tu conocimiento',
)
