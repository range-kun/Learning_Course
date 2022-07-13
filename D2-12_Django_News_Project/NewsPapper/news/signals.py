from django.db.models.signals import post_save, m2m_changed
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(m2m_changed,  sender=Post.category.through)
def notify_subscribers(sender, instance, action,**kwargs):
    if action == 'post_add':
        subscribers = instance.category.all().\
            values_list('subscribers__email', 'subscribers__username')
        for subscriber in subscribers:
            html_content = render_to_string(
                r'mails_forms/post_created.html',
                {
                 'single_news': instance,
                 'username': subscriber[1]
                }
            )
            msg = EmailMultiAlternatives(
                subject=instance.header,
                body=instance.text_content,
                to=[subscriber[0]]
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()


