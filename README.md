# button10.py
Python script to rebind mouse button on per-application basis for hotkeys    

this is a remake of [this crappy bash project](https://github.com/Ao1Pointblank/xinput-mouse-keybinds)    

* FINDING DEVICE NAME  
you will need to find your mouse's name with the ``evtest`` command in terminal:  
(insert this name as the value for ``my_mouse`` in the script)    
![Screenshot from 2024-05-25 20-24-48](https://github.com/Ao1Pointblank/button10.py/assets/88149675/ec75940a-7aa5-4a1b-a801-9ea5fda7d74c)      

* FINDING BUTTON EVENT CODE  
you may also need to modify the line ``button_event_code = ecodes.BTN_FORWARD``, changing the event code to whatever it is on your mouse's button.  
i used Piper/Ratbag to configure my mouse's DPI button to send a "Button 5" press, which shows as "BTN_FORWARD" in evtest.  
just select the deivice you want to monitor in ``evtest`` and spam the button a few times to find the event code name:    
![Screenshot from 2024-05-25 20-30-02](https://github.com/Ao1Pointblank/button10.py/assets/88149675/617fb40b-a54e-4251-a693-79825534ad9e)    

* CONFIGURING COMMANDS    
lastly, you just need to make your own list of commands, preceeded by the WM_CLASS value.
you can use the following terminal command to get the WM_CLASS of a window:  
```bash
sleep 3 ; xprop -id $(xdotool getactivewindow) | awk -F '=' '/WM_CLASS/{print $2}' | tr -d '",' | sed -e 's/^[[:space:]]*//'
```
simply run this, switch to the window you want the class for, and wait 3 seconds. then look at the terminal output and use the second word as the class name:    
![Screenshot from 2024-05-25 20-46-02](https://github.com/Ao1Pointblank/button10.py/assets/88149675/70e3b6c6-bb4d-477e-878c-c92bf6f96326)    

example snippet to show how to bind the mouse button to reload the page in "Youtube Music" desktop app:
```py
#define the commands for different window classes
commands = {
    "Youtube Music": "xdotool key 'ctrl+r'",                       # YTM reload page
}
```
