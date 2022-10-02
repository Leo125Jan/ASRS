# ASRS

## About The Project
This is the the project of Mechanical Practice. In this class, our team want to make a automated storage and retrieval system, we divide into two part:

* Website
Scanning QRcode on the goods, saving data in database and display on website.

* Motor Control
We make a thousandth model and use Raspberry Pi 3B+ to control all sansors and motors.

## Built With
### Website
* Django: High-level Python web framework
* Opencv: Scan QRcode
* Tkinter: Keyboard detect
* Ngrok: Open localhost
* MySQL: Database
* phpMyAdmin: Handle the administration of MySQL over the Web
* WebCam

### Motor Control
* Gpio pinout of Raspberry Pi
* Gpiozero: Control servo motor
* Multi-processing of Python
* Multi-threading of Python
* I2C
  
## Getting Started
### Configuration

#### Website
1. Done all the setup of Django.
2. Connect the website to the database.
3. Create a local server.
4. Open website

#### Motor Control
Configuratint every sensor & motor with wire、driver and circuit board. Then, using Gpio pinout of Raspberry Pi to control.

## Usage

### Website
We use webcam to scan QRcode which content is number on goods, we press a key to start to scan, then, data will store in database and display on website. On the website, we can check and manage all data.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=redsGKPUM9w
" target="_blank"><img src="http://img.youtube.com/vi/redsGKPUM9w/0.jpg" 
width="480" height="270" border="10" /></a>

### Motor Control
All action start with QRcode scan, after key press, the goods will arbitrarily assign to a empty storage area, location of goods can be checked on website. Above is done, the motor will start operate.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=cB7Vchz9FDE
" target="_blank"><img src="http://img.youtube.com/vi/cB7Vchz9FDE/0.jpg" 
width="480" height="270" border="10" /></a>

## Acknowledgments
* [MCP23017_I2C-with-Raspberry-Pi-](https://github.com/rpsreal/MCP23017_I2C-with-Raspberry-Pi-)
* [Django Tutorials](https://www.youtube.com/watch?v=xv_bwpA_aEA&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&ab_channel=DennisIvy)
