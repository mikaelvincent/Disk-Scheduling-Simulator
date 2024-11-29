def simulate_c_look(initial_position, track_requests, disk_size):
    """
    Simulate the C-LOOK (Circular LOOK) disk scheduling algorithm.

    Args:
        initial_position (int): The starting position of the disk arm.
        track_requests (list of int): The sequence of track requests.
        disk_size (int): The total number of tracks on the disk.

    Returns:
        tuple:
            - total_head_movement (int): The total movement of the disk head.
            - service_order (list of int): The order in which tracks are serviced.
    """
    sorted_requests = sorted(track_requests)
    service_order = []
    total_head_movement = 0
    current_position = initial_position

    print("\nC-LOOK Simulation:")
    print(f"Initial Position: {initial_position}")
    print(f"Track Requests: {sorted_requests}")

    # Split the requests into two parts
    left = [track for track in sorted_requests if track < current_position]
    right = [track for track in sorted_requests if track >= current_position]

    # Service the right side first
    for track in right:
        movement = abs(track - current_position)
        total_head_movement += movement
        print(f"Moving from {current_position} to {track}, Movement: {movement}")
        current_position = track
        service_order.append(track)

    # Jump to the first request on the left side
    if left:
        movement = abs(current_position - left[0])
        total_head_movement += movement
        print(f"Jumping from {current_position} to {left[0]}, Movement: {movement}")
        current_position = left[0]
        service_order.append(current_position)

        # Service the rest of the left side
        for track in left[1:]:
            movement = abs(track - current_position)
            total_head_movement += movement
            print(f"Moving from {current_position} to {track}, Movement: {movement}")
            current_position = track
            service_order.append(track)

    print(f"C-LOOK Total Head Movement: {total_head_movement}")

    return total_head_movement, service_order
