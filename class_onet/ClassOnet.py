import requests
from bs4 import BeautifulSoup
import concurrent.futures
import pandas as pd
import os

class Onet:
    def __init__(self, url ):
        self.url = url
        self.section_ids = ['Abilities', 'Knowledge', 'Skills']
        self.info = None
        self.dfs = { 'A': pd.DataFrame(index=['Complex Problem Solving', 'Judgment and Decision Making', 'Systems Analysis', 'Systems Evaluation'], 
                      columns=['Complex Problem Solving & Systems Skills'], 
                      data=0),
                    'B': pd.DataFrame(index=['Management of Financial Resources', 'Management of Material Resources', 'Management of Personnel Resources', 'Time Management'], 
                      columns=['Resource Management Skills'], 
                      data=0),
                    'C': pd.DataFrame(index=['Coordination', 'Instructing', 'Negotiation', 'Persuasion', 'Service Orientation', 'Social Perceptiveness'], 
                      columns=['Social Skills'], 
                      data=0),
                    'D': pd.DataFrame(index=['Equipment Maintenance', 'Equipment Selection', 'Installation', 'Operation and Control', 'Operations Analysis', 
                             'Operations Monitoring', 'Programming', 'Quality Control Analysis', 'Repairing', 'Technology Design', 'Troubleshooting'], 
                      columns=['Technical Skills'], 
                      data=0)}  
        # 將您的 dfs 字典放在這裡
        self.dfs_2 = { 'E': pd.DataFrame(index=['English Language', 'Fine Arts', 'Foreign Language', 'History and Archeology', 'Philosophy and Theology', 'Education and Training'], 
                      columns=['Arts and Humanities'], 
                      data=0),
                    'F': pd.DataFrame(index=['Law and Government', 'Public Safety and Security', 'Psychology', 'Sociology and Anthropology'], 
                      columns=['Law & Social Sciences'], 
                      data=0),
                    'G': pd.DataFrame(index=['Administration and Management', 'Administrative', 'Customer and Personal Service', 'Economics and Accounting', 'Personnel and Human Resources', 'Sales and Marketing'], 
                      columns=['Business and Management'], 
                      data=0),
                    'H': pd.DataFrame(index=['Biology', 'Chemistry', 'Geography', 'Mathematics', 'Physics'], 
                      columns=['Mathematics and Science'], 
                      data=0),
                    'I': pd.DataFrame(index=['Building and Construction', 'Computers and Electronics', 'Design', 'Engineering and Technology', 'Mechanical', 'Communications and Media', 'Telecommunications', 'Food Production', 'Production and Processing', 'Transportation'], 
                      columns=['Engineering and IT'], 
                      data=0),
                    'J': pd.DataFrame(index=['Medicine and Dentistry', 'Therapy and Counseling'], 
                      columns=['Health Services'], 
                      data=0)}  
        # 將您的 dfs_2 字典放在這裡
     
        # 將您的 print_section_info  
    def print_section_info(self, session, url, section_id, df):
        response = session.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            section = soup.find('div', id=section_id)
            if section:
                section_list = section.find_all('div', class_='d-flex')
                for item in section_list:
                    item_name = item.find('b').get_text().strip()
                    if item_name in df.index:
                        df.loc[item_name, df.columns[0]] += 1
                        #print(f"Updated count for {item_name}")
            else:
                print(f"{section_id} section not found")
        else:
            print("Failed to retrieve data from the website")
  
  
    def get_info(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("Failed to retrieve data from the website")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        dt_tags = soup.find_all('dt')
        div_tags = soup.find_all('div', class_='d-flex flex-nowrap pb-1')
        info_keys = ['Title', 'SVP Range', 'Education', 'Time Pressure', 'Projected growth']
        self.info = {key: None for key in info_keys}

        for dt in dt_tags:
            for key in info_keys:
                if key in dt.text:
                    self.info[key] = dt.find_next_sibling('dd').text.strip()
                    break

        for div in div_tags:
            if 'Time Pressure' in div.text:
                self.info['Time Pressure'] = div.text.split('—')[1].strip()
                break

        for key, value in self.info.items():
            if value is None:
                print(f"{key} not found")

        return self.info
    
    def work_skill(self):
        for df in self.dfs.values():
            with requests.Session() as session:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                     executor.map(lambda section_id: self.print_section_info(session, self.url, section_id, df), self.section_ids)
            print(df)

    def work_knowledge(self):
        for df in self.dfs_2.values():
            with requests.Session() as session:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    executor.map(lambda section_id: self.print_section_info(session, self.url, section_id, df), self.section_ids)
            print(df)


    # def save(self, directory, filename):
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)

    #     for name, df in self.dfs.items():
    #         df.to_excel(os.path.join(directory, f"{filename}_{name}_skill.xlsx"))
    #         df.to_csv(os.path.join(directory, f"{filename}_{name}_skill.csv"))
    #         df.to_csv(os.path.join(directory, f"{filename}_{name}_skill.txt"), sep='\t')

    #     for name, df in self.dfs_2.items():
    #         df.to_excel(os.path.join(directory, f"{filename}_{name}_knowledge.xlsx"))
    #         df.to_csv(os.path.join(directory, f"{filename}_{name}_knowledge.csv"))
    #         df.to_csv(os.path.join(directory, f"{filename}_{name}_knowledge.txt"), sep='\t')
   
# if __name__ == '__main__':
#     url = 'https://www.onetonline.org/link/summary/15-1132.00'
#     onet = Onet(url)
#     onet.work_skill()
#     onet.work_knowledge()
#     onet.save('onet')