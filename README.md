QR4CV is a minimal Python class to create QR codes to be used in a CV. The class is built on top of [Segno](https://github.com/heuer/segno).

## Installation
1. Clone the repository to your local:
```
$ git clone https://github.com/Karolsoon/QR4CV.git
```
<br/><br/><br/>
3. And use `pip` to install the dependencies:
```
$ pip install -r requirements.txt
```
<br/><br/><br/>
3. Replace the dummy data in `my_secrets.py` with the one you need.
<br/><br/><br/>
4. Afterwards upload/create images to be used as part of your QR codes:
```
static/linkedin-logo-black.png
static/GitHub_Logo.png
static/contact-white.png
```

... or change the location in `main.py`.
<br/><br/><br/>
5. Finally run:
```
python main.py
```

And enjoy the view!

<hr>

- Github QR code
![QR Code with a link to my github page](example_output/github_qr.png)

- Linkedin QR code
![QR Code with a link to my linkedin page](example_output/linkedin_qr.png)

- Contact QR code (a.k.a. vCard 3.0)
![QR Code with dummy contact data](example_output/contactb_qr.png)
