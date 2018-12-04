class CommentsController < ApplicationController
  def create
  	comment = Comment.create(
  		content: params[:comment][:content], 
  		user_id: current_user.id, 
  		post_id: params[:comment][:post_id]
  		)

  	redirect_to root_path

  end

  def destroy
  	@comment=Comment.find(params[:id])
  end

  
end
