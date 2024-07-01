import requests
import threading

def fetch_universities(country, results):
    url = f"http://universities.hipolabs.com/search?country={country}"
    response = requests.get(url)
    if response.status_code == 200:
        universities = [uni['name'] for uni in response.json()]
        results[country] = universities
    else:
        results[country] = []

def main():
    countries = [
        'United States', 'Canada', 'United Kingdom', 'Australia', 'Germany',
        'France', 'Italy', 'Spain', 'Netherlands', 'Sweden',
        'Switzerland', 'Japan', 'China', 'South Korea', 'India'
    ]

    threads = []
    results = {}
    
    for country in countries:
        thread = threading.Thread(target=fetch_universities, args=(country, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for country, universities in results.items():
        print(f"{country}: {universities}")

if __name__ == "__main__":
    main()