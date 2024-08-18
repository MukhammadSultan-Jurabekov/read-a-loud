from engine import init_engine

def read_file_aloud(file_path):
    engine = init_engine()
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            # Reading the code aloud
            engine.say(code)
            engine.runAndWait()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

