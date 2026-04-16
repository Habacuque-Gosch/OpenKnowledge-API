# apps/_template_module/tasks.py

# from celery import shared_task
# from django.conf import settings

# import logging
# logger = logging.getLogger(__name__)


# @shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
# def notify_new_challenge_task(self, challenge_id):
#     print('my-task-celey')