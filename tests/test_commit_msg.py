import os

from hooks.jira_commit_msg import main as hook


def test_should_pass_if_ticket_id_in_commit_message(
    temp_git_dir, git_helper, commit_editmsg_ref, ticket_id, branch_with_ticket_id,
):
    with temp_git_dir.as_cwd():
        git_helper.checkout(branch_with_ticket_id)
        git_helper.stage_new_file()
        git_helper.commit(f"{ticket_id} commit msg")

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Return pass
        assert ret == os.EX_OK


def test_should_pass_when_without_ticket_id_if_commit_is_special_commit(
    temp_git_dir, git_helper, commit_editmsg_ref, special_commit,
):
    with temp_git_dir.as_cwd():
        # Given: Commit is special commit
        git_helper.stage_new_file()
        git_helper.commit(special_commit)

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Return pass
        assert ret == os.EX_OK


def test_should_fail_if_ticket_id_not_in_commit_message(
    temp_git_dir, git_helper, commit_editmsg_ref,
):
    with temp_git_dir.as_cwd():
        # Given: Commit message without ticket id
        git_helper.stage_new_file()
        git_helper.commit("without ticket id")

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Return fail
        assert ret == os.EX_DATAERR


def test_should_fail_if_ticket_id_in_commit_message_does_not_match_ticket_id_in_branch(
    temp_git_dir, git_helper, commit_editmsg_ref, ticket_id, branch_with_ticket_id,
):
    with temp_git_dir.as_cwd():
        # Given: Ticket id isn't match ticket id in branch
        git_helper.checkout(branch_with_ticket_id)
        git_helper.stage_new_file()
        git_helper.commit(f"NO{ticket_id}")

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Return fail
        assert ret == os.EX_DATAERR


def test_should_fail_if_commit_message_is_empty_except_ticket_id(
    temp_git_dir, git_helper, commit_editmsg_ref, ticket_id, branch_with_ticket_id,
):
    with temp_git_dir.as_cwd():
        # Given: Commit message without content but start with ticket id
        git_helper.checkout(branch_with_ticket_id)
        git_helper.stage_new_file()
        git_helper.commit(f"{ticket_id}")

        # When: Call hook
        ret = hook(argv=[commit_editmsg_ref])

        # Then: Return fail
        assert ret == os.EX_DATAERR
