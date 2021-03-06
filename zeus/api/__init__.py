from .controller import Controller
from . import resources as r

app = Controller('api', __name__)
app.add_resource('/', r.IndexResource)
app.add_resource('/auth', r.AuthIndexResource)
app.add_resource('/builds', r.BuildIndexResource)
app.add_resource('/github/orgs', r.GitHubOrganizationsResource)
app.add_resource('/github/repos', r.GitHubRepositoriesResource)
app.add_resource('/repos', r.RepositoryIndexResource)
app.add_resource('/repos/<owner_name>/<repo_name>/builds', r.RepositoryBuildsResource)
app.add_resource('/repos/<owner_name>/<repo_name>/tests', r.RepositoryTestsResource)
app.add_resource('/repos/<owner_name>/<repo_name>/test-tree', r.RepositoryTestTreeResource)
app.add_resource('/repos/<owner_name>/<repo_name>/builds/<build_number>', r.BuildDetailsResource)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/file-coverage',
    r.BuildFileCoverageResource
)
app.add_resource('/repos/<owner_name>/<repo_name>/builds/<build_number>/jobs', r.BuildJobsResource)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/source', r.BuildSourceResource
)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/tests', r.BuildTestsResource
)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/jobs/<job_number>', r.JobDetailsResource
)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/jobs/<job_number>/artifacts',
    r.JobArtifactsResource
)
app.add_resource(
    '/repos/<owner_name>/<repo_name>/builds/<build_number>/jobs/<job_number>/tests',
    r.JobTestsResource
)
app.add_resource('/tests/<test_id>', r.TestDetailsResource)
app.add_resource('/users/<user_id>/builds', r.UserBuildsResource)
app.add_resource('/<path:path>', r.CatchallResource)
