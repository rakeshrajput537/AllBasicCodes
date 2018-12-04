class Post < ApplicationRecord
	belongs_to :user
	has_many :comments
	has_many :likes




		def user_can_like(user_id)
		if self.likes.where(user_id: user_id).length > 0
			return false
		end

		return true

	end


	def like_status_string(user_id)
		if self.user_can_like(user_id)
			return 'Like'
		else
			return 'Unlike'

		end

	end

end
