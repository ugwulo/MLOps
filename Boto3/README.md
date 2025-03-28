# Flow
User/App -> Boto3 SDK -> AWS Services

## Requirements

Python 3.8 or later; support for Python 3.7 and earlier is deprecated
[text](https://www.python.org/downloads/release/python-3132/)

py --version

[VSCode](https://code.visualstudio.com/download)

[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### Setup virtual environment and activate it
```
python -m venv .venv

source .venv/bin/activate #Linux
.venv\Scripts\Activate #Windows
source .venv/Scripts/activate
 
```
Boto3
pip install boto3

to confirm run;
python
import boto3


IAM User (Optional)
Configure credentials with IAM secrets

aws configure