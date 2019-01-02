from django.views.generic import CreateView, ListView, DetailView
from stocks.models import Algorithm
from stocks.forms import AlgorithmForm
import requests

from project.settings import PRICES_API_URL
from stocks.utils import algo_result

# Create your views here.


class AlgorithmCreateView(CreateView):
    template_name = "algorithm_form.html"
    model = Algorithm
    form_class = AlgorithmForm
    success_url = 'algorithm'


class AlgorithmListView(ListView):
    model = Algorithm
    context_object_name = 'algorithm_list'
    queryset = Algorithm.objects.all()
    template_name = "algorithm_list.html"


class AlgorithmDetailView(DetailView):

    template_name = "algorithm_detail.html"
    model = Algorithm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        url = PRICES_API_URL.replace('ticker', instance.ticker)
        response = requests.get(url)
        prices = []
        for item in response.json():
            prices.append(item.get('close'))
        positions, pnl = algo_result(instance.signal, instance.trade, prices)
        context['plot'] = zip(positions, pnl)
        return context

