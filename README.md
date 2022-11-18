# dashboard-streamlit
HHA 507 Assignment 10

# Assignment Details

1. Please create a new repo called 'dashboard-streamlit'

2. Create a basic streamlit dashboard with data that you have access to (e.g., de-identified data from a group project, or data that you find interesting that is publicly available). The data that you select should have at least one (if not more) of the following fields to be able to complete Step 3 of this assignment:
Date/time stamp
Categorical data
Continuous data
OPTIONAL: position/locational data
The dashboard code and data being used should be included within the github repo

3. The dashboard should include the following components based on the streamlit documentation (https://docs.streamlit.io/library/api-reference) of what is available:
a header
some text
a code-block
2 dataframes
at least 2 charts (e.g., line, area, bar, scatter plot)


4. Please deploy the streamlit application to your cloud of choice and take screen shots of the deployed app with your IP (OR you can deploy it to your new domain name if you want to....)

5. Once completed, you can shut down the VM after taking screen shots and including them in the github repo

## Dataset

I got my data from kaggle:

https://www.kaggle.com/datasets/gregorut/videogamesales

https://www.kaggle.com/datasets/unsdsn/world-happiness


## How to install pyenv in Ubuntu

Install pyenv by using `curl https://pyenv.run | bash`

Enter this code to add into `.bashrc`
```yaml
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Lastly run this code to install all pyenv/python dependencies for Ubuntu (works for WSL2)
```yaml
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

Then restart shell with `exec "$SHELL"`

Confirm pyenv was installed with `pyenv -V`

## Install Python

All dependencies require at least Python 3.9

Assignment was done in Python 3.9.4

Please use the following commands to install Python 3.9.4

```yaml
pyenv install 3.9.4

pyenv global 3.9.4
```

Confirm Python 3.9.4 was installed globalled with `python3 -V`
