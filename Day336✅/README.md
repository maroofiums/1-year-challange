# Day 336 - Streamlit Basics Demo App

A beginner-friendly interactive web application built using **Streamlit**.
This project demonstrates core Streamlit components including text rendering, user input handling, layout management, sidebar navigation, file uploads, and basic charts.

---

## Overview

This app showcases:

* Text elements (title, header, markdown, etc.)
* User input fields (text input, number input, button)
* Column-based layout
* Sidebar navigation
* File uploader
* Basic charts (line and bar)

The goal of this project is to understand the fundamental building blocks of Streamlit before moving to ML model deployment.

---

## Tech Stack

* Python 3.x
* Streamlit

---

## Features

### 1. Text Display Components

* `st.title()`
* `st.header()`
* `st.subheader()`
* `st.text()`
* `st.write()`
* `st.markdown()`

### 2. User Input Handling

* Name input using `st.text_input()`
* Age input using `st.number_input()`
* Submit button with dynamic response

### 3. Layout System

* Two-column layout using `st.columns()`
* Sidebar menu using `st.sidebar.selectbox()`

### 4. File Upload

* Upload any file
* Displays:

  * File name
  * File type
  * File size

### 5. Data Visualization

* Line chart
* Bar chart

---

## Project Structure

```
streamlit-basics-app/
│
├── app.py
├── README.md
└── requirements.txt
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/streamlit-basics-app.git
cd streamlit-basics-app
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install streamlit
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

## Learning Outcomes

By building this app, you understand:

* How Streamlit converts Python scripts into interactive web apps
* Handling user input dynamically
* Structuring layouts professionally
* Basic frontend-like interaction without HTML/CSS
* Preparing foundation for ML model deployment

---


