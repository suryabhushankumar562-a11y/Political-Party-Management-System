from datetime import datetime
import os
import qrcode
from io import BytesIO
from django.core.files import File


def generate_membership_id():

    from .models import MemberProfile

    year = datetime.now().year

    last_member = (
        MemberProfile.objects
        .filter(membership_id__startswith=f"NBP-{year}-")
        .order_by("-id")
        .first()
    )

    if last_member:

        last_number = int(last_member.membership_id.split("-")[-1])

        new_number = last_number + 1

    else:

        new_number = 1

    return f"NBP-{year}-{new_number:05d}"



def generate_qr_code(member):

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )

    verification_url = (
        f"http://10.18.201.122:8000/members/verify/"
        f"{member.membership_id}/"
    )

    qr.add_data(verification_url)

    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    filename = f"{member.membership_id}.png"

    member.qr_code.save(
        filename,
        File(buffer),
        save=False
    )