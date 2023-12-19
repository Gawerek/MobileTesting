import re

class ExtractId:
    @staticmethod
    def extract_id(full_id):
        # Use regex to extract the UUID from the resourceId
        match = re.search(r'dashboard-visit-modal-(.*?)-visit-status', full_id)
        if match:
            dynamic_id = match.group(1)
            print(dynamic_id)
            return dynamic_id
        else:
            print("ID pattern not found")
            return None