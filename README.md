# Chatbot_for_Personalized_Learning

This project is an interactive, conversational AI chatbot designed to enhance personalized learning experiences. Built using **Rasa** and **Streamlit**, the chatbot not only offers personalized resource recommendations (videos, books, and courses) based on the user's preferences but also generates dynamic, AI-powered explanations for various topics. The chatbot leverages the **Hugging Face Flan-T5-large model** to deliver accurate, detailed, and concise explanations on user-asked topics, making learning more efficient and accessible.

## Features

### 1. **Personalized Recommendations**
The chatbot is capable of recommending various learning resources tailored to the user's preferences, including:
- **Videos**
- **Books**
- **Courses**
  
These recommendations are dynamically generated based on the user's interests and the topics they inquire about, ensuring that the learning resources are both relevant and useful.

### 2. **Dynamic Explanations**
Using **Hugging Face's Flan-T5-large model**, the chatbot provides accurate, concise, and dynamic explanations for any topic the user requests. It can answer questions, explain concepts in detail, and offer step-by-step instructions on various subjects, making it an excellent tool for both learners and educators.

### 3. **Study Tips and Motivational Support**
In addition to learning resources and explanations, the chatbot also offers:
- **Study Tips**: Helpful strategies for effective learning, time management, and staying focused.
- **Motivational Messages**: Encouraging words to keep learners motivated and on track.

This combination of personalized resources and motivation creates an engaging learning experience.

## Requirements

The following tools and libraries are required to run the project:

- **Python 3.8 or later**: The codebase is compatible with Python 3.8 and above.
- **Rasa Open Source**: Used for building conversational AI models.
- **Hugging Face Transformers**: Essential for integrating the **Flan-T5-large** model, which is used to generate dynamic, accurate explanations.

## Installation

### Step 1: Clone the Repository (Use the latest commited code)
Start by cloning the project repository from GitHub:

```bash
git clone https://github.com/your-username/personalized-learning-chatbot.git
cd personalized-learning-chatbot
```

### Step 2: Install Dependencies
Install the required dependencies listed in `requirements.txt`. This includes libraries for Rasa, Streamlit, Hugging Face Transformers, and any other necessary packages:

```bash
pip install -r requirements.txt
```

### Step 3: Train the Model
Once the dependencies are installed, train the Rasa model using the following command. This will create a model based on the data and configurations defined in the project:

```bash
rasa train
```

After training, the model will be saved in the `models` folder, ready for use.

## Running the Chatbot

### Step 1: Start the Rasa Action Server
To handle custom actions (such as generating dynamic explanations and retrieving resource recommendations), start the Rasa action server:

```bash
rasa run actions
```

This will launch the action server, allowing it to respond to specific requests made by the user.

### Step 2: Start the Rasa Shell
Next, run the Rasa shell to interact with the trained model. This step enables the model to process natural language inputs, process the user's queries, and trigger the appropriate actions (like providing recommendations or explanations):

```bash
rasa run -m models --enable-api --cors "*" --debug
```

The `--debug` flag is optional but useful for troubleshooting, as it will display detailed logs.

### Step 3: Start the Streamlit App
Finally, start the **Streamlit** app, which provides the user interface (UI) for interacting with the chatbot. This step will launch a web app where users can type in their queries and receive personalized responses from the chatbot:

```bash
streamlit run app.py
```

This will open the chatbot in your browser. From here, you can chat with the bot and get personalized learning recommendations, dynamic explanations, study tips, and motivational support.

## How It Works
- **Rasa** powers the conversational capabilities of the chatbot. It handles user inputs, triggers actions (such as recommendations), and provides context-aware responses.

- **Streamlit** serves as the frontend user interface, where users can interact with the bot in a simple, intuitive manner.

- **Hugging Face's Flan-T5-large model** is used for generating intelligent and detailed explanations. This transformer model processes the user’s queries and provides the most relevant responses in real-time.
