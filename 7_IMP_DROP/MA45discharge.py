import pandas as pd
import matplotlib.pyplot as plt

# Read the .dat file into a DataFrame
file_qken = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QKennedybruecke.dat"
file_qmau = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QMauerbachstrasse.dat"
file_qobe = "/Users/lnx/DATA/obs_point/land/MA45_WienerGewaesser/QOberlaa.dat"

#filenames = [file_qken, file_qmau, file_qobe]

# Dictionary of filenames and corresponding information
file_info = {
    file_qken: {
        'skiprows': 26,
        'river': 'Wienfluss',
        'station': 'Kennedybruecke'
    },
    file_qmau: {
        'skiprows': 23,
        'river': 'Mauerbach',
        'station': 'Mauerbachstrasse'
    },
    file_qobe: {
        'skiprows': 23,
        'river': 'Liesingbach',
        'station': 'Oberlaa'
    }
}
# Define time slices
Present1_start = '2004-7-15'
Present2_end = '2004-7-26'
Messperiode_start = '2022-8-10'
Messperiode_end = '2022-8-20'
RCP85_start = '2021-6-9'
RCP85_end = '2021-6-20'
RCP26_start = '2018-8-6'
RCP26_end = '2018-8-17'

##PLOT EPISODES
y_min = 0
y_max = 10
# Iterate over the filenames and corresponding information
for filename, info in file_info.items():
    # Read the data from the file
    data = pd.read_csv(filename, skiprows=info['skiprows'], delimiter='\s+', names=['Date', 'Time', 'Data'], encoding='latin-1')
    # Combine 'Date' and 'Time' columns into a single datetime column
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d.%m.%Y %H:%M:%S')

    # Filter data for Messperiode
    data_messperiode = data[(data['Datetime'] >= Messperiode_start) & (data['Datetime'] <= Messperiode_end)]
    # Filter data for RCP85
    data_rcp85 = data[(data['Datetime'] >= RCP85_start) & (data['Datetime'] <= RCP85_end)]

    # Create separate figures for Messperiode and RCP85
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot combined data for Messperiode
    ax1.plot(data_messperiode['Datetime'], data_messperiode['Data'], label=f"{info['river']} - {info['station']}")
    ax1.set_title("Messperiode")
    ax1.set_xlabel('Datetime')
    ax1.set_ylabel('Data (m³/s)')
    ax1.grid(True)
    ax1.legend()
    ax1.set_ylim(y_min, y_max)


    # Plot combined data for RCP85
    ax2.plot(data_rcp85['Datetime'], data_rcp85['Data'], label=f"{info['river']} - {info['station']}")
    ax2.set_title("RCP85")
    ax2.set_xlabel('Datetime')
    ax2.set_ylabel('Data (m³/s)')
    ax2.grid(True)
    ax2.legend()
    ax2.set_ylim(y_min, y_max)


    # Adjust layout and display the figures
    plt.tight_layout()
    plt.show()

exit()

##PLOT EPISODES OLD VERSION
# Initialize lists to store combined data for each episode
messperiode_data = []
rcp85_data = []

# Initialize lists to store labels
messperiode_labels = []
rcp85_labels = []

# Iterate over the filenames and corresponding information
for filename, info in file_info.items():
    # Read the data from the file
    data = pd.read_csv(filename, skiprows=info['skiprows'], delimiter='\s+', names=['Date', 'Time', 'Data'], encoding='latin-1')
    # Combine 'Date' and 'Time' columns into a single datetime column
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d.%m.%Y %H:%M:%S')
    # Convert 'Data' column to numeric
    data['Data'] = pd.to_numeric(data['Data'], errors='coerce')

    # Filter data for Messperiode
    data_messperiode = data[(data['Datetime'] >= Messperiode_start) & (data['Datetime'] <= Messperiode_end)]
    # Filter data for RCP85
    data_rcp85 = data[(data['Datetime'] >= RCP85_start) & (data['Datetime'] <= RCP85_end)]
    
    # Append filtered data to lists
    messperiode_data.append(data_messperiode)
    rcp85_data.append(data_rcp85)

    # Add labels
    messperiode_labels.append(f"{info['river']} - {info['station']}")
    rcp85_labels.append(f"{info['river']} - {info['station']}")

    # Calculate the mean of the 'Data' column
    mean_data_mess = data_messperiode['Data'].mean()
    mean_data_rcp85 = data_rcp85['Data'].mean()
    print("Mean of the data, 10.-20. Aug 2022 (measurement period):", mean_data_mess)
    print("Mean of the data, 9.-20. Jun 2021 (rcp85 period):", mean_data_rcp85)

# Combine data from all files for each episode
messperiode_combined = pd.concat(messperiode_data)
rcp85_combined = pd.concat(rcp85_data)

# Create separate figures for Messperiode and RCP85
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot combined data for Messperiode
ax1.plot(messperiode_combined['Datetime'], messperiode_combined['Data'], label=', '.join(messperiode_labels))
ax1.set_title("Messperiode")
ax1.set_xlabel('Datetime')
ax1.set_ylabel('Data (m³/s)')
ax1.grid(True)
ax1.legend()

# Plot combined data for RCP85
ax2.plot(rcp85_combined['Datetime'], rcp85_combined['Data'], label=', '.join(rcp85_labels))
ax2.set_title("RCP85")
ax2.set_xlabel('Datetime')
ax2.set_ylabel('Data (m³/s)')
ax2.grid(True)
ax2.legend()


# Adjust layout and display the figures
plt.tight_layout()
plt.show()

exit()

#PLOT FULL DATA SERIES
# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Iterate over the filenames and corresponding information
for filename, info in file_info.items():
    # Read the data from the file
    data = pd.read_csv(filename, skiprows=info['skiprows'], delimiter='\s+', names=['Date', 'Time', 'Data'], encoding='latin-1')
    # Combine 'Date' and 'Time' columns into a single datetime column
    data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d.%m.%Y %H:%M:%S')
    # Convert 'Data' column to numeric
    data['Data'] = pd.to_numeric(data['Data'], errors='coerce')
    # Calculate the mean of the 'Data' column
    mean_data = data['Data'].mean()
    print("Mean of the data:", mean_data)
    # Plot the data
    ax.plot(data['Datetime'], data['Data'], label=f"{info['river']} - {info['station']}")

# Set labels and title
ax.set_xlabel('Datetime')
ax.set_ylabel('Data (m³/s)')
ax.set_title('Data over Time')
ax.grid(True)

# Add legend
ax.legend()

# Show plot
plt.show()

exit()



