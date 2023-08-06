import yaml


class UserMapping:

    def __init__(self, USER_YAML_FILE, jira, default_user):
        self.user_name_selection_dict = {}
        with open(USER_YAML_FILE) as user_yaml_file:
            self.user_name_selection_dict = yaml.load(
                user_yaml_file, Loader=yaml.FullLoader)
        self.USER_YAML_FILE = USER_YAML_FILE
        self.jira = jira
        if(default_user):
            self.default_user = default_user

    def is_user_potentially_the_same(self, firstname, lastname, potential_user_json_response):
        '''
        compare the users based on the first name first, since the lastname may or may not in the Jira
        record, so we compare the last name based on the email or the display name

        Returns:
            Boolean: whether it matches the potential user

        '''
        try:
            potential_user_displayname = potential_user_json_response['displayName']
        except KeyError as identifier:
            potential_user_displayname = ""
        potential_user_email = potential_user_json_response['emailAddress']
        # print (firstname + '  '+ lastname)
        # print (potential_user_displayname.lower()+ "  "+ potential_user_email.lower())

        return ((firstname.lower() in potential_user_displayname.lower() and lastname.lower() in potential_user_displayname.lower())
        or (firstname.lower() in potential_user_email.lower() and lastname.lower() in potential_user_email.lower()))

    def insert_user_to_user_dict(self, firstname, lastname, selected_username):
        if(firstname in self.user_name_selection_dict.keys()):
                self.user_name_selection_dict[firstname][lastname] = selected_username
        else:
            self.user_name_selection_dict[firstname] = {
                lastname: selected_username}

    def filter_users_by_name(self, firstaname, lastname, potentialusers):
        filtered_list = []
        for potentialuser in potentialusers:
            if(self.is_user_potentially_the_same(firstaname, lastname, potentialuser)):
                filtered_list.append(potentialuser)
        return filtered_list

    def write_dict_to_file(self):
        with open(self.USER_YAML_FILE, 'w') as user_yaml_file:
            yaml.dump(self.user_name_selection_dict, user_yaml_file)

    def find_user_name_by_fullname(self,fullname):
        firstname = fullname.split(' ')[0]
        lastname = fullname.split(' ')[-1]
        return (self.find_user_name(firstname,lastname))


    def find_user_name(self, firstname, lastname):
        potentialusers = self.filter_users_by_name(
            firstname, lastname,  self.jira.user_find_by_user_string(firstname, include_inactive_users=True))

        if (len(potentialusers) > 1):
            try:
                selected_username = self.user_name_selection_dict[firstname][lastname]
                return (selected_username)
            except Exception:
                print("First Name: " + firstname + " LastName: " + lastname)
                for i in range(0, len(potentialusers)):
                    print(str(i) + "    " + potentialusers[i]['displayName'] + "   " + potentialusers[i]
                          ['emailAddress'] + '  ;is active:'+str(potentialusers[i]['active']))
                user_selection = input('')
                selected_username = ""
                try:
                    # valid selection
                    selected_username = potentialusers[int(
                        user_selection)]['name']
                except Exception:
                    # invalid selection
                    if(self.default_user):
                        selected_username = firstname.lower()+'.'+lastname.lower()
                    else:
                        selected_username = self.default_user
                self.insert_user_to_user_dict(
                    firstname, lastname, selected_username)
                return (selected_username)

        elif(len(potentialusers) == 1):
            return potentialusers[0]['name']

        else:
            if(self.default_user):
                selected_username = self.default_user
            else:
                selected_username = firstname.lower()+'.'+lastname.lower()
            return (selected_username)