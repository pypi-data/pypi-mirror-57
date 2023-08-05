from kashmir.core.data import Id
from kashmir.core.protocols import PRepository


class NewRelease:

    def __init__(self, repository: PRepository):
        self.repository = repository

    def __call__(self, project_id: Id):
        project = self.repository.get(project_id)
        new_release = project.new_release()
        self.repository.new_release(new_release)
        return new_release
