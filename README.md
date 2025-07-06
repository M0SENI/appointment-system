## Compeleted v1.0
## Appointment Management System

This repository contains a comprehensive appointment management system built with Django. The system includes the following features:

- Integrated Login and Logout: A seamless login and logout experience for users, ensuring secure access to the system.
- Appointment Management: Staff members and employees can manage appointments efficiently, including viewing, editing, and confirming appointments.
- Email Verification: An email verification process is in place to ensure the authenticity of user registrations and appointments.
- User Notifications: Users receive email notifications about the status of their appointments, ensuring they are always informed about any changes or updates.

### Features

1. User Authentication: Secure login and logout functionality with Django's built-in authentication system.
2. Staff and Employee Management: Different roles for staff members to manage appointments.
3. Email Notifications: Automated emails for appointment confirmations, reminders, and status updates.
4. Appointment CRUD: Full CRUD (Create, Read, Update, Delete) operations for managing appointments.
5. Responsive Design: A user-friendly interface that works on both desktop and mobile devices.

### Setup

To set up the project locally, follow these steps:

1. Clone the repository:
  
   [git clone https://github.com/M0SENI/appointment-management-system.git](https://github.com/M0SENI/appointment-system.git)
   cd appointment-system
   
2. Create a virtual environment and install dependencies:
  
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   
3. Apply migrations and run the server:
  
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   
4. Configure email settings in settings.py:
  
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.your-email-provider.com'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'your-email@example.com'
   EMAIL_HOST_PASSWORD = 'your-email-password'

![image alt](https://github.com/M0SENI/appointment-system/blob/main/screen.jpg)
   
### Contribution

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any feature requests or bug reports.

### License

This project is licensed under the MIT License. See the LICENSE file for details.


