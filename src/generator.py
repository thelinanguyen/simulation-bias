import numpy as np

def generate_sensor_data(duration=100, sampling_rate=10):
  """
  Simulates a temperature sensoron a robot arm.
  
  Args:
    duration (int): How many seonds to record.
    sampling_rate (int): How many timmes/per second we measure (Hz).
    
  Returns:
    time, perfect_signal, noisy_reading
  """
  
  #1 . THE CLOCK (Time array)
  # Creating an array of timestamps from 0 to 100 seconds
  time = np.linspace(0, duration, duration * sampling_rate)

  #2. THE SIGNAL 
  # A sine wave signal to simulate temperature changes
  # Base temp = 50 degrees celcius, Amplitude = 5 degrees, Frequency = 0.1 Hz
  base_signal = 50 + 5 * np.sin(0.5 * time)

  #3. THE NOISE
  # Random noise to simulate sensor inaccuracies
  # Gaussian noise with mean = 0 and standard deviation = 0.6 degrees
  noise = np.random.normal(0, 0.6, size=len(time))

  #4. THE SENSOR READING
  # Signal + Noise = What we actually see on the monitor
  sensor_data = base_signal + noise

  return time, base_signal, sensor_data

# This block only runs if this file is executed directly (for testing)
if __name__ == "__main__":
    print("--- Testing Generator Module ---")
    t, s, d = generate_sensor_data()
    print(f"Success! Generated {len(t)} data points.")
    print(f"Sample Reading at 0s: {d[0]:.2f}°C")
    print("--------------------------------")