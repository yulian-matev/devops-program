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
| 3 |  GitHub actions | [GitHub actions](#github-actions) | [PR-github-actions](https://github.com/yulian-matev/devops-program/pull/2)|

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

```text
Make your workflow trigger on pull request.

Make your workflow trigger on pull request and only when specific files are changed

Run a simple workflow with: * lint
```
