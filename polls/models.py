from django.db import models


class Question(models.Model):
    """
    每个字段都是Field类的实例, 需要告诉Django每个字段需要处理的数据类型
    变量的名称就是字段的名称
    激活模型时: (首先需要把我们的应用安装到我们的项目里)
    1> Django为这个应用创建schame (生成CREATE TABLE语句)
    2> 创建可以与Question和Choice对象进行交互的python数据库API
    """
    question_txt = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    auth = models.CharField(max_length=16)

    def __str__(self):
        return "Question[question_text=%s, publish_date=%s, auth=%s]" \
               % (self.question_txt, self.publish_date, self.auth)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "Choice[choice_txt=%s, votes=%d]" % (self.choice_txt, self.votes)
