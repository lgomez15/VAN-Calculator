def select_project_by_van(projects):
    """
    Selects the project with the highest VAN from a list of projects.
    :param projects: List of projects.
    :return: The project with the highest VAN.
    """
    selected_project = None
    for project in projects:
        max = 0
        if project['van'] > max:
            max = project['van']
            selected_project = project
    return selected_project