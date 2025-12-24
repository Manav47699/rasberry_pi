
# What You'll Need

- Raspberry Pi 3 (with power supply and microSD card—8GB or bigger).
- Your PC (Windows, Mac, or Linux like Ubuntu).
- Internet connection (same network for PC and Pi—use Ethernet cable for Pi if no WiFi).
# Free tools needed: 
- Raspberry Pi Imager -> https://www.raspberrypi.com/software/
- Angry IP Scanner -> https://angryip.org
- RealVNC Viewer-> www.realvnc.com/en/connect/download/viewer/

# Step-by-Step Setup

- Prepare the MicroSD Card (Boot the Pi OS)
Download Raspberry Pi Imager from raspberrypi.com/software/.
Insert your microSD card into your PC. Open the Imager, pick "Raspberry Pi OS (32-bit)" as the OS, select your SD card, and click "Write." (Pro tip: In advanced settings—gear icon—set a username like "pi" and password, enable SSH, and add your WiFi details if needed.)
Eject the card, pop it into your Pi, and plug in the power. The Pi boots up quietly!




- Find the Pi's IP Address (Like Finding a Friend's House)
Download Angry IP Scanner from angryip.org.
Open it, set the IP range to something like 192.168.1.0/24 (check your PC's IP first via command prompt/terminal: type ipconfig on Windows or ifconfig on Linux/Mac). Hit "Start."
Look for a device named "raspberrypi" in the list—that's your Pi's IP (e.g., 192.168.1.100). Note it down!



- Connect via SSH (Text Chat with Your Pi)
On your PC, open a terminal (Command Prompt on Windows, Terminal on Mac/Linux).
Type:
```
ssh pi@your-pi-ip (replace with the IP from step 2).
```
Enter your password when asked.
Now you're in! Type
```
sudo raspi-config
```
 to open a menu. Use arrow keys:
Go to "Interface Options" > "VNC" > Enable it (Yes).
Then "Display Options" > "VNC Resolution" > Pick 1280x720.
Finish and reboot (Yes). Exit SSH with exit.

View the Pi Desktop with VNC (Like Remote Control TV)
Download RealVNC Viewer from realvnc.com/download/viewer/.
Open it, enter your Pi's IP in the bar. Log in with the same username/password from SSH.
Boom! You see the Raspberry Pi's full desktop on your PC screen. Now play around—install stuff, code, or build robots!

