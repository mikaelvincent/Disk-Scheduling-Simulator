from tabulate import tabulate

def aggregate_statistics(results):
    """
    Aggregate performance statistics for each scheduling algorithm.

    Args:
        results (dict): Dictionary containing results from each scheduling algorithm.
            Format: {algorithm_name: (total_head_movement, service_order)}

    Returns:
        list: List of dictionaries with aggregated statistics for all algorithms.
    """
    statistics = []
    for algorithm, data in results.items():
        stats = {
            "Algorithm": algorithm,
            "Total Head Movement": data[0],
            "Requests Serviced": len(data[1])
        }
        statistics.append(stats)
    return statistics

def display_summary(statistics):
    """
    Display a summary comparison of scheduling algorithm performance.

    Args:
        statistics (list): Aggregated statistics for all algorithms.
    """
    print("\n=== Performance Summary ===")
    headers = ["Algorithm", "Total Head Movement", "Requests Serviced"]
    table = [[stat["Algorithm"], stat["Total Head Movement"], stat["Requests Serviced"]] for stat in statistics]
    print(tabulate(table, headers=headers, tablefmt="grid"))
