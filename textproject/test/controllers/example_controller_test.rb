require 'test_helper'

class ExampleControllerTest < ActionDispatch::IntegrationTest
  test "should get text" do
    get example_text_url
    assert_response :success
  end

end
