import os

r,w = os.pipe()
pid = os.fork()

if pid > 0:
	#Parent process
	os.close(r)

	print("Enter time (hh mm):")
	time = input()

	os.write(w,str.encode(time))

else:
	os.close(w)
	r = os.fdopen(r)
	time=r.read()
	h,m=map(int,time.split())
	if h < 12:
		print("Good Morning.")
	elif h < 15:
		print("Good Afternoon.")
	elif h < 20:
		print("Good Evening.")
	else:
		print("Good Night.")