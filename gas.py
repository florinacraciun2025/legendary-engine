from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
with SB(uc=True, test=True,locale=f"{language_code.upper()}") as tg3t2t2tt4ted:
    tg3t2t2tt4ted.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    tg3t2t2tt4ted.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    #tg3t2t2tt4ted.set_window_size(resolution.width, resolution.height)
    #"#live-channel-stream-information"
    url = "https://kick.com/brutalles"
    tg3t2t2tt4ted.uc_open_with_reconnect(url, 4)
    tg3t2t2tt4ted.sleep(4)
    tg3t2t2tt4ted.uc_gui_click_captcha()
    tg3t2t2tt4ted.sleep(1)
    tg3t2t2tt4ted.uc_gui_handle_captcha()
    tg3t2t2tt4ted.sleep(4)
    if tg3t2t2tt4ted.is_element_present('button:contains("Accept")'):
        tg3t2t2tt4ted.uc_click('button:contains("Accept")', reconnect_time=4)
    if tg3t2t2tt4ted.is_element_visible('#injected-channel-player'):
        tg3t2t2tt4ted.uc_open_with_reconnect("https://www.twitch.tv/brutalles", 4)
        tg3t2t2tt4ted.sleep(4)
        tg3t2t2tt4ted2 = tg3t2t2tt4ted.get_new_driver(undetectable=True)
        tg3t2t2tt4ted2.uc_open_with_reconnect(url, 5)
        tg3t2t2tt4ted2.uc_gui_click_captcha()
        tg3t2t2tt4ted2.uc_gui_handle_captcha()
        tg3t2t2tt4ted.sleep(5)
        if tg3t2t2tt4ted2.is_element_present('button:contains("Accept")'):
            tg3t2t2tt4ted2.uc_click('button:contains("Accept")', reconnect_time=4)
        while tg3t2t2tt4ted2.is_element_visible('#injected-channel-player'):
            tg3t2t2tt4ted2.sleep(1)
        tg3t2t2tt4ted.quit_extra_driver()
    tg3t2t2tt4ted.sleep(1)
    url = "https://www.twitch.tv/brutalles"
    tg3t2t2tt4ted.uc_open_with_reconnect(url, 5)
    tg3t2t2tt4ted.sleep(14)
    if tg3t2t2tt4ted.is_element_present("#live-channel-stream-information"):

        if tg3t2t2tt4ted.is_element_present('button:contains("Accept")'):
            tg3t2t2tt4ted.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            tg3t2t2tt4ted.uc_open_with_reconnect("https://kick.com/brutalles", 5)
            tg3t2t2tt4ted2 = tg3t2t2tt4ted.get_new_driver(undetectable=True)
            tg3t2t2tt4ted2.uc_open_with_reconnect(url, 5)
            tg3t2t2tt4ted.sleep(10)
            if tg3t2t2tt4ted2.is_element_present('button:contains("Accept")'):
                tg3t2t2tt4ted2.uc_click('button:contains("Accept")', reconnect_time=4)
            while tg3t2t2tt4ted2.is_element_present("#live-channel-stream-information"):
                tg3t2t2tt4ted2.sleep(1)
            tg3t2t2tt4ted.quit_extra_driver()
    tg3t2t2tt4ted.sleep(1)
