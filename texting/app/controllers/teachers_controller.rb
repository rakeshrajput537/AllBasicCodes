class TeachersController < ApplicationController
  def new
    @teacher = Teacher.new
  end

  def create
    @teacher = Teacher.new(params[:user])
   if @teacher.save
    redirect_to root_url, :notice => "Signed up!"
   else
    render "new"
   end
 end
end
