from google.cloud.security.iam import dao
from importer import importer
from sqlalchemy.orm.scoping import scoped_session
from google.cloud.security.common import data_access

def inject_session(f):
    def wrapper(*args):
        model_name = args[1]
        obj = args[0]
        
        scoped_session, data_access = obj.config.model_manager.get(model_name)
        with scoped_session as session:
            args.append(session)
            args.append(data_access)
            return f(*args)

class Explainer():
    def __init__(self, config):
        self.config = config

    def ExplainDenied(self, model_name, member, resources, permissions, roles):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            result = data_access.explain_denied(session,
                                                member,
                                                resources,
                                                permissions,
                                                roles)
            return result

    def ExplainGranted(self, model_name, member, resource, role, permission):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            result = data_access.explain_granted(session,
                                                 member,
                                                 resource,
                                                 role,
                                                 permission)
            return result

    def GetAccessByResources(self, model_name, resource_name, permission_names, expand_groups):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            mapping = data_access.query_access_by_resource(session,
                                                           resource_name,
                                                           permission_names,
                                                           expand_groups)
            return mapping

    def CreateModel(self, source):
        model_manager = self.config.model_manager
        model_name = model_manager.create()
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:

            def doImport():
                importer_cls = importer.by_source(source)
                import_runner = importer_cls(session, model_manager.model(model_name), data_access)
                import_runner.run()

            self.config.runInBackground(doImport)
            return model_name

    def GetAccessByMembers(self, model_name, member_name, permission_names, expand_resources):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            for role, resources in data_access.query_access_by_member(session,
                                                                      member_name,
                                                                      permission_names,
                                                                      expand_resources):
                yield role, resources

    def GetPermissionsByRoles(self, model_name, role_names, role_prefixes):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            for result in data_access.query_permissions_by_roles(session, role_names, role_prefixes):
                yield result
    
    def ListModel(self):
        model_manager = self.config.model_manager
        return model_manager.models()
    
    def DeleteModel(self, model_name):
        model_manager = self.config.model_manager
        model_manager.delete(model_name)
   
    def Denormalize(self, model_name):
        model_manager = self.config.model_manager
        scoped_session, data_access = model_manager.get(model_name)
        with scoped_session as session:
            for tuple in data_access.denormalize(session):
                permission, resource, member = tuple
                yield permission.name, resource.full_name, member.name

if __name__ == "__main__":
    class DummyConfig:
        def __init__(self):
            engine = dao.create_engine('sqlite:////tmp/test.db')
            self.model_manager = dao.ModelManager(engine)
    
        def runInBackground(self, function):
            function()

    e = Explainer(config=DummyConfig())
    e.CreateModel("TEST")