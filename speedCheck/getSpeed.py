import speedtest

def downloadCheck():
    s = speedtest.Speedtest()
    speed_down = s.download(threads=None)*(10**-6)
    speed_down = round(speed_down)
    return speed_down


def uploadCheck():
    s = speedtest.Speedtest()
    speed_up = s.upload(threads=None)*(10**-6)
    speed_up = round(speed_up)
    return speed_up