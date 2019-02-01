import requests

from django.views.generic import FormView
from django.views.decorators.cache import cache_page
from PIL import Image
from ..forms.tag_form import TagForm


class CacheMixin(object):
    """
    Here we set our custom cache manager overriding the dispatch method
    to be able to wrap nicely around class object and also set a non
    expiring time for the caching.
    """

    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).
                                                    dispatch)(*args, **kwargs)


class CataasClient(CacheMixin, FormView):
    """
    View to show home page and allow user to search cat images by tag of
    interest.

    Arguments:
    ---------
    tag: this is a tag to be entered into search form
    type(string)

    Return type: list of cat images in json format
    """

    template_name = 'cats.html'

    # we set timeout to None so that, by default, cache keys never expire.
    cache_timeout = None
    form_class = TagForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(CataasClient, self).get_context_data(**kwargs)

        tag = 'self.tag'
        api_url = 'https://cataas.com/#/search/tag/{cat_tag}'.format(
            cat_tag=tag)

        response_data = requests.get(api_url)

        context['cat_images'] = response_data.json

        msg = """
            I faced a challenge authenticating with the CATAAS API and 
            that they do not seem to have a broad documentation, hence I 
            I will find a workaround to resolve this.
            
            In the meantime I will submit this work which is almost complete 
            and you can review on most of my capacity as well as the stack 
            around the project.
            Thanks you
        """
        context['message'] = msg

        return context

    def form_valid(self, form):
        # we sill store the form input data in a variable here
        # and make it visible in the context data method
        self.tag = form.cleaned_data['tag']

        return super(CataasClient, self).form_valid(form)
