import requests
from datetime import date, timedelta


class Nightscout():

    def __init__(self, url, number_of_days=14):
        start_date = (date.today() - timedelta(days=number_of_days)).strftime("%Y-%m-%d")
        self.url = url + 'api/v1/entries/sgv.json?&count=1000000&find[dateString][$gte]={}'.format(start_date)

        self.response = None
        self.direction = None
        self.sgv = None
        self.date = None
        self.device = None

    def query(self):
        response = requests.get(self.url).json()
        self.response = response

    def get_value(self, value_type):
        """
        Gets specific value type from response string
        :param value_type: e.g. "sgv", "dateString", "device
        :return: list with all values from this value type
        """
        return [item[value_type] for item in self.response]

    def filter_sgv(self):
        """
        In case of multiple uploads, this method filters the sgv entries for only one device and unique sgv dates
        :return: filtered sgv
        """
        filtered_sgv = []
        for i, b in enumerate(self.sgv):
            if i == len(self.sgv) - 1:
                break
            if (self.device[i] == 'AndroidAPS-DexcomG6') & (self.date[i] != self.date[i + 1]):
                filtered_sgv.append(b)
        return filtered_sgv

    def get_filtered_sgv(self):
        self.sgv = self.get_value("sgv")
        self.date = self.get_value("dateString")
        self.device = self.get_value("device")
        filtered_sgv = self.filter_sgv()
        return filtered_sgv

    def get_direction(self):
        self.direction = self.response['direction']
        return self.direction

    def get_arrow(self):
        switcher = {
            "DoubleUp": "⇈",
            "SingleUp": "↑",
            "FortyFiveUp": "↗",
            "Flat": "→",
            "FortyFiveDown": "↘",
            "SingleDown": "↓",
            "DoubleDown": "⇊",
            "NOT COMPUTABLE": "",
            "OUT OF RANGE": "⇕"
        }
        return switcher[self.direction]
