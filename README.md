# DevOps Programme - yulian-matev's personal repo

## Homework map

Below table try to organize __homeworks__ into:

* topics
* specifications
* pull requests  
  * In order to facilitate tracking, course __homework__ solutions are organized
    into pull requests. Each pull request consist of all commits needed to
    solve coresponding homework task:

| N | Topic                    | Specification | Solution Pull Request |
|---|--------------------------|---------------|-----------------------|
| 1 | Configuration Management |  [M1-3-1 Configuration Management Spec](https://github.com/vutoff/devops-programme/blob/main/ansible/README.md) |  [PR M1-3-1](https://github.com/yulian-matev/devops-programme/pull/1) (inside other repo) |
| 2 | Secrets management       | [Ansible vault spec](#secrets-management) | [PR-login-secrets](https://github.com/yulian-matev/devops-program/pull/1)|
| 3 | GitHub actions home work | [GitHub act homework](#github-actions) | [PR-github-actions-homework](https://github.com/yulian-matev/devops-program/pull/2)|
| 4 | GitHub actions practice  | [GitHub act practice](#github-actions-practice)| [PR-github-actions-practice](https://github.com/yulian-matev/devops-program/pull/3)|

## Homework specs

### Secrets management

From [telerikacademy](https://learn.telerikacademy.com/mod/assign/view.php?id=58263)

  ```text
  Create an Ansible vault. Store credentials to your Docker hub in that vault.
  Update the playbook you've created last time to use those credentials to login
  to your DockerHUB account to publish the built image. Open a PR and submit
  a link to ti. Remember - !!!do not publish your Ansible Vault password.!!!
  ```

### GitHub actions

From [telerikacademy](https://learn.telerikacademy.com/calendar/view.php?view=day&time=1699999200)

```text
Make your workflow trigger on pull request.

Make your workflow trigger on pull request and only when specific files are changed

Run a simple workflow with: * lint
```

### GitHub actions practice

Taken from [vutoff/devops-programme/M1-4-2-CI-Practice/readme](https://github.com/vutoff/devops-programme/tree/fd5ac9158bb7d1c0e8c61d066750c387530c10c6/M1-4-2-CI-Practice#readme)

```md
Create a GitHub Actions pipeline that runs on commit to a feature branch (i.e.
not `main`) and performs the following checks on our simple Flask app repository.

* Check `.editorconfig`

* Code Lint and style - use `pylint` and `black` to check for 
  style/formatting/syntax errors

* Check makrdown files [markdownlint-cli](https://www.npmjs.com/package/cli-markdown)

* Code Unittest - there's a simple unit test next to our app called `app_test.py`.
  Make sure our unittest passes (`python -m unittest` executed in the app directory)

* Check for hardcoded secrets (`gitleaks`) - not just our app but the whole repository.

* SAST - SonarCloud; Review code smells and security issues

* SCA - Snyk; review security issues

* Build a Docker image. Use Git commit SHA as an Image tag.

* Scan the built image with `Trivy`

* Push the built image to your Docker HUB account

* (optional) Add CONTRIBUTORS guide. Follow 
  [this](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
  document from GitHUb.

:warning: Make sure that you run as many tests in parallel as you see fit

:warning: Make sure you don't push your image to Docker HUB if Critical
 vulnerabilities are found

:warning: Try and use ready-made GH Actions. Avoid shell-out if possible
```
