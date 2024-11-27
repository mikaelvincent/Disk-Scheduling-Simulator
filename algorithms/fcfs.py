def simulate_fcfs(initial_position, track_requests, disk_size):
    """
    Simulate the First-Come, First-Served (FCFS) disk scheduling algorithm.

    Args:
        initial_position (int): The starting position of the disk arm.
        track_requests (list of int): The sequence of track requests.
        disk_size (int): The total number of tracks on the disk.

    Returns:
        tuple:
            - total_head_movement (int): The total movement of the disk head.
            - service_order (list of int): The order in which tracks are serviced.
    """
    service_order = []
    total_head_movement = 0
    current_position = initial_position

    for track in track_requests:
        service_order.append(track)
        movement = abs(track - current_position)
        total_head_movement += movement
        current_position = track

    return total_head_movement, service_order
