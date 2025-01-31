import json

# Function Description: Get the Personal Access Token (PAT) for the organization
# Input Parameters:
# org: Name of the organization : string
# Return: PAT for the organization : string

def get_pat(org):
    try:
        with open('app/data/pat_list.json', 'r') as file:
            pat_list = json.load(file)
        for pat_data in pat_list:
            if org in pat_data:
                return pat_data[org]
        return None
    except FileNotFoundError:
        print("The file 'pat_list.json' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding the JSON file.")
        return None
    
########################################################################################

# if __name__ == "__main__":
#     organization = "GitOpsLab-3"
#     pat = get_pat(organization)
#     if pat:
#         print(f"PAT for {organization}: {pat}")
#     else:
#         print(f"PAT for {organization} not found.")