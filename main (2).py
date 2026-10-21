import streamlit as st

# Configure the page style to look like a dark tracking dashboard
st.set_page_config(page_title="OSC Fire Control", page_icon="🎯", layout="centered")

st.title("🎯 OSC Fire Control Dashboard")
st.write("Calculate target displacements relative to your cannon coordinates.")

pair_count = st.number_input(
    "Number of origin/target pairs",
    min_value=1,
    value=1,
    step=1,
)

coordinate_pairs = []
valid_origins = True

for index in range(int(pair_count)):
    st.subheader(f"Pair {index + 1}")
    origin_col, target_col = st.columns(2)

    with origin_col:
        st.markdown("**Origin Configuration**")
        origin_x = st.number_input(
            f"Origin X (multiple of 16) — Pair {index + 1}",
            value=0,
            step=16,
            key=f"origin_x_{index}",
        )
        origin_y = st.number_input(
            f"Origin Y — Pair {index + 1}",
            value=64,
            step=1,
            key=f"origin_y_{index}",
        )
        origin_z = st.number_input(
            f"Origin Z (multiple of 16) — Pair {index + 1}",
            value=0,
            step=16,
            key=f"origin_z_{index}",
        )

    with target_col:
        st.markdown("**Target Coordinates**")
        target_x = st.number_input(
            f"Target X — Pair {index + 1}",
            value=100,
            step=1,
            key=f"target_x_{index}",
        )
        target_y = st.number_input(
            f"Target Y — Pair {index + 1}",
            value=64,
            step=1,
            key=f"target_y_{index}",
        )
        target_z = st.number_input(
            f"Target Z — Pair {index + 1}",
            value=100,
            step=1,
            key=f"target_z_{index}",
        )

    if origin_x % 16 != 0:
        st.error(f"⚠️ Origin X for Pair {index + 1} must be divisible by 16.")
        valid_origins = False
    if origin_z % 16 != 0:
        st.error(f"⚠️ Origin Z for Pair {index + 1} must be divisible by 16.")
        valid_origins = False

    coordinate_pairs.append(
        (target_x - origin_x, target_y - origin_y, target_z - origin_z)
    )

st.divider()
st.subheader("📊 Firing Solution Output Vectors")

if valid_origins:
    for index, (output_x, output_y, output_z) in enumerate(coordinate_pairs):
        st.markdown(f"**Pair {index + 1} — Displacement (Target − Origin)**")
        m1, m2, m3 = st.columns(3)
        m1.metric(label="ΔX Output", value=int(output_x))
        m2.metric(label="ΔY Output", value=int(output_y))
        m3.metric(label="ΔZ Output", value=int(output_z))
        st.code(
            f"Relative Offset: ~{int(output_x)} ~{int(output_y)} ~{int(output_z)}"
        )
else:
    st.warning("Please correct invalid origin alignments above to generate the vectors.")

