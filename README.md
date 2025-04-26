# 🩺 AI Doctor VoiceBot  
**A Generative AI-based Clinical Assistant for Voice & Image-Based Medical Assessment**

> *Developed as a practical demonstration of multimodal AI using NLP, Speech Synthesis, and Image Analysis for healthcare applications.*

---
⬇️⬇️ Click the following Porject Demo Button  to explore the full working demo of the project ⬇️⬇️
## 🔗 [🚀↗️Project Demo](https://www.youtube.com/watch?v=q0upOqxN18Y)


---

## 🖼️ Web App UI Preview

Below are the output UI screenshots from the WebApp in action:

<p align="center">
  <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Output%201.jpg?raw=true" width="45%" />
  <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Output%202.jpg?raw=true" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Output%203.jpg?raw=true" width="45%" />
  <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Output%204.jpg?raw=true" width="45%" />
</p>

---

## 🧪 Input vs Output Results

| Input ⬇️ | Output ⬇️ |
|---------|----------|
| <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Input.jpg?raw=true" width="450"/> | <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Ouput.jpg?raw=true" width="450"/> |







---

### 🔄 Case 2

| Input ⬇️ | Output ⬇️ |
|---------|----------|
| <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Input_2.jpg?raw=true" width="450"/> | <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Outpu_2.jpg?raw=true" width="450"/> |

---

### 🔄 Case 3

| Input ⬇️ | Output ⬇️ |
|---------|----------|
| <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Input_3.jpg?raw=true" width="450"/> | <img src="https://github.com/TusharPawa/Ai-Doctor-Voicebot/blob/main/Outputs/Output_3.jpg?raw=true" width="450"/> |

---

## 💡 Key Features

- 🎤 **Voice-to-Text Conversion** for collecting patient symptoms.
- 🖼️ **Image Upload & Analysis** for visible skin conditions.
- 💊 **Prescription Generation** powered by LLMs trained on medical dialogue patterns.
- 🔊 **AI Doctor Voice** delivery using realistic text-to-speech.
- 🧠 **Context-aware system prompt** ensures human-like, empathic outputs.

---

## 🧪 Tech Stack

| Technology       | Purpose |
|------------------|---------|
| 🧩 **Gradio**     | Frontend for multimodal interface (voice + image upload) |
| 🧠 **Groq LLM API** | Language model for generating natural language prescriptions |
| 🔊 **ElevenLabs** | Realistic doctor-style voice synthesis |
| 🖼️ **Python & PIL** | Image pre-processing |
| ☁️ **Hosted Web App** | Easily accessible demo for recruiters and stakeholders |

---

## 🧑‍⚕️ System Prompt

The core behavior of the model is controlled by a **custom system prompt** designed to ensure human-like, empathetic, and concise medical responses:

```python
system_prompt = """You have to act as a professional doctor. I know you are not, but this is for learning purposes. 
What's in this image? Do you find anything wrong with it medically? If you make a differential, suggest some remedies for them.
Do not add any numbers or special characters in your response. Your response should be in one long paragraph. 
Always answer as if you are answering a real person. Do not say 'In the image I see' but say 'With what I see, I think you have ....'
Do not respond as an AI model in markdown, and keep your answer concise (max 2 sentences). No preamble, start your answer immediately."""
