
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MemberProfile
from .utils import generate_qr_code

@receiver(
    post_save,
    sender=MemberProfile
)
def member_post_save(
    sender,
    instance,
    created,
    **kwargs
):

    if created and not instance.qr_code:

        generate_qr_code(instance)

        instance.save(
            update_fields=["qr_code"]
        )