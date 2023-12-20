from datetime import datetime
import openpyxl
from openpyxl import Workbook
import os

class DataSaver:

    @staticmethod
    def save_to_excel(data, step_name, file_path=None):
        # Define the default file path if not provided
        if not file_path:
            file_path = 'C:\\Projekty_Python\\WellmifyTests\\Excel\\data.xlsx'

        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Define the headers
        headers = ["Timestamp", "Step Name", "Duration", "Service", "Price", "Type", "Date", "Address", "Element ID", "UUID", "Status", "Phone","ClientName", "OriginalTime"]

        # Create a new workbook if the file does not exist
        if not os.path.exists(file_path):
            wb = Workbook()
            ws = wb.active
            ws.append(headers)
        else:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active

        # Get current timestamp
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Prepare the data row dynamically including the timestamp
        data_row = [current_timestamp, step_name] + [data.get(header) for header in headers[2:]]

        # Append the data row
        ws.append(data_row)

        # Save the workbook
        wb.save(file_path)
        wb.close()
