import subprocess
import time
import logging
from collections import Counter

# Configure logging
logging.basicConfig(filename='monitoring.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Counter for error messages
error_counter = Counter()

def monitor_log(log_file_path):
    try:
        logging.info(f"Monitoring log file: {log_file_path}")
        process = subprocess.Popen(['tail', '-F', log_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in iter(process.stdout.readline, b''):
            line = line.decode('utf-8').strip()
            logging.info(f"New log entry: {line}")
            analyze_log_line(line)
    except KeyboardInterrupt:
        logging.info("Log monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Error occurred while monitoring log: {str(e)}")
    finally:
        process.kill()

def analyze_log_line(log_line):
    # Count occurrences of specific keywords or patterns
    if "ERROR" in log_line:
        error_counter.update(["ERROR"])  # Increment error counter
    elif "HTTP" in log_line:
        error_counter.update(["HTTP"])  # Increment HTTP counter
    elif "WARNING" in log_line:
        error_counter.update(["WARNING"])  # Increment WARNING counter
    elif "TRACE" in log_line:
        error_counter.update(["TRACE"])  # Increment TRACE counter
    else:
        # Add more conditions for other keywords or patterns as needed
        pass

if __name__ == "__main__":
    log_file_path = "D:\Workspace\python\logfile.log"  # Replace with your actual log file path
    monitor_log(log_file_path)

    # Generate summary reports
    logging.info("Summary Report:")
    logging.info(f"Total Error Messages: {sum(error_counter.values())}")
    logging.info("Top Error Messages:")
    for error_message, count in error_counter.most_common(5):  # Get top 5 error messages
        logging.info(f"{error_message.strip()}: {count}")
