# 🚀 API Automation Framework (Python + Pytest)

A scalable, production-style API automation framework built using **Python**, **Pytest**, and **Requests**.
Designed with clean architecture principles, schema validation, logging, and environment configuration.

---

## 📌 Overview

This framework demonstrates:

* Layered architecture
* Reusable API client
* Endpoint abstraction
* JSON schema validation
* Environment-based configuration
* HTML reporting
* Logging support

It is structured to simulate a real-world API automation project used in backend-heavy systems.

---

## 🏗 Project Architecture

```text
api-automation-framework/
│
├── core/
│   ├── api_client.py        # Handles HTTP requests
│   ├── base_test.py         # Common assertions
│
├── endpoints/
│   ├── users_api.py         # Users API methods
│   ├── auth_api.py          # Authentication API methods
│
├── schemas/
│   ├── create_user_schema.py
│
├── tests/
│   ├── test_users.py
│   ├── test_auth.py
│
├── utils/
│   ├── config.py            # Environment configuration
│   ├── logger.py            # Logging setup
│   ├── helpers.py           # Schema validation helper
│
├── reports/                 # HTML reports & logs
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧠 Design Principles

### 1️⃣ Separation of Concerns

* `APIClient` handles HTTP logic.
* `endpoints` contain business-level API methods.
* `tests` focus only on validation.
* `utils` contain reusable utilities.

### 2️⃣ Reusable Session Management

Uses `requests.Session()` for connection pooling and performance optimization.

### 3️⃣ Schema-Based Validation

Implements JSON schema validation to ensure API contract consistency.

### 4️⃣ Environment Switching

Supports multiple environments (QA / Stage / Prod) using environment variables.

---

## 🛠 Tech Stack

* Python 3.10+
* Pytest
* Requests
* JSONSchema
* Pytest-HTML

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd api-automation-framework
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Generate HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 🌍 Environment Configuration

Set environment variable before running tests:

**Windows**

```bash
set ENV=qa
```

**Mac/Linux**

```bash
export ENV=qa
```

Environments supported in `config.py`:

* qa
* stage
* prod

---

## 📊 Reporting & Logs

After execution:

* 📄 HTML Report → `reports/report.html`
* 📝 Log File → `reports/api.log`

---

## 🧪 Example Test Scenario

### ✔ GET Users

* Validate status code
* Validate response structure
* Validate data presence

### ✔ POST Create User

* Validate response code
* Validate schema contract
* Validate returned fields

---

## 🎯 Key Features

* Layered architecture
* Centralized API client
* JSON schema validation
* Environment-based configuration
* HTML reporting
* Logging support
* Clean, scalable structure

---

## 💡 Future Enhancements (Optional)

* Token-based authentication handling
* Data-driven testing
* Response time validation
* CI/CD integration (Jenkins/GitHub Actions)
* Docker support

---

## 👨‍💻 Author

Gaurav Chaudhari
Python | API Automation | Test Architecture Enthusiast

---

## 📜 License

This project is intended for educational and demonstration purposes.

