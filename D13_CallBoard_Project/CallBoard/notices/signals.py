from django.db.models.signals import post_save
from .models import Reply
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Reply)
def notify_author(sender, instance, created, **kwargs):
    author_of_notice = instance.notice.author
    args = {'author_of_notice': author_of_notice,
            'notice': instance.notice,
            'author_of_reply': instance.user,
            'reply': instance}
    if created:
        html_content = render_to_string(
            r'notices/mail_forms/reply_added.html',
            args
        )
        msg = EmailMultiAlternatives(
            subject='Добавлен отклик',
            to=[author_of_notice.email, ]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    elif not created and instance.accepted:
        html_content = render_to_string(
            r'notices/mail_forms/reply_accepted.html',
            args
        )
        msg = EmailMultiAlternatives(
            subject='Отклик принять',
            to=[instance.user.email, ]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
