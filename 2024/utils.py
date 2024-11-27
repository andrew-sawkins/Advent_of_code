import os

def read_input(year: int, day: int, input_file_name="input.txt"):
    """Reads input file for the given year and day (year/DayX/input.txt)."""
    file_path = os.path.join(os.getcwd(), input_file_name)
    
    try:
        with open(file_path, 'r') as f:
            return f.read()  # Or f.readlines() for a list of lines
    except FileNotFoundError:
        print(f"Input file for Year {year} Day {day} not found at {file_path}")
        return None
