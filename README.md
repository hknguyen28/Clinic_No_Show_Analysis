# Clinic No-Show Predictive Analysis

## Objective
Medical clinics face significant revenue loss and operational inefficiency due to missed appointments. This project analyzes a dataset of clinic appointments to identify variables contributing to patient no-shows.

## Technical Skills Demonstrated
* **SQL:** Data extraction, aggregation, conditional logic (`CASE WHEN`), and filtering (`WHERE`, `GROUP BY`).
* **Systems Analysis:** Translating raw healthcare scheduling data into operational business metrics.

## The Queries
The attached `queries.sql` file contains the logic used to isolate three key metrics:
1. **The Baseline:** Overall no-show percentage to establish the scope of the problem.
2. **Lead Time Impact:** Calculating the average days booked in advance for missed vs. attended appointments.
3. **Time of Day:** Filtering and categorizing missed appointments into Morning vs. Afternoon buckets to identify scheduling bottlenecks.

**appointments.csv**: The foundational operational dataset containing demographics, scheduling windows, and attendance records.
**app.py**: The Python application script that loads the dataset, processes live metrics, and renders the interactive user interface dashboard.

## Live Application Preview
The application utilizes Python and Streamlit to transform our raw backend query logic into dynamic, readable visual components for non-technical healthcare stakeholders:
* **KPI Metrics Cards:** Displays high-level executive summaries including Total Appointments, Missed Appointments, and real-time No-Show Percentages.
* **Interactive Data Grid:** Renders standard clinic data into a filterable dataframe for front-desk staff reference.
