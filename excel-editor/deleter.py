import openpyxl

wb = openpyxl.load_workbook('contactlist.xlsx')

sheet = wb['contacts'] 

column = 'A'
count = 1
# Specify the range of cell numbers you want to iterate through (for example, from row 1 to row 10)
start_row = 2
end_row = 1000
# Iterate through each cell in the specified range of rows in the specified column
for row_number in range(start_row, end_row + 1):
    cell_name = f"{column}{row_number}"  # Construct the cell name (e.g., 'A1', 'A2', ...)
    cell_value = sheet[cell_name].value  # Get the value of the cell
    #print(cell_value)


    if cell_value is None or cell_value == '':
        sheet.delete_rows(row_number)  
        print("deleted") 
        count += 1
    else:
        print("conitnued")
        continue
            
    

print(count)
wb.save('contactlist.xlsx')