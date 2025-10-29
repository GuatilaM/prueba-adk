from google.adk.agents.llm_agent import Agent
from google.adk.agents import ParallelAgent

from agente_prueba.utils import leer_instrucciones

normal_agent = Agent(
    model='gemini-2.5-flash',
    name='normal_agent',
    description='Un asistente presto a ayudar e informar con datos ambientales de Bogotá',
    instruction=leer_instrucciones(),
)

emoji_agent = Agent(
    model='gemini-2.5-flash',
    name='EmojiInterpretingAgent',
    description='Recibe la solicitud del usuario y retorna una interpretación con sólo emojis',
    instruction=leer_instrucciones("ins_emoji_agent.txt"),
)

parallel_agent = ParallelAgent(
    name='ParallelInstructionAgent',
    description='Corre múltiples agentes en paralelo.',
    sub_agents=[normal_agent, emoji_agent],
)

# pendiente un agente integrador

root_agent = parallel_agent