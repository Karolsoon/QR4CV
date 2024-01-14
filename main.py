from datetime import date
from pathlib import Path

import segno
from segno import helpers

from my_secrets import LINKEDIN_URL, GITHUB_URL, COMPANY_NAME, Contact_Data


QR_TYPES = {
    'linkedin': {
        'url': LINKEDIN_URL,
        'target_filename': f'output/{COMPANY_NAME}_{date.today()}/linkedin_qr.png',
        'background_path': 'static/linkedin-logo-black.png'
    },
    'github': {
        'url': GITHUB_URL,
        'target_filename': f'output/{COMPANY_NAME}_{date.today()}/github_qr.png',
        'background_path': 'static/GitHub_Logo.png'
    },
    'contact': {
        'contact_data': Contact_Data,
        'target_filename': f'output/{COMPANY_NAME}_{date.today()}/contact_qr.png',
        'background_path': 'static/contact-white.png'
    }
}


class QR4CV(object):
    def __init__(
            self,
            target_filename: str,
            background_path: str,
            url: str|None = None,
            contact_data: Contact_Data|None = None):
        self.url = url
        self.target_filename = target_filename
        self.background_path = background_path
        self.contact_data = contact_data

    def make_qr(self) -> bool:
        self.create_directory()
        if self.url:
            self.make_url_qr()
        elif self.contact_data:
            self.make_contact_qr()

    def make_url_qr(self):
        qrcode = segno.make_qr(self.url, version=7, error='h')

        qrcode.to_artistic(
            background=self.background_path,
            target=self.target_filename,
            scale=8,
            border=2,
            light='#B3ADA4',
            dark='black'
        )

    def make_contact_qr(self):
        vcard = helpers.make_vcard_data(
            name=self.contact_data.name,
            displayname=self.contact_data.displayname,
            email=self.contact_data.email,
            phone=self.contact_data.phone,
            url=LINKEDIN_URL
        )

        qrcode = segno.make_qr(vcard, error='H')

        qrcode.to_artistic(
            background=self.background_path,
            target=self.target_filename,
            scale=4,
            border=2,
            light='#B3ADA4',
            dark='black'
        )

    def is_valid(self, qr_type: str) -> bool:
        return qr_type in QR_TYPES

    def validate(self, qr_type: str) -> None:
        if not self.is_valid(qr_type):
            raise ValueError(f'Unsupported QR type. Valid values are {QR_TYPES.keys()}')

    def create_directory(self):
        Path(self.target_filename).parent.mkdir(exist_ok=True)


if __name__ == '__main__':
    github_qr = QR4CV(**QR_TYPES['github'])
    github_qr.make_qr()

    linkedin_qr = QR4CV(**QR_TYPES['linkedin'])
    linkedin_qr.make_qr()

    contact_qr = QR4CV(**QR_TYPES['contact'])
    contact_qr.make_qr()
