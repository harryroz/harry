import streamlit as st

# Configure the page style to look like a dark tracking dashboard
st.set_page_config(page_title="OSC Fire Control", page_icon="🎯", layout="centered")

st.title("🎯 OSC Fire Control Dashboard")
st.write("Calculate target displacements relative to your cannon coordinates.")

# Use two clean columns to match a structural layout design
col1, col2 = st.columns(2)

with col1:
    st.subheader("Origin Configuration")
    
    # Input field with built-in validation step for multiples of 16
    origin_x = st.number_input("Origin X (Must be a multiple of 16)", value=0, step=16)
    if origin_x % 16 != 0:
        st.error("⚠️ Origin X must be divisible by 16.")
        
    origin_y = st.number_input("Origin Y", value=64, step=1)
    
    origin_z = st.number_input("Origin Z (Must be a multiple of 16)", value=0, step=16)
    if origin_z % 16 != 0:
        st.error("⚠️ Origin Z must be divisible by 16.")

with col2:
    st.subheader("Target Coordinates")
    target_x = st.number_input("Target X", value=100, step=1)
    target_y = st.number_input("Target Y", value=64, step=1)
    target_z = st.number_input("Target Z", value=100, step=1)

st.divider()

# Compute the trajectory coordinate differences matching your core math logic
output_x = target_x - origin_x
output_y = target_y - origin_y
output_z = target_z - origin_z

# Firing Solution Outputs Display Card
st.subheader("📊 Firing Solution Output Vector")

if (origin_x % 16 == 0) and (origin_z % 16 == 0):
    # Render the text matching your explicit layout variables
    st.info(f"**Displacement Vector (Target - Origin):**")
    
    # Large readable status layout metrics
    m1, m2, m3 = st.columns(3)
    m1.metric(label="ΔX Output", value=int(output_x))
    m2.metric(label="ΔY Output", value=int(output_y))
    m3.metric(label="ΔZ Output", value=int(output_z))
    
    # Useful formatted copy-paste string format for command execution lines
    st.code(f"Relative Offset: ~{int(output_x)} ~{int(output_y)} ~{int(output_z)}")
else:
    st.warning("Please correct the invalid origin alignments above to generate the vector output.")


