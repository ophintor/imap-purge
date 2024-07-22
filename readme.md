**Purge emails from IMAP server**

Default: > 750 days but check the code to amend.

```
cd ~/imap-purge
source .venv/bin/activate
python3 -m pip install imap-tools
python3 purge-email.py <email> <password>
```
