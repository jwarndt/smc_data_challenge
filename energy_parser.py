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

    def set_all(self):
        self.set_annual_absolute_energy()
        self.set_building_area()
        self.set_window_wall_roof_skylight_info()
        self.set_people_density()
        
    def get_all(self):
        return [self.total_source_energy,
        self.total_source_energy_per_building_area,
        self.total_source_energy_per_conditioned_building_area,
        self.building_area,
        self.conditioned_building_area,
        self.unconditioned_building_area,
        self.total_wall_area,
        self.total_wall_area_N,
        self.total_wall_area_E,
        self.total_wall_area_S,
        self.total_wall_area_W,
        self.total_window_area,
        self.total_window_area_N,
        self.total_window_area_E,
        self.total_window_area_S,
        self.total_window_area_W,
        self.total_above_ground_win_wall_ratio,
        self.total_above_ground_win_wall_ratio_N,
        self.total_above_ground_win_wall_ratio_E,
        self.total_above_ground_win_wall_ratio_S,
        self.total_above_ground_win_wall_ratio_W,
        self.roof_area,
        self.skylight_area,
        self.roof_skylight_ratio,
        self.people.density,
        self.building_volume]


file_dir = "D:/ornl/urban_challenge_dataset/energy"
def process_building_energy_info(file_dir, output_csv):
    filelist = []
    for dirpath, dnames, fnames in os.walk(file_dir):
        for f in fnames:
            if f.endswith(".htm"):
                filelist.append(os.path.join(dirpath, f))
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['ID',
                         'node',
                         'tsa',
                         'tsapba',
                         'tsapcba',
                         'building_area',
                         'conditioned_building_area',
                         'unconditioned_building_area',
                         'total_wall_area',
                         'total_wall_area_N',
                         'total_wall_area_E',
                         'total_wall_area_S',
                         'total_wall_area_W',
                         'total_window_area',
                         'total_window_area_N',
                         'total_window_area_E',
                         'total_window_area_S',
                         'total_window_area_W',
                         'total_above_ground_win_wall_ratio',
                         'total_above_ground_win_wall_ratio_N',
                         'total_above_ground_win_wall_ratio_E',
                         'total_above_ground_win_wall_ratio_S',
                         'total_above_ground_win_wall_ratio_W',
                         'roof_area',
                         'skylight_area',
                         'roof_skylight_ratio',
                         'people.density',
                         'building_volume'])
        for energy_doc in filelist:
            en = energy_doc_parser(energy_doc)
            en.set_all()
            results = en.get_all()
            writer.writerow(results)