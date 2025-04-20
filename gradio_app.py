# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import dependencies
import os
import logging
import gradio as gr
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# Ensure FFmpeg is properly set
AudioSegment.converter = "C:\\ffmpeg\\ffmpeg.exe"  # Update the path as needed

# Import custom modules
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# System prompt for AI
system_prompt = """You have to act as a professional doctor. I know you are not, but this is for learning purposes. 
What's in this image? Do you find anything wrong with it medically? If you make a differential, suggest some remedies for them.
Do not add any numbers or special characters in your response. Your response should be in one long paragraph. 
Always answer as if you are answering a real person. Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Do not respond as an AI model in markdown, and keep your answer concise (max 2 sentences). No preamble, start your answer immediately."""


# Function to process user inputs
def process_inputs(audio_filepath, image_filepath):
    logging.info("Processing user inputs...")

    # Step 1: Convert Speech to Text
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )
    logging.info("Speech-to-text conversion complete.")

    # Step 2: Analyze Image (if provided)
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            encoded_image=encode_image(image_filepath),
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for analysis."

    logging.info("Doctor's response generated.")

    # Step 3: Convert Text Response to Speech (MP3)
    voice_of_doctor_mp3 = "final.mp3"
    text_to_speech_with_elevenlabs(
        input_text=doctor_response,
        output_filepath=voice_of_doctor_mp3
    )

    # Step 4: Convert MP3 to WAV (Gradio requires a valid format)
    voice_of_doctor_wav = "final.wav"
    try:
        audio = AudioSegment.from_mp3(voice_of_doctor_mp3)
        audio.export(voice_of_doctor_wav, format="wav")
        logging.info("MP3 to WAV conversion successful.")
    except Exception as e:
        logging.error(f"FFmpeg conversion failed: {e}")
        return "Error: Could not convert speech to WAV format."

    return speech_to_text_output, doctor_response, voice_of_doctor_wav


# Create the Gradio UI
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Speak Your Symptoms"),  # Audio input
        gr.Image(type="filepath", label="📷 Upload an Image (Optional)")  # Image input
    ],
    outputs=[
        gr.Textbox(label="📝 Transcribed Speech", interactive=False),  # Transcribed text
        gr.Textbox(label="👨‍⚕️ AI Doctor's Diagnosis", interactive=False),  # AI-generated response
        gr.Audio(label="🔊 AI Doctor's Voice Response", autoplay=True)  # Autoplay enabled
    ],
    title="🩺 AI Doctor Voicebot",
    description="""
    **Welcome to the AI Doctor Voicebot!** 🎙️  
    - Speak about your symptoms, and our AI doctor will analyze them.  
    - Upload an image for visual diagnosis.  
    - Get a text and voice response with insights about your condition.  
    """,
    theme="compact",  # Optional: Choose a minimal theme for a cleaner look
    allow_flagging="never"  # Disable unnecessary flagging option
)

# Launch the application
iface.launch(debug=True)
