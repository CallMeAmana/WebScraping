import requests
from bs4 import BeautifulSoup
from supabase_py import create_client

# Set up Supabase credentials
supabase_url = 'https://eqeyugzznvjbkywsccfl.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVxZXl1Z3p6bnZqYmt5d3NjY2ZsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDEyODYzMzcsImV4cCI6MjAxNjg2MjMzN30.W2VZCMAKk3UgOjPYMBrB8O7ex8vS7idTPN7xDjeT6Xk'
supabase = create_client(supabase_url, supabase_key)
table_name = 'faces'

# Perform Web Scraping
url = 'https://generated.photos/faces'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract face data from HTML
    face_data = soup.find_all('div', class_='face-data')  # Adjust this based on the HTML structure

    # Process and organize the extracted data
    for data in face_data:
        face_vector = data.find('span', class_='face-vector').text
        metadata = data.find('span', class_='metadata').text

        # Save the extracted data to Supabase
        supabase.table(table_name).insert([{'face_vector': face_vector, 'metadata': metadata}])
else:
    print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
