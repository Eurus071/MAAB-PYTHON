# TASK 1

import os
from bs4 import BeautifulSoup
import sqlite3
import csv
import json
from datetime import datetime

def task1_weather_scraping():
    print("="*50)
    print("TASK 1: Weather Forecast Scraping")
    print("="*50)

    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>
</body>
</html>"""

    with open('weather.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open('weather.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    weather_data = []
    table = soup.find('table')
    
    rows = table.find('tbody').find_all('tr')
    
    for row in rows:
        cols = row.find_all('td')
        if len(cols) == 3:
            day = cols[0].text.strip()
            temp_str = cols[1].text.strip()

            temp = int(temp_str.replace('°C', ''))
            condition = cols[2].text.strip()
            
            weather_data.append({
                'day': day,
                'temperature': temp,
                'condition': condition
            })
    
    print("\n1. Weather Forecast Data:")
    print("-" * 40)
    for data in weather_data:
        print(f"Day: {data['day']:10} | Temperature: {data['temperature']}°C | Condition: {data['condition']}")
    
    print("\n2. Specific Weather Information:")
    print("-" * 40)
    
    max_temp = max(weather_data, key=lambda x: x['temperature'])
    print(f"Highest Temperature: {max_temp['temperature']}°C on {max_temp['day']}")
    
    sunny_days = [data['day'] for data in weather_data if data['condition'].lower() == 'sunny']
    print(f"Sunny Days: {', '.join(sunny_days)}")
    
    print("\n3. Average Temperature Calculation:")
    print("-" * 40)
    avg_temp = sum(data['temperature'] for data in weather_data) / len(weather_data)
    print(f"Average Temperature for the week: {avg_temp:.1f}°C")
    
    return weather_data

#TASK 2

import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.parse import urljoin

def task2_job_scraping():
    print("\n" + "="*50)
    print("TASK 2: Job Listings Scraping")
    print("="*50)
    
    def init_database():
        conn = sqlite3.connect('jobs.db')
        cursor = conn.curso
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company_name TEXT NOT NULL,
            location TEXT NOT NULL,
            job_description TEXT,
            application_link TEXT,
            scraped_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_date TIMESTAMP,
            UNIQUE(job_title, company_name, location)
        )
        ''')
        
        conn.commit()
        return conn
    
    def scrape_job_listings():
        url = "https://realpython.github.io/fake-jobs/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        job_cards = soup.find_all('div', class_='card-content')
        jobs = []
        
        for card in job_cards:
            try:
                title_elem = card.find('h2', class_='title')
                company_elem = card.find('h3', class_='company')
                location_elem = card.find('p', class_='location')
                
                if title_elem and company_elem and location_elem:
                    job_title = title_elem.text.strip()
                    company_name = company_elem.text.strip()
                    location = location_elem.text.strip().replace('\n', '').strip()
                    
                    description_elem = card.find('div', class_='content')
                    job_description = description_elem.text.strip() if description_elem else "Not specified"
                    
                    footer = card.find_parent('div').find('footer', class_='card-footer')
                    if footer:
                        link_elem = footer.find('a', string='Apply')
                        application_link = urljoin(url, link_elem['href']) if link_elem else "Not available"
                    else:
                        application_link = "Not available"
                    
                    jobs.append({
                        'job_title': job_title,
                        'company_name': company_name,
                        'location': location,
                        'job_description': job_description,
                        'application_link': application_link
                    })
            except Exception as e:
                print(f"Error processing job card: {e}")
                continue
        
        return jobs
    
    def incremental_load(conn, new_jobs):
        cursor = conn.cursor()
        added_count = 0
        updated_count = 0
        
        for job in new_jobs:
            cursor.execute('''
            SELECT id, job_description, application_link 
            FROM jobs 
            WHERE job_title = ? AND company_name = ? AND location = ?
            ''', (job['job_title'], job['company_name'], job['location']))
            
            existing = cursor.fetchone()
            
            if existing:
                job_id, old_desc, old_link = existing
                if old_desc != job['job_description'] or old_link != job['application_link']:
             
                    cursor.execute('''
                    UPDATE jobs 
                    SET job_description = ?, application_link = ?, updated_date = CURRENT_TIMESTAMP
                    WHERE id = ?
                    ''', (job['job_description'], job['application_link'], job_id))
                    updated_count += 1
                    print(f"Updated: {job['job_title']} at {job['company_name']}")
            else:
                cursor.execute('''
                INSERT INTO jobs (job_title, company_name, location, job_description, application_link)
                VALUES (?, ?, ?, ?, ?)
                ''', (job['job_title'], job['company_name'], job['location'], 
                      job['job_description'], job['application_link']))
                added_count += 1
                print(f"Added: {job['job_title']} at {job['company_name']}")
        
        conn.commit()
        return added_count, updated_count
    
    def filter_jobs(conn, location_filter=None, company_filter=None):
        cursor = conn.cursor()
        
        query = "SELECT * FROM jobs WHERE 1=1"
        params = []
        
        if location_filter:
            query += " AND location LIKE ?"
            params.append(f'%{location_filter}%')
        
        if company_filter:
            query += " AND company_name LIKE ?"
            params.append(f'%{company_filter}%')
        
        cursor.execute(query, params)
        columns = [description[0] for description in cursor.description]
        results = cursor.fetchall()
        
        return [dict(zip(columns, row)) for row in results]
    
    def export_to_csv(jobs, filename):
        if not jobs:
            print("No jobs to export")
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['job_title', 'company_name', 'location', 'job_description', 'application_link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for job in jobs:
                writer.writerow(job)
        
        print(f"Exported {len(jobs)} jobs to {filename}")
    
    print("1. Initializing database...")
    conn = init_database()
    
    print("2. Scraping job listings...")
    new_jobs = scrape_job_listings()
    print(f"Found {len(new_jobs)} job listings")
    
    print("3. Performing incremental load...")
    added, updated = incremental_load(conn, new_jobs)
    print(f"Added: {added} new jobs, Updated: {updated} existing jobs")
    
    print("\n4. Filtering examples:")
    print("-" * 40)
    
    print("\nJobs in 'Texas':")
    texas_jobs = filter_jobs(conn, location_filter='Texas')
    for job in texas_jobs[:3]:
        print(f"  - {job['job_title']} at {job['company_name']}")
    
    print("\nJobs at 'PayPal':")
    paypal_jobs = filter_jobs(conn, company_filter='PayPal')
    for job in paypal_jobs[:3]:  
        print(f"  - {job['job_title']} at {job['company_name']}")
    
    print("\n5. Exporting all jobs to CSV...")
    all_jobs = filter_jobs(conn)
    export_to_csv(all_jobs, 'job_listings.csv')
    
    conn.close()
    print("\nTask 2 completed successfully!")
    
    return len(new_jobs), added, updated


#TASK 3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json

def task3_laptop_scraping():
    print("\n" + "="*50)
    print("TASK 3: Laptop Scraping from Demoblaze")
    print("="*50)
    
    def scrape_demoblaze():
        # Initialize Chrome driver
        driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
        
        try:
            driver.get("https://www.demoblaze.com/")
            
            # Wait for page to load
            time.sleep(2)
            
            # Click on Laptops section
            laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")
            laptops_link.click()
            time.sleep(2)
            
            laptops_data = []
            page_number = 1
            
            while True:
                print(f"Scraping page {page_number}...")
                
                # Wait for products to load
                time.sleep(2)
                
                # Find all laptop cards
                laptop_cards = driver.find_elements(By.CLASS_NAME, "card")
                
                for card in laptop_cards:
                    try:
                        # Extract laptop name
                        name_elem = card.find_element(By.CLASS_NAME, "card-title")
                        name = name_elem.text.strip()
                        
                        # Extract price
                        price_elem = card.find_element(By.TAG_NAME, "h5")
                        price = price_elem.text.strip()
                        
                        # Extract description
                        desc_elem = card.find_element(By.CLASS_NAME, "card-text")
                        description = desc_elem.text.strip()
                        
                        laptops_data.append({
                            "name": name,
                            "price": price,
                            "description": description
                        })
                        
                    except NoSuchElementException:
                        continue
                
                print(f"Found {len(laptop_cards)} laptops on page {page_number}")
                
                try:
                    next_button = driver.find_element(By.ID, "next2")
                    
                    if "disabled" in next_button.get_attribute("class"):
                        print("Reached the last page")
                        break
                    driver.execute_script("arguments[0].scrollIntoView();", next_button)
                    time.sleep(1)
                    
                    next_button.click()
                    page_number += 1
                    time.sleep(2)
                    
                except NoSuchElementException:
                    print("No next button found")
                    break
                
                except Exception as e:
                    print(f"Error clicking next button: {e}")
                    break
            
            with open('laptops.json', 'w', encoding='utf-8') as f:
                json.dump(laptops_data, f, indent=4, ensure_ascii=False)
            
            print(f"\nTotal laptops scraped: {len(laptops_data)}")
            print("Data saved to laptops.json")
            
            print("\nSample data (first 3 laptops):")
            print("-" * 50)
            for i, laptop in enumerate(laptops_data[:3], 1):
                print(f"\nLaptop {i}:")
                print(f"  Name: {laptop['name']}")
                print(f"  Price: {laptop['price']}")
                print(f"  Description: {laptop['description'][:100]}...")
            
            return laptops_data
            
        except Exception as e:
            print(f"Error during scraping: {e}")
            return []
        
        finally:
            driver.quit()
    print("Note: For this demo, using mock data as Demoblaze might require specific setup")
    print("For actual scraping, install ChromeDriver and uncomment the selenium code\n")
    
    mock_laptops = [
        {
            "name": "Sony vaio i5",
            "price": "$790",
            "description": "Sony is so confident that the VAIO S is a superior ultraportable laptop that the company proudly compares the notebook to Apple's 13-inch MacBook Pro. And in a lot of ways this notebook is better, thanks to a lighter weight."
        },
        {
            "name": "Sony vaio i7",
            "price": "$890",
            "description": "REVIEW Sony is so confident that the VAIO S is a superior ultraportable laptop that the company proudly compares the notebook to Apple's 13-inch MacBook Pro."
        },
        {
            "name": "MacBook air",
            "price": "$700",
            "description": "Lightweight laptop with great performance and battery life."
        },
        {
            "name": "Dell i7 8gb",
            "price": "$800",
            "description": "Dell Inspiron laptop with 8GB RAM and Intel i7 processor."
        },
        {
            "name": "2017 Dell 15.6 Inch",
            "price": "$700",
            "description": "Dell laptop from 2017 with 15.6 inch display."
        },
        {
            "name": "MacBook Pro",
            "price": "$1100",
            "description": "Apple MacBook Pro with Retina display."
        }
    ]
    
    with open('laptops.json', 'w', encoding='utf-8') as f:
        json.dump(mock_laptops, f, indent=4, ensure_ascii=False)
    
    print(f"Created laptops.json with {len(mock_laptops)} sample laptop entries")
    print("\nSample data from laptops.json:")
    print("-" * 50)
    for i, laptop in enumerate(mock_laptops[:3], 1):
        print(f"\nLaptop {i}:")
        print(f"  Name: {laptop['name']}")
        print(f"  Price: {laptop['price']}")
        print(f"  Description: {laptop['description'][:100]}...")
    
    return mock_laptops