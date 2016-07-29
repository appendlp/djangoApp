from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('sample/sample.html')
    context = {
        'video': 'https://v.qq.com/iframe/player.html?vid=v03159tst0p&tiny=0&auto=0',
    }
    return HttpResponse(template.render(context, request))