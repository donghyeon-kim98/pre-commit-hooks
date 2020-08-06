# jira-commit-msg
commit 메시지에 자동으로 Jira 티켓을 추가하고 commit 메시지 검증용으로 사용하던 https://github.com/yogiyo/scripts 훅 스크립트들은 아래의 불편함들이 있어

- 레포 clone하고 링크 파일 생성해서 local의 .git/hooks/ 에 추가해줘야 함.

- git client (e.g. Fork, Sourcetree …)를 사용할 때 추가로 작업을 해줘야 함.

[pre-commit](https://github.com/pre-commit/pre-commit)을 이용하여 이런 불편함을 해소하고자 pre-commit hook을 만들었습니다. (python3.6 이하 버전은…🙇‍♂️)


## 사용법

.pre-commit-config.yaml에 아래의 hooks를 추가합니다. (동작은 기존의 훅들과 동일합니다.)

```yaml
repos:
  - repo: https://github.com/donghyeon-kim98/jira-commit-msg
    rev: ""
    hooks:
      - id: prepare-jira-commit-msg
      - id: jira-commit-msg
```
