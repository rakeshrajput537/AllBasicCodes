class HomeController < ApplicationController
  def index
  end
  def find
  	User.find_by_email("rakeshrajput537@gmail.com");
  end
end
