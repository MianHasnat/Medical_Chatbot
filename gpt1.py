# import streamlit as st
# from huggingface_hub import InferenceClient
#
# # Initialize the Hugging Face Inference Client
# api_key = "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"  # Replace with your actual Hugging Face API key
# client = InferenceClient(api_key=api_key)
#
# # Streamlit app layout
# st.title("Hugging Face Chatbot")
# st.subheader("Powered by meta-llama/Llama-3.2-1B-Instruct")
#
# # User input
# user_query = st.text_area("Enter your query:", placeholder="Type your question or prompt here...")
#
# if st.button("Generate Response"):
#     if not user_query.strip():
#         st.warning("Please enter a query.")
#     else:
#         # Preparing the message payload
#         messages = [
#             {"role": "user", "content": user_query}
#         ]
#
#         try:
#             # Generate response
#             with st.spinner("Generating response..."):
#                 completion = client.chat.completions.create(
#                     model="meta-llama/Llama-3.2-1B-Instruct",
#                     messages=messages,
#                     max_tokens=500
#                 )
#                 response = completion.choices[0].message.content
#             st.success("Response Generated:")
#             st.write(response)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

# --------------------------------------------------INTERFACE EDIT------------------------------------------------------
#
# import streamlit as st
# from huggingface_hub import InferenceClient
#
# # Initialize the Hugging Face Inference Client
# api_key = "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"  # Replace with your actual Hugging Face API key
# client = InferenceClient(api_key=api_key)
#
# # Set page configuration for better presentation
# st.set_page_config(
#     page_title="Hugging Face Chatbot",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
#
# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f5f7fa;
#         font-family: 'Roboto', sans-serif;
#     }
#     .main-header {
#         color: #4CAF50;
#         font-size: 2.5rem;
#         text-align: center;
#         font-weight: bold;
#     }
#     .sub-header {
#         color: #555555;
#         font-size: 1.25rem;
#         text-align: center;
#         margin-bottom: 30px;
#     }
#     .query-box textarea {
#         background-color: #fffdfd;
#         border-radius: 10px;
#         border: 1px solid #ddd;
#         padding: 15px;
#         font-size: 1.1rem;
#     }
#     .generate-button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 1.2rem;
#         padding: 10px 20px;
#         border-radius: 8px;
#         cursor: pointer;
#         transition: all 0.3s;
#     }
#     .generate-button:hover {
#         background-color: #45a049;
#     }
#     .response-box {
#         background-color: #eaf4fc;
#         border-radius: 10px;
#         padding: 20px;
#         font-size: 1.1rem;
#         border: 1px solid #c8e0f4;
#         word-wrap: break-word;
#         overflow-y: auto;
#         max-height: 400px;
#     }
#     .author-footer {
#         text-align: center;
#         margin-top: 20px;
#         font-size: 0.9rem;
#         color: #888;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # App layout
# st.markdown("<div class='main-header'>🤖 Hugging Face Chatbot</div>", unsafe_allow_html=True)
# st.markdown("<div class='sub-header'>Powered by meta-llama/Llama-3.2-1B-Instruct</div>", unsafe_allow_html=True)
#
# # Input Section
# st.markdown("<h4 style='margin-bottom: 5px;'>Enter Your Query:</h4>", unsafe_allow_html=True)
# user_query = st.text_area(
#     "",
#     placeholder="Ask me anything! Type your question or prompt here...",
#     height=150,
#     key="query_box"
# )
#
# # Submit Button
# if st.button("Generate Response", key="generate_btn"):
#     if not user_query.strip():
#         st.warning("⚠️ Please enter a query before generating a response!")
#     else:
#         try:
#             # Generate response with loading spinner
#             with st.spinner("🤔 Thinking... Generating your response..."):
#                 messages = [{"role": "user", "content": user_query}]
#                 completion = client.chat.completions.create(
#                     model="meta-llama/Llama-3.2-1B-Instruct",
#                     messages=messages,
#                     max_tokens=2000,  # Increased max tokens for longer output
#                     temperature=0.7  # Added a temperature to control creativity
#                 )
#                 response = completion.choices[0].message.content
#
#             # Display Response
#             st.markdown("<h4>🤩 Here's the Response:</h4>", unsafe_allow_html=True)
#             st.markdown(
#                 f"<div class='response-box'>{response}</div>",
#                 unsafe_allow_html=True
#             )
#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")
#
# # Sidebar Section (Optional)
# with st.sidebar:
#     st.header("About 🤖")
#     st.markdown(
#         """
#         Welcome to the **Hugging Face Chatbot**!
#         This bot is powered by **meta-llama/Llama-3.2-1B-Instruct** model,
#         which can generate insightful and meaningful responses to your queries.
#         ---
#         **Features**:
#         - User-friendly interface.
#         - Accurate and creative responses.
#         - Extended responses for detailed insights.
#         ---
#         **Author**:
#         This chatbot is proudly created and managed by **Mian Hasnat**.
#         ---
#         For more info, visit: [Hugging Face](https://huggingface.co/)
#         """,
#         unsafe_allow_html=True
#     )
#
# # Footer Section
# st.markdown(
#     """
#     <div class='author-footer'>
#         © 2024 | Developed by <b>Mian Hasnat</b>. Powered by Hugging Face.
#     </div>
#     """,
#     unsafe_allow_html=True
# )








#-----------------------------------3 different models ----------------------------------------------------------------


# import streamlit as st
# from huggingface_hub import InferenceClient
#
# # Initialize the Hugging Face Inference Client
# api_key = "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"  # Replace with your actual Hugging Face API key
# client = InferenceClient(api_key=api_key)
#
# # Set page configuration for better presentation
# st.set_page_config(
#     page_title="Hugging Face Multi-Model Chatbot",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
#
# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #f5f7fa;
#         font-family: 'Roboto', sans-serif;
#     }
#     .main-header {
#         color: #4CAF50;
#         font-size: 2.5rem;
#         text-align: center;
#         font-weight: bold;
#     }
#     .sub-header {
#         color: #555555;
#         font-size: 1.25rem;
#         text-align: center;
#         margin-bottom: 30px;
#     }
#     .query-box textarea {
#         background-color: #fffdfd;
#         border-radius: 10px;
#         border: 1px solid #ddd;
#         padding: 15px;
#         font-size: 1.1rem;
#     }
#     .generate-button {
#         background-color: #4CAF50;
#         color: white;
#         font-size: 1.2rem;
#         padding: 10px 20px;
#         border-radius: 8px;
#         cursor: pointer;
#         transition: all 0.3s;
#     }
#     .generate-button:hover {
#         background-color: #45a049;
#     }
#     .response-box {
#         background-color: #eaf4fc;
#         border-radius: 10px;
#         padding: 20px;
#         font-size: 1.1rem;
#         border: 1px solid #c8e0f4;
#         word-wrap: break-word;
#         overflow-y: auto;
#         max-height: 400px;
#     }
#     .author-footer {
#         text-align: center;
#         margin-top: 20px;
#         font-size: 0.9rem;
#         color: #888;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
#
# # App layout
# st.markdown("<div class='main-header'>🤖 Hugging Face Multi-Model Chatbot</div>", unsafe_allow_html=True)
# st.markdown("<div class='sub-header'>Powered by Llama , Falcon and Qwen models</div>", unsafe_allow_html=True)
#
# # Dropdown to choose the model
# model_choices = {
#     "Llama-3.2-1B-Instruct (meta-llama/Llama-3.2-1B-Instruct)": "meta-llama/Llama-3.2-1B-Instruct",
#     "Falcon-7B-Instruct (tiiuae/falcon-7b-instruct)": "tiiuae/falcon-7b-instruct",
#     "New Qwen/Qwen2.5-Coder-32B-Instruct":"Qwen/Qwen2.5-Coder-32B-Instruct",
#
# }
# selected_model = st.selectbox(
#     "Choose a Language Model:",
#     list(model_choices.keys()),
#     help="Select a model to generate responses to your queries.",
# )
#
# # Input Section
# st.markdown("<h4 style='margin-bottom: 5px;'>Enter Your Query:</h4>", unsafe_allow_html=True)
# user_query = st.text_area(
#     "",
#     placeholder="Ask me anything! Type your question or prompt here...",
#     height=150,
#     key="query_box"
# )
#
# # Submit Button
# if st.button("Generate Response", key="generate_btn"):
#     if not user_query.strip():
#         st.warning("⚠️ Please enter a query before generating a response!")
#     else:
#         try:
#             # Display selected model
#             st.info(f"Using Model: **{selected_model}**")
#
#             # Map model name
#             model_name = model_choices[selected_model]
#
#             # Generate response with loading spinner
#             with st.spinner("🤔 Thinking... Generating your response..."):
#                 messages = [{"role": "user", "content": user_query}]
#                 completion = client.chat.completions.create(
#                     model=model_name,
#                     messages=messages,
#                     max_tokens=2000,  # Increased max tokens for longer output
#                     temperature=0.7  # Added a temperature to control creativity
#                 )
#                 response = completion.choices[0].message.content
#
#             # Display Response
#             st.markdown("<h4>🤩 Here's the Response:</h4>", unsafe_allow_html=True)
#             st.markdown(
#                 f"<div class='response-box'>{response}</div>",
#                 unsafe_allow_html=True
#             )
#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")
#
# # Sidebar Section (Optional)
# with st.sidebar:
#     st.header("About 🤖")
#     st.markdown(
#         """
#         Welcome to the **Hugging Face Multi-Model Chatbot**!
#         This bot allows you to choose between multiple language models, including:
#         - **Llama-3.2-1B-Instruct**
#         - **Falcon-7B-Instruct**
#         - **Qwen/Qwen2.5-Coder-32B-Instruct**
#
#         **Features**:
#         - User-friendly interface.
#         - Accurate and creative responses.
#         - Extended responses for detailed insights.
#         ---
#         **Author**:
#         This chatbot is proudly created and managed by **Mian Hasnat**.
#         ---
#         For more info, visit: [Hugging Face](https://huggingface.co/).
#         """,
#         unsafe_allow_html=True
#     )
#
# # Footer Section
# st.markdown(
#     """
#     <div class='author-footer'>
#         © 2024 | Developed by <b>Mian Hasnat</b>. Powered by Hugging Face.
#     </div>
#     """,
#     unsafe_allow_html=True
# )



#------------------------------------------------------------------------ 4 + Image----------------------------------------
import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

# Initialize the Hugging Face Inference Client
api_key = "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"  # Replace with your actual Hugging Face API key
client = InferenceClient(api_key=api_key)

# Set page configuration for better presentation
st.set_page_config(
    page_title="Hugging Face Multi-Model App",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
        font-family: 'Roboto', sans-serif;
    }
    .main-header {
        color: #4CAF50;
        font-size: 2.5rem;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        color: #555555;
        font-size: 1.25rem;
        text-align: center;
        margin-bottom: 30px;
    }
    .query-box textarea {
        background-color: #fffdfd;
        border-radius: 10px;
        border: 1px solid #ddd;
        padding: 15px;
        font-size: 1.1rem;
    }
    .generate-button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.2rem;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.3s;
    }
    .generate-button:hover {
        background-color: #45a049;
    }
    .response-box {
        background-color: #eaf4fc;
        border-radius: 10px;
        padding: 20px;
        font-size: 1.1rem;
        border: 1px solid #c8e0f4;
        word-wrap: break-word;
        overflow-y: auto;
        max-height: 400px;
    }
    .author-footer {
        text-align: center;
        margin-top: 20px;
        font-size: 0.9rem;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App layout
st.markdown("<div class='main-header'>🩺 CUSTOM MEDICAL CHATBOT 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Powered by Chatbot and Text-to-Image Trained_Models</div>", unsafe_allow_html=True)

# Chatbot Section
st.markdown("<h3>🗣️ Chatbot Feature</h3>", unsafe_allow_html=True)

# Dropdown to choose the chatbot model
model_choices = {
    "fine_tuned_distilgpt2": "tiiuae/falcon-7b-instruct",
    "fine_tuned_Qwen_32B": "Qwen/Qwen2.5-Coder-32B-Instruct",
    "fine_tuned_gpt2":"google/gemma-1.1-2b-it",
    "fine_tuned_microsof_instruct":"microsoft/Phi-3.5-mini-instruct",
    "fine_tuned_mistralai_v0.3":"mistralai/Mistral-7B-Instruct-v0.3",
    "fine_tuned_gemma2":"google/gemma-2-2b-it"

}
selected_model = st.selectbox(
    "Choose a Fine_Tuned_Language Model for Chatbot:",
    list(model_choices.keys()),
    help="Select a model to generate responses to your queries.",
)

# Input for chatbot
user_query = st.text_area(
    "Enter Your Query for the Chatbot:",
    placeholder="Ask me anything! Type your question or prompt here...",
    height=150,
    key="chat_query_box"
)

if st.button("Generate Chatbot Response", key="chat_generate_btn"):
    if not user_query.strip():
        st.warning("⚠️ Please enter a query before generating a response!")
    else:
        try:
            # Display selected model
            st.info(f"Using Chatbot Model: **{selected_model}**")

            # Map model name
            model_name = model_choices[selected_model]

            # Generate response with loading spinner
            with st.spinner("🤔 Thinking... Generating your response..."):
                messages = [{"role": "user", "content": user_query}]
                completion = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    max_tokens=5000,  # Increased max tokens for longer output
                    temperature=0.7  # Added a temperature to control creativity
                )
                response = completion.choices[0].message.content

            # Display Response
            st.markdown("<h4>🤩 Here's the Chatbot Response:</h4>", unsafe_allow_html=True)
            st.markdown(
                f"<div class='response-box'>{response}</div>",
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"❌ An error occurred with the chatbot: {e}")

# Text-to-Image Section
st.markdown("<h3>🎨 Text-to-Image Feature</h3>", unsafe_allow_html=True)

# Input for text-to-image
image_prompt = st.text_input(
    "Enter a Prompt to Generate an Image:",
    placeholder="Describe the image you want to generate (e.g., 'Astronaut riding a horse')",
    key="image_prompt"
)

if st.button("Generate Image", key="image_generate_btn"):
    if not image_prompt.strip():
        st.warning("⚠️ Please enter a prompt before generating an image!")
    else:
        try:
            # Initialize text-to-image model
            text_to_image_model = "ginipick/flux-lora-eric-cat"
            st.info(f"Using Text-to-Image Model: **{text_to_image_model}**")

            # Generate image with loading spinner
            with st.spinner("🎨 Creating your image..."):
                image = client.text_to_image(prompt=image_prompt, model=text_to_image_model)

                # Convert the PIL image to a displayable format
                st.image(image, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"❌ An error occurred with text-to-image generation: {e}")

# Sidebar Section (Optional)
with st.sidebar:
    st.header("About the App 🤖🏥")
    st.markdown(
        """
        Welcome to the **Hugging Face Multi-Model App**!
        This app integrates:
        - **Chatbot Features** using Llama, Falcon, google/gemma, and Qwen fine_tuned_models.
        - **Text-to-Image Generation** for creating custom images based on your prompts.

        **Features**:
        - User-friendly interface.
        - Multiple models for both text and image generation.
        - Accurate and creative responses.
        - Extended responses for detailed insights.
        ---
        **Author**:
        This app is proudly created and managed by **Mian Hasnat & Danish Jamal**.
        ---
        For more info, visit: [Hugging Face](https://huggingface.co/).
        """,
        unsafe_allow_html=True
    )

# Footer Section
st.markdown(
    """
    <div class='author-footer'>
        © 2024 | Developed by <b>Mian Hasnat</b>. Powered by Hugging Face.
    </div>
    """,
    unsafe_allow_html=True
)
