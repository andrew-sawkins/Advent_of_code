import os

def read_input(year: int, day: int, input_file_name="input.txt"):
    
    file_path = os.path.join(os.getcwd(),f"{year}/Day{day}", input_file_name)
    
    try:
        with open(file_path, 'r') as f:
            return f.read()  # Or f.readlines() for a list of lines
    except FileNotFoundError:
        print(f"Input file for Year {year} Day {day} not found at {file_path}")
        return None
