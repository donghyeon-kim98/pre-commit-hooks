from hooks.helper import get_commit_msg
from hooks.prepare_jira_commit_msg import main


def test_add_ticket_id_if_commit_message_is_not_start_with_ticket_id(
    temp_git_dir, branch_with_ticket_id, commit_editmsg_ref, ticket_id, git_helpers,
):
    with temp_git_dir.as_cwd():
        # Given: Commit with commit message is not start with ticket id
        git_helpers.checkout(branch_with_ticket_id)
        git_helpers.stage_new_file()
        commit_msg = "commit msg"
        git_helpers.commit(commit_msg)

        # When: Call hook
        ret = main(argv=[str(temp_git_dir.join(commit_editmsg_ref))])

        # Then: Commit message should start with ticket id
        assert ret == 0
        assert get_commit_msg(str(temp_git_dir.join(commit_editmsg_ref))) == f"{ticket_id} {commit_msg}"


def test_do_not_add_ticket_id_if_commit_message_is_start_with_ticket_id(
    temp_git_dir, commit_editmsg_ref, branch_with_ticket_id, ticket_id, git_helpers, mocker
):
    with temp_git_dir.as_cwd():
        # Given: Commit with commit message is start with ticket id
        git_helpers.checkout(branch_with_ticket_id)
        git_helpers.stage_new_file()
        commit_msg_with_ticket_id = f"{ticket_id} commit msg"
        git_helpers.commit(commit_msg_with_ticket_id)

        # When: Call hook
        mock_add_ticket_id = mocker.patch("hooks.prepare_jira_commit_msg.add_ticket_id")
        ret = main(argv=[str(temp_git_dir.join(commit_editmsg_ref))])

        assert ret == 0
        mock_add_ticket_id.assert_not_called()
