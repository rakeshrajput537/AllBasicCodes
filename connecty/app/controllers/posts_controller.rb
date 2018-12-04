class PostsController < ApplicationController
  def home
  	@post=Post.new
  	@posts=Post.all
  	@comment=Comment.new
  end

  def create
  	Post.create(content: params[:posts][:content], user_id: current_user.id)
  	redirect_to root_path

  end

  def destroy
  	@post=Post.find(params[:id])
  	@post.destroy
  	redirect_to root_path

  end
end
