from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.shortcuts import render



class IndexView(TemplateView):
    template_name = "romanload/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class DocumentationIndexView(TemplateView):
    template_name = 'romanload/documentation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context.update({
        #    'latest_python2': Release.objects.latest_python2(),
        #    'latest_python3': Release.objects.latest_python3(),
        #})
        return context

def spring(request, img_name):
    return render(request, 'weixinlianjie.html', {'spring': img_name})


def rd(request):
    return render(request, 'rd.html')
