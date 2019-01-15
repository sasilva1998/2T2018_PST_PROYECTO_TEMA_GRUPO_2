"""MIT License

Copyright (c) 2019 sasilva1998

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

from time import sleep, sleep_ms
import machine

class DCMotor:
	def __init__(self, ba, ab):
		self.ba=ba
		self.ab=ab
		self.mota=machine.Pin(ba,machine.Pin.OUT)
		self.motb=machine.Pin(ab,machine.Pin.OUT)

	def forward(self):
		mota.value(1)
		motb.value(0)

	def backwards(self):
		mota.value(0)
		motb.value(1)

	def stop(self):
		mota.value(0)
		motb.value(0)