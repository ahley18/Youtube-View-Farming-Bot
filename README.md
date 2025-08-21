# YouTube View Farming Bot

A Python-based automation tool designed to simulate user interactions on YouTube Shorts by automatically moving the cursor, scrolling, and refreshing content at predefined intervals.

## ⚠️ **IMPORTANT DISCLAIMER**

**This tool is for educational and research purposes only. Using automated bots to artificially inflate view counts on YouTube may violate YouTube's Terms of Service and could result in:**

- Account suspension or termination
- Legal consequences
- Violation of platform policies
- Potential harm to content creators and the platform ecosystem

**Use at your own risk and ensure compliance with all applicable terms of service and laws.**

## 🚀 Features

- **Automated Cursor Movement**: Moves cursor to predefined screen coordinates
- **Auto-scrolling**: Automatically scrolls up and down on YouTube Shorts
- **Content Refresh**: Refreshes YouTube content at regular intervals
- **Configurable Timing**: Adjustable delays between actions
- **Multi-position Support**: Works with multiple screen positions simultaneously
- **Cursor Tracking**: Utility to track and record cursor positions

## 📁 Project Structure

```
├── bot.py              # Main automation script
├── refresher.py        # Content refresh functionality
├── cursor_tracker.py   # Cursor position tracking utility
├── venv/              # Python virtual environment
└── __pycache__/       # Python cache files
```

## 🛠️ Requirements

- Python 3.7+
- Windows OS (due to pyautogui compatibility)
- Required Python packages (see Installation section)

## 📦 Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd youtube-view-farming-bot
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install pyautogui keyboard
   ```

## ⚙️ Configuration

### Main Bot Settings (`bot.py`)

- **Screen Coordinates**: Modify the `x` and `y` arrays to match your screen resolution and desired click positions
- **Time Interval**: Adjust `time_seconds` variable to change delays between actions
- **YouTube Link**: Update `yt_link` variable with your target YouTube channel/shorts URL

### Current Default Settings
```python
x = [370, 900, 1400, 370, 900, 1400]  # X coordinates
y = [300, 300, 300, 700, 700, 700]    # Y coordinates
time_seconds = 60                       # 60-second intervals
yt_link = "https://www.youtube.com/@cla_sterling8633/shorts"
```

## 🎯 Usage

### 1. Main Bot (`bot.py`)
```bash
python bot.py
```
The main bot will:
- Refresh YouTube content every 6 cycles
- Perform scrolling operations (down then up)
- Move cursor to predefined positions
- Automatically repeat the cycle

### 2. Cursor Position Tracker (`cursor_tracker.py`)
```bash
python cursor_tracker.py
```
Use this utility to:
- Track and record cursor positions in real-time
- Find optimal coordinates for your screen setup
- Press `Ctrl+C` to stop tracking

### 3. Content Refresher (`refresher.py`)
```bash
python refresher.py
```
Standalone script for:
- Clicking at specific positions
- Simulating keyboard shortcuts (Ctrl+E, Ctrl+V, Enter)
- Refreshing content manually

## 🔧 Customization

### Adjusting Screen Coordinates
1. Run `cursor_tracker.py` to find desired positions
2. Update the `x` and `y` arrays in `bot.py`
3. Test with small values first

### Modifying Timing
- Change `time_seconds` for different intervals
- Adjust `time.sleep()` values for faster/slower operations

### Adding New Functions
- Extend the main loop in `bot.py`
- Create new automation functions as needed
- Ensure proper error handling and delays

## ⚠️ Safety Features

- **5-second startup delay** before automation begins
- **Configurable delays** between actions to avoid detection
- **Keyboard interrupt support** (Ctrl+C to stop)
- **Position validation** to prevent out-of-bounds clicks

## 🚨 Troubleshooting

### Common Issues

1. **Cursor not moving to expected positions**
   - Check screen resolution compatibility
   - Verify coordinate values are within screen bounds
   - Ensure no other applications are interfering

2. **Actions too fast/slow**
   - Adjust `time.sleep()` values
   - Modify `time_seconds` variable
   - Check system performance

3. **Package import errors**
   - Ensure virtual environment is activated
   - Reinstall required packages
   - Check Python version compatibility

### Performance Tips

- Close unnecessary applications
- Ensure stable internet connection
- Monitor system resources
- Use appropriate delays to avoid detection

## 📋 Dependencies

- **pyautogui**: Cross-platform GUI automation
- **keyboard**: Keyboard input simulation
- **time**: Built-in Python timing functions

## 🔒 Security Considerations

- Never share your YouTube credentials
- Use on dedicated/test accounts only
- Monitor for unusual account activity
- Respect platform rate limits

## 📚 Legal and Ethical Notes

- This tool is for educational purposes
- Respect YouTube's Terms of Service
- Consider the impact on content creators
- Use responsibly and ethically

## 🤝 Contributing

This is an educational project. If you have suggestions for improvements or find bugs, please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is provided as-is for educational purposes. Users are responsible for ensuring compliance with all applicable laws and terms of service.

## ⚡ Quick Start

1. Install dependencies: `pip install pyautogui keyboard`
2. Configure coordinates in `bot.py`
3. Run: `python bot.py`
4. Press `Ctrl+C` to stop

---

**Remember: Use responsibly and in compliance with all platform policies and laws.**
