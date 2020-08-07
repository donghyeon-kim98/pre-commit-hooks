# pre-commit-hooks

## 버전 관리 (Semantic Versioning)

버전은 커밋 메시지를 이용하여 자동으로 릴리즈됩니다.
커밋 메시지 컨벤션(Angular Commit Message Conventions)[https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines]을 확인해주세요.

| Commit message                                                                                               | Release Type     |
| ------------------------------------------------------------------------------------------------------------ | ---------------- |
| fix(pencil): 버그 수정 커밋<br>perf(pencil): 성능 개선 커밋                                                  | Patch Release    |
| feat(pencil): 새로운 기능 추가 커밋                                                                          | Feature Release  |
| feat(pencil): 무언가를 수정했다. <br>BREAKING CHANGE: 위의 수정으로 하위 호환성이 지켜지지 않을 수 있는 커밋 | Breaking Release |

자세한 내용은 [여기](https://github.com/relekang/python-semantic-release)에서 확인해주세요.
