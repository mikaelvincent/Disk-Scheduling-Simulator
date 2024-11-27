def aggregate_statistics(results):
    """
    Aggregate performance statistics for each scheduling algorithm.

    Args:
        results (dict): Dictionary containing results from each scheduling algorithm.
            Format: {algorithm_name: (total_head_movement, service_order)}

    Returns:
        dict: Aggregated statistics for all algorithms.
    """
    statistics = {
        algorithm: {
            "Total Head Movement": data[0],
            "Number of Serviced Requests": len(data[1])
        }
        for algorithm, data in results.items()
    }
    return statistics

def display_summary(statistics):
    """
    Display a summary comparison of scheduling algorithm performance.

    Args:
        statistics (dict): Aggregated statistics for all algorithms.
    """
    print("\n=== Performance Summary ===")
    print(f"{'Algorithm':<30}{'Total Head Movement':<25}{'Requests Serviced':<20}")
    print("-" * 75)
    for algorithm, data in statistics.items():
        print(f"{algorithm:<30}{data['Total Head Movement']:<25}{data['Number of Serviced Requests']:<20}")
    print("\n")
