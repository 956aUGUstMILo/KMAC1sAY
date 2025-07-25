以下是优化后的代码片段：

```python
import RPi.GPIO as GPIO
from time import sleep

def setup_gpio(pin):
    GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers
    GPIO.setup(pin, GPIO.OUT)  # GPIO Assign mode

def toggle_relay(pin):
    try:
        GPIO.output(pin, GPIO.LOW)  # turn relay off
        sleep(5)
        GPIO.output(pin, GPIO.HIGH)  # turn relay on
        sleep(1)
        print('finished turning relay on and off')
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise

def main():
    relay_pin = int(input('Enter the GPIO pin for the relay to toggle on and off: '))
    setup_gpio(relay_pin)
    toggle_relay(relay_pin)

if __name__ == '__main__':
    main()
```

这段代码将原始代码封装成了几个函数，提高了代码的可读性和可维护性。同时，通过使用 `if __name__ == '__main__':` 来确保 `main` 函数只在脚本作为主程序运行时被调用，避免了在导入时执行不必要的代码。