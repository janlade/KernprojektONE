import streamlit as st

# Daten für die KI-Angebote und Experten (ersetzen Sie dies durch Ihre eigene Datenquelle)
ki_angebote = {
    "KI für Echtzeit-Qualitätskontrolle": {
        "summary": "Zusammenfassung Anforderungsprofil"
    },
    "Customer Support Bot": {
        "summary": "Zusammenfassung Anforderungsprofil"
    },
    "Datenstandardisierung und -analyse": {
        "summary": "Zusammenfassung Anforderungsprofil"
    }
}

ki_experten = {
    "Experte1": {
        "name": "Max Mustermann",
        "wissensbereich": "KI für Echtzeit-Qualitätskontrolle",
        "referenz": "Referenz/Bewertung des Experten"
    },
    "Experte2": {
        "name": "Phil Mustermann",
        "wissensbereich": "Customer Support Bot",
        "referenz": "Referenz/Bewertung des Experten"
    },
    "Experte3": {
        "name": "Tom Mustermann",
        "wissensbereich": "Datenstandardisierung und -analyse",
        "referenz": "Referenz/Bewertung des Experten"
    }
}

def anforderungsprofil_anzeigen(ki_auswahl):
    if ki_auswahl in ki_angebote:
        st.subheader(f"Anforderungsprofil für {ki_auswahl}", divider='rainbow')
        # Text-Area für die Zusammenfassung
        summary_text = ki_angebote[ki_auswahl]["summary"]
        st.text_area("Zusammenfassung", value=summary_text, height=200, disabled=True)
    else:
        st.warning("Ungültige Auswahl")

def vermittlungsvorschlag_anzeigen(ki_auswahl):
    match_experten = [experte for experte in ki_experten.values() if experte['wissensbereich'] == ki_auswahl]
    if match_experten:
        st.subheader("Vermittlungsvorschlag", divider='rainbow')
        st.write("Auf Grundlage Ihrer Auswahl können wir Ihnen folgenden Experten empfehlen:")
        
        for experte in match_experten:
            st.write(f"**Name:** {experte['name']}")
            st.write(f"**Wissensbereich:** {experte['wissensbereich']}")
            st.write(f"**Referenz/Bewertung:** {experte['referenz']}")
            
    else:
        st.warning("Ungültige Auswahl")

    vermittlungsvorschlag = experte['name']

    return vermittlungsvorschlag

def chat(ki_auswahl, vermittlungsvorschlag):
    st.subheader("Chat mit KI-Experte", divider='rainbow')
    
    # Initialize session state for the current ki_auswahl
    if ki_auswahl not in st.session_state:
        st.session_state[ki_auswahl] = {"messages": [], "show_chat_input": False, "show_open_chat_button": True}

    if st.session_state[ki_auswahl]["show_open_chat_button"]:
        open_chat_button = st.button(f"Send Message to {vermittlungsvorschlag}")

        if open_chat_button:
            st.session_state[ki_auswahl]["show_chat_input"] = not st.session_state[ki_auswahl]["show_chat_input"]
            st.session_state[ki_auswahl]["show_open_chat_button"] = False
            st.empty()  # Clear the "Open Chat" button space

    # Display chat messages from history on app rerun (display limited to 3)
    for message in st.session_state[ki_auswahl]["messages"][-2:]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # React to user input
    if st.session_state[ki_auswahl]["show_chat_input"]:
        if prompt := st.chat_input(placeholder="Send a message"):
            # Display user message in chat message container
            st.chat_message("human").markdown(prompt)
            # Add user message to chat history
            st.session_state[ki_auswahl]["messages"].append({"role": "human", "content": prompt})

def main():
    st.title("KI-Integration für mittelständische Unternehmen")

    # User Story 1
    ki_auswahl = st.selectbox("Wählen Sie eine KI-Integration aus", list(ki_angebote.keys()), index=None)
    if ki_auswahl is not None:
        anforderungsprofil_anzeigen(ki_auswahl)

    # User Story 2
        vermittlungsvorschlag = vermittlungsvorschlag_anzeigen(ki_auswahl)

    # User Story 3
        chat(ki_auswahl, vermittlungsvorschlag)

if __name__ == "__main__":
    main()