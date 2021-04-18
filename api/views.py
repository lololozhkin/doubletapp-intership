import json

from django.http import HttpRequest, HttpResponse, Http404
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Category, Theme, Word, Level
from .utils import dump_query, dump_obj, prepare_obj_dict, prepare_query


JSON_TYPE = 'application/json'


class CategoriesView(View):
    def get(self, request: HttpRequest):
        return HttpResponse(
            dump_query(Category.objects.all(), fields=('id', 'name', 'icon')),
            content_type=JSON_TYPE
        )


class LevelsView(View):
    def get(self, request: HttpRequest):
        return HttpResponse(
            dump_query(Level.objects.all(), fields=('id', 'name', 'code')),
            content_type=JSON_TYPE
        )


class ThemesView(View):
    def get(self, request: HttpRequest):
        category = request.GET.get(key='category')
        level = request.GET.get(key='level')

        if category is None or level is None:
            raise Http404()

        return HttpResponse(
            dump_query(
                Theme.objects.filter(category__id=category, level__id=level),
                fields=('id', 'category_id', 'level_id', 'name', 'photo'),
                fields_renaming={
                    'category_id': 'category',
                    'level_id': 'level'
                }
            ),
            content_type=JSON_TYPE
        )


class ThemeView(View):
    def get(self, request: HttpRequest, theme_id):
        obj = Theme.objects.get(pk=theme_id)
        serialized = prepare_obj_dict(
            obj,
            fields=('id', 'category_id', 'level_id', 'name', 'photo'),
            fields_renaming={
                'category_id': 'category',
                'level_id': 'level'
            }
        )

        words = prepare_query(
            obj.word_set.all(),
            fields=('id', 'name')
        )
        serialized['words'] = words

        return HttpResponse(
            json.dumps(serialized),
            content_type=JSON_TYPE
        )


class WordsView(View):
    def get(self, reuqest: HttpRequest, word_id):
        obj = get_object_or_404(Word, pk=word_id)

        fields = (
            'id', 'name', 'translation', 'transcription', 'example', 'sound'
        )

        return HttpResponse(
            dump_obj(obj, fields=fields),
            content_type=JSON_TYPE
        )
