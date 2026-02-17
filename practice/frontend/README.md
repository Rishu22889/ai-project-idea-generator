# Task 2: Frontend Practice – Calculator with History

## 📌 Overview

This project is a simple web-based calculator built using **Flask (Python)** for the backend and **HTML5 + Tailwind CSS** for the frontend.

The goal of this task was to strengthen my understanding of basic frontend-backend integration and form handling before starting the main project.

---

## 🚀 Features

* Performs four arithmetic operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Accepts two numeric inputs
* Displays the calculated result
* Shows the **last 5 calculations**
* Handles divide-by-zero errors
* Clean and responsive UI using Tailwind CSS

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML5, Tailwind CSS
* **Templating Engine:** Jinja2

---

## 🧠 What I Learned

### 1. Handling Form Submission in Flask

I learned how to:

* Use `POST` method for form data
* Access form values using `request.form`
* Perform calculations on the server
* Pass results back to the template

### 2. Server-Side Rendering

I understood how Flask uses Jinja templates to dynamically render:

* Calculation results
* Error messages
* History list

### 3. Basic State Handling

I implemented a simple in-memory list to store the last 5 calculations and display them on the UI.

### 4. Error Handling

I handled:

* Invalid numeric input
* Division by zero

This improved the reliability of the calculator.

### 5. Tailwind CSS Practice

I practiced:

* Utility-based styling
* Card layouts
* Button hover effects
* Responsive alignment

---

## 📂 Project Structure

```
practice/
└── frontend/
    ├── app.py
    └── templates/
        └── index.html
```

---

## 💡 Reflection

Although this is a simple calculator, it helped me understand the full flow of a web application:

Form → Backend Processing → Template Rendering → UI Update

This strengthened my fundamentals in Flask and frontend styling before moving on to more advanced projects.

---

## 📸 Demo

Screenshot/demo shared in Discord #showcase channel.

---

## ✅ Status

Task completed as per acceptance criteria.
