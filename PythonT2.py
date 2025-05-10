def is_valid_email(email):
    if "@" in email and "." in email:
        if email.count("@") == 1:
            username, rest = email.split("@")
            if username and "." in rest:
                domain, extension = rest.split(".")
                if domain and extension:
                    return True
    return False


print(is_valid_email("user@domain.com"))   
print(is_valid_email("user@domain"))     
print(is_valid_email("userdomain.com"))    
