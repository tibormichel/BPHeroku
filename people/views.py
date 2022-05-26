from django.views.generic import ListView, DetailView
from .models import Person
import requests


class HomeView(ListView):
    model = Person
    template_name = 'people/people.html'

class ArticleDetailView(DetailView):
    model = Person
    template_name = 'people/person_details.html'
    # print(str(model.maisID))

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        tmp = '@xxaq22'
        obj = Person.objects.all()
        for i in obj:
            field_object = Person._meta.get_field('id')
            field_value = field_object.value_from_object(i)
            if field_value == self.kwargs['pk']:
                field_object = Person._meta.get_field('maisID')
                tmp = field_object.value_from_object(i)

        # print(tmp)
        try:
            context['response'] = requests.get(
                "https://kpi:GWsy6BfLfc9rUB03tT6e@maisutils.tuke.sk/export/?vystup=rozvrh_pedagoga&login=" + tmp).json()
            x = requests.get(
            "https://kpi:GWsy6BfLfc9rUB03tT6e@maisutils.tuke.sk/export/?vystup=rozvrh_pedagoga&login=" + tmp).json()

        # y = json.loads(x)
        # print(x)
            subjects = []
            semester = []
            day = []
            room = []
            time1 = []
            time2 = []
            for i in x:
                # print(i)
                subjects.append(i['skratka_ps'])
                semester.append(i['semester'])
                day.append(i['den'])
                room.append(i['miestnost'])
                time1.append(i['cas1'])
                time2.append(i['cas2'])

            context['subjects'] = subjects
            context['semester'] = semester
            context['day'] = day
            context['room'] = room
            context['time1'] = time1
            context['time2'] = time2

        finally:
            return context
