import responses

from zeus.models import Repository, RepositoryAccess, RepositoryBackend, RepositoryProvider

REPO_DETAILS_RESPONSE = """{
    "id": 1,
    "full_name": "getsentry/zeus",
    "clone_url": "https://github.com/getsentry/zeus.git"
}"""

REPO_LIST_RESPONSE = """[{
    "id": 1,
    "full_name": "getsentry/zeus"
}]"""

KEY_RESPONSE = """{
  "id": 1,
  "key": "ssh-rsa AAA...",
  "url": "https://api.github.com/repos/getsentry/zeus/keys/1",
  "title": "zeus",
  "verified": true,
  "created_at": "2014-12-10T15:53:42Z",
  "read_only": true
}"""


def test_new_repository_github(client, default_login, default_user, default_identity):
    responses.add(
        'GET',
        'https://api.github.com/repos/getsentry/zeus',
        match_querystring=True,
        body=REPO_DETAILS_RESPONSE
    )

    responses.add('POST', 'https://api.github.com/repos/getsentry/zeus/keys', body=KEY_RESPONSE)

    resp = client.post(
        '/api/github/repos', json={
            'name': 'getsentry/zeus',
        }
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data['id']

    repo = Repository.query.unrestricted_unsafe().get(data['id'])
    assert repo.url == 'https://github.com/getsentry/zeus.git'
    assert repo.backend == RepositoryBackend.git
    assert repo.provider == RepositoryProvider.github
    assert repo.external_id == '1'
    assert repo.data == {'github': {'full_name': 'getsentry/zeus'}}

    access = list(RepositoryAccess.query.filter(RepositoryAccess.repository_id == repo.id))
    assert len(access) == 1
    assert access[0].user_id == default_user.id


def test_list_github_repos(client, default_login, default_user, default_identity):
    responses.add(
        'GET', 'https://api.github.com/user/repos', match_querystring=True, body=REPO_LIST_RESPONSE
    )

    resp = client.get('/api/github/repos')
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 1
    assert data[0]['name'] == 'getsentry/zeus'
    # TODO(dcramer): we really should have an active test as its much more critical
    assert not data[0]['active']
