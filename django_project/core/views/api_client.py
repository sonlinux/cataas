import requests

from django.views.generic import FormView

from ..forms.tag_form import TagForm


class CataasClient(FormView):
    """
    ...
    """

    template_name = 'cats.html'
    form_class = TagForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CataasClient, self).get_context_data(**kwargs)

        if self.form_class.is_valid:
            # tag = self.form_class.cleaned_data.get('tag')
            tag = ''
            api_url = 'https://cataas.com/#/search/tag/{cat_tag}'.format(
                cat_tag=tag)
            params = {}
            response_data = requests.get(api_url, params=params)

            context['cat_images'] = response_data

        return context
