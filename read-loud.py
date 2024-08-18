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

if __name__ == "__main__":
    # Example usage: Replace with your file path
    file_path = 'your_code_file.py'
    read_file_aloud(file_path)

# Provide the file you want to read in  read_file_aloud(file_path)