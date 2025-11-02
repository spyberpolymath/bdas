# generate_sample_data.py
import os
import pandas as pd
import numpy as np
from time import sleep

# Project info: folder_name, excel_file_name
projects = [
    ("Sales_Dashboard", "sales_data.xlsx"),
    ("Customer_Segmentation", "customer_data.xlsx"),
    ("Employee_Attendance", "attendance_data.xlsx"),
    ("Marketing_Campaign", "campaign_data.xlsx"),
    ("Inventory_Analysis", "inventory_data.xlsx"),
    ("Employee_Performance", "performance_data.xlsx"),
    ("Financial_Risk", "financial_data.xlsx"),
    ("Customer_Churn", "churn_data.xlsx"),
    ("Operations_Optimization", "operations_data.xlsx"),
    ("Sales_Forecasting", "forecasting_data.xlsx"),
    ("Employee_Attrition", "attrition_data.xlsx"),
    ("Financial_Statement", "financial_statements.xlsx"),
    ("Customer_Lifetime_Value", "clv_data.xlsx"),
    ("Supply_Chain_Optimization", "supply_chain_data.xlsx"),
    ("Financial_Portfolio", "portfolio_data.xlsx"),
    ("Market_Entry", "market_entry_data.xlsx"),
    ("HR_Workforce_Planning", "workforce_data.xlsx"),
]

# ASCII banner
banner = r"""
           BDAS - Business Data Analytics Specialist
                 by Aman Anil
"""

print(banner)
sleep(1)

# Function to generate dummy data based on project type


def generate_sample_data(project_name):
    np.random.seed(42)

    if "Sales" in project_name:
        data = pd.DataFrame({
            "Date": pd.date_range("2025-01-01", periods=100),
            "Region": np.random.choice(["North", "South", "East", "West"], 100),
            "Product": np.random.choice(["A", "B", "C", "D"], 100),
            "Sales": np.random.randint(100, 1000, 100)
        })
    elif "Customer" in project_name:
        data = pd.DataFrame({
            "CustomerID": range(1, 101),
            "Age": np.random.randint(18, 70, 100),
            "Gender": np.random.choice(["Male", "Female"], 100),
            "PurchaseHistory": np.random.randint(1, 20, 100),
            "Segment": np.random.choice(["Low", "Medium", "High"], 100)
        })
    elif "Employee" in project_name:
        data = pd.DataFrame({
            "EmployeeID": range(1, 101),
            "Department": np.random.choice(["HR", "Sales", "IT", "Finance"], 100),
            "Attendance": np.random.randint(0, 31, 100),
            "PerformanceScore": np.random.randint(50, 100, 100)
        })
    elif "Marketing" in project_name:
        data = pd.DataFrame({
            "CampaignID": range(1, 21),
            "Channel": np.random.choice(["Email", "Social Media", "TV", "Radio"], 20),
            "Spend": np.random.randint(1000, 10000, 20),
            "ROI": np.round(np.random.uniform(0.5, 5.0, 20), 2)
        })
    elif "Inventory" in project_name or "Supply" in project_name:
        data = pd.DataFrame({
            "ProductID": range(1, 51),
            "StockLevel": np.random.randint(10, 500, 50),
            "ReorderLevel": np.random.randint(20, 200, 50),
            "SalesLastMonth": np.random.randint(5, 100, 50)
        })
    elif "Financial" in project_name or "Portfolio" in project_name:
        data = pd.DataFrame({
            "Date": pd.date_range("2025-01-01", periods=100),
            "Asset": np.random.choice(["StockA", "StockB", "BondC", "ETF1"], 100),
            "Price": np.round(np.random.uniform(50, 500, 100), 2),
            "RiskScore": np.round(np.random.uniform(0, 1, 100), 2)
        })
    elif "Operations" in project_name:
        data = pd.DataFrame({
            "ResourceID": range(1, 21),
            "AvailableHours": np.random.randint(0, 160, 20),
            "TaskLoad": np.random.randint(0, 200, 20),
            "Efficiency": np.round(np.random.uniform(0.5, 1.0, 20), 2)
        })
    elif "Attrition" in project_name:
        data = pd.DataFrame({
            "EmployeeID": range(1, 101),
            "Age": np.random.randint(22, 60, 100),
            "Tenure": np.random.randint(0, 20, 100),
            "Salary": np.random.randint(30000, 150000, 100),
            "LeftCompany": np.random.choice([0, 1], 100)
        })
    elif "Market" in project_name:
        data = pd.DataFrame({
            "Region": np.random.choice(["North", "South", "East", "West"], 50),
            "CompetitorCount": np.random.randint(1, 10, 50),
            "AvgPrice": np.round(np.random.uniform(50, 500, 50), 2),
            "PotentialCustomers": np.random.randint(1000, 10000, 50)
        })
    elif "HR" in project_name or "Workforce" in project_name:
        data = pd.DataFrame({
            "EmployeeID": range(1, 101),
            "Skill": np.random.choice(["Python", "Excel", "SQL", "Management"], 100),
            "ProjectAllocated": np.random.choice(["ProjectA", "ProjectB", "ProjectC"], 100),
            "HoursWorked": np.random.randint(20, 160, 100)
        })
    else:
        data = pd.DataFrame({"SampleColumn": range(1, 21)})

    return data


# Base data folder
base_folder = "data"
os.makedirs(base_folder, exist_ok=True)

# Generate data for all projects
for idx, (folder, file_name) in enumerate(projects, start=1):
    file_path = os.path.join(base_folder, f"{folder}.xlsx")
    print(f"[{idx}/{len(projects)}] Generating data for {folder}...")
    df = generate_sample_data(folder)
    df.to_excel(file_path, index=False)
    sleep(0.3)

print("\n✅ All sample data generated successfully!")
