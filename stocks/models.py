from django.db import models
import requests

from project.settings import PRICES_API_URL
from stocks.utils import algo_result


class Algorithm(models.Model):
    name = models.CharField(max_length=255)
    signal = models.CharField(max_length=255)
    trade = models.CharField(max_length=255)
    ticker = models.CharField(max_length=255)

    @property
    def average_pnl(self):
        url = PRICES_API_URL.replace('ticker', self.ticker)
        response = requests.get(url)
        if response.status_code == 200:
            prices = []
            for item in response.json():
                prices.append(item.get('close'))
            positions, PnL = algo_result(self.signal, self.trade, prices)
            return sum(PnL)/len(PnL)
        return 0

    def __str__(self):
        return self.name
