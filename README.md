# VulnScan-
The Network Port Scanner Tool is a simple yet powerful Python-based utility designed for network security professionals and enthusiasts. This tool allows users to scan a specified range of ports on a given target URL or IP address to identify open and closed ports.

How to Download and Use the Network Port Scanner Tool
You can easily download and use the Network Port Scanner Tool from GitHub. Below are the steps for installation and usage on all major operating systems: Windows, macOS, and Linux.

Step 1: Install Git
If you haven't installed Git yet, you will need it to clone the repository.

Windows: Download from Git for Windows and follow the installation instructions.
macOS: You can install Git using Homebrew. Open Terminal and run:
bash
Copier le code
brew install git
Linux: Most distributions have Git pre-installed. If not, you can install it via your package manager:
bash
Copier le code
sudo apt-get install git  # For Debian/Ubuntu
sudo yum install git      # For CentOS/RHEL
Step 2: Clone the Repository
Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux) and run the following command:

bash
Copier le code
git clone https://github.com/Mr-Najm-Ouchen/VulnScan-.git
This command will download the repository to your local machine.

Step 3: Navigate to the Directory
Change to the directory where the tool has been downloaded:

bash
Copier le code
cd VulnScan-
Step 4: Install Python
Make sure you have Python installed. You can download it from python.org.

Windows: Download the installer and make sure to check "Add Python to PATH" during installation.
macOS/Linux: Python is usually pre-installed. You can check by running:
bash
Copier le code
python3 --version
If Python is not installed, you can install it using Homebrew on macOS:

bash
Copier le code
brew install python
Or on Ubuntu/Debian:

bash
Copier le code
sudo apt-get install python3
Step 5: Run the Tool
You can now run the tool by executing the following command:

bash
Copier le code
python3 VulnScan.py
(Note: On Windows, you may use python instead of python3.)

Usage Instructions
When prompted, enter the target URL (without http:// or https://).

Example: example.com
Enter the starting port number (e.g., 1 for starting from the first port).

Enter the ending port number (e.g., 1024 to scan up to the 1024th port).

Enter the path for the output file (where you want to save the scan results, e.g., scan_results.json).

The tool will begin scanning the specified range of ports on the target URL and will display the results in the terminal. The scan results will also be saved in the specified output file.

Example Commands
On Windows:

bash
Copier le code
python VulnScan.py
On macOS/Linux:

bash
Copier le code
python3 VulnScan.py
