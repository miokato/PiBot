import pigpio
import time

from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


# home
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/forward')
def forward():
    pi.set_servo_pulsewidth(left_out, 1000)
    pi.set_servo_pulsewidth(right_out, 2000)
    time.sleep(2)
    pi.set_servo_pulsewidth(left_out, 1480)
    pi.set_servo_pulsewidth(right_out, 1480)
    return redirect(url_for('hello_world'))


@app.route('/backward')
def backward():
    pi.set_servo_pulsewidth(left_out, 2000)
    pi.set_servo_pulsewidth(right_out, 1000)
    time.sleep(2)
    pi.set_servo_pulsewidth(left_out, 1480)
    pi.set_servo_pulsewidth(right_out, 1480)
    return redirect(url_for('hello_world'))


@app.route('/right')
def right():
    pi.set_servo_pulsewidth(left_out, 2000)
    pi.set_servo_pulsewidth(right_out, 2000)
    time.sleep(0.3)
    pi.set_servo_pulsewidth(left_out, 1480)
    pi.set_servo_pulsewidth(right_out, 1480)
    return redirect(url_for('hello_world'))


@app.route('/left')
def left():
    pi.set_servo_pulsewidth(left_out, 1000)
    pi.set_servo_pulsewidth(right_out, 1000)
    time.sleep(0.3)
    pi.set_servo_pulsewidth(left_out, 1480)
    pi.set_servo_pulsewidth(right_out, 1480)
    return redirect(url_for('hello_world'))


@app.route('/stop')
def stop():
    pi.set_servo_pulsewidth(left_out, 1480)
    pi.set_servo_pulsewidth(right_out, 1480)
    pi.stop()
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    pi = pigpio.pi()

    left_out = 18
    right_out = 19

    pi.set_mode(left_out, pigpio.OUTPUT)
    pi.set_mode(right_out, pigpio.OUTPUT)

    app.run(host='0.0.0.0', port=80, debug=True)
