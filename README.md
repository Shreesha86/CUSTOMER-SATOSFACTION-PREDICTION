# Customer Satisfaction Prediction (Python + Power BI)

## 📌 Project Overview

This project aims to analyze customer support ticket data to uncover key factors influencing customer satisfaction. It also includes a fully interactive Power BI dashboard to visualize trends and support performance insights. The solution showcases an end-to-end data analysis pipeline — from data cleaning and feature engineering to interactive visual reporting.

---

## 🎯 Objectives

- Analyze customer support data to identify patterns affecting satisfaction.
- Clean and preprocess raw data using Python and pandas.
- Create meaningful features like response delay and resolution time.
- Design an interactive Power BI dashboard with KPIs, charts, and filters.
- Deliver actionable insights to improve customer support performance.

---

## 📁 Dataset Overview

- **Total Records:** 8,469 support tickets  
- **Target Column:** Customer Satisfaction Rating (scale: 1 to 5)  
- **Total Features (before cleaning):** 17  
- **Type:** Binary Classification (Satisfied vs Unsatisfied)

**Key Columns:**
- Customer Age, Gender, Product Purchased  
- Ticket Type, Priority, Status, Channel  
- First Response Time, Time to Resolution  
- Customer Satisfaction Rating (target)

---

## 🧹 Data Cleaning & Feature Engineering (Python)

- Removed rows with missing target values.
- Converted timestamps to datetime format.
- Filled missing resolution times using median logic.
- Engineered:
  - `Response Delay Minutes`
  - `Resolution Time Hours`
  - `Purchase Day of Week`
- Removed rows with negative resolution durations.
- Exported cleaned data to CSV for Power BI.

---

## 📊 Power BI Dashboard

### Pages:
1. **Customer Overview**
   - Total tickets, average satisfaction, response delay
   - Ticket distribution by gender, age, product, priority

2. **Support Performance**
   - Avg satisfaction by support channel
   - Matrix: Satisfaction by priority and weekday
   - Trend analysis of satisfaction over time

3. **Interactive Filters & Drilldown**
   - Slicers for gender, product, priority, channel
   - Visuals dynamically update to reveal hidden patterns
   - Ticket-level detail table for deep dives

---

## 📐 DAX Measures Used

```DAX
Total Tickets = COUNTROWS('custSup_cleaned')
Avg Satisfaction = AVERAGE('custSup_cleaned'[Customer Satisfaction Rating])
Avg Resolution Time = AVERAGE('custSup_cleaned'[Resolution Time Hours])
Avg Response Delay = AVERAGE('custSup_cleaned'[Response Delay Minutes])

🙌 Author
Shreesha P
Data Analyst Intern
🔗 LinkedIn
