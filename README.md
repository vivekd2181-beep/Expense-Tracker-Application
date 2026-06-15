# Expense Tracker Application

A web-based Expense Tracker Application developed using Java, Spring Boot, Hibernate, and MySQL. The application helps users manage their daily expenses by recording, updating, and tracking transactions efficiently. It provides an organized way to monitor spending habits and maintain financial records.

---

## 🚀 Features

- Add New Expenses
- View Expense History
- Update Expense Details
- Delete Expenses
- Categorize Expenses
- Track Spending Records
- Responsive User Interface
- Database Integration with MySQL
- CRUD Operations

---

## 🛠️ Tech Stack

### Backend
- Java
- Spring Boot
- Spring Data JPA
- Hibernate

### Database
- MySQL

### Frontend
- HTML
- CSS
- Bootstrap
- Thymeleaf

### Tools
- Maven
- Git
- GitHub

---

## 📂 Project Structure

```
Expense-Tracker
│
├── src/main/java
│   ├── controller
│   ├── service
│   ├── repository
│   ├── entity
│   └── ExpenseTrackerApplication
│
├── src/main/resources
│   ├── templates
│   ├── static
│   └── application.properties
│
└── pom.xml
```

---

## 📋 Functionalities

- Create Expense Records
- View All Expenses
- Edit Expense Information
- Delete Expenses
- Categorize Transactions
- Monitor Spending History

---

## ⚙️ Installation & Setup

### Prerequisites

- Java 17+
- MySQL
- Maven

### Clone Repository

```bash
git clone https://github.com/vivekd2181-beep/Expense-Tracker.git
```

### Configure Database

Update `application.properties`

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/expense_tracker
spring.datasource.username=root
spring.datasource.password=your_password

spring.jpa.hibernate.ddl-auto=update
```

### Run Application

```bash
mvn spring-boot:run
```

Open:

```bash
http://localhost:8080
```

---

## 📊 Database Fields

| Field | Type |
|---------|---------|
| id | Long |
| title | String |
| amount | Double |
| category | String |
| date | Date |
| description | String |

---

## 🎯 Learning Outcomes

- Built a complete CRUD application using Spring Boot.
- Integrated Hibernate ORM with MySQL.
- Applied MVC architecture.
- Improved backend development skills.
- Gained hands-on experience with database operations.

---

## 🔮 Future Enhancements

- User Authentication & Authorization
- Monthly Expense Reports
- Expense Charts & Analytics
- Budget Management
- Export Reports to PDF/Excel

---

## 👨‍💻 Author

**Vivek D**

GitHub: https://github.com/vivekd2181-beep

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub.
