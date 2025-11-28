# Smart Result Dispatcher
### Automated Student Result Emailing System (PDF + Email + CSV Automation)

Smart Result Dispatcher is a Python-based automation tool designed for schools, coaching institutes, and colleges to automatically generate **student result PDFs** and send **personalized emails in bulk**.  
It eliminates manual work, reduces human errors, and ensures fast and professional delivery of results.

## Features

### Bulk Email Sending
- Reads student data from a CSV file.
- Sends personalized emails containing:
  - Name  
  - Class  
  - Marks  
  - Attendance  
  - Teacher’s remark  
- Sends clean HTML emails using Jinja2 templates.
- Supports attachments (auto-generated PDFs).

### Automatic PDF Generation
For every student, the system generates a neat PDF result containing:
- Student Name  
- Class  
- Marks  
- Attendance  
- Teacher’s remark  

PDFs include:
- Background template  
- Professional formatting  
- Automatic saving inside `output/reports/`

### HTML Email Templates
- Fully customizable email templates.
- Branding/logo support.
- Simple variable replacement using Jinja2.

### Logging System
Every email attempt is logged in:

