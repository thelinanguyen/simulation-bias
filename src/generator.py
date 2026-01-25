import numpy as np

def generate_sensor_data(duration=100, sampling_rate=10, bias_type='none'):
    """
    Simulates a sensor with optional BIAS (Faults).
    
    Args:
        bias_type: 'none', 'drift' (gradual failure), or 'shift' (sudden jump).
    """
    time = np.linspace(0, duration, duration * sampling_rate)
    
    # 1. The True Signal
    base_signal = 50 + 5 * np.sin(0.5 * time) 
    
    # 2. Add Bias (The Sabotage)
    if bias_type == 'drift':
        # The sensor slowly loses calibration (-0.1 degree per second)
        # This mimics a "Sampling Bias" where data changes over time
        bias_effect = -0.1 * time 
        base_signal = base_signal + bias_effect
    elif bias_type == 'shift':
        # Sudden jump at t=50 (mimics someone bumping the machine)
        bias_effect = np.where(time > 50, 10, 0)
        base_signal = base_signal + bias_effect

    # 3. Add Noise
    noise = np.random.normal(0, 1.5, size=len(time))
    sensor_data = base_signal + noise
    
    return time, base_signal, sensor_data

if __name__ == "__main__":
    t, s, d = generate_sensor_data(bias_type='drift')
    print(f"Generated biased data. End signal is {s[-1]:.2f}°C")