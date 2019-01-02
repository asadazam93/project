from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from stocks.models import Algorithm


class AlgorithmForm(forms.ModelForm):
    class Meta:
        model = Algorithm
        fields = ['name', 'signal', 'trade', 'ticker']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.form_method = 'POST'
