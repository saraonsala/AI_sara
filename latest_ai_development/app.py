import streamlit as st
import yaml
from crew import CrewBase, agent, crew, task    # Importerar dekoreringsfunktionerna från crew.py
 # Importerar Config-klassen från config.py
import yaml

agents = yaml.safe_load(open("agents.yaml", "r"))

# Now you can use the `agents` variable which contains the data from the YAML file
# Läs YAML-filen
try:
    with open('agents.yaml', 'r') as file:
        agents = yaml.safe_load(file)
    st.write("YAML file loaded successfully.")
except Exception as e:
    st.error(f"Error loading YAML file: {e}")

# Funktion för att visa agentinformation
def show_agent_info(agent_name, agent_info):
    st.header(agent_name.capitalize())
    st.subheader("Role")
    st.text(agent_info['role'].format(topic="AI"))
    st.subheader("Goal")
    st.text(agent_info['goal'].format(topic="AI"))
    st.subheader("Backstory")
    st.text(agent_info['backstory'].format(topic="AI"))

# Streamlit-app
st.title("Agent Information")

if agent:
    for agent_name, agent_info in agents.items():
        show_agent_info(agent_name, agent_info)
else:
    st.error("No agents found in the YAML file.")