from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Initialize the chat model
# chat = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     google_api_key=os.getenv("GEMINI_API_KEY"),
# )

llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Store chat histories for different sessions (in production, use a database)
chat_sessions = {}

# System message
system_message = SystemMessage(
    content=(
        "You are a licensed professional doctor and must respond exactly as a real doctor would."
        "Your communication style should be calm, clear, medically grounded, and emotionally supportive. "
        "Every response must acknowledge the patient's concern, provide a concise doctor impression, offer practical guidance, and suggest an appropriate follow-up direction. "
        "You should ask brief, relevant diagnostic questions whenever more information is needed, similar to how a doctor conducts an assessment. "
        "You must remain focused strictly on healthcare and mental health. If a topic is outside this domain, redirect the patient gently toward health-related discussion. "
        "Responses must be short, precise, and direct, without unnecessary explanation or storytelling. "
        "Recommend some basic medicine where need and exercises and advises where u as a doctor feel important."
        "Do not use asterisks, bullet points, tables, emojis, or line breaks; write in one continuous paragraph. "
        "Maintain a professional tone at all times and avoid casual or informal language."
    )

)


@app.route('/')
def home():
    return jsonify({"status": "Chatbot API is running"})


@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        # Get the message from request
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')  # Support multiple sessions

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        # Initialize session if it doesn't exist
        if session_id not in chat_sessions:
            chat_sessions[session_id] = {"messages": []}

        # Build message objects (system + history + new message)
        message_objects = [system_message]

        # Add conversation history
        for turn in chat_sessions[session_id]["messages"]:
            message_objects.append(HumanMessage(content=turn["human"]))
            message_objects.append(AIMessage(content=turn["ai"]))

        # Add new user input
        message_objects.append(HumanMessage(content=user_message))

        # Get AI response
        result = llm.invoke(message_objects)
        ai_response = result.content

        # Save turn in session history
        chat_sessions[session_id]["messages"].append({
            "human": user_message,
            "ai": ai_response
        })

        return jsonify({
            "response": ai_response,
            "session_id": session_id
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route('/clear', methods=['POST'])
def clear_history():
    """Clear chat history for a session"""
    data = request.json
    session_id = data.get('session_id', 'default')

    if session_id in chat_sessions:
        chat_sessions[session_id] = {"messages": []}

    return jsonify({"status": "History cleared"})


@app.route('/history', methods=['GET'])
def get_history():
    """Get chat history for a session"""
    session_id = request.args.get('session_id', 'default')

    if session_id in chat_sessions:
        return jsonify(chat_sessions[session_id])

    return jsonify({"messages": []})


if __name__ == '__main__':
    print("🤖 Chatbot Flask API is starting...")
    print("📡 Server will run on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)