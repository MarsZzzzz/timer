import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f" timer set for {minutes} minutes.")

    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up! Stay focused!")

# 设置专注时间为25分钟
focus_timer(25)
