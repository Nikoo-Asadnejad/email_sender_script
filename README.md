# Email Sender Script

This Python script allows you to send an email using the SMTP (Simple Mail Transfer Protocol) service. The script is set up for Gmail but can be modified to work with other SMTP servers.

## Features

- Send an email using a Gmail account.
- Customize the email subject, body, and recipient.
- Secure communication with the email server via SSL.

## Prerequisites

- Python 3.x installed.
- A Gmail account (or other email account with SMTP access).
- No additional libraries are required as it uses Python's built-in `smtplib` and `email` libraries.

## Setup

### sEnable "Less Secure Apps" in Gmail

To send emails via Gmail, you'll need to enable less secure apps:

1. Go to your [Google Account Security settings](https://myaccount.google.com/security).
2. Scroll down to "Less secure app access" and turn it on.

Alternatively, you can use App Passwords for more secure access, or configure OAuth 2.0 (advanced setup).

