from multiprocessing.connection import wait
import requests
import random
import string
import time
import threading
from colored import fg

yellow = fg('yellow')
green = fg('green')
red = fg('red')


def gen():

    print(yellow + "-[Making account]-")

    usernamegen = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    passwordgen = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    emailgen = f"{''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))}@gmail.com"

    payload = {
        "username": usernamegen,
        "password": passwordgen,
        "email": emailgen,
        "acceptPolicy": "on",
        "receiveContact": "",
        "tz": "Pacific/Auckland",
        "qualifying": 1,
        "avgSpeed": 21,
        "avgAcc": 93,
        "carID": 9,
        "raceSounds": "only_fx"
    }

    r = requests.post("https://www.nitrotype.com/api/v2/auth/register/username", headers={"cookie": 'st-id=10; _ga=GA1.2.940758212.1646596591; _gcl_au=1.1.674226475.1646596591; _fbp=fb.1.1646596592053.1438859192; ntdev=166586351; _lr_env_src_ats=false; __gads=ID=93380e5b45f408b7:T=1651542521:S=ALNI_MbEq6dxzfbHt0GlC7zMfRGPsatQig; usprivacy=1---; _pw_fingerprint=%2255c311ba86ccd8bee7f85a3a14ec49af%22; _pbjs_userid_consent_data=3524755945110770; ad_clicker=false; ki_r=; __qca=P0-130142758-1653356968936; _gid=GA1.2.1909788533.1653961976; _lr_retry_request=true; __gpi=UID=00000521e0ce4650:T=1651542521:RT=1653962120:S=ALNI_MZY_V-vjVIpEga89b97iweRKMOscw; _lr_geo_location=NZ; cto_bundle=PTETpl8lMkZ3dUhFR0JobUxTcVNvcGhzJTJCdVVmYnA4ZE54bGVSNkFYdkxlNTZzMEd0VG9nckxVVUVGZVVxcm9GVGFwVHltWWwyWWVSJTJGY3RiU3ppRHNpam5nUFd0UkdIck9BUTVoUEJnMHFITEg1bCUyRkc1OGptMWFOTEpHVXpmRkExeFVGWXNVWldVeU9FWWpUYSUyRnJ5RXBWbmJVdGJRJTNEJTNE; FCNEC=[["AKsRol-IC15rBsYM9QQ3XTZBvVy5O12JTsEd8AM40k8d3g-BPfHM0Lur-AshHGUvqmFEH1d09iQY0HtYPhvXmH8Ts8FC9OfLTg_qVQPdAJSuMWBwdjLp8-tFeaRFHrPgxROxVFzP-5jfQ0OtTlBuxNdW4RKkqZ60fg=="],null,[]]; properSessionData=eyJ1dWlkIjoiMmJlMWZiMDUtZGI2OC00Y2UxLWEwZTAtZWM2ZDZiMDA4NDE2IiwiZGVwdGgiOjYsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cubml0cm90eXBlLmNvbS9yYWNlIiwiZ2NsaWQiOiIiLCJmYmNsaWQiOiIiLCJ1dG1fY2FtcGFpZ24iOiIiLCJ1dG1fc291cmNlIjoiIiwidXRtX21lZGl1bSI6IiIsInV0bV90ZXJtIjoiIiwidXRtX2NvbnRlbnQiOiIiLCJ1dG1fdGVtcGxhdGUiOiIiLCJ1dG1fcmVmZXJyZXIiOiIiLCJ1dG1fYWRzZXQiOiIiLCJ1dG1fc3ViaWQiOiIiLCJyZXZlbnVlIjowLjAwMjEyMDExMjAwMDAwMDAwMDQsImJpZF9hdmciOnt9LCJub19iaWRfY250Ijp7InNvdnJuX3MycyI6NCwibWVkaWFncmlkX3MycyI6NCwidmVyaXpvbl9tZWRpYV9zMnMiOjQsImE5Ijo0LCJlbXgiOjQsImNyaXRlbyI6NCwicnViaWNvbiI6NCwibWVkaWFuZXQiOjQsInB1Ym1hdGljIjo0LCJyaHl0aG1vbmUiOjQsInVuZGVydG9uZSI6NCwiY29udmVyc2FudCI6NCwidHJpcGxlbGlmdCI6NCwidGhpcnR5dGhyZWVhY3Jvc3MiOjQsImluZGV4IjozLCJhcHBuZXh1cyI6Mywib3BlbngiOjIsInNvdnJuIjoyLCJzaGFyZXRocm91Z2giOjJ9LCJhdWN0aW9uX2NvdW50Ijo0LCJsYXN0X3RocmVzaG9sZCI6MH0=; ki_t=1646596592768%3B1653961977214%3B1653962898155%3B15%3B81; ntuserguest=g0.718279406334053; _gali=email'}, json=payload)
    rjson = r.json()

    if rjson["status"] == "OK":
        emailpicked = emailgen
        usernamepicked = rjson["results"]["username"]
        useridpicked = rjson["results"]["userID"]
        passwordpicked = passwordgen
        token = rjson["results"]["token"]

        print(green + f"[{usernamepicked}, {useridpicked}]")

        with open('accounts.txt', 'a') as f:
            f.write(f"{usernamepicked}:{passwordpicked}\n")
        
        print(green + "-[Nitrotype account made and put in accounts.txt]-")

        
    else:
        print(red + "-[Failed to make the account]-")
    
    time.sleep(0.2)

    gen()


for n in range(1, 20):
    t = threading.Thread(target=gen)
    t.start()