import re

class ExtractId:
    @staticmethod
    def extract_id(full_id):
        # Updated regex pattern to be more generic and capture any UUID format
        match = (re.search(r'visit-item-status-(.+)$', full_id)
                 or re.search(r'clients-database-client-(.+)$', full_id))
        if match:
            dynamic_id = match.group(1)
            print("Extracted UUID:", dynamic_id)
            return dynamic_id
        else:
            print("ID pattern not found in:", full_id)
            return None