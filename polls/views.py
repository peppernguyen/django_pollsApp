from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question
from django.utils import timezone
from django.shortcuts import HttpResponseRedirect, redirect
# class IndexView(generic.ListView):
    # template_name = 'polls/index.html'
    # context_object_name = 'latest_question_list'
    #
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
    # return res
def index(request):
    # context = {'name': 'Miojd', 'age': 19}
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    all_choices = question.choice_set.all()
    context = {'question': question, 'all_choices': all_choices}
    return render(request, 'polls/detail.html', context)

#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

def results(request, question_id):
    return render(request, 'polls/results.html')

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def add(request):
    # myDict =dict((request.POST).list())
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    if request.method == "GET":
        return render(request, 'polls/add.html')
    question = request.POST.get("question")
    content = {'latest_question_list': latest_question_list, 'question': question}
    if request.POST.get("submit") == "Submit":
        q = Question(question_text=question, pub_date=timezone.now())
        q.save()
    if request.POST.get("home") == "Home":
        return render(request, 'polls/index.html', content)
    # print(dir(request))
    return render(request, 'polls/add.html',content)

def edit(request, question_id):
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    content = {'latest_question_list': latest_question_list, 'question': question, 'id': question_id}
    if request.POST.get("update") == "Update":
        question.question_text = request.POST.get("question")
        question.pub_date = request.POST.get("pubdate")
        question.save()
    if request.POST.get("home") == "Home":
        return render(request, 'polls/index.html', content)
    return render(request,'polls/edit.html',content)

def delete(request, question_id):
    question = Question.objects.get(pk=question_id)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    content ={'latest_question_list': latest_question_list, 'question': question, 'id': question_id}
    if request.POST.get('Yes') == "Yes, sure!":
        question.delete()
        return render(request, 'polls/index.html', content)
    if request.POST.get("No") == "No, take me back!":
        return render(request, 'polls/index.html', content)

    return render(request, 'polls/del.html', content)
