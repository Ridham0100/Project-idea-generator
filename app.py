import streamlit as st
from project_ideas import project_idea_generator
import os


st.title("Project idea Generator")
idea = st.sidebar.selectbox("Select your Domain:", ("Medical", "Finance", "Entertainment", "Gaming", "Automobile", "Education", "Retail", "Agriculture", "E-commerce", "Real Estate", "Travel and Tourism", "Food and Beverage", "Human Resources", "Customer Service", "Marketing and Advertising", "Legal", "Supply Chain and Logistics", "Energy and Utilities", "Telecommunications", "Media and Publishing", "Non-Profit and Social Impact"))

if idea:
    response = project_idea_generator(idea)
    # Display restaurant name
    st.write(response['items'])
    

