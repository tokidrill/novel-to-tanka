from django.shortcuts import render
from django.http import HttpResponse
from app.modules import novel_string

import random
import re

def index(request):
    return render(request, "app/index.html", context=None)

def run1(request):
    novel_text = novel_string.hayabusa()
    trimmed = novel_string.remove_symbols(novel_text)

    string = 'あそび'

    tankaText = novel_string.pick_text_by_keyword(string, trimmed)

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/index.html", context=context)

def run3(request):
    novel_text = novel_string.hayabusa()
    trimmed_text = novel_string.remove_symbols(novel_text)

    textCount = len(trimmed_text)
    randomNumber = (random.randint(0, textCount - 31))

    tankaText = trimmed_text[randomNumber:randomNumber + 31]

    semitoneStr = "ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ"
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = trimmed_text[randomNumber:randomNumber+31+semitoneCount]

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/index.html", context=context)