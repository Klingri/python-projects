# The 'psutil' library is used to get system information.
# If you don't have it, you can install it using: pip install psutil
import psutil
# The 'datetime' library is used to get a timestamp for each log entry.
import datetime
# The 'time' library is used to set the monitoring interval.
import time

def log_performance(interval_seconds=5, log_file="performance.log"):
    """
    Monitors system performance (CPU and memory usage) and logs it to a file.

    Args:
        interval_seconds (int): The time in seconds between each log entry.
        log_file (str): The name of the file to write the logs to.
    """
    # Open the log file in append mode. This will create the file if it doesn't exist.
    print(f"Starting performance monitoring. Logging to {log_file} every {interval_seconds} seconds. Press Ctrl+C to stop.")
    with open(log_file, "a") as f:
        # Write the header for the log file.
        f.write("Timestamp,CPU_Usage_%,Memory_Usage_%\n")

        try:
            # Loop indefinitely to continuously monitor the system.
            while True:
                # Get the current CPU usage as a percentage. The interval=1 argument is needed for an accurate reading.
                cpu_usage = psutil.cpu_percent(interval=1)

                # Get the current memory usage information.
                memory_info = psutil.virtual_memory()
                # Calculate the memory usage as a percentage.
                memory_usage = memory_info.percent

                # Get the current timestamp.
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Create the log entry string.
                log_entry = f"{timestamp},{cpu_usage},{memory_usage}\n"

                # Write the log entry to the file.
                f.write(log_entry)
                # Flush the file buffer to ensure data is written immediately.
                f.flush()

                # Print the log entry to the console for real-time viewing.
                print(log_entry.strip())

                # Wait for the specified interval before the next reading.
                time.sleep(interval_seconds)

        except KeyboardInterrupt:
            # Handle the user pressing Ctrl+C to stop the script.
            print("Monitoring stopped.")
        except Exception as e:
            # Handle any other exceptions that might occur.
            print(f"An error occurred: {e}")

# This check ensures the function is called only when the script is executed directly.
if __name__ == "__main__":
    log_performance(interval_seconds=5)
