# City_Data_Scraping_from_Wikipedia_using_Python
## City Data Scraping from Wikipedia using Python

This repository contains Python code for scraping city data from Wikipedia. The code provided in this repository allows you to extract information about cities such as population, area, coordinates, and more from Wikipedia pages.
Furthermore, if sql tables with the same specification(column names and workbook names) are already created the code also provides options to transfer the scraped data to sql. 
## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Python code in this repository demonstrates how to scrape city data from Wikipedia using the BeautifulSoup library. By leveraging web scraping techniques, you can automate the retrieval of city information and store it in a structured format for further analysis.

## Prerequisites

To run the Python code in this repository, you need the following:

- Python 3 installed on your local machine.
- Python libraries: BeautifulSoup, requests.
- Basic understanding of HTML structure and web scraping concepts.

## Installation

1. Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/ajwazir/City_Data_Scraping_from_Wikipedia_using_Python/tree/main
```

2. Ensure that you have Python 3 installed. You can download it from the official Python website.

3. Install the required Python libraries using the following command:

```bash
pip install beautifulsoup4 requests
```

## Usage

To use the Python code in this repository, follow these steps:

1. Open a Python IDE or text editor of your choice.

2. Navigate to the directory where you cloned this repository.

3. Open the `Asim_wiki_citiesdata_scraping.ipynb` file and modify it if needed to customize the scraping process.

4. Run the script using the Python interpreter.

5. The script will scrape the city data from Wikipedia and store it in a structured format (e.g. JSON) as specified in the code.

6. Analyze and process the scraped data according to your requirements.

## Examples

Here's an example of how the Python code can be used to scrape city data:

```python
from bs4 import BeautifulSoup
import requests

# Specify the Wikipedia URL of the city you want to scrape
url = 'https://en.wikipedia.org/wiki/Berlin'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired information from the parsed HTML
# For example, retrieve the city population
population = soup.find('table', class_='infobox').find(text='Population').find_next('td').text.strip()

# Print the extracted information
print(f"Population: {population}")
```

Feel free to explore the repository for more examples and customization options for scraping city data from Wikipedia.

## Contributing

Contributions to this repository are welcome! If you have improvements or additional features to add, feel free to submit a pull request. Please ensure that your contributions follow the established coding style and best practices.

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code in this repository for commercial or non-commercial purposes. See the [LICENSE](LICENSE) file for more details.

