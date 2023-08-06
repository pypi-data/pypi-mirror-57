import json
import os
from http.client import HTTPConnection
from dotenv import load_dotenv
from .Parser import COMMANDS, RpiArgumentParser


class ApiHelper(object):
    conn: HTTPConnection

    def __init__(self):
        load_dotenv()
        self.FUNCTIONS = {COMMANDS.GET_ALARMS: self.__get_alarms, COMMANDS.GET_ALARM: self.__get_alarms,
                          COMMANDS.CHANGE_ALARM: self.__change_alarm}

    def do_command(self, cmd, args):
        self.conn = HTTPConnection(os.getenv('RPI-RADIO-ALARM-URL'))
        return self.FUNCTIONS.get(cmd)(args)

    def __get_alarms(self, args):
        has_args = len(args) > 0
        if has_args:
            self.conn.request("GET", '/alarm/' + str(args).replace(' ', ''))
        else:
            self.conn.request("GET", "/alarm")
        resp = json.loads(self.conn.getresponse().read().decode())

        if isinstance(resp, dict):
            resp = [resp]

        return (
                   '' if has_args else f'__**Alarms**__ \n') + f'{"".join("__**Alarm " + str(args if has_args else idx) + "**__" + self.__alarm_string(alarm, True) for idx, alarm in enumerate(resp))}'

    def __change_alarm(self, args=dict):
        alarm_id = args.pop(RpiArgumentParser.ALARM_IDX)
        print(args)
        headers = {"Content-type": "application/json", "Accept": "text/plain"}
        self.conn.request("PUT", "/alarm/" + str(alarm_id), json.dumps(args), headers=headers)
        resp = json.loads(self.conn.getresponse().read().decode())

        return f"__**Alarm {alarm_id}**__" + self.__alarm_string(resp, True)

    def __start_radio(self, args):
        return self.__change_radio(True)

    def __stop_radio(self, args):
        return self.__change_radio(False)

    def __change_radio(self, running: bool):
        headers = {"Content-type": "application/json"}
        self.conn.request("POST", "/radio", json.dumps({"switch": "on" if running else "off"}), headers=headers)
        resp = json.loads(self.conn.getresponse().read().decode())

        return f"__**Radio**__ Is playing:" + str(resp["isPlaying"])

    @staticmethod
    def __alarm_string(alarm, preline):
        if preline:
            prefix = '\n\t'
        else:
            prefix = ''
        return prefix + f'name: {alarm["name"]} \n\t' \
                        f'time: {alarm["hour"]}:{alarm["min"]} \n\t' \
                        f'days: {alarm["days"]} \n\t' \
                        f'on: {alarm["on"]} \n'
