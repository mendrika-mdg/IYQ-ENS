import streamlit as st                                                      # type: ignore

# Seminar Information
seminar_title = "IYQ Seminar: Celebrating Quantum Science and Honouring ENS Physics Founders"
date = "16 January 2025"
time = "12:15 - 14:15 (Madagascar Time, UTC+3)"
location = "Hybrid (Online and ENS Campus, Madagascar)"
description = (
    "Join us to celebrate the International Year of Quantum Science and Technology, "
    "featuring inspiring keynotes and panel discussions on quantum physics, laser physics, "
    "machine learning, astronomy, and outreach. This seminar also honours the founders of "
    "the ENS Physics programme for their invaluable contributions."
)

# Layout
st.title(seminar_title)
st.subheader(f"📅 {date} | ⏰ {time} | 📍 {location}")

# Description Section
st.write(description)

# Schedule Section
st.subheader("📋 Seminar Schedule")
schedule = {
    "12:15 - 12:25": "Welcome and Opening Remarks",
    "12:25 - 12:45": "Keynote 1: Advancing Thunderstorm Prediction - Mendrika Rakotomanga",
    "12:45 - 13:05": "Keynote 2: New-generation Satellite Data for Nowcasting - Dr. Stephan Bojinski",
    "13:05 - 13:25": "Panel Discussion: Quantum Physics, Machine Learning, and Astronomy",
    "13:25 - 13:45": "Keynote 3: Laser Physics and Microscopy - Dina Ratsimandresy",
    "13:45 - 14:15": "Closing Remarks and Networking",
}
for time, session in schedule.items():
    st.write(f"**{time}** - {session}")

# Speakers Section
st.subheader("🎙️ Featured Speakers")
speakers = [
    {
        "name": "Mendrika Rakotomanga",
        "title": "Postgraduate Researcher, University of Leeds",
        "talk": "Advancing Thunderstorm Prediction: The Role of AI and Satellite Data in Africa",
    },
    {
        "name": "Dr. Stephan Bojinski",
        "title": "Scientist, EUMETSAT",
        "talk": "New-generation Satellite Data for Nowcasting from Meteosat Third Generation",
    },
    {
        "name": "Dina Ratsimandresy",
        "title": "Researcher, Medical Research Council, Laboratory of Molecular Biology",
        "talk": "Laser Physics and Microscopy",
    },
]
for speaker in speakers:
    st.write(f"**{speaker['name']}** - {speaker['title']}")
    st.write(f"*Talk:* {speaker['talk']}")

# Joining Links Section
st.subheader("🔗 Join the Seminar")
st.write("The seminar is hybrid. Use the links below to join online or access the recording:")
st.markdown(
    """
    - **[Join via Zoom](#)**  
    - **[Watch Recording](#)** (Available after the event)
    """
)

# Footer
st.write("---")
st.write("Organised by ENS Physics Alumni | Contact: [mendrika@aims.ac.za](mailto:mendrika@aims.ac.za)")
