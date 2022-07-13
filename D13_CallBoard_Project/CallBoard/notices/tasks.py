from django_apscheduler.models import DjangoJobExecution
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Notice
from django.contrib.auth import get_user_model
from datetime import date, timedelta

User = get_user_model()

def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def send_daily_mails():
    list_of_mails = [i[0] for i in list(User.objects.all().values_list('email')) if i[0]]
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    notices = Notice.objects.filter(date_of_creation__date=yesterday)

    if notices and list_of_mails:
        html_content = render_to_string(
            r'notices/mail_forms/daily_mails.html',
            {
                'notices': notices,
                'yesterday': yesterday
            }
        )
        msg = EmailMultiAlternatives(
            subject='Ежедневная рассылка',
            to=list_of_mails
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        print('задача по ежедневной рассылке успещно выполнена')
    else:
        print('письма не была разосланы')
