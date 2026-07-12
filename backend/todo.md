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

