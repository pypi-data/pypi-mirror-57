from office365.runtime.resource_path_entity import ResourcePathEntity
from office365.sharepoint.principal import Principal


class Group(Principal):
    """Represents a collection of users in a SharePoint site. A group is a type of SP.Principal."""

    @property
    def users(self):
        """Gets a collection of user objects that represents all of the users in the group."""
        from office365.sharepoint.user_collection import UserCollection
        if self.is_property_available('Users'):
            return self.properties['Users']
        else:
            return UserCollection(self.context, ResourcePathEntity(self.context, self.resource_path, "Users"))
