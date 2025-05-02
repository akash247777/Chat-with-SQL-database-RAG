import datetime
from decimal import Decimal

few_shots = [
    {
        'Question': "How many Medicine do we have left for Paracetamol",
        'SQLQuery': "SELECT SUM([Stock_Quantity]) AS Total_Paracetamol_Stock FROM [Medicines] WHERE [Medicine_Name] = 'Paracetamol 500mg'",
        'SQLResult': "Result of the SQL query",  # qns1 is already a string
        'Answer': [(150,), (170,), (160,), (140,), (130,)]
    },
    {   'Question': "List all medicines with stock less than 100 units",
        'SQLQuery': "SELECT [Medicine_Name], [Stock_Quantity] FROM [Medicines] WHERE [Stock_Quantity] < 100",
        'SQLResult': "Result of the SQL query",
        'Answer': [('Erythromycin 250mg', 90), ('Erythromycin 500mg', 90), ('Erythromycin 250mg', 95)]
    },
    {   'Question': " Find medicines priced above ₹3",
        'SQLQuery': "SELECT [Medicine_Name], [Price] FROM [Medicines] WHERE [Price] > 3",
        'SQLResult': "Result of the SQL query",
        'Answer': [('Metformin 500mg', Decimal('3.20')), ('Atorvastatin 10mg', Decimal('4.50')), ('Azithromycin 500mg', Decimal('5.75')), ('Metformin 500mg', Decimal('3.25')), ('Montelukast 10mg', Decimal('3.10'))]
    },
    {   'Question': "Show medicines that are expired",
        'SQLQuery': "SELECT [Medicine_Name], [Expiry_Date] FROM [Medicines] WHERE [Expiry_Date] < GETDATE()",
        'SQLResult': "Result of the SQL query",
        'Answer':[('Ibuprofen 400mg', datetime.date(2025, 4, 14)), ('Levocetirizine 5mg', datetime.date(2025, 2, 28)), ('Amlodipine 5mg', datetime.date(2025, 2, 9)), ('Losartan 50mg', datetime.date(2025, 1, 4)), ('Montelukast 10mg', datetime.date(2024, 11, 30))]
    },
    {   'Question': "List medicine names with their discount percentage",
        'SQLQuery': "SELECT [Medicine_Name], [Discount_Percentage] FROM [Medicines]",
        'SQLResult': "Result of the SQL query",
        'Answer': [('Paracetamol 500mg', Decimal('5.00')), ('Amoxicillin 250mg', Decimal('10.00')), ('Ibuprofen 400mg', Decimal('7.50')), ('Cetirizine 10mg', Decimal('3.00')), ('Metformin 500mg', Decimal('4.00')), ('Atorvastatin 10mg', Decimal('6.00')), ('Azithromycin 500mg', Decimal('8.00')), ('Pantoprazole 40mg', Decimal('2.50')), ('Levocetirizine 5mg', Decimal('3.50')), ('Diclofenac 50mg', Decimal('5.00')), ('Paracetamol 500mg', Decimal('5.00')), ('Paracetamol 500mg', Decimal('5.50')), ('Ibuprofen 400mg', Decimal('7.00')), ('Cetirizine 10mg', Decimal('3.20')), ('Metformin 500mg', Decimal('4.10')), ('Amlodipine 5mg', Decimal('2.80')), ('Losartan 50mg', Decimal('2.90')), ('Montelukast 10mg', Decimal('3.00')), ('Dolo 650mg', Decimal('4.20')), ('Erythromycin 250mg', Decimal('6.30')), ('Paracetamol 500mg', Decimal('4.50')), ('Azithromycin 500mg', Decimal('3.00')), ('Ibuprofen 400mg', Decimal('1.50')), ('Cetirizine 10mg', Decimal('2.00')), ('Dolo 650mg', Decimal('3.50')), ('Levocetirizine 5mg', Decimal('4.00')), ('Pantoprazole 40mg', Decimal('5.00')), ('Amoxicillin 250mg', Decimal('1.00')), ('Metformin 500mg', Decimal('2.50')), ('Amlodipine 5mg', Decimal('3.00')), ('Losartan 50mg', Decimal('2.50')), ('Montelukast 10mg', Decimal('4.00')), ('Dolo 650mg', Decimal('3.00')), ('Erythromycin 250mg', Decimal('2.00')), ('Paracetamol 500mg', Decimal('4.50')), ('Amoxicillin 500mg', Decimal('3.50')), ('Metformin 1000mg', Decimal('4.00')), ('Ibuprofen 200mg', Decimal('2.00')), ('Cetirizine 5mg', Decimal('3.00')), ('Pantoprazole 20mg', Decimal('5.00')), ('Dolo 650mg', Decimal('3.50')), ('Azithromycin 250mg', Decimal('2.00')), ('Atorvastatin 20mg', Decimal('1.50')), ('Amlodipine 10mg', Decimal('4.00')), ('Losartan 100mg', Decimal('2.50')), ('Montelukast 5mg', Decimal('3.50')), ('Erythromycin 500mg', Decimal('4.50')), ('Ibuprofen 600mg', Decimal('2.00')), ('Paracetamol 650mg', Decimal('3.00')), ('Levocetirizine 2.5mg', Decimal('1.50')), ('Metformin 500mg', Decimal('2.50')), ('Pantoprazole 40mg', Decimal('4.00')), ('Cetirizine 10mg', Decimal('3.00')), ('Amoxicillin 250mg', Decimal('2.00')), ('Dolo 650mg', Decimal('3.50')), ('Azithromycin 500mg', Decimal('2.50')), ('Paracetamol 500mg', Decimal('4.00')), ('Ibuprofen 400mg', Decimal('1.00')), ('Levocetirizine 5mg', Decimal('5.00')), ('Amlodipine 5mg', Decimal('3.00')), ('Losartan 50mg', Decimal('2.00')), ('Montelukast 10mg', Decimal('3.50')), ('Pantoprazole 20mg', Decimal('4.50')), ('Amoxicillin 500mg', Decimal('2.50')), ('Paracetamol 650mg', Decimal('3.00')), ('Ibuprofen 200mg', Decimal('4.00')), ('Dolo 650mg', Decimal('1.50')), ('Levocetirizine 2.5mg', Decimal('2.00')), ('Metformin 1000mg', Decimal('5.00')), ('Amlodipine 10mg', Decimal('3.50')), ('Montelukast 5mg', Decimal('2.00')), ('Losartan 100mg', Decimal('4.00')), ('Azithromycin 250mg', Decimal('3.50')), ('Pantoprazole 40mg', Decimal('2.50')), ('Dolo 650mg', Decimal('3.00')), ('Paracetamol 500mg', Decimal('4.50')), ('Levocetirizine 5mg', Decimal('1.00')), ('Cetirizine 10mg', Decimal('2.50')), ('Metformin 500mg', Decimal('3.50')), ('Ibuprofen 400mg', Decimal('2.00')), ('Pantoprazole 20mg', Decimal('3.00')), ('Amoxicillin 250mg', Decimal('4.00')), ('Levocetirizine 2.5mg', Decimal('2.50')), ('Dolo 650mg', Decimal('3.50')), ('Azithromycin 500mg', Decimal('1.50')), ('Paracetamol 650mg', Decimal('2.00')), ('Montelukast 10mg', Decimal('4.50')), ('Losartan 50mg', Decimal('3.00')), ('Metformin 1000mg', Decimal('2.50')), ('Cetirizine 10mg', Decimal('3.00'))]
    },
    {   'Question': "Count how many medicines are manufactured by each manufacturer",
        'SQLQuery': "SELECT [Manufacturer], COUNT(*) AS Medicine_Count FROM [Medicines] GROUP BY [Manufacturer]",
        'SQLResult': "Result of the SQL query",
        'Answer':  [('Biocon Ltd', 10), ('Cipla', 20), ("Dr. Reddy's", 10), ('Lupin', 20), ('Sun Pharma', 20), ('Torrent Pharmaceuticals Ltd', 10), ('Zydus Cadila', 10)]
    }
]
