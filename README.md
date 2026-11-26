
# E-commerce Ticket Assistant

## Project Description
This project is an E-commerce Customer Support Ticket Assistant. It analyzes customer support tickets and assigns one of 10 predefined categories.

## Categories
1. Order Issue
2. Delivery Issue
3. Payment Issue
4. Refund Request
5. Return Request
6. Product Damage
7. Wrong Product
8. Account Issue
9. Cancellation
10. Product Inquiry

## Technologies Used
- Python
- Pandas
- Pydantic
- FastAPI
- Streamlit
- Scikit-learn

## Project Files
- main.ipynb: Dataset analysis, keyword baseline, TF-IDF evaluation and prompt experiments.
- service.py: Ticket analysis service and Pydantic output validation.
- api.py: FastAPI backend.
- app.py: Streamlit frontend.
- ecommerce_ticket_dataset_100.csv: 100 labeled support tickets.

## Installation
Install required packages:

```bash
python -m pip install pandas scikit-learn pydantic fastapi uvicorn streamlit requests
```

## Run the Project

### Step 1: Start API
```bash
python -m uvicorn api:app --reload
```

### Step 2: Start Frontend
Open a second terminal:

```bash
python -m streamlit run app.py
```

### Step 3: Open Application
Open the local Streamlit URL shown in the terminal.

## Testing
- Valid ticket test
- Blank ticket test
- Refund request test
- Account issue test
- Backend unavailable test

## Important Note
The current service uses a keyword-based mock classifier. It is not a real AI language model.
[https://github.com/hammad27992/Ecommerce-Ticket-Assistant]