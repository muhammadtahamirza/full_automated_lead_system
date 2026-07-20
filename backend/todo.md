heres the complete tables

lead
mailaccount
template
campaign


campaginTemplate (many to many between camp and template)
campaingLead (connecting lead, mailaccount. template , capmagin, status)


----- Workflow :

1. user will add list of leads via csv etc
2. uesr will add templates manually
3. user will add Mailaccounts manually


4. user will inialize campgsin by setting up system settings for AI llm
5. user will import related templates from stored db
6. uesr will impiort unsent leads from stored db


7. sysetm will create schedulize emails
8. system will start sending emails


brief tasks:
1.1 upload csv for leads
1.2 upload templates to particular campgasin


2. warm up mailboxes tool,


3.1 creat campgasinLeads by using (particular campgsin templates + leads selected ) round robins scheduling
3.2 send them efficeiently


later tasks:
1. scraping, validating leads
2. AI based personalized emails for specific leads


$ docker run -d --name redis -p 6379:6379 -p 8001:8001 redis:latest
