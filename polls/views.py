from django.http.response import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import logging
logging.basicConfig(level=logging.INFO)


# 定义问题索引页
def index(request):
    logging.info("index view.")
    # 查询数据库, 列出以publish_date排序的最近5个问题, 以空格分开, 加-的意思是降序排序
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    # 使用列表生成式生成问题列表
    # output = ", ".join([q.question_txt for q in latest_question_list])

    # 加载模板, 是templates目录的相对路径
    template = loader.get_template("polls/index.html")
    # 提供一个上下文, 字典中的key在模板中作为变量名来应用
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


# 第二版, 使用快捷函数: render(), 该方法接收三个必须参数: 第一个request对象, 第二个模板名称, 第三个上下文.
# 可选参数content_type, status
def index_v2(request):
    logging.info("index_v2 view.")
    # 查询数据库, 列出以publish_date排序的最近5个问题, 以空格分开, 加-的意思是降序排序
    latest_question_list = Question.objects.order_by("-publish_date")[:5]
    # 使用列表生成式生成问题列表
    # output = ", ".join([q.question_txt for q in latest_question_list])

    # 提供一个上下文, 字典中的key在模板中作为变量名来应用
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context, "text/html", 200)


# 问题详情页
def detail(request, question_id):
    logging.info("detail view. ")
    # 抛出404错误
    try:
        question = Question.objects.get(pk=question_id)
        context = {"question": question.question_txt}
    except Question.DoesNotExist:
        raise Http404("Question dose not exist.")
    return render(request, "polls/detail.html", context, content_type="text/html", status=200)


# 详情页v2, 使用快捷函数get_object_or_404(), 该方法尝试获取一个对象, 如果对象不存在则报错404
def detail_v2(request, question_id):
    logging.info("detail_v2 view. ")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


# 问题结果页
def results(request, question_id):
    return HttpResponse("You're looking at the result of question [%s]." % question_id)


# 投票处理器
def vote(request, question_id):
    return HttpResponse("You're voting on question [%s]." % question_id)
