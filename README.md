# Device Tracker

This project is a Django-based API for managing companies, employees, devices, and transactions.

## Features

- Create, retrieve, update, and delete operations for companies, employees, devices, and transactions.
- Automated API documentation using Swagger UI and Redoc.
- Custom API endpoints for various actions.

## Installation

1. Clone the repository:

   ```bash
git clone [<repository-url>](https://github.com/ibugithub/Repliq-test.git)
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Usage
Start the Django development server:

bash
Copy code
python manage.py runserver
Visit the following URLs to access the API endpoints and documentation:

API Root: http://localhost:8000/
API Documentation (Swagger UI): http://localhost:8000/swagger/
API Documentation (Redoc): http://localhost:8000/redoc/
Use API endpoints to perform CRUD operations on companies, employees, devices, and transactions.

API Endpoints
Create Company: POST /create_company/
Show Companies: GET /show_company/
Create Employee: POST /create_employee/
Show Employees: GET /show_employee/
Create Device: POST /create_device/
Show Devices: GET /show_device/
Create Transaction: POST /create_transaction/
Show Transactions: GET /show_transaction/
Contributing
Contributions are welcome! Please follow the contribution guidelines.

## 👥 Authors <a name="authors"></a>

This project was developed by 
👤 **Ibrahim Hossain**
- GitHub: [ibugithub](https://github.com/ibugithub)
- LinkedIn: [ibuu](https://www.linkedin.com/in/ibuu/)
- Twitter: [@mdibrahimibuu](https://twitter.com/mdibrahimibuu)



## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>