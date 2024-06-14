from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import TopicForm, EntryForm
from .models import Topic


def index(request):
    # Página inicial
    return render(request, "learning_logs/index.html")


def topics(request):
    # Página de topicos

    topics = Topic.objects.order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    # Mostra um unico tópico
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


def new_topic(request):
    """Adiciona novo assunto"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("topics"))

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("topic", args=[topic_id]))
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)
