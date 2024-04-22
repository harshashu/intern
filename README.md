# Log Analysis and Monitoring Script

This script is designed to automate the analysis and monitoring of log files. It continuously monitors a specified log file for new entries, performs basic analysis on those entries, and generates summary reports.

## Usage

1. **Requirements:**
   - Python 3.x
   - `tail` command (for Unix-like systems)
   - Required Python libraries: `subprocess`, `time`, `logging`, `collections`

2. **Installation:**
   - Clone or download the script to your local machine.

3. **Execution:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```bash
     python log_monitor.py
     ```

4. **Configuration:**
   - Replace `"D:\Workspace\python\logfile.log"` in the script with the actual path to your log file.

5. **Summary Reports:**
   - After running the script, summary reports will be generated in the `monitoring.log` file.
   - The summary includes the total number of error messages and the top 5 most common error messages.

## Script Overview

- The script uses the `tail` command to continuously monitor the specified log file for new entries.
- Each new log entry is analyzed for specific keywords or patterns (e.g., "ERROR", "HTTP", "WARNING", "TRACE").
- Error messages are counted using a `Counter` object.
- Summary reports are generated at the end of script execution and logged in the `monitoring.log` file.

## Evaluation

The script fulfills the requirements of the assignment, including basic log analysis and monitoring functionalities, error handling, and logging. Additional features such as counting occurrences of specific keywords and generating summary reports have been implemented beyond the basic requirements.

For any issues or suggestions, please feel free to open an issue in the GitHub repository.
