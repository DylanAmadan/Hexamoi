# CamusBot
Development of a chatbot to aid in french language learning chatbot

1. Purpose
The purpose of this document is to outline the product requirements for a Chatbot application, designed to aid users in learning the French language. The application allows users to interact with a chatbot through a voice-based interface. The chatbot analyzes user input, provides corrections to pronunciation, and suggests possible correct interpretations. It also responds to accurate prompts in French, offering a continuous and interactive learning experience.

2. Product Overview
The French Tutor Chatbot is an interactive web-based application that uses a voice-to-text API and a GPT-based language model. It aims to provide users an immersive language learning experience, enabling them to practice French pronunciation and conversation in a supportive environment.

3. Functional Requirements
3.1 User Interface
  The user interface should be clean and intuitive, enabling users to interact with the chatbot efficiently. The user will be able to:
  Start and end voice conversations with the chatbot.
  Adjust the 'difficulty setting' which determines how strict the chatbot is in correcting the user.
3.2 Voice-to-Text
  An API will be developed using Django that accepts audio input from the user.
  The API will convert the audio input into text using voice-to-text technology.
3.3 Language Processing and Response Generation
  The text generated from the user's speech is fed into a GPT-based language model.
  If the user's French pronunciation or grammar is accurate according to the set 'difficulty setting', the model will generate a response   in French to continue the conversation.
  If the user's French pronunciation or grammar is inaccurate, the chatbot will:
  Ask the user to repeat the prompt with better pronunciation.
  Provide guesses or suggestions of what the user might have been trying to say in correct French.

4. Non-functional Requirements
  The application should be accessible via modern web browsers (Chrome, Firefox, Safari, Edge).
  The application must provide real-time feedback to the user.
  The application must ensure user data privacy and comply with relevant data protection regulations.
  
5. Future Enhancements
  The product roadmap could include options for text-based conversations, a wider range of languages to learn, and a mobile application
  or iOS and Android platforms.
