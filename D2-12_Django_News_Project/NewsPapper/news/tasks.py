from django_apscheduler.models import DjangoJobExecution
from .models import Category, Post
from datetime import datetime
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def send_weekly_mails():
    categories = Category.objects.all()
    for category in categories:
        last_week = datetime.today().isocalendar()[1]
        posts = category.post_set.filter(date_of_creation__week=last_week)
        subscribers_email = [i[0] for i in list(category.subscribers.all().values_list('email'))]
        if posts and subscribers_email:
            html_content = render_to_string(
                r'mails_forms/weekly_news.html',
                {
                    'news': posts
                }
            )
            msg = EmailMultiAlternatives(
                subject='Еженедельная рассылка по подписке',
                to=subscribers_email,
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    print('рассылка писем завершена')
