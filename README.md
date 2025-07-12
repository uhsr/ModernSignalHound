# ModernSignalHound: A Python Interface for Signal Hound Spectrum Analyzers

ModernSignalHound provides a modern and efficient Python interface for controlling and acquiring data from Signal Hound spectrum analyzers. It aims to simplify the process of integrating Signal Hound devices into Python-based measurement and automation workflows, offering a higher-level abstraction than the native API while retaining flexibility and performance.

This project addresses the common challenges faced when working directly with the Signal Hound API, such as complex configuration settings and low-level data handling. ModernSignalHound offers a streamlined approach, allowing users to quickly configure their spectrum analyzer, initiate sweeps, and retrieve data in a readily usable format. The library focuses on providing a robust and well-documented interface for developers seeking to leverage the power of Signal Hound devices within a modern Python environment. It supports common tasks such as frequency sweeping, signal monitoring, and data analysis, making it suitable for a wide range of applications including RF testing, spectrum monitoring, and educational purposes.

ModernSignalHound is designed with modularity and extensibility in mind. The core library provides fundamental functionality, while additional modules can be easily added to support specific use cases or device models. We encourage community contributions to expand the library's capabilities and ensure its continued relevance in the evolving landscape of RF measurement technology. This project prioritizes clear documentation, comprehensive testing, and adherence to Python best practices to ensure a stable and user-friendly experience.

Key Features:

*   **Simplified Device Configuration:** Abstracts away the complexities of the Signal Hound API with a high-level configuration interface, allowing users to quickly set parameters such as center frequency, span, resolution bandwidth (RBW), and video bandwidth (VBW) using Pythonic syntax.
*   **Automated Data Acquisition:** Provides functions for initiating sweeps and retrieving I/Q data or power spectrum data directly into NumPy arrays, eliminating the need for manual data conversion and formatting. For example, the `get_sweep()` function returns a NumPy array containing the measured power levels for each frequency point.
*   **Error Handling and Logging:** Implements robust error handling and logging mechanisms to facilitate debugging and troubleshooting. All function calls are wrapped in try-except blocks to catch potential exceptions raised by the Signal Hound API, and detailed error messages are logged to a file.
*   **Multi-Device Support:** Allows control of multiple Signal Hound devices simultaneously, enabling parallel measurements and synchronized data acquisition. Each device is represented by a separate object, and the library ensures proper resource management and synchronization between devices.
*   **Frequency Domain Analysis:** Offers built-in functions for performing basic frequency domain analysis, such as peak detection, signal averaging, and noise floor estimation. These functions leverage NumPy and SciPy for efficient data processing.
*   **IQ Data Streaming (Experimental):** Includes experimental support for real-time IQ data streaming, enabling applications such as software-defined radio (SDR) and advanced signal analysis. The streaming interface provides a continuous flow of IQ samples that can be processed in real-time.
*   **Spectrum Masking:** Allows the setting of spectrum masks and generation of pass/fail results. Users can define upper and lower limits for the spectrum and automatically determine if the measured signal falls within the defined mask.

Technology Stack:

*   **Python 3.7+:** The core programming language used for development, ensuring compatibility with modern Python features and libraries.
*   **NumPy:** A fundamental library for numerical computing in Python, used for efficient array manipulation and mathematical operations on acquired data.
*   **SciPy:** A library for scientific computing in Python, providing advanced signal processing and analysis functions.
*   **Signal Hound API (provided by Signal Hound):** The underlying C-based API used to communicate with the Signal Hound spectrum analyzers. This library provides a Python wrapper around the C API.
*   **Logging:** A built-in Python module used for logging events and errors, facilitating debugging and troubleshooting.

Installation:

1.  Ensure you have Python 3.7 or later installed on your system.
2.  Install the Signal Hound device drivers according to the manufacturer's instructions.
3.  Install the required Python packages using pip:
    `pip install numpy scipy`
4.  Download the ModernSignalHound repository from GitHub.
5.  Navigate to the downloaded directory.
6.  Install the ModernSignalHound package:
    `python setup.py install`

Configuration:

ModernSignalHound relies on the Signal Hound API for device communication. Ensure the necessary environment variables are set correctly, including any paths to the Signal Hound DLLs. A recommended approach is to add the directory containing the `sa_api.dll` to your system's PATH environment variable. Alternatively, you can specify the path to the DLL within the Python code using the `ctypes.cdll.LoadLibrary()` function if necessary. Specific configuration parameters, such as default RBW and VBW values, can be set within the `config.py` file.

Usage:

Here's a basic example of how to use ModernSignalHound to perform a spectrum sweep:

import ModernSignalHound as sh

# Connect to the Signal Hound device
device = sh.Device()

# Configure the spectrum analyzer
device.center_frequency = 2.45e9  # Set center frequency to 2.45 GHz
device.span = 10e6  # Set span to 10 MHz
device.rbw = 10e3  # Set resolution bandwidth to 10 kHz

# Initiate a sweep and retrieve the data
frequencies, power_levels = device.get_sweep()

# Process the data (e.g., plot the spectrum)
# (Requires matplotlib)
# import matplotlib.pyplot as plt
# plt.plot(frequencies, power_levels)
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Power (dBm)")
# plt.show()

# Disconnect from the device
device.disconnect()

Contributing:

We welcome contributions to ModernSignalHound. Please follow these guidelines:

1.  Fork the repository and create a branch for your changes.
2.  Ensure your code adheres to the PEP 8 style guide.
3.  Write comprehensive unit tests for your code.
4.  Submit a pull request with a clear description of your changes.

License:

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/ModernSignalHound/blob/main/LICENSE) file for details.

Acknowledgements:

We would like to thank Signal Hound for providing the underlying API and for their support in developing this project.