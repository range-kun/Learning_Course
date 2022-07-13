from django.core.management import BaseCommand, CommandError
from news.models import Category


class Command(BaseCommand):

    help = 'Delete all posts from selected category'
    missing_args_message = 'write name of category'

    def add_arguments(self, parser):
        parser.add_argument(
                            'category',
                            nargs=1,
                            type=str
                             )

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Are you sure you want to delete all '
                          f'posts from {options["category"][0]} category? yes/no')
        response = input()

        if response != 'yes':
            return

        try:
            category = Category.objects.get(category=options["category"][0])
        except Category.DoesNotExist:
            self.stdout.write('This category does not exists')
        else:
            posts = category.post_set.all()
            for post in posts:
                post.delete()
