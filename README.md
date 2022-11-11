# Sauce Demo Test

This is a Sauce Demo Test interaction using Python and Selenium.

## Setup

Depending on your OS choose and install latest [Python](https://python.org/) version alongside [pip](https://pip.pypa.io/en/stable/) package manager to install dependencies needed. [Virtualenv](https://virtualenv.pypa.io/en/latest/) is also required for having your projects, code and packages installed in isolation. Don't forget to install [Chromedriver](https://chromedriver.chromium.org/downloads) depending on your current Chrome version for automated tests execution visualization.

## Installation

After downloading this repository proceed with below steps:

- Create a new Virtualenv as a hidden folder in your current directory:

```bash
python3 -m venv .venv
```

- Activate new Virtualenv:

```bash
source .venv/bin/activate
```

- Install dependencies using Pip:

```bash
pip install requirements.txt
```

## Usage

### Add One Article

Automated test can be executed by typing:

```bash
python add_one_article.py
```

Gherkin file can be located as `buy_one_article.feature`

### Add Multiple Articles

Automated test can be executed by typing:

```bash
python add_multiple_articles.py
```

Gherkin file can be located as `buy_multiple_articles.feature`

## Demo (Bonus)

A sample demo file has been included as `demo.json` that consists in automated test flow recording using [Chrome Developers Recorder Tool](https://developer.chrome.com/docs/devtools/recorder/) as an extra point to show a different approach. This file can be imported from Recorder tab and flow will be visualized inside Chrome without further installation needed.

[Playwright Codegen](https://playwright.dev/docs/codegen) feature has been considered also as an alternative for this extra point.
