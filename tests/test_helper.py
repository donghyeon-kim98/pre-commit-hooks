import pytest

from hooks.helper import get_commit_msg, get_current_branch_name, get_ticket_id, is_special_commit


def test_return_expected_branch_name(temp_git_dir, branch_with_ticket_id, git_helper):
    with temp_git_dir.as_cwd():
        # When: Checkout branch
        git_helper.checkout(branch_with_ticket_id)

        # Then: Return name of current branch
        assert get_current_branch_name() == branch_with_ticket_id


def test_return_expected_commit_msg(temp_git_dir, commit_editmsg_ref, git_helper):
    with temp_git_dir.as_cwd():
        # Given: Commit new file
        git_helper.stage_new_file()

        expected_commit_msg = "commit msg"
        git_helper.commit(expected_commit_msg)

        # Expect: Return return expected commit message
        assert get_commit_msg(commit_editmsg_ref).strip() == expected_commit_msg


def test_return_ticket_id_in_branch_name(temp_git_dir, branch_with_ticket_id, ticket_id, git_helper):
    with temp_git_dir.as_cwd():
        # When: Checkout to branch name with ticket id
        git_helper.checkout(branch_with_ticket_id)

        # Then: Return ticket id in branch name
        assert get_ticket_id(branch_with_ticket_id) == ticket_id


def test_return_true_if_special_commit(special_commit):
    # Expect: Return True
    assert is_special_commit(special_commit) is True


@pytest.mark.parametrize("commit_msg", ("general commit message",))
def test_return_false_if_general_commit(commit_msg):
    # Expect: Return False
    assert is_special_commit(commit_msg) is False
