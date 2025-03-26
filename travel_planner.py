import streamlit as st

st.title("AI Travel Planner")

# Gather user input
destination = st.text_input("Where are you going?")
start_location = st.text_input("Where are you starting from?")
duration = st.number_input("How many days?", min_value=1, step=1)
budget = st.number_input("What’s your budget ($)?", min_value=100, step=50)
interests = st.text_input("What do you love (e.g., food, museums)?")
submit = st.button("Plan My Trip")

# Generate a basic itinerary
if submit:
    st.write(f"Here’s a simple {duration}-day trip to {destination} from {start_location}!")
    st.write(f"Budget: ${budget}, Interests: {interests}")
    st.write("Day 1: Arrive and explore downtown.")
    st.write("Day 2: Visit a key attraction based on your interests.")
    st.write(f"Days 3-{duration-1}: Enjoy local food and sights.")
    st.write(f"Day {duration}: Head back home.")
    st.write("For a detailed plan, check the full assignment prompts!")
