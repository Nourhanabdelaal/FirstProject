email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawe@sgh.waw.'
email4 = 'pawesgh.waw.'
email5 = 'pawesgh.waw.@'
email6 = 'pawesgh.waw.@sgh'

email_list = [email1, email2, email3, email4, email5, email6]

def email_validation(email):
    at_pos = email.find("@")
    if email[-1] in ["@", "."]:
        return False
    elif at_pos == 0:
        return False

    return True

for em in email_list:
    print('{}: {}'.format(em, email_validation(em)))



