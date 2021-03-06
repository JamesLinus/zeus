import React from 'react';
import {IndexRoute, Route, IndexRedirect} from 'react-router';

import App from './pages/App';
import BuildCoverage from './pages/BuildCoverage';
import BuildDetails from './pages/BuildDetails';
import BuildDiff from './pages/BuildDiff';
import BuildOverview from './pages/BuildOverview';
import BuildTestList from './pages/BuildTestList';
import Login from './pages/Login';
import GitHubRepositoryList from './pages/GitHubRepositoryList';
import NotFound from './pages/NotFound';
import RepositoryDetails from './pages/RepositoryDetails';
import RepositoryBuildList from './pages/RepositoryBuildList';
import RepositoryTestList from './pages/RepositoryTestList';
import UserBuildList from './pages/UserBuildList';

import requireAuth from './utils/requireAuth';

export default (
  <Route path="/" component={App}>
    <IndexRedirect to="/builds" />
    <Route path="/settings/github/repos" component={requireAuth(GitHubRepositoryList)} />
    <Route path="/builds" component={requireAuth(UserBuildList)} />
    <Route path="/login" component={Login} />
    <Route path="/:ownerName/:repoName" component={requireAuth(RepositoryDetails)}>
      <IndexRoute component={RepositoryBuildList} />
      <Route path="tests" component={RepositoryTestList} />
      <Route path="builds/:buildNumber" component={BuildDetails}>
        <IndexRoute component={BuildOverview} />
        <Route path="coverage" component={BuildCoverage} />
        <Route path="diff" component={BuildDiff} />
        <Route path="tests" component={BuildTestList} />
      </Route>
    </Route>
    <Route path="*" component={NotFound} />
  </Route>
);
