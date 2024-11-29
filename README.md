# Disk Scheduling Simulator

## Overview

This application simulates various disk scheduling algorithms, including First Come First Serve (FCFS), Circular SCAN (C-SCAN), and Circular LOOK (C-LOOK). It calculates and displays key metrics such as total head movement and the order of serviced requests.

## Installation

Install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Prepare the Input File

Create a text file containing the track request sequence. The sequence should consist of non-negative integers separated by spaces. For example:

```
98 183 37 122 14 124 65 67
```

### 2. Run the Application

Execute the main application script:

```bash
python main.py
```

### 3. Provide Input When Prompted

- **Enter the path to the input file:** Specify the path to your track request sequence file.
- **Enter the initial disk arm position:** Provide the starting position of the disk head as a non-negative integer.
- **Enter the disk size:** Specify the total number of tracks on the disk as a positive integer.
- **Select Scheduling Algorithms:** Choose one or more scheduling algorithms to execute by entering their corresponding numbers:
  - `1`: First-Come, First-Served (FCFS)
  - `2`: Circular SCAN (C-SCAN)
  - `3`: Circular LOOK (C-LOOK)

### 4. View Results

- The application will display the following results for each selected algorithm:
  - **Total Head Movement:** The total distance moved by the disk head.
  - **Service Order:** The order in which track requests were serviced.
- A performance summary comparing the selected algorithms will also be shown.
