import sys
from algorithms.fcfs import simulate_fcfs
from algorithms.c_scan import simulate_c_scan
from algorithms.c_look import simulate_c_look
from statistics import aggregate_statistics, display_summary
from utils.input_handling import get_initial_position, get_track_requests
from utils.display import display_results
from utils.logging import setup_logging

def main():
    """
    Entry point for the Disk Scheduling Simulator application.
    """
    logger = setup_logging()
    logger.info("Starting Disk Scheduling Simulator.")

    print("Welcome to the Disk Scheduling Simulator.")

    initial_position = get_initial_position()
    file_path = input("Enter the file path for track request sequence: ")
    track_requests = get_track_requests(file_path)

    disk_size = 200  # Default disk size; can be modified if required.
    logger.debug(f"Initial disk arm position: {initial_position}")
    logger.debug(f"Track requests: {track_requests}")
    logger.debug(f"Disk size: {disk_size}")

    # Prompt user to select scheduling algorithms
    available_algorithms = {
        '1': 'First-Come, First-Served (FCFS)',
        '2': 'Circular SCAN (C-SCAN)',
        '3': 'Circular LOOK (C-LOOK)'
    }

    print("\nSelect Scheduling Algorithms to Execute:")
    for key, name in available_algorithms.items():
        print(f"{key}. {name}")

    selected_options = input("Enter the numbers of the algorithms to run (comma-separated): ")
    selected_keys = [option.strip() for option in selected_options.split(',') if option.strip() in available_algorithms]

    if not selected_keys:
        logger.warning("No valid algorithms selected. Exiting application.")
        print("No valid algorithms selected. Exiting.")
        sys.exit(0)

    selected_algorithms = {key: available_algorithms[key] for key in selected_keys}
    logger.info(f"Selected algorithms: {selected_algorithms}")

    # Collect results for selected algorithms
    results = {}

    for key, algorithm_name in selected_algorithms.items():
        logger.info(f"Executing algorithm: {algorithm_name}")
        if key == '1':
            total, service = simulate_fcfs(initial_position, track_requests, disk_size, logger)
        elif key == '2':
            total, service = simulate_c_scan(initial_position, track_requests, disk_size, logger)
        elif key == '3':
            total, service = simulate_c_look(initial_position, track_requests, disk_size, logger)
        else:
            continue  # Should not reach here

        results[algorithm_name] = (total, service)
        display_results(algorithm_name, total, service)
        logger.debug(f"{algorithm_name} - Total Head Movement: {total}, Service Order: {service}")

    # Generate and display statistics
    statistics = aggregate_statistics(results)
    display_summary(statistics)
    logger.info("Disk Scheduling Simulator execution completed.")

if __name__ == "__main__":
    main()
