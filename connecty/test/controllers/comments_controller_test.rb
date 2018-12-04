require 'test_helper'

class CommentsControllerTest < ActionDispatch::IntegrationTest
  test "should get content:text" do
    get comments_content:text_url
    assert_response :success
  end

  test "should get user_id:integer" do
    get comments_user_id:integer_url
    assert_response :success
  end

  test "should get post_id:integer" do
    get comments_post_id:integer_url
    assert_response :success
  end

end
