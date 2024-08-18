import pyttsx3

# Initialize the text-to-speech engine
def init_engine():
    engine = pyttsx3.init()

    # Set properties before adding anything to the queue
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

    # Choose a voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female

    return engine
