from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ..forms.tag_form import TagForm
import requests

from django.views.generic import TemplateView


class CataasClient(TemplateView):
    """
    ...
    """

    template_name = 'cats.html'

    def get_context_data(self, **kwargs):
        context = super(CataasClient, self).get_context_data(**kwargs)
        cat_tag = 'cute'
        # api_url = ('https://cataas.com/c/{cat_tag}'.format(**locals()))
        # img_response = requests.get(api_url)
        # tag_images_list = []
        # tag_images_list.append(img_response)
        #
        # context['cat_images'] = tag_images_list

        return context
#
# @cache_page(60 * 15)
# def cataas_client(request):
#     """
#     View function for home page of site.
#     """
#     # Render the HTML template cats.html with the data in the context variable
#     cat_tag = 'cute'
#     api_url = ('https://cataas.com/c/{cat_tag}'.format(**locals())) # single
#     # image
#
#     response = requests.get(api_url)
#     context_data = {'cats': response}
#
#     return render(
#         request,
#         'core/base_tempaltes/cats.html',
#         context_data,
#     )