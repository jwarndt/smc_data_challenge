from bs4 import BeautifulSoup

class energy_doc_parser():
    
    def __init__(self, html_filename):
        
        doc = open(html_filename)
        html_doc = doc.read()
        
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.tables = self.soup.body.find_all('table')
        
        self.total_source_energy = None
        self.total_source_energy_per_building_area = None
        self.total_source_energy_per_conditioned_building_area = None
        
        self.building_area = None
        self.conditioned_building_area = None
        self.unconditioned_building_area = None
        
        self.total_wall_area = None
        self.total_wall_area_N = None
        self.total_wall_area_E = None
        self.total_wall_area_S = None
        self.total_wall_area_W = None
        
        self.total_window_area = None
        self.total_window_area_N = None
        self.total_window_area_E = None
        self.total_window_area_S = None
        self.total_window_area_W = None
        
        self.total_above_ground_win_wall_ratio = None
        self.total_above_ground_win_wall_ratio_N = None
        self.total_above_ground_win_wall_ratio_E = None
        self.total_above_ground_win_wall_ratio_S = None
        self.total_above_ground_win_wall_ratio_W = None
        
        self.roof_area = None
        self.skylight_area = None
        self.roof_skylight_ratio = None
        
        self.people.density = None
        self.building_volume = None

    def set_annual_absolute_energy(self):
        ann_abs = self.soup.table.contents[7]
        self.total_source_energy = float(ann_abs.contents[3].get_text())
        self.total_source_energy_per_building_area = float(ann_abs.contents[5].get_text())
        self.total_source_energy_per_conditioned_building_area = float(ann_abs.contents[7].get_text())
    
    def print_annual_absolute_energy(self):
        print("total source energy: " + str(self.total_source_energy))
        print("total source energy per building area: " + str(self.total_source_energy_per_building_area))
        print("total source energy per conditioned building area: " + str(self.total_source_energy_per_conditioned_building_area))
      
    def set_building_area(self):
        build_area = self.tables[2]
        self.building_area = float(build_area.contents[3].contents[3].get_text())
        self.conditioned_building_area = float(build_area.contents[5].contents[3].get_text())
        self.unconditioned_building_area = float(build_area.contents[7].contents[3].get_text())
        
    def print_building_area(self):
        print(self.building_area)
        print(self.conditioned_building_area)
        print(self.unconditioned_building_area)

    def set_window_wall_roof_skylight_info(self):
        win_wall = self.tables[13] # window-wall area (non-conditioned)
        self.total_wall_area = float(win_wall.contents[3].contents[3].get_text())
        self.total_wall_area_N = float(win_wall.contents[3].contents[5].get_text())
        self.total_wall_area_E = float(win_wall.contents[3].contents[7].get_text())
        self.total_wall_area_S = float(win_wall.contents[3].contents[9].get_text())
        self.total_wall_area_W = float(win_wall.contents[3].contents[11].get_text())
        
        self.total_window_area = float(win_wall.contents[7].contents[3].get_text())
        self.total_window_area_N = float(win_wall.contents[7].contents[5].get_text())
        self.total_window_area_E = float(win_wall.contents[7].contents[7].get_text())
        self.total_window_area_S = float(win_wall.contents[7].contents[9].get_text())
        self.total_window_area_W = float(win_wall.contents[7].contents[11].get_text())
        
        self.total_ground_win_wall_ratio = float(win_wall.contents[9].contents[3].get_text())
        self.total_ground_win_wall_ratio_N = float(win_wall.contents[9].contents[5].get_text())
        self.total_ground_win_wall_ratio_E = float(win_wall.contents[9].contents[7].get_text())
        self.total_ground_win_wall_ratio_S = float(win_wall.contents[9].contents[9].get_text())
        self.total_ground_win_wall_ratio_W = float(win_wall.contents[9].contents[11].get_text())
        
        self.roof_area = float(self.tables[15].contents[3].contents[3].get_text())
        self.skylight_area = float(self.tables[15].contents[5].contents[3].get_text())
        self.roof_skylight_ratio = float(self.tables[15].contents[7].contents[3].get_text())
        
    def set_people_density(self):
        self.people_density = float(self.tables[16].contents[-8].contents[-4].get_text())
        self.building_volume = float(self.tables[16].contents[-8].contents[9].get_text())