Tempura WIP
Home security system.

Using
ESP32
RPi Pico
RPi 4

Currently prototyping and plans outlines the following:
- Vibration sensors on windows
- Mag switches on doors
- Hall sensors on doors (anti-tamper - without expensive switches with tampering detection)
- Motion sensors in rooms

- Safe Room:
  - Solenoid locked door. Alarm sets 4 on each cornor to lock the door in place. 
  - 3 factor authentication. Something you have (key card or fob) something you know (keypad) and something you have (finger print).
  - Camera on the door's exterior with a screen to monitor it in the room. 
  - Two-way communication via microphone and speaker. 

Ideally have everything wired together, but due to my current circumstances I cannot start hiding wires or fixing conduits. 
Current plan for connectivity:
- Each sensor array wired into an ESP32 for monitoring which will send heartbeat requests, trigger request, and tamper requests. 
- Raspberry pi 4 will be set as a hidden network which the ESP32s will be connected to. Everything will happen over that netowrk. 
- The server will allow users to monitor the system globally (monitor, not disable).   

Threats:
- Signal jamming:
  -   Although you could wipe out wireless communication remotely fairly trivially, it's easy to detect. The downside however, if the system cannot call externally for help then we must trigger defense mode. 

Defense Mode:
In the even of a trigger with no outside help, we must trigger defensive capabilities. 
- Light control. Deactivating lights may be good enough but my plan is to strobe. Strobe all lighting to blind an intruder. 
- Sound. Set off 2 16v sirens in every room.
- Smokescreen? A bit out of my budget for now. 


Credits:
- https://github.com/chrisb2/micropython-fingerprint
