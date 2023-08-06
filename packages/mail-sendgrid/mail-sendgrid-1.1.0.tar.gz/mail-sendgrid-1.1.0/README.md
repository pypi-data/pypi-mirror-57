# mail-sendgrid

[![Travis](https://img.shields.io/travis/hardwario/mail-sendgrid/master.svg)](https://travis-ci.org/hardwario/mail-sendgrid)
[![Release](https://img.shields.io/github/release/hardwario/mail-sendgrid.svg)](https://github.com/hardwario/mail-sendgrid/releases)
[![License](https://img.shields.io/github/license/hardwario/mail-sendgrid.svg)](https://github.com/hardwario/mail-sendgrid/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/mail-sendgrid.svg)](https://pypi.org/project/mail-sendgrid/)


```sh
mail-sendgrid --help
```

```
Usage: mail-sendgrid [OPTIONS]

  Cli tool for send mail over sendgrid.

Options:
  -f, --from EMAIL         Email address to send from.  [required]
  -t, --to EMAIL/FILE      Email address or file with address, recipient to
                           receive of this email.  [multiple]  [required]
  --cc EMAIL/FILE          Email address or file with address, recipient to
                           receive a copy of this email.  [multiple]
  --bcc EMAIL/FILE         Email address or file with address, recipient to
                           receive a blind carbon copy of this email.
                           [multiple]
  -s, --subject SUBJECT    Email subject.  [required]
  -c, --content TEXT/FILE  Email content, support jinja2 template.  [required]
  -a, --attachment FILE    Email attachment.  [multiple]
  --var KEY VALUE          Jinja2 template variable.  [multiple]
  --variable-yaml FILE     Jinja2 template variables in YAML format.
                           [multiple]
  --nl2br                  Replace all new line with br tag.
  --no-send                Skip send, print rendered content.
  --apikey APIKEY          Sendgrid api key or use env: SENDGRID_API_KEY.
                           [required]
  --version                Show the version and exit.
  -v, --verbosity LVL      Either CRITICAL, ERROR, WARNING, INFO or DEBUG
  --help                   Show this message and exit.
```

## Development
```
git clone git@github.com:hardwario/mail-sendgrid.git
cd mail-sendgrid
sudo python3 setup.py develop
```
