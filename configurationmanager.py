test_settings = {
    "theme" : "dark",
    "notifications" : "enabled",
    "volume" : "high"
}

def add_setting(dictionary_settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()

    if key in dictionary_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    dictionary_settings.update({f"{key}" : f"{value}"})
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary_settings, setting):
    key = setting[0].lower()
    value = setting[1].lower()
    if key in dictionary_settings:
        dictionary_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary_settings, setting):
    key = setting.lower()
    if key in dictionary_settings:
        del dictionary_settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(dictionary_settings):
    if dictionary_settings == {}:
        return "No settings available."
    text = "Current User Settings:\n"
    for key, value in dictionary_settings.items():
        line = f"{key.capitalize()}: {value}\n"
        text+=line
    return text
add_setting(test_settings, ("brightness", "low"))
update_setting(test_settings, ("volume", "low"))
delete_setting(test_settings, "ThemE")
print(view_settings(test_settings))
