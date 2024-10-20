import streamlit as st
import yaml

# Läs YAML-filen
with open('agents.yaml', 'r') as file:
    agents = yaml.safe_load(file)

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

for agent_name, agent_info in agents.items():
    show_agent_info(agent_name, agent_info)