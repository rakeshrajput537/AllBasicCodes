.[class CommentsController < ApplicationController


	def create
		comment = Comment.create(content: params[:comment][:content], post_id: params[:comment][:post_id], user_id: current_user.id)
		return redirect_to post_path(params[:comment][:post_id])
	end
	def destroy
		#Assignment

		@comment = Comment.find(params[:id])
		post_id = @comment.post_id
		@comment.destroy
		redirect_to controller:'posts' , action:'show' ,id:post_id
		
	end

end
