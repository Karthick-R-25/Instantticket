# **Real-Time Ticket Booking System**

This is a **Real-Time Ticket Booking System** for local and overcrowded Buses  , built with the following technologies:

### **Frontend:**
- **HTML**
- **CSS**
- **JavaScript**
- **Bootstrap**

### **Backend:**
- **Python**
- **Django**
- **REST API**
- **SQL** (MYSQL)

### **Authentication and Security:**
- **CSRF Token** for protection against cross-site request forgery

### **Features:**
- **Passenger Registration:** Passengers register with their details, including mobile number.
- **Bus Owner Registration:** Bus owners register with their license plate number and required details.
- **Conductor Dashboard:** The conductor can log in and manage routes, along with their prices.
- **Dynamic Pricing for Passengers:** Passengers log in, enter the bus ID and passenger count to see available stops and dynamic pricing.
- **Payment and Verification:** After making a payment, passengers receive a unique 3-digit code for verifying their route, price, and details.
- **Ticket Generation:** Conductor verifies the code, confirms passenger details, and prints the ticket. All information is stored in the passenger history.

### **Technologies Used:**
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Backend:** Python, Django, REST API, MYSQL, SQL
- **Security:** CSRF Token, User Authentication

### **Setup and Installation:**

1. Clone the repository:
   ```bash
   git clone https://github.com/Karthick-R-25/Realtime-Ticket-Booking.git
### **Setup and Running the Project**
2. MySQL Database Configuration in Django

To configure your MySQL database in Django, update the `DATABASES` setting in your `settings.py` file like the following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use MySQL database engine
        'NAME': 'yourdb_name',                 # Your database name
        'USER': 'root',                        # Your MySQL username
        'PASSWORD': 'Your_password',           # Your MySQL password
        'HOST': 'localhost',                   # Host of the database, use 'localhost' or your server IP
        'PORT': '3306',                        # Default MySQL port
    }
}


3. **Create and Activate Virtual Environment:**
   For Linux/MacOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   cd engine
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver


4.Also have Amazon EC2 Instance contact I can start live server mailid:karthickr2429@gmailcom


5.Preview Video
  https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22django%20final%20video.mp4%22%2C%22type%22%3A%22video%2Fmp4%22%2C%22signedurl_expire%22%3A%222028-04-21T04%3A03%3A47.311Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2Fff9d7318389f45bc%2Fdjango%20final%20video.mp4%3FExpires%3D1839902627%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3Dy0gW0Wm8joG0CSnB2oc5f2kbVvdRfkdlDRQ5yIoqMR7XV8D5BYRAsemXP52Lw57YXB1l-xJbOWJYZxmnLTks9zatAgpI28Rt7WVA8UaI~ZZoy6VNUn~G3SNSNbH9zat6nxZuMm2u70YgaOUfYkBwH53cvfTE7GoWWelT-abudTggQ4QMJQAKK-WAv3w4eSqZy6E-lEvcjXeC6yqU3ld2AElNs~YdD9RwhVPOeXV8p1PgDgZaXPnJvyfSxzTDrGUZyt~KE4rWA9oaPImliZeWXNQg8O8D0uhUBgL9PNINIfL~fzEJ3uy5jW1bYFKjas41Cm-MWngFkaIUR16Gughtfg__%22%7D





