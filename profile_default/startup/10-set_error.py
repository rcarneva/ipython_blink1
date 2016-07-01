import time, blink1py
from multiprocessing import Process

def blinken(n, r=200, g=0, b=0, t=150):
	try:
		with blink1py.open_blink1() as b1:
			for _ in xrange(n):
				b1.fade_rgb(r, g, b, t)
				time.sleep(t/1000.*1.3)
				b1.fade_rgb(0, 0, 0, t)
				time.sleep(t/1000.*1.3)
			b1.off()
	except:
		pass

def thread_blink(n=3, r=200, g=0, b=0, t=150):
	Process(target=lambda: blinken(n, r, g, b, t)).start()

def custom_exc(shell, etype, evalue, tb, tb_offset=None):
	thread_blink()
	shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)

get_ipython().set_custom_exc((Exception,), custom_exc)
get_ipython().events.register("post_execute", lambda: thread_blink(1, 0, 180, 0, 150))
