import os
import json
import pprint


def match_two_list(list_a, list_b, pseudo=False):
    """
    To find if any element of list_a is in list_b and return True else return False
    :param pseudo: bool
    :param list_a: list
    :param list_b: list
    :return: bool
    """
    pass_flag = False  # required for negative food matching
    if pseudo:
        pass_flag = True
    for i in list_a:
        for j in list_b:
            if not pseudo:
                if i == j:
                    pass_flag = True
            else:
                if i == j:
                    pass_flag = False
    return pass_flag


def read_json(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
    return json_data


def main():
    team_member_file = input("Enter path to Team Member Files:")
    venue_file = input("Enter path to Venues:")

    if os.path.exists(team_member_file) and os.path.exists(venue_file):
        team_member_file_data = read_json(team_member_file)  # json team members
        venue_file_data = read_json(venue_file)  # json venue
        output_data = {}
        out_fields = ['places_to_visit', 'places_to_avoid']
        to_visit_flag = True
        for row in venue_file_data:
            name = row['name']
            food = row['food']
            drinks = row['drinks']
            row_dict = {}
            reasons = []
            avoid_dict = {}
            to_visit_flag = True
            for member in team_member_file_data:
                member_name = member['name']
                wont_eat = member['wont_eat']
                drinks_like = member['drinks']

                food_case = match_two_list(wont_eat, food, pseudo=True)
                drinks_case = match_two_list(drinks, drinks_like)
                if food_case and drinks_case:
                    pass
                else:
                    to_visit_flag = False
                    avoid_dict = {'name': name}
                    if not food_case:
                        reasons.append(f"There's nothing for {member_name} to eat.")
                    if not drinks_case:
                        reasons.append(f"There's nothing to for {member_name} to drink.")
                    if out_fields[1] not in row_dict.keys():
                        row_dict[out_fields[1]] = []
            # if reasons == []:
            #     print(row)
            avoid_dict['reason'] = reasons
            if output_data == {}:
                output_data[out_fields[0]] = []
                output_data[out_fields[1]] = []
            if to_visit_flag:
                output_data[out_fields[0]].extend([name])
            else:
                output_data[out_fields[1]].extend([avoid_dict])

        pprint.PrettyPrinter(indent=1, width=100).pprint(output_data)
        
        # uncomment below two lines if you want to save your data
        #with open('output.json', 'w') as output_file:
        #    json.dump(output_data, output_file, indent=3)

main()
