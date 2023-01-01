import matplotlib.pyplot as plt
import matplotlib.animation as animation
import psutil
import time

# Set the refresh rate (in seconds)
refresh_rate = 1

# Initialize the figure and axes
fig, ax = plt.subplots()

# Initialize lists to store the data
times = []
tcp_traffic_data = []

# Function to get the TCP traffic data
def get_tcp_traffic_data():
  # Get the TCP traffic data using the psutil library
  tcp_traffic = psutil.net_io_counters(pernic=True)['Ethernet'].bytes_sent + psutil.net_io_counters(pernic=True)['Ethernet'].bytes_recv
  return tcp_traffic

# Function to update the plot
def update_plot(i):
  # Get the current time and traffic data
  current_time = time.strftime("%H:%M:%S")
  current_tcp_traffic = get_tcp_traffic_data()
  
  # Add the data to the lists
  times.append(current_time)
  tcp_traffic_data.append(current_tcp_traffic)
  
  print("times:", times)
  print("tcp_traffic_data:", tcp_traffic_data)
  
  # Clear the previous plot
  ax.clear()
  
  # Plot the data
  ax.plot(times, tcp_traffic_data)
  
  print("times:", times)
  print("tcp_traffic_data:", tcp_traffic_data)
  
  # Set the x and y limits
  ax.set_xlim(left=max(0, len(times) - 10), right=len(times) + 1)
  ax.set_ylim(bottom=0)
  
  # Add labels and a title
  ax.set_xlabel("Time (seconds)")
  ax.set_ylabel("Traffic (bytes)")
  ax.set_title("Real-time TCP Traffic")




# Set the animation
ani = animation.FuncAnimation(fig, update_plot, interval=refresh_rate*1000)

# Show the plot
plt.show()
