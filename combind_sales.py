import csv
import xlsxwriter

# dictionary to store sales data for each month
monthly_sales = {}

# Initialize variables for minimum and maximum sales
minSale = None
maxSale = None

# Open the CSV file for reading
with open('sales.csv', 'r') as file:
    # Create a CSV reader object
    spreadsheet = csv.DictReader(file)

    # Iterate through each row in the CSV file
    for row in spreadsheet:
        month = row['month']
        sales = float(row['sales'])  # 'Sales' column contains numeric values

        # Check if the month is already in the dictionary
        if month in monthly_sales:
            # If yes, add the sales to the existing value
            monthly_sales[month] += sales
        else:
            # If no, create a new entry for the month
            monthly_sales[month] = sales

        # Update minimum and maximum sales
        if minSale is None or sales < minSale:
            minSale = sales
        if maxSale is None or sales > maxSale:
            maxSale = sales

# Calculate the total sales across all months
total_sales = sum(monthly_sales.values())

# Calculate the average sales per month
average_sales = round((total_sales / len(monthly_sales)), 2)

# Calculate monthly changes as a percentage
monthly_changes = {}
previous_month_sales = None

for month, sales in monthly_sales.items():
    if previous_month_sales is not None:
        monthly_change_percentage = round((((sales - previous_month_sales) / previous_month_sales) * 100), 0)
        monthly_changes[month] = monthly_change_percentage
    previous_month_sales = sales


# Find months with the highest and lowest sales
highest_sales_month = max(monthly_sales, key=monthly_sales.get)
lowest_sales_month = min(monthly_sales, key=monthly_sales.get)

# Create a CSV file and write the summary data to it
with open('sales_summary1.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(
        ["Month", "Total Sales", "Monthly Change (%)", "Average Sales", "Highest Sales Month", "Lowest Sales Month",
         "Minimum Sales", "Maximum Sales"])

    # Write data rows
    for month, sales in monthly_sales.items():
        monthly_change = monthly_changes.get(month, "")
        highest_month = highest_sales_month if month == highest_sales_month else ""
        lowest_month = lowest_sales_month if month == lowest_sales_month else ""
        min_sales = minSale if month == lowest_sales_month else ""
        max_sales = maxSale if month == highest_sales_month else ""
        csv_writer.writerow(
            [month, sales, monthly_change, average_sales, highest_month, lowest_month, min_sales, max_sales])