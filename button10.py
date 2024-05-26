import subprocess
import evdev
from evdev import InputDevice, ecodes

#to find my_mouse, run evtest in terminal
my_mouse = "Logitech G403 HERO Gaming Mouse"

device_paths = evdev.list_devices()

for dev_path in device_paths:
    device = evdev.InputDevice(dev_path)
    if device.name == my_mouse:
        device_path = device.path
        print(my_mouse, "=", device_path)
        break
else:
    print("Device not found.")

device = InputDevice(device_path)

#define the event code for the desired button (BTN_FORWARD in my case, aka button 10 according to Xev)
button_event_code = ecodes.BTN_FORWARD

#define the commands for different window classes
commands = {
    "Dorion": "xdotool key 'alt+shift+Up'",                       # DISCORD navigate to unread
    "discord": "xdotool key 'alt+shift+Up'",                       # DISCORD navigate to unread
    "vesktop": "xdotool key 'alt+shift+Up'",                       # VESKTOP navigate to unread
    "PortalWars-Linux-Shipping": "xdotool key 'f+h'",              # SPLITGATE pick up weapon and use spray
    "steam_app_782330": "xdotool key 'g+f'; xdotool key 'g'",      # DOOMETERNAL icebomb (and switch back to frag)
    "steam_app_553850": "xdotool key 'b'",                         # HELLDIVERS2 free keybind
    "steam_app_1240440": "xdotool key 'g'",                        # HALOINFINITE
    "Audacious": "bash -c '/home/pointblank/.local/share/nemo/scripts/💿\ Music/🎼\ Edit\ Current\ Audacious\ Opus'",
    "Nemo-desktop": "sleep 0.2; dbus-send --session --dest=org.Cinnamon --type=method_call --print-reply /org/Cinnamon org.Cinnamon.ShowOverview 1> /dev/null",
    "cube2_client": "play -q ~/.sounds/save_open.ogg"
}

#listen for events
for event in device.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.code == button_event_code:
            if event.value == 1:  #check for button press event
                #execute xdotool command to get the active window ID
                xdotool_process = subprocess.Popen(["xdotool", "getactivewindow"], stdout=subprocess.PIPE)
                #get the output of the xdotool command
                active_window_id, _ = xdotool_process.communicate()
                #decode the output to a string
                active_window_id = active_window_id.decode("utf-8").strip()

                #execute xprop with the active window ID to get the window class
                xprop_process = subprocess.Popen(["xprop", "-id", active_window_id, "WM_CLASS"], stdout=subprocess.PIPE)
                #get the output of xprop
                xprop_output, _ = xprop_process.communicate()
                #decode the output to a string
                xprop_output = xprop_output.decode("utf-8").strip()

                #parse the output to extract the window class
                window_class = xprop_output.split('"')[3]

                #execute the corresponding command based on the window class
                if window_class in commands:
                    command = commands[window_class]
                    print(f"Window Detected: {window_class}. Executing command:")
                    print(command)
                    subprocess.Popen(["/bin/bash", "-c", command])
                else:
                    print(f"No command defined for window class: {window_class}")
