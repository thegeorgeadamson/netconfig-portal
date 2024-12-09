# Netconfig Portal for Cisco and Juniper

### Themed as a macOS Terminal Application

This project is designed for Nucor but can be customized to suit your needs.

## Features

- **Supports Cisco and Juniper devices:** 
  - Compatible with Cisco IOS, IOS XE, NX-OS, and Juniper.
- **User-friendly interface:**
  - Simulates a macOS terminal for an intuitive experience.
- **Dynamic authentication flow:**
  - Guides users step-by-step to connect and execute commands.
- **Customizable:**
  - Easily adaptable to other brands or preferences.

## Requirements

- Python 3.8 or later
- Flask
- Netmiko

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/netconfig-portal.git
   cd netconfig-portal
   ```
2. Install dependencies:
   ```bash
   pip install Flask Netmiko
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Usage

1. Follow the on-screen prompts to:
   - Select your device type.
   - Enter the device's IP address, username, and password.
   - Execute your desired command.
2. View the command output directly in the terminal-like interface.

## Customization

### To Change the Theme
Modify the `styles.css` file in the `static` folder. For example:
- Update colors, fonts, or layout to suit your preferences.

### To Extend Device Support
Edit the `app.py` file to add more `device_type` options supported by Netmiko.