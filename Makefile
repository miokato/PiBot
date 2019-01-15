.PHONY gpio:
gpio:
	sudo pigpiod


.PHONY servo_test:
servo_test:
	sudo python3 servo_test.py


.PHONY app:
app:
	sudo python3 app.py