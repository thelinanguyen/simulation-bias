import matplotlib.pyplot as plt

def plot_sensor_data(time, signal, noisy_reading):
  """
  Draws the sensor data graph using MAtplotlib.

  Args:
      time (_type_): the timeline
      signal (_type_): The perfect sine wave signal
      noisy_reading (_type_): The signal with added noise
  """
  #1. Setup the canvas
  plt.figure(figsize=(10,8))
  
  #2. Draw the noise data 
  plt.plot(time, noisy_reading, label='Noisy Sensor Reading', color='green', alpha=0.5)
  
  #3. Draw the perfect signal
  plt.plot(time, signal, label='True Temperature Signal', color='red', linewidth=2)
  
  #4. Add titles and labels
  plt.title("Temperature Sensor")
  plt.xlabel("Time (seconds)")
  plt.ylabel("Temperature (°C)")
  
  plt.legend()
  plt.grid(True, alpha=0.3)
  plt.show()
  
  
  