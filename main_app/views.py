from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus


# Create your views here.
def home(request):
    content = []
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        url = requests.get(f"https://search.yahoo.com/search?p={quote_plus(request.GET.get('search'))}")
        soup = BeautifulSoup(url.content, 'html.parser')
        parent_div = soup.find_all("div", {'class': 'dd'})
        for data in parent_div:
            search_title = data.find("a", {'class': 'ac-algo'})
            if search_title is not None:
                search_description = data.find("p", {'class': 'lh-16'})
                content.append(
                    [search_title.text, search_title.get('href'), search_description.text if search_description else '']
                )
            context = {
                'search': search,
                'content': content
            }
    context = {
        'search': search,
        'content': content
    }
    return render(request, 'index.html', context)
