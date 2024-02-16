# MP-AS5600

Micropython project linking an ESP32-C3 to an AS5600 magnetic rotary position sensor 

## Image of working breadboard

![alt text](image.png)

## Hardware
 - [ESP32-C3-DevKitC-02](https://docs.espressif.com/projects/esp-idf/en/latest/esp32c3/hw-reference/esp32c3/user-guide-devkitc-02.html#esp32-c3-devkitc-02)
 - [AS5600 breakout board](https://www.amazon.com/dp/B09QYC916Q/)
 - [SSD1306 OLED display](https://www.amazon.com/DIYmall-Serial-128x64-Display-Arduino/dp/B00O2KDQBE)
 - [Servo SG90](https://www.adafruit.com/product/169)
 - [Breadboard](https://www.adafruit.com/product/239)

## Wiring

- ESP32-C3-DevKitC-02
  - 3V3 -> Breadboard + rail
  - GND -> Breadboard - rail
  - GPIO 9 -> Breadboard Row 22
  - GPIO 8 -> Breadboard Row 23
  - 5V -> Servo Red
  - GND -> Servo Black
  - GPIO 0 -> Servo PWM
- SSD1306 OLED display
  - Breadboard + rail -> VCC
  - Breadboard - rail -> GND
  - Breadboard Row 22 -> SSD1306 SDA
  - Breadboard Row 23 -> SSD1306 SCL
- AS5600 breakout board
  - Breadboard + rail -> VCC
  - Breadboard - rail -> GND
  - Breadboard Row 22 -> AS5600 SDA
  - Breadboard Row 23 -> AS5600 SCL

## Software

- [Micropython](https://micropython.org/)
  - [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html)
- Libraries
  - [SSD1306](https://github.com/adafruit/micropython-adafruit-ssd1306/tree/master)
  - [AS5600](https://github.com/owen-gervais/as5600-uPython-driver)
  - [Servo](https://www.upesy.com/blogs/tutorials/esp32-servo-motor-sg90-on-micropython)

## Deployment instructions

- Install Micropython on the ESP32-C3-DevKitC-02
- Copy all files in /src to the ESP32-C3-DevKitC-02

```bash

cd src/

# Make directory structure on the ESP32-C3-DevKitC-02 matching the directory structure of src
find . -type d | grep -v '^\.$' | sed 's;\./;;' | while read dir; do mpremote mkdir :$dir; done
mkdir :lib

# Copy files in src to the ESP32-C3-DevKitC-02
find . -type f | grep -v '^\.$' | sed 's;\./;;' | while read file; do mpremote cp $file :$file; done

```