# Example of a setup_st.py file which is called in your main file to setup the UI/UX and initialize the session

#1. Function to set up the page's layout and design elements
def set_design():
    # Creating a 3-column layout for the Streamlit app
    col1, col2, col3 = st.columns([1, 2, 1])
    
    # The main logo will be displayed in the middle column
    with col2:
        # Loading and displaying a logo image from the repository, and centering it
        st.image("sample_logo.png", use_column_width=True)

    # Adding a title to the Streamlit app, center-aligned
    st.markdown("<p style='text-align: center; font-size: 30px;'><b>[Sample Generative AI Chatbot]</b></p>", unsafe_allow_html=True)

# 2. Function to initialize variables that will hold the state of the app (illustrative list, not complete)
def initialize_session_state():
    # Used to generate the initial message for the conversation
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            {"role": "assistant", "content": "Hi there, what can I help you with today?"}
        ]
    # Can be used to make the chatbot end the convo or perform an action when some limit is reached
    if 'message_count' not in st.session_state:
        st.session_state['message_count'] = 0
    # Initializes the model_name session state variable
    if 'model_name' not in st.session_state:
        st.session_state['model_name'] = ""
    # Initializes the temperature session state variable
    if 'temperature' not in st.session_state:
        st.session_state['temperature'] = []
    # Initializes the OpenAI API key variable
    if 'api_key' not in st.session_state:
        st.session_state['api_key'] = ""
    # Initializes the use index variable to determine if we use index in replies
    if 'use_index' not in st.session_state:
        st.session_state['use_index'] = False

# 3. Function to initialize the sidebar UI elements
def sidebar():
    # Adding a header to the sidebar
    st.sidebar.markdown("""
    <h1 style='color: black; font-size: 24px;'>Chatbot Configuration</h1>
    """, unsafe_allow_html=True)

# 4.Function to create a 'Clear Conversation' button on the sidebar
def clear_button():
    # Creating the 'Clear Conversation' button
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    
    # If the button is clicked, this block will execute and the conversation will clear
    if clear_button:
        st.session_state['messages'] = [
            {"role": "assistant", "content": "Hi there, what can I help you with today?"}
        ]
        st.session_state['message_count'] = 0

# 5. Function to track the conversation for download functionality
def download_convo():
    # Checking if there are enough messages to download
    if 'messages' in st.session_state and len(st.session_state['messages']) > 0:
        # Concatenating all messages into a single string
        full_conversation = "\n".join([
            f"\n{'-'*20}\n"
            f"Role: {msg['role']}\n"
            f"{'-'*20}\n"
            f"{msg['content']}\n"
            for msg in st.session_state['messages']
        ])
        return full_conversation
    else:
        # If not enough messages, show a warning
        st.warning("There aren't enough messages in the conversation to download it. Please refresh the page")
        return ""

# 6. Function to create a 'Download Conversation' button on the sidebar
def download_button():
    # Generating the full conversation text
    full_conversation = download_convo()
    
    # Creating a download button for the full conversation
    st.sidebar.download_button(
        label="Download conversation",
        data=full_conversation,
        file_name='conversation.txt',
        mime='text/plain'
    )
