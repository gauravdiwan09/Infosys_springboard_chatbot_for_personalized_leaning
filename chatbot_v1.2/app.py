import streamlit as st
import requests
import uuid
import json


class PersonalizedLearningChatbot:
    def __init__(self):
        """
        Initialize the chatbot with comprehensive setup and personalization features.

        This method sets up:
        - Session state management
        - Page configuration
        - Custom UI styling
        """
        self.initialize_session_state()
        self.configure_page()
        self.apply_custom_styling()

    def initialize_session_state(self):
        """
        Manage session state variables for persistent user experience.

        Key session state components:
        - Unique session ID
        - Chat history
        - User learning preferences
        """
        # Generate unique session identifier
        if 'session_id' not in st.session_state:
            st.session_state.session_id = str(uuid.uuid4())

        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []

        # Initialize user learning preferences
        if 'user_preferences' not in st.session_state:
            st.session_state.user_preferences = {
                'learning_style': None,
                'interests': [],
                'education_level': None
            }

        # Initialize example prompts
        if 'example_prompts' not in st.session_state:
            st.session_state.example_prompts = []

    def configure_page(self):
        """
        Configure Streamlit page settings for optimal user experience.

        Features:
        - Custom page title
        - Brain emoji as page icon
        - Wide layout
        - Expanded sidebar
        """
        st.set_page_config(
            page_title="AI Learning Sarthi",
            page_icon="🧠",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    def apply_custom_styling(self):
        """
        Apply advanced CSS styling for modern, educational UI.

        Styling focuses on:
        - Clean, professional color scheme
        - Readable typography
        - Subtle gradients
        - Responsive design elements
        """
        st.markdown("""
        <style>
            body {
                background-color: #f4f6f9;
                font-family: 'Inter', sans-serif;
            }
            .chat-container {
                background-color: white;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                padding: 20px;
                margin-top: 20px;
            }
            .user-message {
                background: linear-gradient(135deg, #e6f2ff 0%, #d6e6f3 100%);
                border-radius: 15px;
                padding: 15px;
                margin-bottom: 15px;
            }
            .bot-message {
                background: linear-gradient(135deg, #e8f5e9 0%, #d0e1d0 100%);
                border-radius: 15px;
                padding: 15px;
                margin-bottom: 15px;
            }
            .header-title {
                color: #2c3e50;
                text-align: center;
                font-size: 2.5rem;
                font-weight: 700;
                margin-bottom: 20px;
            }
        </style>
        """, unsafe_allow_html=True)

    def get_example_prompts(self, learning_style, interests, education_level):
        """
        Generate context-aware example prompts based on user's preferences.

        Provides intelligent, tailored question suggestions that match:
        - Learning style
        - Areas of interest
        - Educational background
        """
        example_prompts_map = {
            'Visual': {
                'Technology': [
                    "Show me a diagram explaining blockchain",
                    "Create a visual guide to machine learning algorithms",
                    "Explain the structure of a computer network using a diagram",
                    "Illustrate the components of a smartphone",
                    "Visualize the difference between frontend and backend development"
                ],
                'Science': [
                    "Visualize the process of photosynthesis",
                    "Draw a diagram of DNA replication",
                    "Show me a schematic of the solar system",
                    "Illustrate the layers of the Earth's atmosphere",
                    "Draw the lifecycle of a butterfly"
                ],
                'Arts': [
                    "Show me a flowchart of art history movements",
                    "Visualize the steps of drawing a human face",
                    "Create a color wheel diagram",
                    "Illustrate how to sketch perspective in art"
                ],
                'Mathematics': [
                    "Visualize the Pythagorean theorem",
                    "Draw a graph of a quadratic equation",
                    "Illustrate the steps of solving an equation",
                    "Create a diagram explaining fractions",
                    "Show me a chart for basic geometry formulas"
                ],
                'Business': [
                    "Create a flowchart explaining the sales process",
                    "Visualize the structure of a startup organization",
                    "Draw a pie chart of market share for industries",
                    "Illustrate the customer journey in a business",
                    "Create a bar graph showing profit vs expenses"
                ],
                'Humanities': [
                    "Visualize a timeline of World War II events",
                    "Illustrate the structure of a democracy",
                    "Draw a chart of ancient civilizations",
                    "Create a map showing major trade routes in history",
                    "Visualize the family tree of a royal dynasty"
                ]
            },
            'Auditory': {
                'Technology': [
                    "Recommend podcasts about AI trends",
                    "Explain coding concepts through storytelling",
                    "Describe machine learning algorithms narratively",
                    "Talk about the history of programming languages",
                    "Narrate the evolution of the internet"
                ],
                'Science': [
                    "Explain quantum physics in a narrative way",
                    "Describe biological processes as a story",
                    "Tell a story about the discovery of gravity",
                    "Explain the water cycle in simple words",
                    "Describe the journey of a single raindrop"
                ],
                'Arts': [
                    "Tell a story about the life of a famous artist",
                    "Narrate how a painting can convey emotions",
                    "Explain the evolution of modern art styles",
                    "Describe the process of composing music",
                    "Talk about the significance of colors in art"
                ],
                'Mathematics': [
                    "Tell a story about the discovery of zero",
                    "Explain how math is used in everyday life",
                    "Describe a simple way to remember multiplication tables",
                    "Narrate the concept of infinity in mathematics",
                    "Explain how math was used in ancient architecture"
                ],
                'Business': [
                    "Describe the basics of entrepreneurship narratively",
                    "Talk about the story of a successful startup",
                    "Explain marketing strategies through examples",
                    "Tell a story about the evolution of the stock market",
                    "Describe the life of a famous businessperson"
                ],
                'Humanities': [
                    "Explain the French Revolution as a story",
                    "Narrate the causes and effects of the Industrial Revolution",
                    "Describe the daily life of ancient Romans",
                    "Tell the story of a famous historical figure",
                    "Explain the Silk Road trade as a journey"
                ]
            },
            'Kinesthetic': {
                'Technology': [
                    "Suggest hands-on coding projects",
                    "Describe interactive learning for programming",
                    "Recommend project-based learning resources",
                    "Create a small project to understand IoT concepts",
                    "Try building a simple website step by step"
                ],
                'Science': [
                    "Suggest science experiments for learning",
                    "Describe interactive ways to understand complex concepts",
                    "Recommend building a simple volcano model",
                    "Do an experiment to measure the speed of a toy car",
                    "Test the pH of common household liquids"
                ],
                'Arts': [
                    "Try painting a landscape using watercolors",
                    "Sculpt a small model using clay",
                    "Create a collage using old magazines",
                    "Design your own greeting card",
                    "Sketch a still life scene from your surroundings"
                ],
                'Mathematics': [
                    "Use paper to fold shapes and learn geometry",
                    "Solve puzzles to understand number patterns",
                    "Build a model of a 3D shape using toothpicks",
                    "Measure items around you to practice units and scales",
                    "Create your own math game using dice"
                ],
                'Business': [
                    "Simulate a negotiation exercise with friends",
                    "Create a simple business plan for a lemonade stand",
                    "Role-play pitching a product idea to investors",
                    "Track expenses and profits from a small activity",
                    "Conduct a mock customer survey"
                ],
                'Humanities': [
                    "Recreate a historical event as a small play",
                    "Map the journey of an explorer using a globe",
                    "Create a scrapbook of cultural festivals",
                    "Draw a timeline of key historical events",
                    "Write a letter as if you're living in a historical period"
                ]
            }
        }

        # Select prompts based on preferences
        selected_prompts = example_prompts_map.get(learning_style, {}).get(
            interests[0] if interests else 'Technology',
            ["Ask about study strategies", "Get learning recommendations"]
        )

        return selected_prompts[:5]  # Return top 3 prompts

    def display_sidebar(self):
        """
        Create an interactive, intelligent sidebar for personalization.

        Features:
        - Learning style selection
        - Interest area multi-select
        - Education level dropdown
        - Dynamic example prompts
        - Resource recommendation buttons
        """
        st.sidebar.title("🧠 Learning Sarthi")

        # Learning Style Selection
        learning_style = st.sidebar.selectbox(
            "Select Your Learning Style",
            ["Visual", "Auditory", "Kinesthetic", "Reading/Writing"],
            help="Choose how you best absorb information"
        )
        st.session_state.user_preferences['learning_style'] = learning_style

        # Interest Areas
        interests = st.sidebar.multiselect(
            "Your Interest Areas",
            ["Technology", "Science", "Arts", "Mathematics", "Business", "Humanities"],
            help="Select topics you're passionate about"
        )
        st.session_state.user_preferences['interests'] = interests

        # Education Level
        education_level = st.sidebar.selectbox(
            "Your Education Level",
            ["High School", "Undergraduate", "Postgraduate", "Professional"],
            help="Help us tailor content to your academic stage"
        )
        st.session_state.user_preferences['education_level'] = education_level

        # Generate and Display Example Prompts
        if learning_style and interests and education_level:
            st.session_state.example_prompts = self.get_example_prompts(
                learning_style, interests, education_level
            )

            st.sidebar.markdown("### 💡 Suggested Questions")
            for prompt in st.session_state.example_prompts:
                if st.sidebar.button(prompt):
                    st.session_state.chat_input = prompt

    def get_bot_response(self, user_input):
        """
        Send user input to Rasa server with personalized context.

        Enhanced request includes:
        - User message
        - Session tracking
        - Personalization context
        """
        try:
            rasa_url = "http://localhost:5005/webhooks/rest/webhook"
            headers = {"Content-Type": "application/json"}

            # Include personalization context
            data = {
                "sender": st.session_state.session_id,
                "message": user_input,
                "context": {
                    "learning_style": st.session_state.user_preferences.get('learning_style'),
                    "interests": st.session_state.user_preferences.get('interests', []),
                    "education_level": st.session_state.user_preferences.get('education_level')
                }
            }

            response = requests.post(rasa_url, json=data, headers=headers)

            if response.status_code == 200:
                bot_responses = response.json()
                if bot_responses:
                    bot_reply = "<br>".join([resp.get("text", "") for resp in bot_responses])
                    return bot_reply if bot_reply else "I'm thinking... Could you rephrase that?"
                else:
                    return "I'm not sure how to respond. Can you try asking differently?"
            else:
                return f"Oops! Something went wrong. Status code: {response.status_code}"

        except requests.RequestException as e:
            return f"Network error: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def run(self):
        """
        Main method to orchestrate chatbot interaction.

        Handles:
        - Header display
        - Sidebar rendering
        - User input processing
        - Chat history management
        """
        st.markdown("<div class='header-title'>🧠 AI Learning Sarthi</div>", unsafe_allow_html=True)

        self.display_sidebar()

        # Chat input section
        user_input = st.text_input(
            "💬 Ask me anything about learning",
            placeholder="Type your learning question here...",
            key="chat_input"
        )

        # Send button with interaction logic
        if st.button("🚀 Send Message", key="send_button"):
            if user_input.strip():
                with st.spinner('🤖 Generating personalized response...'):
                    bot_response = self.get_bot_response(user_input)

                    st.session_state.chat_history.append({
                        'type': 'user',
                        'message': user_input
                    })
                    st.session_state.chat_history.append({
                        'type': 'bot',
                        'message': bot_response
                    })
            else:
                st.warning("Please enter a message before sending.")

        self.display_chat_history()

    def display_chat_history(self):
        """
        Render chat history with enhanced visual presentation.

        Features:
        - Styled message containers
        - Emoji-based message identification
        - Responsive design
        """
        if st.session_state.chat_history:
            st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

            for message in st.session_state.chat_history:
                if message['type'] == 'user':
                    st.markdown(
                        f"<div class='user-message'>🧑 <b>You:</b> {message['message']}</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<div class='bot-message'>🤖 <b>Learning Companion:</b> {message['message']}</div>",
                        unsafe_allow_html=True
                    )

            st.markdown("</div>", unsafe_allow_html=True)


def main():
    """
    Entry point for the Streamlit application.
    Initializes and runs the personalized learning chatbot.
    """
    chatbot = PersonalizedLearningChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()