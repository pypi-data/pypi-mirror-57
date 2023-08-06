#!/usr/bin/python
"""
soundboard-relay

forwards mqtt messages to an mpd
"""

from contextlib import contextmanager
import argparse
import logging
import time

import paho.mqtt.client as mqtt
from mpd import MPDClient


# pylint: disable=invalid-name
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@contextmanager
def log_exception(sleep=0):
    """Helper for exception handling."""
    try:
        yield
    except Exception as exc: # pylint: disable=broad-except
        logger.exception(exc)
        if sleep:
            logger.warning("sleeping %s sec", sleep)
            time.sleep(sleep)


class MPD:
    """Contextmanager for MPDClient."""
    def __init__(self, host, port):
        self.client = MPDClient()
        self.host = host
        self.port = port

    def __enter__(self):
        logger.info("connecting to %s:%s", self.host, self.port)
        self.client.connect(self.host, self.port, 5)
        return self

    def __exit__(self, etype, value, traceback):
        with log_exception():
            self.client.disconnect()
        return True

    def play(self, soundfile):
        """Play a soundfile."""
        with log_exception():
            self.client.clear()
            self.client.add(soundfile)
            self.client.play()


def on_connect(client, userdata, flags, rc): # pylint: disable=unused-argument,invalid-name
    """MQTT connection handler"""
    client.subscribe("psa/sound")
    client.subscribe("psa/alarm")
    client.subscribe("sensor/door/frame")
    client.subscribe("sensor/door/bell")
    print("subscribed to all topics")


def on_message_for_mpd(host, port):
    """wrapper for mpd configurated MQTT message handler"""
    def on_message(client, userdata, msg): # pylint: disable=unused-argument
        """MQTT message handler"""
        with log_exception():
            with MPD(host, port) as mpd:
                topic = msg.topic
                payload = msg.payload.decode()
                soundfile = None
                if topic == "psa/alarm":
                    soundfile = "ALARM.ogg"
                elif topic == "sensor/door/frame" and payload == "open":
                    soundfile = "door-louder.opus"
                elif topic == "sensor/door/bell" and payload == "pressed":
                    soundfile = "door-bell.ogg"
                elif topic == "psa/sound":
                    soundfile = payload
                if soundfile:
                    logger.info("playing %s", payload)
                    mpd.play(soundfile)
    return on_message


def main():
    """main"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--mqtt', dest='mqtt', default='mqtt.example.com')
    parser.add_argument('--mqtt-port', dest='mqtt_port', type=int, default=1883)
    parser.add_argument('--mpd', dest='mpd', default='mpd.example.com')
    parser.add_argument('--mpd-port', dest='mpd_port', type=int, default=6600)
    args = parser.parse_args()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message_for_mpd(args.mpd, args.mpd_port)
    while True:
        with log_exception(sleep=5):
            client.connect(args.mqtt, args.mqtt_port, 60)
            client.loop_forever()

if __name__ == '__main__':
    main()
