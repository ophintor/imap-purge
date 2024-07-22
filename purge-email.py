import datetime, sys
from imap_tools import MailBox, A

email_address = sys.argv[1]
password = sys.argv[2]

# TODO: import config file with default / non-default times
older_than_days_dict = {
    "default": 750,
    # "INBOX.0-hilda": 365,
    # "INBOX.admin.bills": 365,
    # "INBOX.admin.kirsty": 365,
    # "INBOX.admin.school": 365,
    # "INBOX.bristol.shirehampton": 365,
    # "INBOX.shopping": 365,
}

with MailBox('mail.dreamhost.com').login(email_address, password) as mailbox:
    for f in mailbox.folder.list('INBOX'):
        print(f"Purging {f.name}... ", end='')
        with MailBox('mail.dreamhost.com').login(email_address, password, f.name) as mailbox_folder:
            if f.name in older_than_days_dict.keys():
                print(f"[{older_than_days_dict[f.name]} days]")
                mailbox_folder.delete(mailbox_folder.uids(A(date_lt=datetime.date.today() - datetime.timedelta(days=older_than_days_dict[f.name]))))
            else:
                print(f"[{older_than_days_dict["default"]} days]")
                mailbox_folder.delete(mailbox_folder.uids(A(date_lt=datetime.date.today() - datetime.timedelta(days=older_than_days_dict["default"]))))
