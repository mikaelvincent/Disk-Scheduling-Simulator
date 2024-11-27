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
