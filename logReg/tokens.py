from .models import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: CustomUser, timestamp):
        login_timestamp = timezone.datetime.timestamp(user.date_joined)
        return str(user.pk) + str(timestamp) + str(user.is_active) + str(login_timestamp)
