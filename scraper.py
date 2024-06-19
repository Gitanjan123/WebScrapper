import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.1mg.com"
ALL_DISEASES_URL = f"{BASE_URL}/all-diseases"

def get_disease_links():
    response = requests.get(ALL_DISEASES_URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    disease_links = []

    # Finding all disease links
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/diseases'):
            disease_name = link.text.strip()
            disease_url = BASE_URL + href
            disease_links.append({"name": disease_name, "url": disease_url})
    
    return disease_links

def scrape_disease_details(disease_url):
    response = requests.get(disease_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    disease_details = {
        "overview": "",
        "key_facts": "",
        "symptoms": "",
        "causes": "",
        "types": "",
        "risk_factors": "",
        "diagnosis": "",
        "prevention": "",
        "specialist_to_visit": "",
        "treatment": "",
        "home_care": "",
        "alternative_therapies": "",
        "living_with": "",
        "faqs": [],
        "references": []
    }

    sections = soup.find_all('section')
    for section in sections:
        header = section.find('h2')
        if header:
            section_title = header.text.strip().lower()
            section_content = section.get_text(separator=' ', strip=True)
            
            if 'overview' in section_title:
                disease_details["overview"] = section_content
            elif 'key facts' in section_title:
                disease_details["key_facts"] = section_content
            elif 'symptoms' in section_title:
                disease_details["symptoms"] = section_content
            elif 'causes' in section_title:
                disease_details["causes"] = section_content
            elif 'types' in section_title:
                disease_details["types"] = section_content
            elif 'risk factors' in section_title:
                disease_details["risk_factors"] = section_content
            elif 'diagnosis' in section_title:
                disease_details["diagnosis"] = section_content
            elif 'prevention' in section_title:
                disease_details["prevention"] = section_content
            elif 'specialist to visit' in section_title:
                disease_details["specialist_to_visit"] = section_content
            elif 'treatment' in section_title:
                disease_details["treatment"] = section_content
            elif 'home care' in section_title:
                disease_details["home_care"] = section_content
            elif 'alternative therapies' in section_title:
                disease_details["alternative_therapies"] = section_content
            elif 'living with' in section_title:
                disease_details["living_with"] = section_content
            elif 'faq' in section_title:
                faq_section = section.find_all('div', class_='faq-item')
                faqs = []
                for faq in faq_section:
                    question = faq.find('h3').text.strip()
                    answer = faq.find('p').text.strip()
                    faqs.append({"question": question, "answer": answer})
                disease_details["faqs"] = faqs

    for a_tag in soup.find_all('a', href=True):
        disease_details["references"].append(a_tag['href'])

    return disease_details
