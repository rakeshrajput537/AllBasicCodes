require 'test_helper'

class CreditCardControllerTest < ActionDispatch::IntegrationTest
  test "should get open" do
    get credit_card_open_url
    assert_response :success
  end

  test "should get credit" do
    get credit_card_credit_url
    assert_response :success
  end

  test "should get debit" do
    get credit_card_debit_url
    assert_response :success
  end

  test "should get close" do
    get credit_card_close_url
    assert_response :success
  end

end
