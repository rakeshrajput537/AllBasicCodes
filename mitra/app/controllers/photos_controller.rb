class PhotosController < ApplicationController
	def index
  @photos = Photo.order('created_at')
 end

 #New action for creating a new photo
 def new
  @photo = Photo.new
 end
  def create
  @photo = Photo.new(photo_params)
  if @photo.save
   flash[:notice] = "Successfully added new photo!"
   redirect_to root_path
  else
   flash[:alert] = "Error adding new photo!"
   render :new
  end
 end
  private

 #Permitted parameters when creating a photo. This is used for security reasons.
 def photo_params
  params.require(:photo).permit(:title, :image)
 end
end
