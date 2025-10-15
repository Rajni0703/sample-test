import csv
import xml.etree.ElementTree as ET
from datetime import datetime

try:
    tree = ET.parse('test-reports/test-results.xml')
    root = tree.getroot()

    with open('test-reports/test-results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Test Name', 'Status', 'Duration (seconds)', 'Timestamp', 'Error Message'])
        
        for testcase in root.findall('.//testcase'):
            test_name = testcase.get('name', '')
            class_name = testcase.get('classname', '')
            full_name = f'{class_name}.{test_name}' if class_name else test_name
            duration = testcase.get('time', '0')

            if testcase.find('failure') is not None:
                status = 'FAILED'
                error_msg = testcase.find('failure').get('message', 'Assertion Error')
            elif testcase.find('error') is not None:
                status = 'ERROR'
                error_msg = testcase.find('error').get('message', 'Runtime Error')
            else:
                status = 'PASSED'
                error_msg = ''

            writer.writerow([full_name, status, duration, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), error_msg])

    print('CSV report generated: test-reports/test-results.csv')
except Exception as e:
    print(f'Error generating CSV report: {e}')
    exit(1)