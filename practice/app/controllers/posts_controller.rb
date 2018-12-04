class PostsController < ApplicationController
	def index
		@posts= Post.all
		
	end
	def new
		
	end
	def show
		@post = Post.find(params[:id])
	end
	def create
	  # render plain: params[:post].inspect
		@post = Post.create(post_params)
		redirect_to root_path
		
	end
	private def post_params
		params.require(:post).permit(:title, :body)
		
	end
end
