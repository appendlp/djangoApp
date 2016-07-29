from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('sample/sample.html')
    context = {
        'video': 'http://103.7.29.34/vhot2.qqvideo.tc.qq.com/v03159tst0p.mp4?sdtfrom=v1010&guid=7f8d114d960a6e164a63b9b675293070&vkey=50AC628DE93D7A70D0BEDF80C97580455AA3FD68767AD3224E6646967B18EC572D973AEA043BE650E285C87CC4076FBB3725330AD683CE4F07B8C42FF10DE5F396ACBFF001172E17BF83DA83E732625C31439AD6C3AD4916&guid=7f8d114d960a6e164a63b9b675293070',
    }
    return HttpResponse(template.render(context, request))