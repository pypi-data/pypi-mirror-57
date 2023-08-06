import unicodedata
import re
import json

from django.http import HttpResponse
from django.utils.functional import lazy
from django.urls import path, re_path
from django.views.generic.base import TemplateView


class JSONResponse(HttpResponse):
    def __init__(self, content, mimetype="application/json", *args, **kwargs):
        encoded_content = json.dumps(content)
        super(JSONResponse, self).__init__(
            content=encoded_content,
            mimetype="application/json",
            status=200,
            *args,
            **kwargs
        )


def slugify(phrase):
    """
    Removes all non-important words to generate a meaningful slug.
    """
    from nltk import pos_tag, word_tokenize

    tokens = pos_tag(word_tokenize(phrase))
    words = []
    for token, pos in tokens:
        if pos in ["CD", "IN", "JJ", "JJR", "NN", "NNP", "VB", "VBG", "VBN", "WRB"]:
            words.append(token)
    phrase = " ".join(words)
    symbols = re.compile(r"[^\w]")
    dashes = re.compile(r"-+")
    phrase = phrase.decode("unicode_escape")
    phrase = unicodedata.normalize("NFKD", phrase)
    phrase = phrase.encode("ascii", "ignore")
    phrase = phrase.lower()
    phrase = symbols.sub("-", phrase)
    phrase = dashes.sub("-", phrase)
    phrase = phrase.strip("-")
    return phrase


def template_url(path):
    """
    Shortcut method that generates a url for paths which map directly to
    templates.

    For example, the following will map "/home" to the `home.html` template.

        simple_url('home')

    :param path: the URL path that you would like to the template to
    :type path: str
    """
    return re_path(
        r"^{}$".format(path), TemplateView.as_view(template_name=path + ".html")
    )


def home_url(logged_out_name, logged_in_name=None, app_name="app"):
    """
    Shortcut method that serves two different views at '/', depending
    on whether the user is logged in or logged out.

    For example, the following will map "/" to the `home` view when the user is
    logged in, and the `landing` view when the user is not logged in.

        home_url('landing', 'home')

    :param logged_out_name: the name of the view that's served when the user is
    logged out
    :type logged_out_name: str

    :param logged_in_name: the name of the view that's served when the user is
    logged in
    :type logged_in_name: str

    :param app_name: the Django application used to serve the views
    :type app_name: str
    """
    app = __import__(app_name, fromlist=["views"])
    logged_out_view = getattr(app.views, logged_out_name)

    if logged_in_name:
        logged_in_view = getattr(app.views, logged_in_name)

        def authentication_redirect(request):
            if request.user.is_authenticated():
                return logged_in_view(request)
            else:
                return logged_out_view(request)

        return re_path(r"^$", authentication_redirect)

    return re_path(r"^$", logged_out_view)


def status_204(request):
    """ Simple view which returns an empty 204 No Content response """
    return HttpResponse(status=204)
