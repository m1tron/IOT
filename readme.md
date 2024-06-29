# Pico Cabin Monitor
---

Henrik Oskarsson - ho222pk

---
### Overview

The aim of this project is to create a monitor for a Cabin by tracking temperature, humidity and entry (door sensor) using a Raspberry Pi Pico that then interfaces with Adafruit to visualize the data, and even provide warnings if the temperature drops to low.

The estimated time to setup this device following the instructions outlined here should be approximately a day. 

### Objective

The reason for this projects existence is that my father owns a cottage that uses electrically powered water heating. A power failure, or a fuse tripping, might result in the temperature dropping below zero in winter time,  with the freezing of the water piping as a consequence. 

Monitoring the temperature over time will also provide good insight for selecting a good temperature setting for the maintenance heating.


---
## Materials

The following materials were used.
Link to elektrokit: https://www.electrokit.com/

| Hardware                                       | Description                          | Price inc. VAT (SEK) |
| ---------------------------------------------- | ------------------------------------ | -------------------- |
| Raspberry Pi Pico WH                           | Microcontroller that reads sensors.  | 109                  |
| Breadboard 840 connections                     | Mainly used to simplify connections. | 69                   |
| **Sensors & Components**                       |                                      |                      |
| DHT-11 Digital Temperature and Humidity Sensor | Sensor for humidity and temperature  | 49                   |
| Lab wire male/male kit                         | Interconnect                         | 29                   |
| Micro USB cable                                | System power                         | 19                   |
| Reed Sensor                                    | Front door monitoring                | 25                   |

---

### Computer Setup

To program the Pico, a Windows machine was used running Visual Studio Code with the Pymakr extension. Before any coding begins, it is a good idea to update the firmware with the latest micropython. By holding the BOOTSEL button when connecting the device to the computer, it will show up as a folder similar to a normal USB drive. The firmware can then be [downloaded](https://micropython.org/download/RPI_PICO_W/) and dropped just dropped to the Pico that automatically will install the firmware. 

Programming can now commence by making a new project in Pymakr.
![[img/Pasted image 20240629221654.png]]
First click the Pymakr icon (bottom left), and select *New Project*.  After selecting a folder you will get the option to select a COM port, in my case I could select 1,3 or 4. If you are uncertain, you can try this procedure with and without the Pico connected and the correct COM port will be apparent. In the screenshot, the Pico is added successfully, and the lightning symbol can be clicked to connect to the device, which will then look like this:

![[img/Pasted image 20240629222040.png]]

To upload files from you project folder, the arrow into the cloud can be clicked and after a second or two the files will be loaded on the device. The Pico will normally look for two python files, *boot.py* and *main.py*. The first one will run directly after booting followed by the *main.py*. In my case, only a main file was used. Instead of rebooting the device to run the code, I clicked the terminal icon and entered `exec(open('main.py').read())`. Execution is easily stopped using the universal Ctrl+C command.

### Putting everything together

