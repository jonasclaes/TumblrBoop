# TumblrBoop

TumblrBoop is a Python automation script designed to leverage the Playwright framework to automate the process of "
booping" users on Tumblr.  
This feature, introduced as part of an April Fools' day event, allows users to boop others for fun and earn badges based
on the number of boops sent. With TumblrBoop, you can automate sending boops to a specified account, including your own,
to participate in the event without manual intervention.

## Features

- Automated booping using Playwright.
- Configurable target account and boop count.
- Optional TOTP (Time-based One-Time Password) for enhanced login security.

## Requirements

Before running TumblrBoop, ensure you have the following installed:

- Python 3.6 or later.

You can install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to configure it by filling out your Tumblr credentials and target account details
in `config.py`:

- `ACCOUNT_EMAIL`: Your email address used for Tumblr.
- `ACCOUNT_PASSWORD`: Your password for Tumblr.
- `ACCOUNT_TOTP_SECRET`: (Optional) Your TOTP secret if you have two-factor authentication enabled. Leave as `None` if
  not used.
- `BOOP_LIST`: The Tumblr username of the accounts you wish to boop, separated by space. e.g. "blog1 blog2 blog3" This can be your own account.
- `AMOUNT_OF_BOOPS_TO_SEND`: The total number of boops you wish to send.

## Usage

To run the script, use the following command in your terminal:

```bash
python main.py
```

Ensure you're in the same directory as `main.py` when you run this command.

## Security Note

Your account credentials are sensitive information. Ensure that `config.py` is stored securely and is not shared or
committed to version control systems.

## Disclaimer

This script is intended for educational purposes and to demonstrate automation with Playwright. Please respect Tumblr's
terms of service when using this script. The creators of TumblrBoop are not responsible for any potential consequences
of using this automation tool.

## Contributing

Contributions to TumblrBoop are welcome. Please feel free to fork the repository, make your changes, and submit a pull
request.
