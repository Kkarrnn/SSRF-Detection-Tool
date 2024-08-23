# SSRF Detection Tool 🔒

## Overview
The **SSRF Detection Tool** is a Python-based script developed for use in Visual Studio, designed to identify Server-Side Request Forgery (SSRF) vulnerabilities in web applications. This tool assists security professionals and developers in finding and mitigating SSRF issues, which can enable attackers to manipulate server-side requests.

## Features
- **Automated Detection**: Scans target URLs for potential SSRF vulnerabilities by sending crafted requests.
- **Custom Payloads**: Includes a variety of SSRF payloads to test different attack vectors.
- **Detailed Reporting**: Outputs clear and detailed reports on detected vulnerabilities directly within Visual Studio.

## Prerequisites
- **Python**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/)
- **Visual Studio**: Install Visual Studio with Python support. [Download Visual Studio](https://visualstudio.microsoft.com/)

## Installation
1. **Clone the Repository**:
    - Open Visual Studio.
    - Go to **File > Clone Repository**.
    - Enter the repository URL:
    ```bash
    https://github.com/YourGitHubUsername/ssrf-detection-tool.git
    ```
2. **Set Up the Environment**:
    - In Visual Studio, open the cloned project.
    - Go to **Python Environments** in the Solution Explorer.
    - Select your Python environment or create a new one.
    - Install dependencies using the terminal within Visual Studio:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Script**:
    - In Visual Studio, open the `detect_ssrf.py` file.
    - Modify the script if necessary to target the desired URL.
    - Start debugging or run the script using **F5** or the **Run** button.
    - To scan a specific URL, modify the command in the script:
    ```python
    target_url = "http://example.com/vulnerable-endpoint"
    ```
2. **View Results**:
    - The script will output the results directly in the Visual Studio terminal, indicating whether an SSRF vulnerability was detected.

## Customization
- **Adding Payloads**: You can add your own SSRF payloads by editing the `ssrf_payloads.txt` file.
- **Adjusting Detection Logic**: Modify the `detect_ssrf` function in `detect_ssrf.py` to tweak the detection logic according to your needs.


  ## Contact
  - **GitHub**: [Kkarrnnb](https://github.com/Kkarrnn)
