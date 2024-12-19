import serial
import csv
import time
import matplotlib.pyplot as plt
import pandas as pd

# Set up the serial port for Arduino Mega on COM4
ser = serial.Serial('COM4', 9600, timeout=1)

# Allow time for the serial connection to establish
time.sleep(3)

# Ask the user for the filename
filename = input("Enter the filename for the CSV file (without extension): ") + '.csv'

# Ask the user for the duration in seconds
duration = int(input("Enter the duration for data gathering in seconds: "))

# Open the CSV file to save the data
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header row
    csvwriter.writerow(["MQ2", "MQ3", "MQ4", "MQ5", "MQ6", "MQ7", "MQ8", "MQ9", "MQ135", "MQ137"])

    start_time = time.time()
    
    try:
        while (time.time() - start_time) < duration:
            # Read a line of data from COM4
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if line:
                # Split the comma-separated values
                data = line.split(',')
                
                # Check if the data has the correct number of fields (10 fields)
                if len(data) == 10:
                    # Write the sensor values to the CSV file
                    csvwriter.writerow(data)
                    print(data)
                else:
                    print(f"Skipped invalid data: {data}")

    except KeyboardInterrupt:
        print("Data collection stopped by user.")

# Close the serial port
ser.close()

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Create a time axis (in seconds)
df['Time'] = range(1, len(df) + 1)

# Create a 5x2 subplot layout
fig, axs = plt.subplots(2, 5, figsize=(20, 10))  # Adjust the width and height

# Sensor names corresponding to their subplot positions
sensor_names = ["MQ2", "MQ3", "MQ4", "MQ5", "MQ6", "MQ7", "MQ8", "MQ9", "MQ135", "MQ137"]

# Plot each sensor's data
for i, sensor in enumerate(sensor_names):
    row = i // 5  # Determine the row (0 for top, 1 for bottom)
    col = i % 5   # Determine the column (0 to 4)
    axs[row, col].plot(df['Time'], df[sensor], label=sensor)
    axs[row, col].set_title(f'{sensor} Readings Over Time')
    axs[row, col].set_xlabel('Time (seconds)')
    axs[row, col].set_ylabel('Sensor Value')
    axs[row, col].set_ylim(0, 800)  # Fix y-axis scaling from 0 to 800
    axs[row, col].legend(loc='upper right')
    axs[row, col].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
