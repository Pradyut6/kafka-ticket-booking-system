# 📁 Kafka-Based Ticket Booking System

A microservices-based ticket booking system built using FastAPI, Kafka, and Docker. It simulates a real-world flow of booking tickets, notifying users, and processing payments using decoupled services.

---

## 🧰 Tech Stack
- **FastAPI**: REST APIs for Booking and Services
- **Kafka**: Event-driven communication between services
- **Docker**: Containerized microservices
- **Playwright + PyTest**: End-to-end and unit testing
- **GitHub Actions**: CI/CD pipeline
- **Terraform (Optional)**: Infrastructure as Code for EC2 deployment

---

## 🧱 Architecture Diagram

```plaintext
+------------+        POST /book         +-------------------+
|  Frontend  |  --------------------->   | Booking Service   |
+------------+                          +-------------------+
                                              |
                                              | Kafka (booking_topic)
                                              v
                                   +---------------------+
                                   | Notification Service|
                                   +---------------------+
                                              |
                                              v
                                   +------------------+
                                   | Payment Service  |
                                   +------------------+
```

---

## 📦 Features
- Book tickets via API (`/book`)
- Kafka event publishing for new bookings
- Real-time notification service
- Simulated payment processing
- Containerized services with `docker-compose`
- CI/CD pipeline and unit + E2E tests

---

## 🚀 Running the Project Locally

### 🔧 Prerequisites
- Docker & Docker Compose
- Python 3.9 (for running tests)

### 🐳 Step-by-step
```bash
# Create Docker network (if not already created)
docker network create kafka-net

# Run Kafka stack
docker-compose up --build

# (Optional) Test the booking API
curl -X POST http://localhost:8000/book \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"event_id":101,"seat_number":"A12"}'
```

---

## 🧪 Running Tests
```bash
# Run unit tests
pytest tests/api_tests
pytest tests/kafka_tests

# Run Playwright tests
npx playwright test tests/playwright_tests
```

---

## 📂 Project Structure
Refer to the full file tree at the top of this repo for detailed layout.

---

## 🔄 CI/CD Workflow
- Automated tests for all services (Booking, Notification, Payment)
- Run in GitHub Actions via `.github/workflows/ci-cd.yml`
- Builds Docker images and runs all tests on every push to `main`

---

## 👤 Author
- GitHub: [Pradyut](https://github.com/Pradyut6)
- LinkedIn: [Pradyut Kumar Ghosh](https://www.linkedin.com/in/pradyut5/)

---

## 📃 License
    License

 
