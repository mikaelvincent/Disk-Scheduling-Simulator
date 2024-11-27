import sys
from algorithms.fcfs import simulate_fcfs
from algorithms.c_scan import simulate_c_scan
from algorithms.c_look import simulate_c_look

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

def display_results(algorithm_name, total_head_movement, service_order):
    """
    Display the results of a disk scheduling algorithm execution.

    Args:
        algorithm_name (str): Name of the scheduling algorithm.
        total_head_movement (int): Total movement of the disk head.
        service_order (list of int): Order of track servicing.
    """
    print(f"\n=== {algorithm_name} Results ===")
    print(f"Total Head Movement: {total_head_movement}")
    print(f"Service Order: {', '.join(map(str, service_order))}\n")

def main():
    """
    Entry point for the Disk Scheduling Simulator application.
    """
    print("Welcome to the Disk Scheduling Simulator.")
    
    initial_position = get_initial_position()
    
    file_path = input("Enter the file path for track request sequence: ")
    track_requests = get_track_requests(file_path)

    disk_size = 200  # Default disk size; can be modified if required.

    # Execute FCFS algorithm
    total_fcfs, service_fcfs = simulate_fcfs(initial_position, track_requests, disk_size)
    display_results("First-Come, First-Served (FCFS)", total_fcfs, service_fcfs)

    # Execute C-SCAN algorithm
    total_c_scan, service_c_scan = simulate_c_scan(initial_position, track_requests, disk_size)
    display_results("Circular SCAN (C-SCAN)", total_c_scan, service_c_scan)

    # Execute C-LOOK algorithm
    total_c_look, service_c_look = simulate_c_look(initial_position, track_requests, disk_size)
    display_results("Circular LOOK (C-LOOK)", total_c_look, service_c_look)

if __name__ == "__main__":
    main()
