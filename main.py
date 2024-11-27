import sys

def get_initial_position():
    """
    Prompt the user to enter the initial disk arm position.
    """
    while True:
        try:
            position = int(input("Enter the initial disk arm position: "))
            if position < 0:
                raise ValueError("Initial position must be a non-negative integer.")
            return position
        except ValueError as ve:
            print(f"Invalid input: {ve}")

def get_track_requests(file_path):
    """
    Read and parse the track request sequence from the specified file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            track_requests = [int(track.strip()) for track in content.split(',')]
            if not track_requests:
                raise ValueError("Track request sequence is empty.")
            if any(track < 0 for track in track_requests):
                raise ValueError("Track requests must be non-negative integers.")
            return track_requests
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Invalid track requests: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Entry point for the Disk Scheduling Simulator application.
    """
    print("Welcome to the Disk Scheduling Simulator.")
    
    initial_position = get_initial_position()
    
    file_path = input("Enter the file path for track request sequence: ")
    track_requests = get_track_requests(file_path)
    
    print(f"Initial Disk Arm Position: {initial_position}")
    print(f"Track Requests: {track_requests}")
    # Further implementation will be added in subsequent features.

if __name__ == "__main__":
    main()
