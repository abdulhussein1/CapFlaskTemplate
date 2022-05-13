# The purpose of this file is to hold sensitive information that you don't want to 
# post publicly to GitHub.  This file is excluded from being sent to github by .gitignore

# For the email recovery using a gmail account to work you need to turn on "less secure apps" 
# here https://myaccount.google.com/lesssecureapps

def getSecrets():
    secrets = {
        'MAIL_PASSWORD':'00268551',
        'MAIL_USERNAME':'s_abdul.hussein@ousd.org',
        'MONGO_HOST': 'mongodb+srv://abdul:1234@cluster0.9zq8v.mongodb.net/capstone?retryWrites=true&w=majority',
        'MONGO_DB_NAME':'capstone'
        }
    return secrets