class Product < ApplicationRecord
	#Mounts paperclip image
  has_attached_file :image
  validates_attachment_content_type :image, content_type: /\Aimage\/.*\z/
end
