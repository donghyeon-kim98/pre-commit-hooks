from hooks.consts import PASS
from hooks.helper import get_commit_msg
from hooks.prepare_jira_commit_msg import main as hook


def test_should_remove_leading_and_trailing_whitespaces_in_commit_message(
    temp_git_dir, branch_with_ticket_id, commit_editmsg_ref, ticket_id, git_helpers,
):
    with temp_git_dir.as_cwd():
        # Given: Commit message with leading and trailing whitespaces
        git_helpers.checkout(branch_with_ticket_id)
        git_helpers.stage_new_file()
        commit_message_with_whitespaces = "   commit msg   "
        git_helpers.commit(commit_message_with_whitespaces)

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Should remove leading and trailing whitespaces in commit message
        assert ret == PASS
        assert get_commit_msg(commit_editmsg_ref)


def test_should_add_ticket_id_if_commit_message_is_not_start_with_ticket_id(
    temp_git_dir, branch_with_ticket_id, commit_editmsg_ref, ticket_id, git_helpers,
):
    with temp_git_dir.as_cwd():
        # Given: Commit with commit message is not start with ticket id
        git_helpers.checkout(branch_with_ticket_id)
        git_helpers.stage_new_file()
        commit_msg = "commit msg"
        git_helpers.commit(commit_msg)

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Commit message should start with ticket id
        assert ret == PASS
        assert get_commit_msg(commit_editmsg_ref) == f"{ticket_id} {commit_msg}"


def test_should_not_add_ticket_id_if_commit_message_is_start_with_ticket_id(
    temp_git_dir, commit_editmsg_ref, branch_with_ticket_id, ticket_id, git_helpers, mocker,
):
    with temp_git_dir.as_cwd():
        # Given: Commit with commit message is start with ticket id
        git_helpers.checkout(branch_with_ticket_id)
        git_helpers.stage_new_file()
        commit_msg_with_ticket_id = f"{ticket_id} commit msg"
        git_helpers.commit(commit_msg_with_ticket_id)

        # When: Call hook
        mock_add_ticket_id = mocker.patch("hooks.prepare_jira_commit_msg.add_ticket_id")
        ret = hook(argv=[commit_editmsg_ref])

        # Then: add_ticket_id not called
        assert ret == PASS
        mock_add_ticket_id.assert_not_called()
