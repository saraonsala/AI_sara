import streamlit as st
import yaml

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

if agents:
    for agent_name, agent_info in agents.items():
        show_agent_info(agent_name, agent_info)
else:
    st.error("No agents found in the YAML file.")